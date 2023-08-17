import argparse
import json
import sys
import requests
from eyeson.eyeson import EyesonClient


def main(argv):
    parser = argparse.ArgumentParser(
        description='Main Test Application')
    parser.add_argument('-f', '--foreground', required=False)
    parser.add_argument('-b','--background', required=False)
    # parser.add_argument('-a', '--access_token', required=True)
    args = parser.parse_args(argv)

    with open('../current_room.json', 'r') as f:
        current_room = json.load(f)
    access_key = current_room['access_key']

    ec = EyesonClient.get_room(access_key)
    # ec.broadcast_message('Hello World')

    ec.change_layout(layout_type='auto', layout_name='present-lower-4-spaced-aspect-fit', users=['', '', 'test_id', '', ''])
    if args.foreground:
        ec.local_image_overlay(filename=args.foreground, z_index=1)
    if args.background:
        ec.local_image_overlay(filename=args.background, z_index=-1)

if __name__ == "__main__":
    main(sys.argv[1:])
