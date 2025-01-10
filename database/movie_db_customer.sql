-- MySQL dump 10.13  Distrib 8.0.40, for Win64 (x86_64)
--
-- Host: localhost    Database: movie_db
-- ------------------------------------------------------
-- Server version	8.0.40

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `customer`
--

DROP TABLE IF EXISTS `customer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `customer` (
  `name` varchar(25) DEFAULT NULL,
  `phone` varchar(10) NOT NULL,
  PRIMARY KEY (`phone`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `customer`
--

LOCK TABLES `customer` WRITE;
/*!40000 ALTER TABLE `customer` DISABLE KEYS */;
INSERT INTO `customer` VALUES ('Lian','900000000'),('Michael','900844284'),('Charlotte','900867731'),('Harper','901084866'),('Emma','901444973'),('Ethan','902156760'),('John','902347578'),('Michael','904992361'),('Mia','906644544'),('William','907134880'),('Alexander','907229784'),('Daniel','908164069'),('Harper','909366560'),('David','909713918'),('Robert','910751414'),('Tina','911111111'),('Ethan','911379976'),('name1','912222222'),('Lian','912345678'),('Robert','912706538'),('Charlotte','912826474'),('Robert','913562153'),('Evelyn','914154293'),('Alexander','914318732'),('David','915258931'),('Evelyn','915478066'),('Matthew','915506086'),('David','917253778'),('Sophia','918556434'),('Matthew','918716467'),('Sophia','920061647'),('Isabella','920299681'),('Harper','920596481'),('Matthew','920915420'),('Mia','921822318'),('Olivia','922068463'),('Evelyn','922680593'),('James','924254084'),('Robert','924506072'),('Alexander','924910264'),('Emma','925778468'),('Amelia','925887475'),('Isabella','926257252'),('Robert','929944591'),('Michael','930990545'),('Michael','934293350'),('James','935684772'),('John','936672027'),('Evelyn','937253154'),('Matthew','937419327'),('Daniel','939704215'),('William','939899650'),('Ethan','942576992'),('Daniel','946769540'),('Daniel','947033625'),('Charlotte','947729687'),('Michael','949358516'),('Michael','949831314'),('Matthew','951602203'),('Olivia','952992533'),('Charlotte','954805511'),('Matthew','955272583'),('William','956880745'),('Alexander','958610400'),('James','959518135'),('Ethan','961273328'),('James','962350413'),('Isabella','962512205'),('Olivia','970171439'),('Tiffany','970501959'),('James','971535206'),('Sophia','972062126'),('Sophia','973063915'),('James','975284300'),('Robert','976179325'),('James','976501554'),('Daniel','978542599'),('John','980031674'),('Sophia','980192702'),('Charlotte','980327509'),('Ethan','982780961'),('Evelyn','984613861'),('Sophia','985681013'),('John','985734187'),('Alexander','985997954'),('Olivia','986477502'),('Amelia','986695783'),('Emma','988093998'),('Daniel','989311969'),('Matthew','990405654'),('Charlotte','991812477'),('Charlotte','992009340'),('James','992340688'),('John','992621280'),('Emma','992973550'),('Emma','993542736'),('Isabella','993890751'),('Amelia','995681016'),('Isabella','996077603'),('Alexander','996382939'),('Alexander','998767390'),('Ethan','999462531'),('name','phone');
/*!40000 ALTER TABLE `customer` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-01-02 10:41:32
