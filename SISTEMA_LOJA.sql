-- MySQL dump 10.13  Distrib 8.0.31, for Linux (x86_64)
--
-- Host: localhost    Database: SISTEMA_LOJA
-- ------------------------------------------------------
-- Server version	8.0.31

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `CARRINHO`
--

DROP TABLE IF EXISTS `CARRINHO`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `CARRINHO` (
  `ID` int unsigned NOT NULL AUTO_INCREMENT,
  `CLIENTE_ID` int unsigned DEFAULT NULL,
  `PRODUTO_ID` int unsigned DEFAULT NULL,
  `PEDIDO_ID` int unsigned DEFAULT NULL,
  `QUANTIDADE` int unsigned DEFAULT NULL,
  PRIMARY KEY (`ID`),
  KEY `PEDIDO_CARRINHO` (`PEDIDO_ID`),
  KEY `PRODUTO_CARRINHO` (`PRODUTO_ID`),
  KEY `CLIENTE_CARRINHO` (`CLIENTE_ID`),
  CONSTRAINT `CLIENTE_CARRINHO` FOREIGN KEY (`CLIENTE_ID`) REFERENCES `CLIENTE` (`ID`) ON DELETE SET NULL ON UPDATE CASCADE,
  CONSTRAINT `PEDIDO_CARRINHO` FOREIGN KEY (`PEDIDO_ID`) REFERENCES `PEDIDO` (`ID`) ON DELETE RESTRICT ON UPDATE CASCADE,
  CONSTRAINT `PRODUTO_CARRINHO` FOREIGN KEY (`PRODUTO_ID`) REFERENCES `PRODUTO` (`ID`) ON DELETE SET NULL ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=61 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `CARRINHO`
--

LOCK TABLES `CARRINHO` WRITE;
/*!40000 ALTER TABLE `CARRINHO` DISABLE KEYS */;
INSERT INTO `CARRINHO` VALUES (41,18,3,20,3),(42,18,13,21,1),(43,18,14,21,2),(44,18,9,22,1),(45,18,10,22,2),(46,18,12,22,1),(47,20,4,23,1),(48,19,5,24,1),(49,19,11,24,1),(50,19,3,25,2),(51,19,9,25,1),(52,19,4,25,1),(53,19,10,25,2),(54,16,9,26,1),(55,21,11,27,1),(56,21,12,27,1),(57,21,3,27,2),(58,21,13,28,1),(59,22,12,29,1),(60,22,14,29,2);
/*!40000 ALTER TABLE `CARRINHO` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `CLIENTE`
--

DROP TABLE IF EXISTS `CLIENTE`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `CLIENTE` (
  `ID` int unsigned NOT NULL AUTO_INCREMENT,
  `NOME` varchar(255) DEFAULT NULL,
  `TELEFONE` varchar(15) DEFAULT NULL,
  `CPF` char(11) DEFAULT NULL,
  `TIPO` varchar(255) DEFAULT NULL,
  `ENDERECO_ID` int unsigned DEFAULT NULL,
  PRIMARY KEY (`ID`),
  UNIQUE KEY `CPF` (`CPF`),
  KEY `ENDERECO` (`ENDERECO_ID`),
  CONSTRAINT `ENDERECO` FOREIGN KEY (`ENDERECO_ID`) REFERENCES `ENDERECO` (`ID`) ON DELETE SET NULL ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `CLIENTE`
--

LOCK TABLES `CLIENTE` WRITE;
/*!40000 ALTER TABLE `CLIENTE` DISABLE KEYS */;
INSERT INTO `CLIENTE` VALUES (16,'Sophia Fernandes','84989044286','67675743768','Telefone',15),(18,'Bruno Castro','94992770940','66410405936','Cliente Web',17),(19,'Vicente Ribeiro','61983881068','59616549588','Cliente Web',18),(20,'Elaine Barbosa','95985566820','90499546423','Cliente Web',19),(21,'Bernardo Viana','84996451015','59412672586','Telefone',20),(22,'Laís Moura','81995928816','24570104037','Catálogo',21);
/*!40000 ALTER TABLE `CLIENTE` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ENDERECO`
--

DROP TABLE IF EXISTS `ENDERECO`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ENDERECO` (
  `ID` int unsigned NOT NULL AUTO_INCREMENT,
  `BAIRRO` varchar(255) DEFAULT NULL,
  `CIDADE` varchar(255) DEFAULT NULL,
  `ESTADO` char(2) DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ENDERECO`
--

LOCK TABLES `ENDERECO` WRITE;
/*!40000 ALTER TABLE `ENDERECO` DISABLE KEYS */;
INSERT INTO `ENDERECO` VALUES (15,'Potengi','Natal','RN'),(17,'São Félix Pioneiro','Marabá','PA'),(18,'Samambaia Norte (Samambaia)','Brasília','DF'),(19,'Raiar do Sol','Boa Vista','RR'),(20,'Alecrim','Natal','RN'),(21,'Brasília Teimosa','Recife','PE');
/*!40000 ALTER TABLE `ENDERECO` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `FORMA_PAGAMENTO`
--

DROP TABLE IF EXISTS `FORMA_PAGAMENTO`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `FORMA_PAGAMENTO` (
  `ID` int unsigned NOT NULL AUTO_INCREMENT,
  `NOME` varchar(255) DEFAULT NULL,
  `PEDIDO_ID` int unsigned DEFAULT NULL,
  PRIMARY KEY (`ID`),
  KEY `PEDIDO_PAGAMENTO` (`PEDIDO_ID`),
  CONSTRAINT `PEDIDO_PAGAMENTO` FOREIGN KEY (`PEDIDO_ID`) REFERENCES `PEDIDO` (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=30 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `FORMA_PAGAMENTO`
--

LOCK TABLES `FORMA_PAGAMENTO` WRITE;
/*!40000 ALTER TABLE `FORMA_PAGAMENTO` DISABLE KEYS */;
INSERT INTO `FORMA_PAGAMENTO` VALUES (16,'PIX',20),(17,'Cartão de Crédito',21),(18,'Cartão de Crédito',22),(19,'Cartão de Débito',22),(20,'PIX',23),(21,'Cartão de Crédito',24),(22,'Boleto',25),(23,'Cartão de Crédito',25),(24,'Cartão de Débito',25),(25,'Cartão de Crédito',26),(26,'Cartão de Crédito',27),(27,'PIX',27),(28,'Cartão de Crédito',28),(29,'Cartão de Crédito',29);
/*!40000 ALTER TABLE `FORMA_PAGAMENTO` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `PEDIDO`
--

DROP TABLE IF EXISTS `PEDIDO`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `PEDIDO` (
  `ID` int unsigned NOT NULL AUTO_INCREMENT,
  `DATA_PEDIDO` date DEFAULT NULL,
  `STATUS_PEDIDO` varchar(255) DEFAULT NULL,
  `TOTAL` decimal(6,2) DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=30 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `PEDIDO`
--

LOCK TABLES `PEDIDO` WRITE;
/*!40000 ALTER TABLE `PEDIDO` DISABLE KEYS */;
INSERT INTO `PEDIDO` VALUES (20,'2022-12-10','Em Processamento',149.97),(21,'2022-12-10','Em Processamento',209.79),(22,'2022-12-10','Em Processamento',479.60),(23,'2022-12-10','Em Processamento',119.99),(24,'2022-12-10','Em Processamento',89.98),(25,'2022-12-10','Em Processamento',509.67),(26,'2022-12-10','Em Processamento',89.90),(27,'2022-12-10','Em Processamento',349.87),(28,'2022-12-10','Em Processamento',149.99),(29,'2022-12-10','Em Processamento',249.70);
/*!40000 ALTER TABLE `PEDIDO` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `PRODUTO`
--

DROP TABLE IF EXISTS `PRODUTO`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `PRODUTO` (
  `ID` int unsigned NOT NULL AUTO_INCREMENT,
  `NOME` varchar(255) DEFAULT NULL,
  `VALOR` decimal(6,2) DEFAULT NULL,
  `DESCRICAO` text,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `PRODUTO`
--

LOCK TABLES `PRODUTO` WRITE;
/*!40000 ALTER TABLE `PRODUTO` DISABLE KEYS */;
INSERT INTO `PRODUTO` VALUES (3,'Camisa Manga Curta',49.99,'Branca'),(4,'Calça',119.99,'Jeans / Skinny'),(5,'Boné',29.99,'Preto / Aba Reta'),(6,'Casaco',79.90,'Verde / Moletom'),(9,'Camisa Manga Comprida',89.90,'Preta'),(10,'Bermuda',99.90,'Azul Claro'),(11,'Gorro',59.99,'Bordô'),(12,'Mochila',189.90,'Roxa'),(13,'Tênis',149.99,'Branco / Cano Curto'),(14,'Meias',29.90,'Temática Disney');
/*!40000 ALTER TABLE `PRODUTO` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `USUARIO`
--

DROP TABLE IF EXISTS `USUARIO`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `USUARIO` (
  `ID` int unsigned NOT NULL AUTO_INCREMENT,
  `NOME_USUARIO` varchar(255) DEFAULT NULL,
  `SENHA_USUARIO` varbinary(8000) DEFAULT NULL,
  `STATUS_USUARIO` varchar(255) DEFAULT NULL,
  `CLIENTE_ID` int unsigned DEFAULT NULL,
  PRIMARY KEY (`ID`),
  KEY `CLIENTE_USUARIO` (`CLIENTE_ID`),
  CONSTRAINT `CLIENTE_USUARIO` FOREIGN KEY (`CLIENTE_ID`) REFERENCES `CLIENTE` (`ID`) ON DELETE SET NULL ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `USUARIO`
--

LOCK TABLES `USUARIO` WRITE;
/*!40000 ALTER TABLE `USUARIO` DISABLE KEYS */;
INSERT INTO `USUARIO` VALUES (13,'bruno_castro',_binary '123','Ativo',18),(14,'vicente_ribeiro',_binary '123','Ativo',19),(15,'elaine_barbosa',_binary '123','Ativo',20);
/*!40000 ALTER TABLE `USUARIO` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-12-14  9:42:22
