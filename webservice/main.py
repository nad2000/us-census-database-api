#-------------------------------------------------------------------------------
# Name:       main.py
# Purpose:    REST JSON Web Service for querying US census 2010 data
#
#
# Author:     Radomirs Cirskis
#
# Created:    20/10/2011
# Copyright:  (c) nowITworks.eu 2011
# Licence:    WTFPL
#-------------------------------------------------------------------------------
#!/usr/bin/env python

import webapp2, sqlite3, os.path
import simplejson as json

def set_trace():
  """
  Support for debugging GAE application.
  Alsternatively you can start debugging running:
  python -m pdb main.py <app dir>
  """
  # ignore, if it's not "localhost"
  if not( webapp2.get_request().environ['SERVER_NAME'] in ['localhost','127.0.0.1','0.0.0.0'] ):
      return
  import pdb, sys
  debugger = pdb.Pdb(stdin=sys.__stdin__,
      stdout=sys.__stdout__)
  debugger.set_trace(sys._getframe().f_back)

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


def get_data( zip_code):
  """
  Selects and returs all data for given ZIP Code
  """
  cn = sqlite3.connect( os.path.join( os.path.dirname( __file__ ), 'db', 'uscensus2010.db' ) )
  cn.row_factory = lambda cursor, row: { col[0]:row[idx] for idx, col in enumerate(cursor.description)}
  c = cn.execute(
"""SELECT r.* FROM record AS r JOIN ZCTA_MA AS m
  ON r.STATE=m.statefips AND r.COUNTY=m.countyfips AND r.COUSUB=m.mcdfips
WHERE m.zcta=?""", (zip_code,))
  return c.fetchall()

def handle_request( request, *args, **kwargs):
  #set_trace()
  zip_code = args[0]
  records = get_data(zip_code)
  response = webapp2.Response()
  response.headers.add_header('Content-type', 'application/json')
  json.dump( records, response.out)
  return response

app = webapp2.WSGIApplication([
    (r'/records/([A-Za-z0-9]+)', handle_request),
], debug=True)


def main():
  from paste import httpserver
  httpserver.serve(app, host='0.0.0.0', port='9999')

if __name__ == '__main__':
    main()
