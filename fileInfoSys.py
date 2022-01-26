from __future__ import print_function

import os
import stat
import sys
import time

if sys.version_info >= (3, 0):
    raw_input = input

file_name = raw_input("Enter a file name: ")
count = 0
t_char = 0

try:
    with open(file_name) as f:
        count = (sum(1 for line in f))
        f.seek(0)
        t_char = (sum([len(line) for line in f]))
except FileNotFoundError as e:
    print(e)
    sys.exit(1)
except IOError:
    pass
except IsADirectoryError:
    pass

file_stats = os.stat(file_name)

file_info_keys = ('file name', 'file size', 'last modified', 'last accessed',
                  'creation time', 'Total number of lines are',
                  'Total number of characters are')
file_info_vales = (file_name, str(file_stats[stat.ST_SIZE]) + " bytes",
                   time.strftime("%d/%m/%Y %I:%M:%S %p",time.localtime(file_stats[stat.ST_MTIME])),
                   time.strftime("%d/%m/%Y %I:%M:%S %p",time.localtime(file_stats[stat.ST_ATIME])),
                   time.strftime("%d/%m/%Y %I:%M:%S %p",time.localtime(file_stats[stat.ST_CTIME])),
                   count, t_char)

for f_key, f_value in zip(file_info_keys, file_info_vales):
    print(f_key, ' =', f_value)


if stat.S_ISDIR(file_stats[stat.ST_MODE]):
    print("This a directory.")
else:
    file_stats_fmt = ''
    print("\nThis is not a directory.")
    stats_keys = ("st_mode", "st_ino (inode number)",
                  "st_dev (device)", "st_nlink (number of hard links)",
                  "st_uid (user ID of owner)", "st_gid (group ID of owner)",
                  "st_size (file size bytes)",
                  "st_atime (last access time seconds since epoch)",
                  "st_mtime (last modification time)",
                  "st_ctime (time of creation Windows)")
    for s_key, s_value in zip(stats_keys, file_stats):
        print(s_key, ' =', s_value)
