import socket
from concurrent.futures import ThreadPoolExecutor
from itertools import repeat
import argparse

open_ports = []


def user_input():

    parser = argparse.ArgumentParser()

    parser.add_argument('-ip', '--ip_address', type=str, help='Target IP address.', required=True)
    parser.add_argument('-p', '--port_range', type=int, nargs=2, help='Target port range.', required=True)
    parser.add_argument('-t', '--threads', type=int, help="[Optional] Number of concurrent workers (default: 10)", default=10)
    parser.add_argument('-v', '--verbose', action="store_true", help='[Optional] Enable verbose output.')

    args = parser.parse_args()
    scan_threading(args)

    return args


def port_scan(ports, args):

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.5)
    result = sock.connect_ex((args.ip_address, ports))
    sock.close()

    if result == 0:
        open_ports.append(ports)

    if result == 0 and args.verbose == True:
        print(ports, "PORT OPEN")

    elif result != 0 and args.verbose == True:
        print("PORT", ports, " Connection refused. Socket error code:", result)


def scan_threading(args):

    threads = ThreadPoolExecutor(max_workers=args.threads)
    ports = list(threads.map(port_scan, range(args.port_range[0], args.port_range[1] + 1), repeat(args)))
    return ports


def main():

    user_input()
    print("\nOPEN PORTS:", ', '.join(map(str, open_ports)), "\n")


if __name__ == "__main__":
    main()
