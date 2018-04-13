import sys
import argparse

# arguments = sys.argv
# print(len(sys.argv))
# print(arguments)


# for argument in arguments[1:]:
#     if argument == '-L' or argument == '--logical':
#         cluster_address_found = False
#         physical_address_found = False
#     if argument == '-P' or argument == '--physical':
#         cluster_address_found = False
#         logical_address_found = False
#     if argument == '-C' or argument == '--cluster':
#         logical_address_found = False
#         physical_address_found = False
#     if argument == '-b':
#         offset = arguments[arguments.index(argument) + 1]
#     elif "--partition-start" in argument:
#         option, offset = argument.split("=")
#     if argument == '-s':
#         sector_size = arguments[arguments.index(argument) + 1]
#     elif "--sector-size" in argument:
#         option, sector_size = argument.split("=")
#     if argument == '-l':
#         logical_address = arguments[arguments.index(argument) + 1]
#         print(logical_address)
#     elif "--logical-known" in argument:
#         option, logical_address = argument.split("=")
#         print(logical_address)
#     if argument == '-p':
#         physical_address = arguments[arguments.index(argument) + 1]
#         print(physical_address)
#     elif "--physical-known" in argument:
#         option, physical_address = argument.split("=")
#         print(physical_address)
#     if argument == '-c':
#         cluster_address = arguments[arguments.index(argument) + 1]
#         print(cluster_address)
#     elif "--cluster-known" in argument:
#         option, cluster_address = argument.split("=")
#         print(cluster_address)
#     if argument == '-k':
#         cluster_size = arguments[arguments.index(argument) + 1]
#         print(cluster_size)
#     elif "--cluster-size" in argument:
#         option, cluster_size = argument.split("=")
#         print(cluster_size)
#     if argument == '-r':
#         reserved = arguments[arguments.index(argument) + 1]
#         print(reserved)
#     elif "--reserved" in argument:
#         option, reserved = argument.split("=")
#         print(reserved)
#     if argument == '-t':
#         tables = arguments[arguments.index(argument) + 1]
#         print(tables)
#     elif "--fat-tables" in argument:
#         option, tables = argument.split("=")
#         print(tables)
#     if argument == '-f':
#         length = arguments[arguments.index(argument) + 1]
#         print(length)
#     elif "--fat-length" in argument:
#         option, length = argument.split("=")
#         print(length)

# from https://youtu.be/q94B9n_2nf0
def parseCommands():
    # parse input out of sys.argv
    parser = argparse.ArgumentParser(prog='Address Conversion')

    # mutual exclusivity.  Either L or P or C. One is required.  Doc 16.4
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-L', '--logical', action='store_true')
    group.add_argument('-P', '--physical', action='store_true')
    group.add_argument('-C', '--cluster', action='store_true')

    # the offset
    parser.add_argument('-b', '--partition-start', metavar='offset', type=int, default=0)

    # the byte address
    parser.add_argument('-B', '--byte-address', action='store_true')
    # group2 = parser.add_argument_group()
    # group2.add_argument('-B', '--byte-address', action='store_true')
    parser.add_argument('-s', '--sector-size', metavar='bytes', type=int, default=512)
    parser.add_argument('-l', '--logical-known', metavar='address', type=int)
    parser.add_argument('-p', '--physical-known', metavar='address', type=int)

    # should be grouped [-c -k -r -t -f]
    parser.add_argument('-c', '--cluster-known', metavar='address', type=int)
    parser.add_argument('-k', '--cluster-size', metavar='sectors', type=int)
    parser.add_argument('-r', '--reserved', metavar='sectors', type=int)
    parser.add_argument('-t', '--fat-tables', metavar='tables', type=int)
    parser.add_argument('-f', '--fat-length', metavar='sectors', type=int)

    return parser


def logical(physicalKnown, clusterKnown, offset):
    """given physical or cluster address calculate logical address"""

    # given only physical address and cluster address left empty
    if physicalKnown is not None and clusterKnown is None:
        logicalAddress = physicalKnown - offset
    # given only cluster (-c) as well as -k -r -t -f.  physical left empty
    elif clusterKnown is not None and physicalKnown is None:
        logicalAddress = ((clusterKnown - 2) * namespace.cluster_size) + \
                         namespace.reserved + (namespace.fat_tables * namespace.fat_length)
    # nothing was given so error
    else:
        print("error")
        return
    return logicalAddress


def physical(logicalKnown, clusterKnown, offset):
    """given logical or cluster calculate physical address"""

    # given only logical address and cluster address left empty
    if logicalKnown is not None and clusterKnown is None:
        physicalAddress = logicalKnown + offset
    # given only cluster (-c) as well as -k -r -t -f.  logical is left empty
    elif clusterKnown is not None and logicalKnown is None:
        physicalAddress = offset + ((clusterKnown - 2) * namespace.cluster_size) + \
                            namespace.reserved + (namespace.fat_tables * namespace.fat_length)
    else:
        print("error")
        return
    return physicalAddress


def cluster(logicalKnown, physicalKnown, offset):
    """given logical or physical calculate cluster address"""

    if logicalKnown is not None and physicalKnown is None:
        print("TODO")  # TODO


def main():
    command = parseCommands()

    # print usage to show command options
    # command.print_usage()

    # namespace holds the values entered from the command line
    global namespace
    namespace = command.parse_args()

    # print(namespace)

    # user wants logical, physical, or cluster
    if namespace.logical:
        address = logical(namespace.physical_known, namespace.cluster_known, namespace.partition_start)
        print(address)
    elif namespace.physical:
        address = physical(namespace.logical_known, namespace.cluster_known, namespace.partition_start)
        print(address)
    elif namespace.cluster:
        print("TODO")  # TODO 

    # print(command)


if __name__ == '__main__':
    main()
