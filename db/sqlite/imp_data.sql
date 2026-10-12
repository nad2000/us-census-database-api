.separator |

DELETE FROM demographic_profile;
.import ../data/demographic_profile.txt demographic_profile

DELETE FROM matrix;
.import ../data/matrix.txt matrix

DELETE FROM ZCTA_MA;
.import ../data/ZCTA_MA.txt ZCTA_MA

.quit
