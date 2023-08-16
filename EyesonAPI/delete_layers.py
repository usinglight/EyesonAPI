import argparse
import json
import sys
import requests
import os
from eyeson import EyesonClient

BASE_URL = 'https://api.eyeson.team'


def main(argv):



    parser = argparse.ArgumentParser(
        description='Main Test Application')
    # parser.add_argument('-a', '--access_key', required=True)
    parser.add_argument('-p', '--api_token', required=False, default=os.environ['EYESON_API'])
    args = parser.parse_args(argv)

    headers = {'Authorization': args.api_token}

    with open('../current_room.json', 'r') as f:
        current_room = json.load(f)
    access_key = current_room['access_key']

    ec = EyesonClient.get_room(access_key, debug=True)
    ec.delete_layers(1)
    ec.delete_layers(-1)

    # response = requests.delete(BASE_URL + '/rooms/' + access_key + '/layers/1', headers=headers)
    # response = requests.delete(BASE_URL + '/rooms/' + access_key + '/layers/-1', headers=headers)


if __name__ == '__main__':
    main(sys.argv[1:])
