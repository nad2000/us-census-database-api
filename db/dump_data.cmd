REM mysqldump -e --skip-add-drop-table --skip-add-locks --skip-comments --skip-opt --skip-quote-names --quick --no-create-db --no-create-info --extended-insert uscensus2010 demographic_profile > data\load_data.sql
mysqldump --skip-add-drop-table --skip-add-locks --skip-comments --skip-opt --skip-quote-names --quick --no-create-db --no-create-info --extended-insert uscensus2010 demographic_profile > data\load_data.sql
REM mysqldump -t -T./data uscensus2010 --fields-enclosed-by=\" --fields-terminated-by=,
mysqldump -t -T./data uscensus2010 --fields-terminated-by="|" --fields-enclosed-by=   --user=root


