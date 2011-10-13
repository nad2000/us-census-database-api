SELECT
  concat( f.field_id, ' = substring( @line, ', CAST( start_pos AS CHAR(10)),',',CAST( field_len AS CHAR(10)),'),' )
FROM field AS f JOIN field_position AS fp
  ON fp.field_id=f.field_id;


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

