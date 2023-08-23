import argparse
import json
import sys
import requests
import os
from eyeson.eyeson import EyesonClient


def main(argv):
    parser = argparse.ArgumentParser(
        description='Main Test Application')
    parser.add_argument('-p', '--api_token', required=False, default=os.environ['EYESON_API'])
    parser.add_argument('-a', '--access_key', required=True)
    args = parser.parse_args(argv)

    ec = EyesonClient.get_room(args.access_key)
    ec.authenticate(args.api_token)
    print(ec.get_webhooks())


if __name__ == '__main__':
    main(sys.argv[1:])
