import argparse
import sys
from eyeson.eyeson import EyesonClient


def main(argv):
    parser = argparse.ArgumentParser(
        description='Main Test Application')
    parser.add_argument('-u', '--guest_link', required=False)
    parser.add_argument('-a', '--access_key', required=False)
    args = parser.parse_args(argv)

    if args.guest_link:
        print("Parse as guest_token")
        ec = EyesonClient.register_guest(args.url)
    elif args.access_key:
        print("Parse as access_token")
        ec = EyesonClient.get_room(args.access_key)
    else:
        print("can't continue - need either a guest_link or access_key")
        sys.exit(1)

    print(ec.access_key)

if __name__ == '__main__':
    main(sys.argv[1:])
