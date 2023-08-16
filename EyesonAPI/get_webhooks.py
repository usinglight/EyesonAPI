import argparse
import json
import sys
import requests
import os

BASE_URL = 'https://api.eyeson.team'

def main(argv):

    parser = argparse.ArgumentParser(
        description='Main Test Application')
    parser.add_argument('-p', '--api_token', required=False, default=os.environ['EYESON_API'])
    args = parser.parse_args(argv)

    headers = {'Authorization': args.api_token}
    response = requests.get(BASE_URL + '/webhooks', headers=headers)
    print(response.status_code)
    print(response.text)
    json_response = json.loads(response.text)

if __name__ == '__main__':
    main(sys.argv[1:])