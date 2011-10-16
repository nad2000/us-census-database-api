.separator |

DELETE FROM demographic_profile;
.import ../data/demographic_profile.txt demographic_profile

DELETE FROM matrix;
.import ../data/matrix.txt matrix

.quit
