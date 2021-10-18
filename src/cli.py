import argparse

from checkip import get_ip, resolve_ip
from checkip.providers import providers

def main():
    parser = argparse.ArgumentParser(prog='checkip')
    subparser = parser.add_subparsers(dest='command')

    get_ip_parser = subparser.add_parser('get')
    get_ip_parser.add_argument('provider', choices=providers.keys())

    resolve_ip_parser = subparser.add_parser('resolve')
    resolve_ip_parser.add_argument('providers', nargs='+', choices=providers.keys())

    args = parser.parse_args()
    if args.command == 'get':
        print(get_ip(args.provider))
    elif args.command == 'resolve':
        print(resolve_ip(args.providers))
    else:
        parser.print_help()
