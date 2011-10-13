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

    """
    parser = argparse.ArgumentParser(description='US Census Demographic Profile File import into MySQL DB')
    parser.add_argument( '-s', '--server', help='Server', default='localhost')
    parser.add_argument( '-P', '--port', help='Server communication port', default=3306)
    parser.add_argument( '-d', '--db', help='Database, e.g., cdrg_alpha', default='uscensus2010')
    parser.add_argument( '-u', '--user', help='DB User', default='root')
    parser.add_argument( '-p', '--password', help='User password', default='')
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

def loadRawData( fileName):
    """
    Loads all rows, skipping the header row, from CSV file.
    """

    tempScript = tempfile.mktemp('.sql')
    f = open( tempScript, 'w' )
    f.write(
    """
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
		STUSAB = substring( @line, 7,2),
		SUMLEV = substring( @line, 9,3),
		GEOCOMP = substring( @line, 12,2),
		CHARITER = substring( @line, 14,3),
		CIFSN = substring( @line, 17,2),
		LOGRECNO = substring( @line, 19,7),
		REGION = substring( @line, 26,1),
		DIVISION = substring( @line, 27,1),
		STATECE = substring( @line, 28,2),
		`STATE` = substring( @line, 30,2),
		COUNTY = substring( @line, 32,3),
		COUNTYSC = substring( @line, 35,2),
		COUSUB = substring( @line, 37,5),
		COUSUBCC = substring( @line, 42,2),
		COUSUBSC = substring( @line, 44,2),
		PLACE = substring( @line, 46,5),
		PLACECC = substring( @line, 51,2),
		PLACESC = substring( @line, 54,2),
		TRACT = substring( @line, 56,6),
		BLKGRP = substring( @line, 62,1),
		BLOCK = substring( @line, 63,4),
		IUC = substring( @line, 67,2),
		CONCIT = substring( @line, 69,5),
		CONCITCC = substring( @line, 74,2),
		CONCITSC = substring( @line, 76,2),
		AIANHH = substring( @line, 78,4),
		AIANHHFP = substring( @line, 82,5),
		AIANHHCC = substring( @line, 87,2),
		AIHHTLI = substring( @line, 89,1),
		AITSCE = substring( @line, 90,3),
		AITS = substring( @line, 93,5),
		AITSCC = substring( @line, 98,2),
		ANRC = substring( @line, 100,5),
		ANRCCC = substring( @line, 105,2),
		MSACMSA = substring( @line, 107,4),
		MASC = substring( @line, 111,2),
		CMSA = substring( @line, 113,2),
		MACCI = substring( @line, 115,1),
		PMSA = substring( @line, 116,4),
		NECMA = substring( @line, 120,4),
		NECMACCI = substring( @line, 124,1),
		NECMASC = substring( @line, 125,2),
		EXI = substring( @line, 127,1),
		UA = substring( @line, 128,5),
		UASC = substring( @line, 133,2),
		UATYPE = substring( @line, 135,1),
		UR = substring( @line, 136,1),
		CD106 = substring( @line, 137,2),
		CD108 = substring( @line, 139,2),
		CD109 = substring( @line, 141,2),
		CD110 = substring( @line, 143,2),
		SLDU = substring( @line, 145,3),
		SLDL = substring( @line, 148,3),
		VTD = substring( @line, 151,6),
		VTDI = substring( @line, 157,1),
		ZCTA3 = substring( @line, 158,3),
		ZCTA5 = substring( @line, 161,5),
		SUBMCD = substring( @line, 166,5),
		SUBMCDCC = substring( @line, 171,2),
		AREALAND = substring( @line, 173,14),
		AREAWATR = substring( @line, 187,14),
		NAME = substring( @line, 201,90),
		FUNCSTAT = substring( @line, 291,1),
		GCUNI = substring( @line, 292,1),
		POP100 = substring( @line, 293,9),
		HU100 = substring( @line, 302,9),
		INTPTLAT = substring( @line, 311,9),
		INTPTLON = substring( @line, 320,10),
		LSADC = substring( @line, 330,2),
		PARTFLAG = substring( @line, 332,1),
		SDELM = substring( @line, 333,5),
		SDSEC = substring( @line, 338,5),
		SDUNI = substring( @line, 343,5),
		TAZ = substring( @line, 348,6),
		UGA = substring( @line, 354,5),
		PUMA5 = substring( @line, 359,5),
		PUMA1 = substring( @line, 364,5),
		RESERVE2 = substring( @line, 369,15),
		MACC = substring( @line, 384,5),
		UACP = substring( @line, 389,5),
		RESERVED = substring( @line, 394,7);


ALTER TABLE demographic_profile ENABLE KEYS;

""" % {
        'file':fileName.replace('\\','\\\\'),
        'state':getUSStateFromFileName( fileName) } )
    f.close()
    cmd = getMySqlCommand()+"<\""+tempScript+"\""
    os.system( cmd  )

def processRows():
    """
    Invokes process_rows.sql to process loaded rows from the CSV file
    """
    cmd = getMySqlCommand()+"<\""+ getScriptAbsPath('process_rows.sql') +"\""
    os.system( cmd  )

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

    # List of *geo2010.dp files:
    source = [source] if os.path.isfile( source) else glob.glob( os.path.join( source, '*geo2010.dp') )

    totalRowCount = 0
    for f in source:
      data_load_start = time.time()
      loadRawData(f)
      showMsg( "--- Data import from %s completed in %.5f sec.\n"
          % (f, (time.time()-data_load_start)) )

    showMsg( "Data processing completed in %.5f sec."
        % (time.time()-time_start))


if __name__ == '__main__':
    main()
