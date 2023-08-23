import argparse
import sys
from eyeson.eyeson import EyesonClient


def main(argv):
    parser = argparse.ArgumentParser(
        description='Main Test Application')
    parser.add_argument('-a', '--access_key', required=True)
    args = parser.parse_args(argv)

    ec = EyesonClient.get_room(args.access_key, debug=True)
    ec.delete_layers(1)
    ec.delete_layers(-1)


if __name__ == '__main__':
    main(sys.argv[1:])
