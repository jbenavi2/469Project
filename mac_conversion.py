import sys

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'June', 'July', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec']
arguments = sys.argv
print(len(sys.argv))
print(arguments)

if arguments[1] == '-T':
    conversion = 'time'
else:
    conversion = 'date'

if arguments[2] == '-f':
    filename = arguments[3]
else:
    prefix, hex_value = arguments[3].split('x')

little_endian = hex_value[2:] + hex_value[0:2]
binary = format(int(little_endian, 16), '0>16b')

if conversion == 'date':
    year = binary[0:7]
    year = int(year, 2) + 1980

    month = binary[7:11]
    month = months[int(month, 2) - 1]

    day = binary[11:]
    day = int(day, 2)

    print("Date: " + month + " " + str(day) + ", " + str(year))
elif conversion == 'time':
