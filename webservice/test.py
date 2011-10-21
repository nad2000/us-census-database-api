#-------------------------------------------------------------------------------
# Name:       test.py
# Purpose:    Application Unit Test
#
#
# Author:     Radomirs Cirskis
#
# Created:    22/10/2011
# Copyright:  (c) nowITworks.eu 2011
# Licence:    WTFPL
#-------------------------------------------------------------------------------
#!/usr/bin/env python

from main import *
import simplejson as json

def run_test():
  # Test the app, passing parameters to build a request.
  response = app.get_response('/records/390HH')
  assert response.status_int == 200
  records = json.loads(response.body)
  assert records[0]['dpsf0230002'] == '2.57'
  assert len(records)==9

  response = app.get_response('/records/48873')
  assert response.status_int == 200
  records = json.loads(response.body)
  assert records[0]['dpsf0230002'] == '2.33'
  assert len(records)==2

  response = app.get_response('/records/14824')
  assert response.status_int == 200
  records = json.loads(response.body)
  assert records[0]['dpsf0230002'] == '2.17'
  assert len(records)==2


if __name__ == '__main__':
  run_test()
