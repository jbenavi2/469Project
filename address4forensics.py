import sys

arguments = sys.argv
print(len(sys.argv))
print(arguments)

for argument in arguments[1:]:
    if argument == '-L' or argument == '--logical':
        cluster_address_found = False
        physical_address_found = False
    if argument == '-P' or argument == '--physical':
        cluster_address_found = False
        logical_address_found = False
    if argument == '-C' or argument == '--cluster':
        logical_address_found = False
        physical_address_found = False
    if argument == '-b':
        offset = arguments[arguments.index(argument) + 1]
    elif "--partition-start" in argument:
        option, offset = argument.split("=")
    if argument == '-s':
        sector_size = arguments[arguments.index(argument) + 1]
    elif "--sector-size" in argument:
        option, sector_size = argument.split("=")
    if argument == '-l':
        logical_address = arguments[arguments.index(argument) + 1]
        print(logical_address)
    elif "--logical-known" in argument:
        option, logical_address = argument.split("=")
        print(logical_address)
    if argument == '-p':
        physical_address = arguments[arguments.index(argument) + 1]
        print(physical_address)
    elif "--physical-known" in argument:
        option, physical_address = argument.split("=")
        print(physical_address)
    if argument == '-c':
        cluster_address = arguments[arguments.index(argument) + 1]
        print(cluster_address)
    elif "--cluster-known" in argument:
        option, cluster_address = argument.split("=")
        print(cluster_address)
    if argument == '-k':
        cluster_size = arguments[arguments.index(argument) + 1]
        print(cluster_size)
    elif "--cluster-size" in argument:
        option, cluster_size = argument.split("=")
        print(cluster_size)
    if argument == '-r':
        reserved = arguments[arguments.index(argument) + 1]
        print(reserved)
    elif "--reserved" in argument:
        option, reserved = argument.split("=")
        print(reserved)
    if argument == '-t':
        tables = arguments[arguments.index(argument) + 1]
        print(tables)
    elif "--fat-tables" in argument:
        option, tables = argument.split("=")
        print(tables)
    if argument == '-f':
        length = arguments[arguments.index(argument) + 1]
        print(length)
    elif "--fat-length" in argument:
        option, length = argument.split("=")
        print(length)
