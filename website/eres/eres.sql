-- MySQL dump 10.13  Distrib 5.7.12, for Linux (x86_64)
--
-- Host: localhost    Database: eres
-- ------------------------------------------------------
-- Server version	5.7.12-0ubuntu1

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
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
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
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissi_permission_id_84c5c92e_fk_auth_permission_id` (`permission_id`),
  CONSTRAINT `auth_group_permissi_permission_id_84c5c92e_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
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
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permissi_content_type_id_2f476e4b_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=49 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can add permission',2,'add_permission'),(5,'Can change permission',2,'change_permission'),(6,'Can delete permission',2,'delete_permission'),(7,'Can add group',3,'add_group'),(8,'Can change group',3,'change_group'),(9,'Can delete group',3,'delete_group'),(10,'Can add user',4,'add_user'),(11,'Can change user',4,'change_user'),(12,'Can delete user',4,'delete_user'),(13,'Can add content type',5,'add_contenttype'),(14,'Can change content type',5,'change_contenttype'),(15,'Can delete content type',5,'delete_contenttype'),(16,'Can add session',6,'add_session'),(17,'Can change session',6,'change_session'),(18,'Can delete session',6,'delete_session'),(19,'Can add usuario',7,'add_usuario'),(20,'Can change usuario',7,'change_usuario'),(21,'Can delete usuario',7,'delete_usuario'),(22,'Can add regiao',8,'add_regiao'),(23,'Can change regiao',8,'change_regiao'),(24,'Can delete regiao',8,'delete_regiao'),(25,'Can add destinatario',9,'add_destinatario'),(26,'Can change destinatario',9,'change_destinatario'),(27,'Can delete destinatario',9,'delete_destinatario'),(28,'Can add recibo',10,'add_recibo'),(29,'Can change recibo',10,'change_recibo'),(30,'Can delete recibo',10,'delete_recibo'),(31,'Can add funcionario',11,'add_funcionario'),(32,'Can change funcionario',11,'change_funcionario'),(33,'Can delete funcionario',11,'delete_funcionario'),(34,'Can add gerente',12,'add_gerente'),(35,'Can change gerente',12,'change_gerente'),(36,'Can delete gerente',12,'delete_gerente'),(37,'Can add entregador',13,'add_entregador'),(38,'Can change entregador',13,'change_entregador'),(39,'Can delete entregador',13,'delete_entregador'),(40,'Can add cliente',14,'add_cliente'),(41,'Can change cliente',14,'change_cliente'),(42,'Can delete cliente',14,'delete_cliente'),(43,'Can add entrega',15,'add_entrega'),(44,'Can change entrega',15,'change_entrega'),(45,'Can delete entrega',15,'delete_entrega'),(46,'Can add veiculo',16,'add_veiculo'),(47,'Can change veiculo',16,'change_veiculo'),(48,'Can delete veiculo',16,'delete_veiculo');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(30) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$24000$0Zxjo7VkiPLx$bx9zhxpCgk01C9ru/mnAniVH+pp3BVJracHTiKsweSE=','2016-05-12 13:20:01.099759',1,'gabriel','','','gabriel@localhost',1,1,'2016-05-11 00:37:28.696158'),(2,'pbkdf2_sha256$24000$nx8u2rIFAjdf$rxmBrSWE7ED9CMo+rVzWGM1Pm1sS6JekXSjE0bH2JUQ=',NULL,1,'admin','','','admin@llocalhost.com',1,1,'2016-05-13 16:11:39.857396');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_perm_permission_id_1fbb5f2c_fk_auth_permission_id` (`permission_id`),
  CONSTRAINT `auth_user_user_perm_permission_id_1fbb5f2c_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
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
  KEY `django_admin__content_type_id_c4bce8eb_fk_django_content_type_id` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin__content_type_id_c4bce8eb_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
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
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(5,'contenttypes','contenttype'),(14,'home','cliente'),(9,'home','destinatario'),(15,'home','entrega'),(13,'home','entregador'),(11,'home','funcionario'),(12,'home','gerente'),(10,'home','recibo'),(8,'home','regiao'),(7,'home','usuario'),(16,'home','veiculo'),(6,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2016-05-10 23:28:23.495791'),(2,'auth','0001_initial','2016-05-10 23:28:31.944360'),(3,'admin','0001_initial','2016-05-10 23:28:33.782841'),(4,'admin','0002_logentry_remove_auto_add','2016-05-10 23:28:33.906263'),(5,'contenttypes','0002_remove_content_type_name','2016-05-10 23:28:35.013265'),(6,'auth','0002_alter_permission_name_max_length','2016-05-10 23:28:35.148360'),(7,'auth','0003_alter_user_email_max_length','2016-05-10 23:28:35.271941'),(8,'auth','0004_alter_user_username_opts','2016-05-10 23:28:35.335421'),(9,'auth','0005_alter_user_last_login_null','2016-05-10 23:28:35.866570'),(10,'auth','0006_require_contenttypes_0002','2016-05-10 23:28:35.912450'),(11,'auth','0007_alter_validators_add_error_messages','2016-05-10 23:28:35.975673'),(12,'home','0001_initial','2016-05-10 23:28:52.749276'),(13,'sessions','0001_initial','2016-05-10 23:28:53.457075'),(14,'home','0002_auto_20160512_1343','2016-05-12 13:44:08.247859'),(15,'home','0003_auto_20160513_1411','2016-05-13 14:12:02.830394'),(16,'home','0004_auto_20160513_1427','2016-05-13 14:27:57.632133'),(17,'home','0005_auto_20160513_1430','2016-05-13 14:30:57.005582');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_de54fa62` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `home_cliente`
--

DROP TABLE IF EXISTS `home_cliente`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `home_cliente` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nome` varchar(45) NOT NULL,
  `email` varchar(45) NOT NULL,
  `endereco` varchar(45) NOT NULL,
  `telefone` varchar(20) NOT NULL,
  `CNPJ` varchar(45) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `home_cliente`
--

LOCK TABLES `home_cliente` WRITE;
/*!40000 ALTER TABLE `home_cliente` DISABLE KEYS */;
/*!40000 ALTER TABLE `home_cliente` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `home_destinatario`
--

DROP TABLE IF EXISTS `home_destinatario`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `home_destinatario` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nome` varchar(256) NOT NULL,
  `complemento` varchar(45) NOT NULL,
  `estado` varchar(2) NOT NULL,
  `logradouro` varchar(45) NOT NULL,
  `municipio` varchar(45) NOT NULL,
  `numero` varchar(4) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `home_destinatario`
--

LOCK TABLES `home_destinatario` WRITE;
/*!40000 ALTER TABLE `home_destinatario` DISABLE KEYS */;
/*!40000 ALTER TABLE `home_destinatario` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `home_entrega`
--

DROP TABLE IF EXISTS `home_entrega`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `home_entrega` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `dataPedido` date NOT NULL,
  `preco` double NOT NULL,
  `prioridade` int(11) NOT NULL,
  `status` varchar(45) NOT NULL,
  `qtd_tentativas` int(11) NOT NULL,
  `cliente_id` int(11) NOT NULL,
  `destinatario_id` int(11) NOT NULL,
  `recibo_id` int(11) NOT NULL,
  `regiao_id` int(11) NOT NULL,
  `entregador_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `home_entrega_cliente_id_fc757439_fk_home_cliente_id` (`cliente_id`),
  KEY `home_entrega_destinatario_id_cbb66eb3_fk_home_destinatario_id` (`destinatario_id`),
  KEY `home_entrega_8b77cbb1` (`recibo_id`),
  KEY `home_entrega_4968fcf4` (`regiao_id`),
  KEY `home_entrega_f33b3f83` (`entregador_id`),
  CONSTRAINT `hom_entregador_id_c2e5e522_fk_home_entregador_funcionario_ptr_id` FOREIGN KEY (`entregador_id`) REFERENCES `home_entregador` (`funcionario_ptr_id`),
  CONSTRAINT `home_entrega_cliente_id_fc757439_fk_home_cliente_id` FOREIGN KEY (`cliente_id`) REFERENCES `home_cliente` (`id`),
  CONSTRAINT `home_entrega_destinatario_id_cbb66eb3_fk_home_destinatario_id` FOREIGN KEY (`destinatario_id`) REFERENCES `home_destinatario` (`id`),
  CONSTRAINT `home_entrega_recibo_id_d631e08d_fk_home_recibo_id` FOREIGN KEY (`recibo_id`) REFERENCES `home_recibo` (`id`),
  CONSTRAINT `home_entrega_regiao_id_8bc37277_fk_home_regiao_id` FOREIGN KEY (`regiao_id`) REFERENCES `home_regiao` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `home_entrega`
--

LOCK TABLES `home_entrega` WRITE;
/*!40000 ALTER TABLE `home_entrega` DISABLE KEYS */;
/*!40000 ALTER TABLE `home_entrega` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `home_entregador`
--

DROP TABLE IF EXISTS `home_entregador`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `home_entregador` (
  `funcionario_ptr_id` int(11) NOT NULL,
  `status` int(11) NOT NULL,
  PRIMARY KEY (`funcionario_ptr_id`),
  CONSTRAINT `home_entregad_funcionario_ptr_id_1e61189c_fk_home_funcionario_id` FOREIGN KEY (`funcionario_ptr_id`) REFERENCES `home_funcionario` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `home_entregador`
--

LOCK TABLES `home_entregador` WRITE;
/*!40000 ALTER TABLE `home_entregador` DISABLE KEYS */;
INSERT INTO `home_entregador` VALUES (2,1);
/*!40000 ALTER TABLE `home_entregador` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `home_funcionario`
--

DROP TABLE IF EXISTS `home_funcionario`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `home_funcionario` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nome` varchar(45) NOT NULL,
  `dataNascimento` date NOT NULL,
  `CPF` varchar(45) NOT NULL,
  `salario` double NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `home_funcionario`
--

LOCK TABLES `home_funcionario` WRITE;
/*!40000 ALTER TABLE `home_funcionario` DISABLE KEYS */;
INSERT INTO `home_funcionario` VALUES (1,'Gabriel Casarin da Silva','1993-10-16','123456789',100),(2,'Gabriel Casarin da Silva','1993-10-16','1234567890',1000);
/*!40000 ALTER TABLE `home_funcionario` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `home_gerente`
--

DROP TABLE IF EXISTS `home_gerente`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `home_gerente` (
  `funcionario_ptr_id` int(11) NOT NULL,
  PRIMARY KEY (`funcionario_ptr_id`),
  CONSTRAINT `home_gerente_funcionario_ptr_id_7d39be79_fk_home_funcionario_id` FOREIGN KEY (`funcionario_ptr_id`) REFERENCES `home_funcionario` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `home_gerente`
--

LOCK TABLES `home_gerente` WRITE;
/*!40000 ALTER TABLE `home_gerente` DISABLE KEYS */;
/*!40000 ALTER TABLE `home_gerente` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `home_recibo`
--

DROP TABLE IF EXISTS `home_recibo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `home_recibo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `assinatura` varchar(45) NOT NULL,
  `dataRecebimento` date NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `home_recibo`
--

LOCK TABLES `home_recibo` WRITE;
/*!40000 ALTER TABLE `home_recibo` DISABLE KEYS */;
/*!40000 ALTER TABLE `home_recibo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `home_regiao`
--

DROP TABLE IF EXISTS `home_regiao`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `home_regiao` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nome` varchar(45) NOT NULL,
  `precoBase` double NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `home_regiao`
--

LOCK TABLES `home_regiao` WRITE;
/*!40000 ALTER TABLE `home_regiao` DISABLE KEYS */;
/*!40000 ALTER TABLE `home_regiao` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `home_usuario`
--

DROP TABLE IF EXISTS `home_usuario`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `home_usuario` (
  `username` varchar(15) NOT NULL,
  `password` varchar(15) NOT NULL,
  `tipoUsuario` int(11) NOT NULL,
  PRIMARY KEY (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `home_usuario`
--

LOCK TABLES `home_usuario` WRITE;
/*!40000 ALTER TABLE `home_usuario` DISABLE KEYS */;
/*!40000 ALTER TABLE `home_usuario` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `home_veiculo`
--

DROP TABLE IF EXISTS `home_veiculo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `home_veiculo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `entregador_id` int(11) NOT NULL,
  `ano` varchar(4) NOT NULL,
  `marca` varchar(45) NOT NULL,
  `modelo` varchar(45) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `home_veiculo_f33b3f83` (`entregador_id`),
  CONSTRAINT `home_veiculo_entregador_id_422f4018_fk_home_funcionario_id` FOREIGN KEY (`entregador_id`) REFERENCES `home_funcionario` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `home_veiculo`
--

LOCK TABLES `home_veiculo` WRITE;
/*!40000 ALTER TABLE `home_veiculo` DISABLE KEYS */;
/*!40000 ALTER TABLE `home_veiculo` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2016-05-13 13:12:15
