SELECT * INTO OUTFILE 'demographic_profile.csv'
FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '"'
LINES TERMINATED BY '\n'
FROM uscensus2010.demographic_profile;