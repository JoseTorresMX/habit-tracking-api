-- MariaDB dump 10.19  Distrib 10.4.32-MariaDB, for Win64 (AMD64)
--
-- Host: localhost    Database: habit_tracker
-- ------------------------------------------------------
-- Server version	10.4.32-MariaDB

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `habit_tracking`
--

DROP TABLE IF EXISTS `habit_tracking`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `habit_tracking` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `habit_id` int(11) NOT NULL,
  `date` date NOT NULL,
  `status` enum('completado','pendiente') DEFAULT 'pendiente',
  PRIMARY KEY (`id`),
  UNIQUE KEY `unique_habit_date` (`habit_id`,`date`),
  CONSTRAINT `habit_tracking_ibfk_1` FOREIGN KEY (`habit_id`) REFERENCES `habits` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `habit_tracking`
--

LOCK TABLES `habit_tracking` WRITE;
/*!40000 ALTER TABLE `habit_tracking` DISABLE KEYS */;
INSERT INTO `habit_tracking` VALUES (1,5,'2024-12-11','completado');
/*!40000 ALTER TABLE `habit_tracking` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `habits`
--

DROP TABLE IF EXISTS `habits`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `habits` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `name` varchar(100) NOT NULL,
  `description` varchar(255) DEFAULT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp(),
  PRIMARY KEY (`id`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `habits_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `habits`
--

LOCK TABLES `habits` WRITE;
/*!40000 ALTER TABLE `habits` DISABLE KEYS */;
INSERT INTO `habits` VALUES (1,3,'Maraton','por la tarde crre','2024-12-08 06:36:17'),(2,17,'Ejercicio','sadasdasdasd','2024-12-11 15:20:38'),(3,17,'Ejercicio','sadasdasdasd','2024-12-11 15:20:47'),(4,17,'Ejercicio','sadasdasdasd','2024-12-11 15:23:37'),(5,17,'paso la prueba','pasola prueba','2024-12-11 15:25:41'),(6,17,'paso la prueba','pasola prueba','2024-12-11 15:35:58'),(7,17,'paso la prueba','pasola prueba','2024-12-11 15:43:31'),(8,17,'paso la prueba','pasola prueba','2024-12-11 15:43:32'),(9,17,'paso la prueba','pasola prueba','2024-12-11 15:43:33'),(10,17,'paso la prueba','pasola prueba','2024-12-11 15:43:34');
/*!40000 ALTER TABLE `habits` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(50) NOT NULL,
  `email` varchar(100) NOT NULL,
  `password_hash` varchar(255) NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp(),
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'usuarioPruopeba41','usuarhjio@ejemplo.com','$2b$12$9eDxwK4YDE1ykkOkDiWeYu7pusxnX1Gj0PWBQuH1fuZMZw7XKlnmq','2024-12-08 05:57:14'),(2,'usuario','usuarhjiosws@ejemplo.com','$2b$12$l05yaaiLLbKNmB0CBDyTzOhIq9.cv.S2MrzI7Sz.wg.oKsPASy0rm','2024-12-08 05:58:40'),(3,'jtorres','jtorres@gmail.com','$2b$12$X.vk4/5e2Cx6kaoJU43IMOyJicEufNZn7iv7oBYmag4WH0ltl50rW','2024-12-08 06:01:54'),(4,'jtorress','jtorres@ji.com','$2b$12$CuPYBhqJSNNanOrOhEhlf.LSCIgKnzZqWXh6CNgaXh1IOPsrDztwm','2024-12-08 06:06:52'),(5,'jtorres48521','itcj@itcj.com','$2b$12$dXx0QuSRa2v/.Wi74vSUeueDahTLO3MxO06SI74xQmGeCGlIWavLS','2024-12-08 06:45:55'),(6,'jtorres48521uyy','itcj@itcghhj.com','$2b$12$NCVyiB9z9ljZJhtBMrRm8OFmmoGVCuvk5kEGbkhHomqIFn8tqYuTO','2024-12-08 06:46:42'),(7,'julio70','julio70@itcj.com','$2b$12$G1sqqy2KptAr.XbaKhQy8O9HQKAar6LIwK2dNdIK6yIHfO.2igFKi','2024-12-08 06:47:33'),(8,'julio74','julio77@itcj.com','$2b$12$Chd0UoGfaAHS1aRD6X3G0.VzLWNS4B7jZikdkupzsrL6r0sSTkvty','2024-12-08 06:48:33'),(9,'julio744','julio774@itcj.com','$2b$12$FR/d26OMePU4UGXw0EI/Q.noqZZzTm8D1KK8R4aaO8CnqewJDA7wG','2024-12-08 06:51:27'),(10,'julio74p4','juliop774@itcj.com','$2b$12$fZMGbCCh3mec8RQ2aswlDeVRK6uLPM4qTZEVveqeyDKBdnoibON96','2024-12-08 06:51:56'),(11,'prueba1','prueba@example.com','$2b$12$ydfhOZ/cS1d6l.pEXQwUxeNvKd4z1t7TsiCh7gdkmYwc7KWVjcY/K','2024-12-08 07:18:46'),(12,'Jose','l19@example.com','$2b$12$GtH.rBoYi2gZe5JLsuHK9uCOp5ZLJ4UfQRnaba4pRQAMq9nv7KNCO','2024-12-11 11:22:52'),(13,'Jose9','l198@example.com','$2b$12$b9N9xZWUQmJquWnw1aCzP.gEk9njwFs/NI86PMKW.CkFoO96qLCd6','2024-12-11 05:07:20'),(14,'Jose79','l194788@example.com','$2b$12$9iUeVPwt01Y1e9AS3i9ACOUdk0MpvmkREBdJmrF3Lv7f9.SN8O1xm','2024-12-11 05:21:01'),(15,'Jos44e79','l19444788@example.com','$2b$12$fG.9zy5HGilD1Iup1kt.x.RibgGCnFTWW3NliCptIZSbtTLw9UuUS','2024-12-11 12:30:30'),(16,'Jos44es79','l19444ss788@example.com','$2b$12$2YgUoSQi/nPja3rc89Jq5OTg4d3zaXbW25AC7kaJeEnkpY6xjN5hS','2024-12-11 14:24:30'),(17,'torres','torres@example.com','$2b$12$jSdkNP9QGWORXoVvov9XoupDQnAisQlJzK17VATEIgqG7jCH2XLta','2024-12-11 15:19:08');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-12-11  1:45:48
