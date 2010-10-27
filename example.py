#!/usr/bin/python

"""
Author: SpliFF
License: Public Domain

Example usage of ioctl module

!! WARNING EXPERIMENTAL SOFTWARE !!
I don't recommend using this example on any important data. Both btrfs and the ioctl module are highly experimental!
"""

import ioctl
import fcntl

# constant for sizeof(int)
INT = 4

# these are actual ioctl constants from the btrfs kernel module
BTRFS_IOCTL_MAGIC = 0x94
BTRFS_IOC_SYNC =  ioctl.IO(BTRFS_IOCTL_MAGIC, 8)
BTRFS_IOC_CLONE = ioctl.IOW(BTRFS_IOCTL_MAGIC, 9, INT)

print("BTRFS_IOCTL_MAGIC:", BTRFS_IOCTL_MAGIC)
print("BTRFS_IOC_SYNC:", BTRFS_IOC_SYNC)
print("BTRFS_IOC_CLONE:", BTRFS_IOC_CLONE)

# change these to some files you don't mind destroying
srcfd = open('/some/file/on/btrfs','rb')
dstfd = open('/some/file/on/same/btrfs/partition','wb')

# this should perform a "copy on write" operation which makes the destination file a clone of the source (sharing same blocks on disk)
ret = fcntl.ioctl(srcfd.fileno(), BTRFS_IOC_CLONE, dstfd.fileno())

# this should sync the destination file, committing any buffered writes to disk
ret = fcntl.ioctl(dstfd.fileno(), BTRFS_IOC_SYNC)
