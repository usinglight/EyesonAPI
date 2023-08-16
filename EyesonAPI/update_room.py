import argparse
import json
import sys
import requests
import os
from eyeson import EyesonClient

BASE_URL = 'https://api.eyeson.team'


def update_room(guest_token, user, api_token):
    headers = {'Authorization': api_token}
    response = requests.post(BASE_URL + '/guests/' + guest_token + '?name=' + user)

    if (response.status_code == 201):
        print('Success:')
        json_response = json.loads(response.text)
        print(json_response)


        with open('../current_room.json', 'w') as f:
            json.dump(json_response, f)
    else:
        print('Failed to update room: ' + str(response.status_code))
        print(response.text)


def main(argv):
    parser = argparse.ArgumentParser(
        description='Main Test Application')
    parser.add_argument('-u', '--guest_link', required=True)
    parser.add_argument('-p', '--api_token', required=False, default=os.environ['EYESON_API'])
    args = parser.parse_args(argv)

    url = args.guest_link
    if url.find('?guest=') >= 0:
        guest_token = url[url.find('?guest=') + len('?guest='):]
        print(guest_token)
        update_room(guest_token, 'Demo User', args.api_token)
    else:
        print('Invalid guest token parsing')
        sys.exit()

    # ec = EyesonClient.get_room(access_key, base_url=BASE_URL)
    # details = ec.get_room_details
    # print(details)

if __name__ == '__main__':
    main(sys.argv[1:])
