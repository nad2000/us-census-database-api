--
-- Table structure for table `ZCTA_MA`
--

DROP TABLE IF EXISTS `ZCTA_MA`;

CREATE TABLE `ZCTA_MA` (
  `msa_cmsa` char(4) DEFAULT NULL COMMENT 'MSA/CMSA code',
  `pmsa` char(4) DEFAULT NULL COMMENT 'PMSA code',
  `statefips` char(2) DEFAULT NULL COMMENT 'FIPS State code ',
  `countyfips` char(3) DEFAULT NULL COMMENT 'FIPS County code',
  `mcdfips` char(5) DEFAULT NULL COMMENT 'FIPS MCD code',
  `zcta` char(5) DEFAULT NULL COMMENT 'ZCTA code',
  `partflag` tinyint(1) DEFAULT NULL COMMENT 'Multi-part ZCTA flag'
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

