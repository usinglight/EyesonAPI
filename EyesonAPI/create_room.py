import argparse
import json
import sys
import requests
import os

BASE_URL = 'https://api.eyeson.team'

def create_room(room, user, api_token):
    headers = {'Authorization': api_token}
    params = {'user[name]': user,
              'user[id]': "test_id",
              'id': room,
              'options[layout]': 'custom',
              'options[sfu_mode]': 'disabled',
              'options[cupythostom_fields][virtual_background]': True,
              # 'options[widescreen]': True,
              'options[custom_fields][virtual_background_allow_guest]': True

              }

    response = requests.post(BASE_URL + '/rooms', headers=headers, params=params)
    # print(response.text)

    if (response.status_code == 201):
        print('Success:')
        json_response = json.loads(response.text)
        print('GUI: ' + json_response['links']['gui'])
        print('Guest: ' + json_response['links']['guest_join'])
        print('Access Key: ' + json_response['access_key'])

        with open('../current_room.json', 'w') as f:
            json.dump(json_response, f)
    else:
        print('Failed to create room: ' + str(response.status_code))
        print(response.text)


def main(argv):
    parser = argparse.ArgumentParser(
        description='Main Test Application')
    parser.add_argument('-n', '--room', required=True)
    parser.add_argument('-u', '--user', required=True)
    parser.add_argument('-p', '--api_token', required=False, default=os.environ['EYESON_API'])
    args = parser.parse_args(argv)

    create_room(args.room, args.user, args.api_token)


if __name__ == '__main__':
    main(sys.argv[1:])
