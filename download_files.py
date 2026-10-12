#-------------------------------------------------------------------------------
# Name:        US Census File download from FTP server
# Purpose:
#
# Author:      Radomirs Cirskis
#
# Created:     13/10/2011
# Copyright:   (c) nowITworks.eu 2011
# Licence:     WTFPL
#-------------------------------------------------------------------------------
#!/usr/bin/env python

from ftplib import FTP
import os, sys, os.path


def main():
  data_dir = os.path.join(os.path.dirname(__file__), 'data')
  ftp = FTP('ftp.census.gov','anonymous','nad2000@gmail.com')
  ftp.cwd('/census_2010/03-Demographic_Profile')
  dir_list = []
  for state_dir in ftp.nlst():
    # exclude fils
    if '.' in state_dir: continue
    file_list = ftp.nlst("%s/*dp.zip" % state_dir)
    if file_list:
      file_name = file_list[0]
      local_file_name = os.path.join(data_dir, os.path.basename(file_name))
      file = open(local_file_name, 'wb')
      ftp.retrbinary('RETR '+ file_name, file.write)
      file.close()

  ftp.close()


if __name__ == '__main__':
    main()
