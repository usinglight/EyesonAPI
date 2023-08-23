import argparse
import json
import sys
import requests
from eyeson.eyeson import EyesonClient


def main(argv):
    parser = argparse.ArgumentParser(
        description='Main Test Application')
    parser.add_argument('-a', '--access_key', required=True)
    args = parser.parse_args(argv)

    ec = EyesonClient.get_room(args.access_key)
    ec.broadcast_message('Hello World')
    # ec.change_layout(layout_type='auto', layout_name='six', users=['','','test_id','','',''])
    # ec.create_snapshot()
    # ec.get_room_details()
    # ec.image_overlay(url='https://eyeson-team.github.io/api/images/eyeson-overlay.png')
    ec.local_image_overlay(filename='resources/images/eyeson-overlay.png')
    ec.playback(url='http://commondatastorage.googleapis.com/gtv-videos-bucket/sample/WeAreGoingOnBullrun.mp4', )


if __name__ == "__main__":
    main(sys.argv[1:])
