.separator |

.read cr_file_field.sql

-- .read cr_matrix.sql
-- DELETE FROM matrix;
-- .import ../data/matrix.txt matrix

-- .read cr_geoheader.sql
-- DELETE FROM geoheader;
-- .import ../data/geoheader.txt geoheader

.read cr_record.sql
DELETE FROM record;
.import ../data/record.txt record

.read cr_ZCTA_MA.sql
DELETE FROM ZCTA_MA;
.import ../data/ZCTA_MA.txt ZCTA_MA

CREATE INDEX record_idx ON record ("STATE",COUNTY,COUSUB);
CREATE UNIQUE INDEX record2_idx ON record (STUSAB,LOGRECNO);
CREATE INDEX ZCTA_MA_idx ON ZCTA_MA( zcta);


.quit
