import argparse
import json
import sys
import requests
import os
from eyeson import EyesonClient


def main(argv):

    parser = argparse.ArgumentParser(
        description='Main Test Application')
    parser.add_argument('-p', '--api_token', required=False, default=os.environ['EYESON_API'])
    args = parser.parse_args(argv)

    with open('../current_room.json', 'r') as f:
        current_room = json.load(f)
    access_key = current_room['access_key']

    ec = EyesonClient.get_room(access_key)
    ec.authenticate(args.api_token)
    print(ec.get_webhooks())


if __name__ == '__main__':
    main(sys.argv[1:])