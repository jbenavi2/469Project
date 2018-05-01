import argparse
import sys
import datetime as dt


def macCommands():
    # parse input out of sys.argv
    parser = argparse.ArgumentParser(prog='MAC Conversion')

    # mutual exclusive.  Either T or D
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-T', action='store_true')
    group.add_argument('-D', action='store_true')

    # mutual exclusive.  Either f or h
    group2 = parser.add_mutually_exclusive_group(required=True)
    group2.add_argument('-f', metavar='filename')
    # can't use -h as it's already used for help by default by argparse
    group2.add_argument('-hex', metavar='hex_value')

    return parser


def hex2bin(string):
    # remove 0x from hex input
    string = string[2:]
    binary = bin(int(string, 16))
    # remove 0b from binary output
    binary = binary[2:]
    return binary


def bin2date(binary):
    year = int(binary[0:6], 2) + 1980
    month = int(binary[6:10], 2)
    day = int(binary[10:], 2)
    date = dt.date(year, month, day)
    return date.strftime("Date: %b %d, %Y")


def bin2time(binary):
    hour = int(binary[0:4], 2)
    min = int(binary[4:10], 2)
    sec = int(binary[10:15], 2) * 2
    time = dt.time(hour, min, sec)
    return time.strftime("Time: %I:%M:%S %p")


def main():
    command = macCommands()

    command.print_usage()

    """test conversions"""
    # sample_date = '0x4f42'
    # print(bin2date(hex2bin(sample_date)))
    #
    # sample_time = '0x53f6'
    # print(bin2time(hex2bin(sample_time)))

    namespace = command.parse_args()

    if namespace.f is not None:
        fopen = open(namespace.f, 'r')
        hex_input = fopen.readline()
        fopen.close()
    else:
        hex_input = namespace.hex

    if namespace.T:
        print(bin2time(hex2bin(hex_input)))
    elif namespace.D:
        print(bin2date(hex2bin(hex_input)))


if __name__ == '__main__':
    main()
