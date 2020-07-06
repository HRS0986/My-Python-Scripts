from argparse import ArgumentParser
from blocker import Blocker, UrlNotFoundError

# usage : blox [-b url | -u url | -g | -i url] 

parser = ArgumentParser(
    description='Command Line Website Blocker',
    prog='blox',
    usage='%(prog)s [-b url | -u url | -g | -i url | -h]',
    epilog='By Hirusha Fernando'
)

group = parser.add_mutually_exclusive_group()
group.add_argument('-b', help='Blocking Mode', type=str, dest='urlB', metavar='URL')
group.add_argument('-u', help='Unblocking Mode', type=str, dest='urlU', metavar='URL')
group.add_argument('-i', help='Check Mode', type=str, dest='urlI', metavar='URL')
group.add_argument('-g', help='Get Blocked URL list', action='store_true')

args = parser.parse_args()

b = Blocker()

if args.urlB == None and args.urlU == None and args.urlI == None and args.g == False:
    parser.print_help()

elif args.g:
    url_list = b.get_blocked()

    print('\n==================={ Blox }===================\n')
    print('[!] Blocked URL list\n')
    
    for url in url_list:
        print(f'  [+] {url}')

    print('\n==================={ Blox }===================\n')

elif args.urlB:
    b.block_site(args.urlB)

elif args.urlU:
    try: b.unblock(args.urlU)
    except UrlNotFoundError: print('\n[!] URL Cannot Be Found\n')

elif args.urlI:
    isBlocked = b.is_blocked(args.urlI)
    
    if isBlocked: print('\n[!] This URL is blocked.\n')
    else: print('\n[!] This URL is not blocked.\n')