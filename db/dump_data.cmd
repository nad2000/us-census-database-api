REM mysqldump -e --skip-add-drop-table --skip-add-locks --skip-comments --skip-opt --skip-quote-names --quick --no-create-db --no-create-info --extended-insert uscensus2010 demographic_profile > data\load_data.sql
REM --defaults-extra-file="/tmp/tmpWMaehW/extraparams.cnf"  
REM mysqldump --skip-add-drop-table --skip-add-locks --skip-comments --skip-opt --skip-quote-names --quick --no-create-db --no-create-info --extended-insert  demographic_profile > data\load_data.sql
REM mysqldump --skip-add-drop-table --skip-add-locks --skip-comments --skip-opt --skip-quote-names --quick --no-create-db --no-create-info --extended-insert --order-by-primary=FALSE --force=FALSE --no-data=FALSE --tz-utc=TRUE --flush-privileges=FALSE --compress=TRUE --replace=TRUE --host=localhost --insert-ignore=FALSE --extended-insert=TRUE --user=root --quote-names=TRUE --hex-blob=FALSE --complete-insert=FALSE --add-locks=TRUE --disable-keys=TRUE --delayed-insert=FALSE --create-options=TRUE --delete-master-logs=FALSE --comments=TRUE --max_allowed_packet=1G --flush-logs=FALSE --dump-date=TRUE --lock-tables=TRUE --allow-keywords=FALSE --events=FALSE --databases "uscensus2010"  > data\load_data.sql
REM mysqldump -t -T./data uscensus2010 --fields-enclosed-by=\" --fields-terminated-by=,
mysqldump -t -T./data uscensus2010 --fields-terminated-by="|" --fields-enclosed-by=   --user=root


