-- MySQL dump 10.13  Distrib 5.7.17, for macos10.12 (x86_64)
--
-- Host: 127.0.0.1    Database: Halodb
-- ------------------------------------------------------
-- Server version	5.7.21

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `keys`
--

DROP TABLE IF EXISTS `keys`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `keys` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `key` varchar(45) DEFAULT NULL,
  `value` varchar(45) DEFAULT NULL,
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP,
  `userid` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `userid_idx` (`userid`),
  CONSTRAINT `userid` FOREIGN KEY (`userid`) REFERENCES `keys` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `keys`
--

LOCK TABLES `keys` WRITE;
/*!40000 ALTER TABLE `keys` DISABLE KEYS */;
INSERT INTO `keys` VALUES (1,'cp2','hub caps','2018-07-08 17:47:41',NULL),(2,'cp5','steering wheel','2018-07-08 17:47:41',NULL),(3,'cp9','head lights','2018-07-08 17:47:41',NULL),(4,'ret3','tshirt','2018-07-08 17:47:41',NULL),(7,'vac1','Florida','2018-07-08 17:47:41',NULL),(8,'vac2','Hawaii','2018-07-08 17:47:41',NULL),(9,'Steering Wheel','cp1','2018-07-08 17:47:41',NULL),(10,'cp1','Steering Wheel','2018-07-08 17:47:41',NULL),(11,'ret4','long shorts','2018-07-08 17:47:41',NULL);
/*!40000 ALTER TABLE `keys` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-07-08 19:24:14
