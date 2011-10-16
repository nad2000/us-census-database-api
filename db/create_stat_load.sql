SELECT
  concat( field_code, ' = ',
    if( field_type='N', 'cast( ',''),
  'trim(substring( @line, ', CAST( start_pos AS CHAR(10)),',',CAST( field_len AS CHAR(10)),'))',
    if( field_type='N', ' AS SIGNED )',''),
  ',' )
FROM file_field
ORDER BY start_pos;


/* -- Model
LOAD DATA CONCURRENT -- LOCAL
    INFILE 'E:\\2010-08-05_EU_pitch_SHORTENED'
    IGNORE -- REPLACE
    INTO TABLE proof_of_concept
    -- FIELDS TERMINATED BY '' 
    -- ENCLOSED BY ''
    LINES TERMINATED BY '\n'
    -- LINES TERMINATED BY '\r\n'
    -- IGNORE 1 LINES
    ( @line)
    SET
    f1 = substring( @line, 1, 35),
    f2 = substring( @line, 36, 11);
*/

DELETE FROM demographic_profile WHERE STUSAB='AK';

ALTER TABLE demographic_profile DISABLE KEYS;

LOAD DATA LOCAL
    INFILE 'E:\\projects\\us-census-database-api\\data\\akgeo2010.dp'
    IGNORE -- REPLACE
    INTO TABLE demographic_profile
    -- FIELDS TERMINATED BY ''
    -- ENCLOSED BY ''
    LINES TERMINATED BY '\n'
    -- LINES TERMINATED BY '\r\n'
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
