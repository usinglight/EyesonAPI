import argparse
import json
import sys
import requests
import os
from eyeson.eyeson import EyesonClient


# response = requests.post(BASE_URL + '/guests/' + guest_token + '?name=' + user)


def main(argv):
    parser = argparse.ArgumentParser(
        description='Main Test Application')
    parser.add_argument('-u', '--guest_link', required=True)
    parser.add_argument('-a', '--access_key', required=False)
    args = parser.parse_args(argv)

    #TODO:  This method isn't functional yet
    if args.guest_link:
        print("Parse as guest_token")
    elif args.access_key:
        print("Parse as access_token")
    else:
        print("can't continue")

    # ec = EyesonClient.get_room(access_key, base_url=BASE_URL)
    # details = ec.get_room_details
    # print(details)

if __name__ == '__main__':
    main(sys.argv[1:])
