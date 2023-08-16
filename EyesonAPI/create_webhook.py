import argparse
import json
import sys
import requests
import os

BASE_URL = 'https://api.eyeson.team'


def main(argv):
    parser = argparse.ArgumentParser(
        description='Main Test Application')
    parser.add_argument('-u', '--url', required=False, default="https://shenoy.requestcatcher.com/snapshot")
    parser.add_argument('-t', '--types', required=False, default="snapshot_update")
    parser.add_argument('-p', '--api_token', required=False, default=os.environ['EYESON_API'])
    args = parser.parse_args(argv)

    headers = {"Authorization": args.api_token}
    params = {"url": args.url,
              "types": args.types}

    response = requests.post(BASE_URL + "/webhooks", headers=headers, params=params)
    print(response.status_code)
    print(response.text)


if __name__ == "__main__":
    main(sys.argv[1:])
