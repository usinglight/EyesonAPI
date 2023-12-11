import argparse
import sys
from eyeson.eyeson import EyesonClient


def main(argv):
    parser = argparse.ArgumentParser(
        description='Main Test Application')
    parser.add_argument('-f', '--foreground', required=False)
    parser.add_argument('-b','--background', required=False)
    parser.add_argument('-a', '--access_key', required=True)
    parser.add_argument('-l', '--layout', required=False, default='present-lower-4-spaced-aspect-fit')
    args = parser.parse_args(argv)

    ec = EyesonClient.get_room(args.access_key)
    # ec.broadcast_message('Hello World')

    if args.foreground:
        ec.local_image_overlay(filename=args.foreground, z_index=1)
    if args.background:
        ec.local_image_overlay(filename=args.background, z_index=-1)

    users = ['', '', '', '', 'jsmith']
    ec.change_layout(layout_type='auto', layout_name=args.layout, users=users)


if __name__ == "__main__":
    main(sys.argv[1:])
