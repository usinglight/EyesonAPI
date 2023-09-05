import aiohttp
import asyncio
import json
import re

from aiortc import RTCPeerConnection, VideoStreamTrack, RTCIceServer, RTCConfiguration
from aiortc.contrib.media import MediaBlackhole, MediaPlayer, MediaRecorder
from av import VideoFrame
import numpy as np
from PIL import Image, ImageDraw, ImageFont


class TextVideoStreamTrack(VideoStreamTrack):
    """
    A VideoStreamTrack that returns frames of a black screen with text.
    """

    def __init__(self, text):
        super().__init__()  # don't forget this!

        # Create an image of a black screen
        self.image = Image.new('RGB', (640, 480), color=(0, 0, 0))

        # Draw the text on the image
        d = ImageDraw.Draw(self.image)
        fnt = ImageFont.load_default()
        d.text((10, 10), text, font=fnt, fill=(255, 255, 255))

    async def recv(self):
        pts, time_base = await self.next_timestamp()

        img_frame = np.array(self.image)
        frame = VideoFrame.from_ndarray(img_frame, format="rgb24")
        frame.pts = pts
        frame.time_base = time_base

        return frame


def get_token(s):
    match = re.search(r'guest=(.*)', s)
    if match:
        return match.group(1)
    return None


async def main():
    pc = RTCPeerConnection()

    guest_link = input("Please enter guest link:")
    guest_token = get_token(guest_link)

    url = "https://api.eyeson.team/guests/" + guest_token

    headers = {
        "Content-Type": "application/json"
    }
    payload = {
        "id": "Assistant",
        "name": "Assistant"
    }

    async with aiohttp.ClientSession() as session:
        async with session.post(url, data=json.dumps(payload), headers=headers) as response:
            response_text = await response.text()
            data = json.loads(response_text)
            with open("response.json", "w") as file:
                file.write(response_text)

            access_key = data['access_key']
            websocket_url = data['links']['websocket']
            stun_servers = data['signaling']['options']['stun_servers']
            turn_servers = data['signaling']['options']['turn_servers']
            signaling_options = data['signaling']['options']

            ice_servers = []
            for url in stun_servers:
                ice_servers.append(RTCIceServer(urls=[url]))
            for server in turn_servers:
                ice_servers.append(RTCIceServer(**server))

            configuration = RTCConfiguration(iceServers=ice_servers)

            # error when trying to execute because the password comes unexpected
            # added json above to look in detail for any access token...

            pc = RTCPeerConnection(configuration)

            pc.addTrack(TextVideoStreamTrack("test"))

            await pc.close()

asyncio.run(main())
