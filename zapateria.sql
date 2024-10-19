-- MySQL dump 10.13  Distrib 8.0.38, for Win64 (x86_64)
--
-- Host: localhost    Database: zapateria
-- ------------------------------------------------------
-- Server version	8.0.39

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
-- Table structure for table `empleados`
--

DROP TABLE IF EXISTS `empleados`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `empleados` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) NOT NULL,
  `apellido` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `telefono` varchar(10) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`),
  UNIQUE KEY `telefono` (`telefono`)
) ENGINE=InnoDB AUTO_INCREMENT=51 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `empleados`
--

LOCK TABLES `empleados` WRITE;
/*!40000 ALTER TABLE `empleados` DISABLE KEYS */;
INSERT INTO `empleados` VALUES (1,'Carlos','Gonzalez','carlos.gonzalez1@gmail.com','3001111111'),(2,'Ana','Martinez','ana.martinez2@gmail.com','3002222222'),(3,'Jose','Rodriguez','jose.rodriguez3@gmail.com','3003333333'),(4,'Maria','Perez','maria.perez4@gmail.com','3004444444'),(5,'Luis','Garcia','luis.garcia5@gmail.com','3005555555'),(6,'Sofia','Lopez','sofia.lopez6@gmail.com','3006666666'),(7,'Andres','Torres','andres.torres7@gmail.com','3007777777'),(8,'Laura','Ramirez','laura.ramirez8@gmail.com','3008888888'),(9,'Pedro','Fernandez','pedro.fernandez9@gmail.com','3009999999'),(10,'Camila','Gutierrez','camila.gutierrez10@gmail.com','3010000000'),(11,'Juan','Vargas','juan.vargas11@gmail.com','3011111111'),(12,'Valentina','Morales','valentina.morales12@gmail.com','3012222222'),(13,'Felipe','Mendoza','felipe.mendoza13@gmail.com','3013333333'),(14,'Daniela','Castro','daniela.castro14@gmail.com','3014444444'),(15,'Sebastian','Rios','sebastian.rios15@gmail.com','3015555555'),(16,'Isabella','Salazar','isabella.salazar16@gmail.com','3016666666'),(17,'Nicolas','Mejia','nicolas.mejia17@gmail.com','3017777777'),(18,'Daniel','Cruz','daniel.cruz18@gmail.com','3018888888'),(19,'Paula','Vera','paula.vera19@gmail.com','3019999999'),(20,'Jorge','Blanco','jorge.blanco20@gmail.com','3020000000'),(21,'Sara','Ortiz','sara.ortiz21@gmail.com','3021111111'),(22,'Miguel','Ruiz','miguel.ruiz22@gmail.com','3022222222'),(23,'Elena','Santos','elena.santos23@gmail.com','3023333333'),(24,'Santiago','Nieto','santiago.nieto24@gmail.com','3024444444'),(25,'Natalia','Palacios','natalia.palacios25@gmail.com','3025555555'),(26,'Cristian','Muñoz','cristian.munoz26@gmail.com','3026666666'),(27,'Diana','Hernandez','diana.hernandez27@gmail.com','3027777777'),(28,'David','Acosta','david.acosta28@gmail.com','3028888888'),(29,'Lucia','Cortes','lucia.cortes29@gmail.com','3029999999'),(30,'Tomas','Gil','tomas.gil30@gmail.com','3030000000'),(31,'Victoria','Arias','victoria.arias31@gmail.com','3031111111'),(32,'Julian','Reyes','julian.reyes32@gmail.com','3032222222'),(33,'Andrea','Sanchez','andrea.sanchez33@gmail.com','3033333333'),(34,'Gabriel','Velez','gabriel.velez34@gmail.com','3034444444'),(35,'Angela','Espinosa','angela.espinosa35@gmail.com','3035555555'),(36,'Martin','Padilla','martin.padilla36@gmail.com','3036666666'),(37,'Carolina','Peña','carolina.pena37@gmail.com','3037777777'),(38,'Oscar','Ochoa','oscar.ochoa38@gmail.com','3038888888'),(39,'Julieta','Campos','julieta.campos39@gmail.com','3039999999'),(40,'Samuel','Suarez','samuel.suarez40@gmail.com','3040000000'),(41,'Alejandra','Cano','alejandra.cano41@gmail.com','3041111111'),(42,'Manuel','Velasquez','manuel.velasquez42@gmail.com','3042222222'),(43,'Fernanda','Gomez','fernanda.gomez43@gmail.com','3043333333'),(44,'Pablo','Castillo','pablo.castillo44@gmail.com','3044444444'),(45,'Esteban','Cabrera','esteban.cabrera45@gmail.com','3045555555'),(46,'Margarita','Quintero','margarita.quintero46@gmail.com','3046666666'),(47,'Roberto','Rivas','roberto.rivas47@gmail.com','3047777777'),(48,'Renata','Delgado','renata.delgado48@gmail.com','3048888888'),(49,'Carlos','Barrera','carlos.barrera49@gmail.com','3049999999'),(50,'Veronica','Flores','veronica.flores50@gmail.com','3050000000');
/*!40000 ALTER TABLE `empleados` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `login_users`
--

DROP TABLE IF EXISTS `login_users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `login_users` (
  `id` int NOT NULL AUTO_INCREMENT,
  `email` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email_UNIQUE` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `login_users`
--

LOCK TABLES `login_users` WRITE;
/*!40000 ALTER TABLE `login_users` DISABLE KEYS */;
INSERT INTO `login_users` VALUES (1,'correo123@gmail.com','123456789');
/*!40000 ALTER TABLE `login_users` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `productos`
--

DROP TABLE IF EXISTS `productos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `productos` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(255) NOT NULL,
  `descripcion` text,
  `precio` decimal(10,2) NOT NULL,
  `cantidad` int NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `productos`
--

LOCK TABLES `productos` WRITE;
/*!40000 ALTER TABLE `productos` DISABLE KEYS */;
INSERT INTO `productos` VALUES (1,'Zapato Deportivo','Zapato ideal para actividades deportivas y casuales',120000.00,100),(2,'Bota de Cuero','Bota de cuero premium, resistente al agua',250000.00,75),(3,'Zapato Formal','Zapato elegante para ocasiones especiales',180000.00,50),(4,'Sandalia Casual','Sandalia cómoda y ligera para el verano',60000.00,200),(5,'Zapato de Negocios','Zapato de negocios con diseño clásico y moderno',220000.00,80);
/*!40000 ALTER TABLE `productos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `register_users`
--

DROP TABLE IF EXISTS `register_users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `register_users` (
  `id` int NOT NULL AUTO_INCREMENT,
  `fullname` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email_UNIQUE` (`email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `register_users`
--

LOCK TABLES `register_users` WRITE;
/*!40000 ALTER TABLE `register_users` DISABLE KEYS */;
/*!40000 ALTER TABLE `register_users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-10-18 23:43:22
