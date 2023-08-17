import argparse
import json
import sys
import requests
import os
from eyeson.eyeson import EyesonClient


def main(argv):
    parser = argparse.ArgumentParser(
        description='Main Test Application')
    parser.add_argument('-u', '--user', required=True)
    parser.add_argument('-p', '--api_token', required=False, default=os.environ['EYESON_API'])
    args = parser.parse_args(argv)

    ec = EyesonClient.create_room(args.user, args.api_token)



if __name__ == '__main__':
    main(sys.argv[1:])
