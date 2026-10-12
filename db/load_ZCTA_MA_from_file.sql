TRUNCATE TABLE ZCTA_MA;

LOAD DATA LOCAL
    -- INFILE '/home/local/ENDACE/rad.cirskis/Downloads/zcta_msa/zcta_to_99msa_rel.txt'
    INFILE 'E:\\projects\\us-census-database-api\\data\\zcta_to_99msa_rel.txt'
    REPLACE -- IGNORE --
    INTO TABLE ZCTA_MA
    FIELDS TERMINATED BY '\t'
    -- ENCLOSED BY ''
    LINES TERMINATED BY '\n'
    -- LINES TERMINATED BY '\\r\\n'
    IGNORE 1 LINES
    ( msa_cmsa,pmsa,statefips,countyfips,mcdfips,zcta,@partflag)
	SET partflag = IF(trim(@partflag) LIKE '%part%', TRUE, FALSE);

