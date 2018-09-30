-- MySQL dump 10.13  Distrib 8.0.12, for Win64 (x86_64)
--
-- Host: localhost    Database: noobcommenderDB
-- ------------------------------------------------------
-- Server version	8.0.12

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
 SET NAMES utf8mb4 ;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=53 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add content type',4,'add_contenttype'),(14,'Can change content type',4,'change_contenttype'),(15,'Can delete content type',4,'delete_contenttype'),(16,'Can view content type',4,'view_contenttype'),(17,'Can add session',5,'add_session'),(18,'Can change session',5,'change_session'),(19,'Can delete session',5,'delete_session'),(20,'Can view session',5,'view_session'),(21,'Can add course',6,'add_course'),(22,'Can change course',6,'change_course'),(23,'Can delete course',6,'delete_course'),(24,'Can view course',6,'view_course'),(25,'Can add problem',7,'add_problem'),(26,'Can change problem',7,'change_problem'),(27,'Can delete problem',7,'delete_problem'),(28,'Can view problem',7,'view_problem'),(29,'Can add programmer solution',8,'add_programmersolution'),(30,'Can change programmer solution',8,'change_programmersolution'),(31,'Can delete programmer solution',8,'delete_programmersolution'),(32,'Can view programmer solution',8,'view_programmersolution'),(33,'Can add solution',9,'add_solution'),(34,'Can change solution',9,'change_solution'),(35,'Can delete solution',9,'delete_solution'),(36,'Can view solution',9,'view_solution'),(37,'Can add taken course',10,'add_takencourse'),(38,'Can change taken course',10,'change_takencourse'),(39,'Can delete taken course',10,'delete_takencourse'),(40,'Can view taken course',10,'view_takencourse'),(41,'Can add user',11,'add_user'),(42,'Can change user',11,'change_user'),(43,'Can delete user',11,'delete_user'),(44,'Can view user',11,'view_user'),(45,'Can add programmer',12,'add_programmer'),(46,'Can change programmer',12,'change_programmer'),(47,'Can delete programmer',12,'delete_programmer'),(48,'Can view programmer',12,'view_programmer'),(49,'Can add user contest data',13,'add_usercontestdata'),(50,'Can change user contest data',13,'change_usercontestdata'),(51,'Can delete user contest data',13,'delete_usercontestdata'),(52,'Can view user contest data',13,'view_usercontestdata');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `codecourse_course`
--

DROP TABLE IF EXISTS `codecourse_course`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `codecourse_course` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `tag` varchar(15) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `codecourse_course`
--

LOCK TABLES `codecourse_course` WRITE;
/*!40000 ALTER TABLE `codecourse_course` DISABLE KEYS */;
/*!40000 ALTER TABLE `codecourse_course` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `codecourse_problem`
--

DROP TABLE IF EXISTS `codecourse_problem`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `codecourse_problem` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `problem_title` varchar(255) NOT NULL,
  `problem_code` varchar(50) NOT NULL,
  `course_id` int(11) NOT NULL,
  `problem_points` double NOT NULL,
  PRIMARY KEY (`id`),
  KEY `CodeCourse_problem_course_id_884af4bb_fk_CodeCourse_course_id` (`course_id`),
  CONSTRAINT `CodeCourse_problem_course_id_884af4bb_fk_CodeCourse_course_id` FOREIGN KEY (`course_id`) REFERENCES `codecourse_course` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `codecourse_problem`
--

LOCK TABLES `codecourse_problem` WRITE;
/*!40000 ALTER TABLE `codecourse_problem` DISABLE KEYS */;
/*!40000 ALTER TABLE `codecourse_problem` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `codecourse_programmer`
--

DROP TABLE IF EXISTS `codecourse_programmer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `codecourse_programmer` (
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`user_id`),
  CONSTRAINT `CodeCourse_programmer_user_id_e5fc34e0_fk_CodeCourse_user_id` FOREIGN KEY (`user_id`) REFERENCES `codecourse_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `codecourse_programmer`
--

LOCK TABLES `codecourse_programmer` WRITE;
/*!40000 ALTER TABLE `codecourse_programmer` DISABLE KEYS */;
INSERT INTO `codecourse_programmer` VALUES (4);
/*!40000 ALTER TABLE `codecourse_programmer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `codecourse_programmersolution`
--

DROP TABLE IF EXISTS `codecourse_programmersolution`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `codecourse_programmersolution` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `solution_id` int(11) NOT NULL,
  `programmer_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `CodeCourse_programme_programmer_id_b95f018e_fk_CodeCours` (`programmer_id`),
  KEY `CodeCourse_programme_solution_id_22ecd697_fk_CodeCours` (`solution_id`),
  CONSTRAINT `CodeCourse_programme_programmer_id_b95f018e_fk_CodeCours` FOREIGN KEY (`programmer_id`) REFERENCES `codecourse_programmer` (`user_id`),
  CONSTRAINT `CodeCourse_programme_solution_id_22ecd697_fk_CodeCours` FOREIGN KEY (`solution_id`) REFERENCES `codecourse_solution` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `codecourse_programmersolution`
--

LOCK TABLES `codecourse_programmersolution` WRITE;
/*!40000 ALTER TABLE `codecourse_programmersolution` DISABLE KEYS */;
/*!40000 ALTER TABLE `codecourse_programmersolution` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `codecourse_solution`
--

DROP TABLE IF EXISTS `codecourse_solution`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `codecourse_solution` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `is_correct` tinyint(1) NOT NULL,
  `problem_id` int(11) NOT NULL,
  `text` varchar(255) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `CodeCourse_solution_problem_id_fb4f8387_fk_CodeCourse_problem_id` (`problem_id`),
  CONSTRAINT `CodeCourse_solution_problem_id_fb4f8387_fk_CodeCourse_problem_id` FOREIGN KEY (`problem_id`) REFERENCES `codecourse_problem` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `codecourse_solution`
--

LOCK TABLES `codecourse_solution` WRITE;
/*!40000 ALTER TABLE `codecourse_solution` DISABLE KEYS */;
/*!40000 ALTER TABLE `codecourse_solution` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `codecourse_takencourse`
--

DROP TABLE IF EXISTS `codecourse_takencourse`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `codecourse_takencourse` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `score` double NOT NULL,
  `date` datetime(6) NOT NULL,
  `course_id` int(11) NOT NULL,
  `programmer_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `CodeCourse_takencour_course_id_92432409_fk_CodeCours` (`course_id`),
  KEY `CodeCourse_takencour_programmer_id_89e37e8b_fk_CodeCours` (`programmer_id`),
  CONSTRAINT `CodeCourse_takencour_course_id_92432409_fk_CodeCours` FOREIGN KEY (`course_id`) REFERENCES `codecourse_course` (`id`),
  CONSTRAINT `CodeCourse_takencour_programmer_id_89e37e8b_fk_CodeCours` FOREIGN KEY (`programmer_id`) REFERENCES `codecourse_programmer` (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `codecourse_takencourse`
--

LOCK TABLES `codecourse_takencourse` WRITE;
/*!40000 ALTER TABLE `codecourse_takencourse` DISABLE KEYS */;
/*!40000 ALTER TABLE `codecourse_takencourse` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `codecourse_user`
--

DROP TABLE IF EXISTS `codecourse_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `codecourse_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  `access_token` varchar(50) NOT NULL,
  `refresh_token` varchar(50) NOT NULL,
  `slug` char(32) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `codecourse_user`
--

LOCK TABLES `codecourse_user` WRITE;
/*!40000 ALTER TABLE `codecourse_user` DISABLE KEYS */;
INSERT INTO `codecourse_user` VALUES (4,'pbkdf2_sha256$100000$HJK4fORJHvMt$TvR0cngWXwT6Woy17Wn2zeSDv/BHwf5INTieECHcJhk=','2018-09-12 15:44:16.180074',0,'shubham1singh','Shubham','Singh','',0,1,'2018-09-12 08:41:43.391666','3a041758413f2444c771c85cce3bd4468d15a395','e5b7482ebdc01ef231025de46c866ce0f6af6084','b410bc5c89ed42f3af83eb0f8b5655eb');
/*!40000 ALTER TABLE `codecourse_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `codecourse_user_groups`
--

DROP TABLE IF EXISTS `codecourse_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `codecourse_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `CodeCourse_user_groups_user_id_group_id_8c700362_uniq` (`user_id`,`group_id`),
  KEY `CodeCourse_user_groups_group_id_220c2f49_fk_auth_group_id` (`group_id`),
  CONSTRAINT `CodeCourse_user_groups_group_id_220c2f49_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `CodeCourse_user_groups_user_id_d0964fb5_fk_CodeCourse_user_id` FOREIGN KEY (`user_id`) REFERENCES `codecourse_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `codecourse_user_groups`
--

LOCK TABLES `codecourse_user_groups` WRITE;
/*!40000 ALTER TABLE `codecourse_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `codecourse_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `codecourse_user_user_permissions`
--

DROP TABLE IF EXISTS `codecourse_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `codecourse_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `CodeCourse_user_user_per_user_id_permission_id_e45d8b3f_uniq` (`user_id`,`permission_id`),
  KEY `CodeCourse_user_user_permission_id_416ba072_fk_auth_perm` (`permission_id`),
  CONSTRAINT `CodeCourse_user_user_permission_id_416ba072_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `CodeCourse_user_user_user_id_89081f41_fk_CodeCours` FOREIGN KEY (`user_id`) REFERENCES `codecourse_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `codecourse_user_user_permissions`
--

LOCK TABLES `codecourse_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `codecourse_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `codecourse_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `coreengine_usercontestdata`
--

DROP TABLE IF EXISTS `coreengine_usercontestdata`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `coreengine_usercontestdata` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `solved_cc` varchar(10) NOT NULL,
  `partially_solved_cc` varchar(10) NOT NULL,
  `user_id` int(11) NOT NULL,
  `attempted_cc` varchar(10) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`),
  CONSTRAINT `CoreEngine_userconte_user_id_2c3d96e8_fk_CodeCours` FOREIGN KEY (`user_id`) REFERENCES `codecourse_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `coreengine_usercontestdata`
--

LOCK TABLES `coreengine_usercontestdata` WRITE;
/*!40000 ALTER TABLE `coreengine_usercontestdata` DISABLE KEYS */;
/*!40000 ALTER TABLE `coreengine_usercontestdata` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_CodeCourse_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_CodeCourse_user_id` FOREIGN KEY (`user_id`) REFERENCES `codecourse_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(6,'CodeCourse','course'),(7,'CodeCourse','problem'),(12,'CodeCourse','programmer'),(8,'CodeCourse','programmersolution'),(9,'CodeCourse','solution'),(10,'CodeCourse','takencourse'),(11,'CodeCourse','user'),(4,'contenttypes','contenttype'),(13,'CoreEngine','usercontestdata'),(5,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2018-09-12 08:34:16.951506'),(2,'contenttypes','0002_remove_content_type_name','2018-09-12 08:34:24.168307'),(3,'auth','0001_initial','2018-09-12 08:34:38.534814'),(4,'auth','0002_alter_permission_name_max_length','2018-09-12 08:34:40.534342'),(5,'auth','0003_alter_user_email_max_length','2018-09-12 08:34:40.753038'),(6,'auth','0004_alter_user_username_opts','2018-09-12 08:34:40.924875'),(7,'auth','0005_alter_user_last_login_null','2018-09-12 08:34:41.018603'),(8,'auth','0006_require_contenttypes_0002','2018-09-12 08:34:41.096707'),(9,'auth','0007_alter_validators_add_error_messages','2018-09-12 08:34:41.159222'),(10,'auth','0008_alter_user_username_max_length','2018-09-12 08:34:41.206057'),(11,'auth','0009_alter_user_last_name_max_length','2018-09-12 08:34:41.518494'),(12,'CodeCourse','0001_initial','2018-09-12 08:35:42.048169'),(13,'CodeCourse','0002_auto_20180903_2040','2018-09-12 08:35:42.157412'),(14,'CodeCourse','0003_solution_text','2018-09-12 08:35:43.516495'),(15,'CodeCourse','0004_problem_problem_score','2018-09-12 08:35:49.104113'),(16,'CodeCourse','0005_auto_20180904_1733','2018-09-12 08:35:49.982091'),(17,'CodeCourse','0006_auto_20180904_1818','2018-09-12 08:35:50.747538'),(18,'CodeCourse','0007_auto_20180905_2318','2018-09-12 08:35:55.668248'),(19,'CodeCourse','0008_user_slug','2018-09-12 08:35:56.824348'),(20,'CoreEngine','0001_initial','2018-09-12 08:36:01.854286'),(21,'admin','0001_initial','2018-09-12 08:36:09.548963'),(22,'admin','0002_logentry_remove_auto_add','2018-09-12 08:36:09.658317'),(23,'admin','0003_logentry_add_action_flag_choices','2018-09-12 08:36:09.752072'),(24,'sessions','0001_initial','2018-09-12 08:36:12.220257'),(25,'CoreEngine','0002_auto_20180912_1409','2018-09-12 08:39:25.570514');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-09-29 20:47:02
