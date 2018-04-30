import hashlib
import os
import struct

PartitionTypes = {
'0x0': "Empty",
'0x1': "DOS 12-bit FAT",
'0x4': "DOS 16-bit FAT for partitions smaller than 32 MB",
'0x5': "Extended partition",
'0x6': "DOS 16-bit FAT for partitions larger than 32 MB",
'0x7': "NTFS",
'0x8': "AIX bootable partition",
'0x9': "AIX data partition",
'0xb': "DOS 32-bit FAT",
'0xc': "DOS 32-bit FAT for interrupt 13 support",
'0x17': "Hidden NTFS partition (XP and earlier)",
'0x1b': "Hidden FAT32 partition",
'0x1e': "Hidden VFAT partition",
'0x3c': "Partition Magic recovery partition",
'0x66': "Novell partition",
'0x67': "Novell partition",
'0x68': "Novell partition",
'0x69': "Novell partition",
'0x81': "Linux",
'0x82': "Linux swap partition",
'0x83': "Linux native file systems (Ext2, Ext3, Reiser, xiafs)",
'0x86': "FAT 16 volume/stripe set (Windows NT)",
'0x87': "High Performance File System (HPFS) fault-tolerant mirrored partition or NTFS volume/stripe set",
'0xa5': "FreeBSD and BSD/386",
'0xa6': "OpenBSD",
'0xa9': "NetBSD",
'0xc7': "Typical of a corrupted NTFS volume/stripe set",
'0xeb': "BeOS",
}

file_path = raw_input()
head, tail = os.path.split(file_path)
file_name, file_format = tail.split(".")
md5 = hashlib.md5()
sha1 = hashlib.sha1()
file_size = os.path.getsize(file_path)
boot_sector_size = 512

with open(file_path, 'rb') as file_object:
	data = file_object.read(file_size)
	md5.update(data)
	sha1.update(data)

with open(file_path, 'rb') as file_object:
	MBR_data = file_object.read(boot_sector_size) #read first 512 bytes

#first partition
ptype = struct.unpack("<B", MBR_data[450:451])
if hex(ptype[0]) in PartitionTypes:
	hex_value = hex(ptype[0])
	partition_type = PartitionTypes[hex(ptype[0])]
start_address = struct.unpack("<L", MBR_data[454:458])
partition_size = struct.unpack("<L", MBR_data[458:462])
print("({:0>2}) {}, {:0>10}, {:0>10}".format(hex_value.lstrip('0x'), partition_type, start_address[0], partition_size[0]))
if hex(ptype[0]) == '0xb' or hex(ptype[0]) == '0xc':
	print(start_address)


#second partition
ptype = struct.unpack("<B", MBR_data[466:467])
if hex(ptype[0]) in PartitionTypes:
	hex_value = hex(ptype[0])
	partition_type = PartitionTypes[hex(ptype[0])]
start_address = struct.unpack("<L", MBR_data[470:474])
partition_size = struct.unpack("<L", MBR_data[474:478])
print("({:0>2}) {}, {:0>10}, {:0>10}".format(hex_value.lstrip('0x'), partition_type, start_address[0], partition_size[0]))

#third partition
ptype = struct.unpack("<B", MBR_data[482:483])
if hex(ptype[0]) in PartitionTypes:
	hex_value = hex(ptype[0])
	partition_type = PartitionTypes[hex(ptype[0])]
start_address = struct.unpack("<L", MBR_data[486:490])
partition_size = struct.unpack("<L", MBR_data[490:494])
print("({:0>2}) {}, {:0>10}, {:0>10}".format(hex_value.lstrip('0x'), partition_type, start_address[0], partition_size[0]))

#fourth partition
ptype = struct.unpack("<B", MBR_data[498:499])
if hex(ptype[0]) in PartitionTypes:
	hex_value = hex(ptype[0])
	partition_type = PartitionTypes[hex(ptype[0])]
start_address = struct.unpack("<L", MBR_data[502:506])
partition_size = struct.unpack("<L", MBR_data[506:510])
print("({:0>2}) {}, {:0>10}, {:0>10}".format(hex_value.lstrip('0x'), partition_type, start_address[0], partition_size[0]))

#FAT16/32 partition
first = struct.unpack(">L", MBR_data[0:4])
second = struct.unpack(">L", MBR_data[4:8])
third = struct.unpack(">L", MBR_data[8:12])
fourth = struct.unpack(">L", MBR_data[12:16])

print(hex(first[0]))
print(hex(second[0]))
print(hex(third[0]))
print(hex(fourth[0]))

print(file_name)
print(md5.hexdigest())
print(sha1.hexdigest())
