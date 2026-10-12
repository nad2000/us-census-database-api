#-------------------------------------------------------------------------------
# Name:        US Census File import into MySQL DB
# Purpose:
#
# Author:      Radomirs Cirskis
#
# Created:     13/10/2011
# Copyright:   (c) nowITworks.eu 2011
# Licence:     WTFPL
#-------------------------------------------------------------------------------
#!/usr/bin/env python

import sys
import os
import os.path
import argparse
import datetime
import glob
import time
import tempfile
import re

def getArgs():
    """
    Command argument parser

    Returns structure:
        args.server
        args.port
        args.db
        args.user
        args.password
        args.input
        args.source

    """
    parser = argparse.ArgumentParser(description="""
US Census Demographic Profile File import into MySQL DB, e.g.,\n\n\

import.py -S B data\\\n
""")
    parser.add_argument( '-s', '--server', help='Server', default='localhost')
    parser.add_argument( '-P', '--port', help='Server communication port', default=3306)
    parser.add_argument( '-d', '--db', help='Database, e.g., cdrg_alpha', default='uscensus2010')
    parser.add_argument( '-u', '--user', help='DB User', default='root')
    parser.add_argument( '-p', '--password', help='User password', default='')
    parser.add_argument( '-S', '--source', help='Data source: G - geographic header file, D - data file, B - both', default='B')
    parser.add_argument( 'input',
      help='US Census Demographic Profile File data file or directory containing files',
      default=os.path.join( os.path.dirname( __file__ ), 'data') )

    args = parser.parse_args()
    return args

def getScriptAbsPath( scriptName ):
    if os.name == 'posix':
	    return os.path.join( os.getcwd(), scriptName )
    else:
        return os.path.join( os.path.dirname( __file__ ), scriptName )

def setMySqlCommand( args):
    """
    Create mysql command with parameters for executing a script file
    """
    global sqlCmd
    sqlCmd = "mysql -u%(user)s -h%(host)s -P%(port)s -D%(db)s -v -v -v -f " % {
        'host': args.server,
        'user': args.user,
        'db'  : args.db,
        'port': args.port
    }
    if args.password!= None and args.password!='':
        sqlCmd += " -p%s " % args.password
    return sqlCmd

def getMySqlCommand():
    """
    a gloal variable wrapper
    """
    global sqlCmd
    if not(sqlCmd) or sqlCmd=='':
      args = getArgs()
      setMySqlCommand( args)
    return sqlCmd

def startTimer():
    """
    Sets/resets timer
    """
    global g_time_start
    g_time_start = time.time()

def getTimeSpent():
    """
    Get time (seconds) spent
    """
    global g_time_start
    return (time.time()-g_time_start)

def getDateFromFileName( file_name):
    """
    Extracts date from the file name like "xxx YYYY-MM-DD xxx"
    """
    date_match = re.search('(20\d\d-[01]\d-[0-3]\d)', file_name )

    return date_match.group(1)

def getUSStateFromFileName( file_name):
    """
    Extracts State Code (State/U.S.-Abbreviation (USPS))
    from the file name like "ca000012010.dp"

    Return:
      State Code converted in upper case
    """
    return os.path.basename( file_name)[0:2].upper()

def showMsg( message):
    """
    Displays a message printing it to the standart streem STDERR
    """
    sys.stderr.write( message+'\n' )

def loadRawData( file_name, data_source='G'):
    """
    Loads all rows, skipping the header row, from CSV file.
    """
    if not( data_source in ['G','D']):
      return

    tempScript = tempfile.mktemp('.sql')
    f = open( tempScript, 'w' )
    if data_source == 'D':
      sql = """
DELETE FROM matrix WHERE STUSAB='%(state)s';

ALTER TABLE matrix DISABLE KEYS;

LOAD DATA LOCAL
    INFILE '%(file)s'
    REPLACE -- IGNORE --
    INTO TABLE matrix
    FIELDS TERMINATED BY ','
    -- ENCLOSED BY ''
    LINES TERMINATED BY '\\n'
    -- LINES TERMINATED BY '\\r\\n'
    -- IGNORE 1 LINES
    ( FILEID,
      STUSAB,
      CHARITER,
      CIFSN,
      LOGRECNO,
      dpsf0010001,
      dpsf0010002,
      dpsf0010003,
      dpsf0010004,
      dpsf0010005,
      dpsf0010006,
      dpsf0010007,
      dpsf0010008,
      dpsf0010009,
      dpsf0010010,
      dpsf0010011,
      dpsf0010012,
      dpsf0010013,
      dpsf0010014,
      dpsf0010015,
      dpsf0010016,
      dpsf0010017,
      dpsf0010018,
      dpsf0010019,
      dpsf0010020,
      dpsf0010021,
      dpsf0010022,
      dpsf0010023,
      dpsf0010024,
      dpsf0010025,
      dpsf0010026,
      dpsf0010027,
      dpsf0010028,
      dpsf0010029,
      dpsf0010030,
      dpsf0010031,
      dpsf0010032,
      dpsf0010033,
      dpsf0010034,
      dpsf0010035,
      dpsf0010036,
      dpsf0010037,
      dpsf0010038,
      dpsf0010039,
      dpsf0010040,
      dpsf0010041,
      dpsf0010042,
      dpsf0010043,
      dpsf0010044,
      dpsf0010045,
      dpsf0010046,
      dpsf0010047,
      dpsf0010048,
      dpsf0010049,
      dpsf0010050,
      dpsf0010051,
      dpsf0010052,
      dpsf0010053,
      dpsf0010054,
      dpsf0010055,
      dpsf0010056,
      dpsf0010057,
      dpsf0020001,
      dpsf0020002,
      dpsf0020003,
      dpsf0030001,
      dpsf0030002,
      dpsf0030003,
      dpsf0040001,
      dpsf0040002,
      dpsf0040003,
      dpsf0050001,
      dpsf0050002,
      dpsf0050003,
      dpsf0060001,
      dpsf0060002,
      dpsf0060003,
      dpsf0070001,
      dpsf0070002,
      dpsf0070003,
      dpsf0080001,
      dpsf0080002,
      dpsf0080003,
      dpsf0080004,
      dpsf0080005,
      dpsf0080006,
      dpsf0080007,
      dpsf0080008,
      dpsf0080009,
      dpsf0080010,
      dpsf0080011,
      dpsf0080012,
      dpsf0080013,
      dpsf0080014,
      dpsf0080015,
      dpsf0080016,
      dpsf0080017,
      dpsf0080018,
      dpsf0080019,
      dpsf0080020,
      dpsf0080021,
      dpsf0080022,
      dpsf0080023,
      dpsf0080024,
      dpsf0090001,
      dpsf0090002,
      dpsf0090003,
      dpsf0090004,
      dpsf0090005,
      dpsf0090006,
      dpsf0100001,
      dpsf0100002,
      dpsf0100003,
      dpsf0100004,
      dpsf0100005,
      dpsf0100006,
      dpsf0100007,
      dpsf0110001,
      dpsf0110002,
      dpsf0110003,
      dpsf0110004,
      dpsf0110005,
      dpsf0110006,
      dpsf0110007,
      dpsf0110008,
      dpsf0110009,
      dpsf0110010,
      dpsf0110011,
      dpsf0110012,
      dpsf0110013,
      dpsf0110014,
      dpsf0110015,
      dpsf0110016,
      dpsf0110017,
      dpsf0120001,
      dpsf0120002,
      dpsf0120003,
      dpsf0120004,
      dpsf0120005,
      dpsf0120006,
      dpsf0120007,
      dpsf0120008,
      dpsf0120009,
      dpsf0120010,
      dpsf0120011,
      dpsf0120012,
      dpsf0120013,
      dpsf0120014,
      dpsf0120015,
      dpsf0120016,
      dpsf0120017,
      dpsf0120018,
      dpsf0120019,
      dpsf0120020,
      dpsf0130001,
      dpsf0130002,
      dpsf0130003,
      dpsf0130004,
      dpsf0130005,
      dpsf0130006,
      dpsf0130007,
      dpsf0130008,
      dpsf0130009,
      dpsf0130010,
      dpsf0130011,
      dpsf0130012,
      dpsf0130013,
      dpsf0130014,
      dpsf0130015,
      dpsf0140001,
      dpsf0150001,
      dpsf0160001,
      dpsf0170001,
      dpsf0180001,
      dpsf0180002,
      dpsf0180003,
      dpsf0180004,
      dpsf0180005,
      dpsf0180006,
      dpsf0180007,
      dpsf0180008,
      dpsf0180009,
      dpsf0190001,
      dpsf0200001,
      dpsf0210001,
      dpsf0210002,
      dpsf0210003,
      dpsf0220001,
      dpsf0220002,
      dpsf0230001,
      dpsf0230002);

ALTER TABLE matrix ENABLE KEYS;
"""
    else:
      sql = """
DELETE FROM demographic_profile WHERE STUSAB='%(state)s';

ALTER TABLE demographic_profile DISABLE KEYS;

LOAD DATA LOCAL
    INFILE '%(file)s'
    IGNORE -- REPLACE
    INTO TABLE demographic_profile
    -- FIELDS TERMINATED BY ''
    -- ENCLOSED BY ''
    LINES TERMINATED BY '\\n'
    -- LINES TERMINATED BY '\\r\\n'
    -- IGNORE 1 LINES
    ( @line)
	SET
		FILEID = trim(substring( @line, 1,6)),
		STUSAB = trim(substring( @line, 7,2)),
		SUMLEV = trim(substring( @line, 9,3)),
		GEOCOMP = trim(substring( @line, 12,2)),
		CHARITER = trim(substring( @line, 14,3)),
		CIFSN = trim(substring( @line, 17,2)),
		LOGRECNO = cast( trim(substring( @line, 19,7)) AS SIGNED ),
		REGION = trim(substring( @line, 26,1)),
		DIVISION = trim(substring( @line, 27,1)),
		`STATE` = trim(substring( @line, 28,2)),
		COUNTY = trim(substring( @line, 30,3)),
		COUNTYCC = trim(substring( @line, 33,2)),
		COUNTYSC = trim(substring( @line, 35,2)),
		COUSUB = trim(substring( @line, 37,5)),
		COUSUBCC = trim(substring( @line, 42,2)),
		COUSUBSC = trim(substring( @line, 44,2)),
		PLACE = trim(substring( @line, 46,5)),
		PLACECC = trim(substring( @line, 51,2)),
		PLACESC = trim(substring( @line, 53,2)),
		TRACT = trim(substring( @line, 55,6)),
		BLKGRP = trim(substring( @line, 61,1)),
		BLOCK = trim(substring( @line, 62,4)),
		IUC = trim(substring( @line, 66,2)),
		CONCIT = trim(substring( @line, 68,5)),
		CONCITCC = trim(substring( @line, 73,2)),
		CONCITSC = trim(substring( @line, 75,2)),
		AIANHH = trim(substring( @line, 77,4)),
		AIANHHFP = trim(substring( @line, 81,5)),
		AIANHHCC = trim(substring( @line, 86,2)),
		AIHHTLI = trim(substring( @line, 88,1)),
		AITSCE = trim(substring( @line, 89,3)),
		AITS = trim(substring( @line, 92,5)),
		AITSCC = trim(substring( @line, 97,2)),
		TTRACT = trim(substring( @line, 99,6)),
		TBLKGRP = trim(substring( @line, 105,1)),
		ANRC = trim(substring( @line, 106,5)),
		ANRCCC = trim(substring( @line, 111,2)),
		CBSA = trim(substring( @line, 113,5)),
		CBSASC = trim(substring( @line, 118,2)),
		METDIV = trim(substring( @line, 120,5)),
		CSA = trim(substring( @line, 125,3)),
		NECTA = trim(substring( @line, 128,5)),
		NECTASC = trim(substring( @line, 133,2)),
		NECTADIV = trim(substring( @line, 135,5)),
		CNECTA = trim(substring( @line, 140,3)),
		CBSAPCI = trim(substring( @line, 143,1)),
		NECTAPCI = trim(substring( @line, 144,1)),
		UA = trim(substring( @line, 145,5)),
		UASC = trim(substring( @line, 150,2)),
		UATYPE = trim(substring( @line, 152,1)),
		UR = trim(substring( @line, 153,1)),
		CD = trim(substring( @line, 154,2)),
		SLDU = trim(substring( @line, 156,3)),
		SLDL = trim(substring( @line, 159,3)),
		VTD = trim(substring( @line, 162,6)),
		VTDI = trim(substring( @line, 168,1)),
		RESERVE2 = trim(substring( @line, 169,3)),
		ZCTA5 = trim(substring( @line, 172,5)),
		SUBMCD = trim(substring( @line, 177,5)),
		SUBMCDCC = trim(substring( @line, 182,2)),
		SDELM = trim(substring( @line, 184,5)),
		SDSEC = trim(substring( @line, 189,5)),
		SDUNI = trim(substring( @line, 194,5)),
		AREALAND = cast( trim(substring( @line, 199,14)) AS SIGNED ),
		AREAWATR = cast( trim(substring( @line, 213,14)) AS SIGNED ),
		NAME = trim(substring( @line, 227,90)),
		FUNCSTAT = trim(substring( @line, 317,1)),
		GCUNI = trim(substring( @line, 318,1)),
		POP100 = cast( trim(substring( @line, 319,9)) AS SIGNED ),
		HU100 = cast( trim(substring( @line, 328,9)) AS SIGNED ),
		INTPTLAT = trim(substring( @line, 337,11)),
		INTPTLON = trim(substring( @line, 348,12)),
		LSADC = trim(substring( @line, 360,2)),
		PARTFLAG = trim(substring( @line, 362,1)),
		RESERVE3 = trim(substring( @line, 363,6)),
		UGA = trim(substring( @line, 369,5)),
		STATENS = trim(substring( @line, 374,8)),
		COUNTYNS = trim(substring( @line, 382,8)),
		COUSUBNS = trim(substring( @line, 390,8)),
		PLACENS = trim(substring( @line, 398,8)),
		CONCITNS = trim(substring( @line, 406,8)),
		AIANHHNS = trim(substring( @line, 414,8)),
		AITSNS = trim(substring( @line, 422,8)),
		ANRCNS = trim(substring( @line, 430,8)),
		SUBMCDNS = trim(substring( @line, 438,8)),
		CD113 = trim(substring( @line, 446,2)),
		CD114 = trim(substring( @line, 448,2)),
		CD115 = trim(substring( @line, 450,2)),
		SLDU2 = trim(substring( @line, 452,3)),
		SLDU3 = trim(substring( @line, 455,3)),
		SLDU4 = trim(substring( @line, 458,3)),
		SLDL2 = trim(substring( @line, 461,3)),
		SLDL3 = trim(substring( @line, 464,3)),
		SLDL4 = trim(substring( @line, 467,3)),
		AIANHHSC = trim(substring( @line, 470,2)),
		CSASC = trim(substring( @line, 472,2)),
		CNECTASC = trim(substring( @line, 474,2)),
		MEMI = trim(substring( @line, 476,1)),
		NMEMI = trim(substring( @line, 477,1)),
		PUMA = trim(substring( @line, 478,5)),
		RESERVED = trim(substring( @line, 483,18));

ALTER TABLE demographic_profile ENABLE KEYS;
"""
    f.write( sql % {
        'file':file_name.replace('\\','\\\\'),
        'state':getUSStateFromFileName( file_name) } )
    f.close()
    cmd = getMySqlCommand()+"<\""+tempScript+"\""
    os.system( cmd  )

def processRows():
    """
    Invokes process_rows.sql to process loaded rows from the CSV file
    """
    cmd = getMySqlCommand()+"<\""+ getScriptAbsPath('process_rows.sql') +"\""
    os.system( cmd  )

def processFileList( file_list, data_source='G'):
  """
  Process list of files
  """
  totalRowCount = 0
  for f in file_list:
    data_load_start = time.time()
    loadRawData(f, data_source)
    showMsg( "--- Data import from %s completed in %.5f sec.\n"
        % (f, (time.time()-data_load_start)) )


def main():
  """
  1. parse parameters;
  2. loops through the file list (one file or all in the directory);
  3. loads file and prcesses it;
  """
  time_start = time.time()
  args = getArgs()
  setMySqlCommand( args)
  # data source:
  source = os.path.abspath( args.input)

  if not os.path.exists( source ):
    raise Exception("File %s doesn't exist!" % args.input)

  if (args.source  in ['G','B']):
    if os.path.isfile( source):
      file_list = [source]
    else:
      file_list = glob.glob(os.path.join( source, '*geo2010.dp' ) )
    processFileList( file_list, 'G' )
  if (args.source  in ['D','B']):
    if os.path.isfile( source):
      file_list = [source]
    else:
      file_list = glob.glob(os.path.join( source, '*000012010.dp' ) )
    processFileList( file_list, 'D' )

  showMsg( "Data processing completed in %.5f sec."
      % (time.time()-time_start))


if __name__ == '__main__':
    main()
