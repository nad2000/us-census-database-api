-- DROP TABLE IF EXISTS record;

/*
The 2010 Census Demographic Profile Summary File records:
- Geografic header and data rows merged together.
*/
CREATE TABLE IF NOT EXISTS record 
AS 
SELECT
    g.id, g.FILEID, g.STUSAB, g.SUMLEV, g.GEOCOMP, g.CHARITER, g.CIFSN, g.LOGRECNO, 
    g.REGION, g.DIVISION, g.STATE, g.COUNTY, g.COUNTYCC, g.COUNTYSC, g.COUSUB, g.COUSUBCC, g.COUSUBSC, 
    g.PLACE, g.PLACECC, g.PLACESC, g.TRACT, g.BLKGRP, g.BLOCK, g.IUC, g.CONCIT, g.CONCITCC, g.CONCITSC, 
    g.AIANHH, g.AIANHHFP, g.AIANHHCC, g.AIHHTLI, g.AITSCE, g.AITS, g.AITSCC, g.TTRACT, g.TBLKGRP, g.ANRC, 
    g.ANRCCC, g.CBSA, g.CBSASC, g.METDIV, g.CSA, g.NECTA, g.NECTASC, g.NECTADIV, g.CNECTA, g.CBSAPCI, 
    g.NECTAPCI, g.UA, g.UASC, g.UATYPE, g.UR, g.CD, g.SLDU, g.SLDL, g.VTD, g.VTDI, g.RESERVE2, g.ZCTA5, 
    g.SUBMCD, g.SUBMCDCC, g.SDELM, g.SDSEC, g.SDUNI, g.AREALAND, g.AREAWATR, g.NAME, g.FUNCSTAT, g.GCUNI, 
    g.POP100, g.HU100, g.INTPTLAT, g.INTPTLON, g.LSADC, g.PARTFLAG, g.RESERVE3, g.UGA, g.STATENS, g.COUNTYNS, 
    g.COUSUBNS, g.PLACENS, g.CONCITNS, g.AIANHHNS, g.AITSNS, g.ANRCNS, g.SUBMCDNS, g.CD113, g.CD114, g.CD115, 
    g.SLDU2, g.SLDU3, g.SLDU4, g.SLDL2, g.SLDL3, g.SLDL4, g.AIANHHSC, g.CSASC, g.CNECTASC, g.MEMI, g.NMEMI, 
    g.PUMA, g.RESERVED,
    /* m.id, m.FILEID, m.STUSAB, m.CHARITER, m.CIFSN, m.LOGRECNO,*/ 
    m.dpsf0010001, m.dpsf0010002, m.dpsf0010003, m.dpsf0010004, m.dpsf0010005, m.dpsf0010006, m.dpsf0010007, 
    m.dpsf0010008, m.dpsf0010009, m.dpsf0010010, m.dpsf0010011, m.dpsf0010012, m.dpsf0010013, m.dpsf0010014, 
    m.dpsf0010015, m.dpsf0010016, m.dpsf0010017, m.dpsf0010018, m.dpsf0010019, m.dpsf0010020, m.dpsf0010021, 
    m.dpsf0010022, m.dpsf0010023, m.dpsf0010024, m.dpsf0010025, m.dpsf0010026, m.dpsf0010027, m.dpsf0010028, 
    m.dpsf0010029, m.dpsf0010030, m.dpsf0010031, m.dpsf0010032, m.dpsf0010033, m.dpsf0010034, m.dpsf0010035, 
    m.dpsf0010036, m.dpsf0010037, m.dpsf0010038, m.dpsf0010039, m.dpsf0010040, m.dpsf0010041, m.dpsf0010042, 
    m.dpsf0010043, m.dpsf0010044, m.dpsf0010045, m.dpsf0010046, m.dpsf0010047, m.dpsf0010048, m.dpsf0010049, 
    m.dpsf0010050, m.dpsf0010051, m.dpsf0010052, m.dpsf0010053, m.dpsf0010054, m.dpsf0010055, m.dpsf0010056, 
    m.dpsf0010057, m.dpsf0020001, m.dpsf0020002, m.dpsf0020003, m.dpsf0030001, m.dpsf0030002, m.dpsf0030003, 
    m.dpsf0040001, m.dpsf0040002, m.dpsf0040003, m.dpsf0050001, m.dpsf0050002, m.dpsf0050003, m.dpsf0060001, 
    m.dpsf0060002, m.dpsf0060003, m.dpsf0070001, m.dpsf0070002, m.dpsf0070003, m.dpsf0080001, m.dpsf0080002, 
    m.dpsf0080003, m.dpsf0080004, m.dpsf0080005, m.dpsf0080006, m.dpsf0080007, m.dpsf0080008, m.dpsf0080009, 
    m.dpsf0080010, m.dpsf0080011, m.dpsf0080012, m.dpsf0080013, m.dpsf0080014, m.dpsf0080015, m.dpsf0080016, 
    m.dpsf0080017, m.dpsf0080018, m.dpsf0080019, m.dpsf0080020, m.dpsf0080021, m.dpsf0080022, m.dpsf0080023, 
    m.dpsf0080024, m.dpsf0090001, m.dpsf0090002, m.dpsf0090003, m.dpsf0090004, m.dpsf0090005, m.dpsf0090006, 
    m.dpsf0100001, m.dpsf0100002, m.dpsf0100003, m.dpsf0100004, m.dpsf0100005, m.dpsf0100006, m.dpsf0100007, 
    m.dpsf0110001, m.dpsf0110002, m.dpsf0110003, m.dpsf0110004, m.dpsf0110005, m.dpsf0110006, m.dpsf0110007, 
    m.dpsf0110008, m.dpsf0110009, m.dpsf0110010, m.dpsf0110011, m.dpsf0110012, m.dpsf0110013, m.dpsf0110014, 
    m.dpsf0110015, m.dpsf0110016, m.dpsf0110017, m.dpsf0120001, m.dpsf0120002, m.dpsf0120003, m.dpsf0120004, 
    m.dpsf0120005, m.dpsf0120006, m.dpsf0120007, m.dpsf0120008, m.dpsf0120009, m.dpsf0120010, m.dpsf0120011, 
    m.dpsf0120012, m.dpsf0120013, m.dpsf0120014, m.dpsf0120015, m.dpsf0120016, m.dpsf0120017, m.dpsf0120018, 
    m.dpsf0120019, m.dpsf0120020, m.dpsf0130001, m.dpsf0130002, m.dpsf0130003, m.dpsf0130004, m.dpsf0130005, 
    m.dpsf0130006, m.dpsf0130007, m.dpsf0130008, m.dpsf0130009, m.dpsf0130010, m.dpsf0130011, m.dpsf0130012, 
    m.dpsf0130013, m.dpsf0130014, m.dpsf0130015, m.dpsf0140001, m.dpsf0150001, m.dpsf0160001, m.dpsf0170001, 
    m.dpsf0180001, m.dpsf0180002, m.dpsf0180003, m.dpsf0180004, m.dpsf0180005, m.dpsf0180006, m.dpsf0180007, 
    m.dpsf0180008, m.dpsf0180009, m.dpsf0190001, m.dpsf0200001, m.dpsf0210001, m.dpsf0210002, m.dpsf0210003, 
    m.dpsf0220001, m.dpsf0220002, m.dpsf0230001, m.dpsf0230002
FROM geoheader AS g JOIN matrix AS m
    ON m.STUSAB=g.STUSAB AND m.LOGRECNO=g.LOGRECNO;

DROP INDEX record_idx ON record;

CREATE INDEX record_idx ON record( state, county, cousub );