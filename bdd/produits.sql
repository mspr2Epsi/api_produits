-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: May 13, 2024 at 01:38 PM
-- Server version: 8.0.31
-- PHP Version: 8.0.26

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `mspr2`
--

-- --------------------------------------------------------

--
-- Table structure for table `produits`
--

DROP TABLE IF EXISTS `produits`;
CREATE TABLE IF NOT EXISTS `produits` (
  `ProduitID` int NOT NULL AUTO_INCREMENT,
  `Nom` varchar(255) DEFAULT NULL,
  `Description` text,
  `PrixUnitaire` decimal(10,2) DEFAULT NULL,
  `Stock` int DEFAULT NULL,
  `Fournisseur` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`ProduitID`)
) ENGINE=MyISAM AUTO_INCREMENT=32 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `produits`
--

INSERT INTO `produits` (`ProduitID`, `Nom`, `Description`, `PrixUnitaire`, `Stock`, `Fournisseur`) VALUES
(1, 'Table en bois', 'Table en bois massif', '199.99', 50, 'Ikea'),
(2, 'Chaise de bureau', 'Chaise ergonomique avec accoudoirs', '129.99', 30, 'Staples'),
(3, 'Lampe de chevet', 'Lampe de chevet avec abat-jour', '29.99', 100, 'Philips'),
(5, 'Sofa en cuir', 'Sofa en cuir noir', '899.99', 70, 'Ashley Furniture'),
(6, 'Matelas à mémoire de forme', 'Matelas 140x200 cm', '499.99', 20, 'Tempur-Pedic'),
(7, 'Réfrigérateur', 'Réfrigérateur à double porte', '699.99', 200, 'LG'),
(8, 'Four micro-ondes', 'Four micro-ondes 900W', '79.99', 10, 'Samsung'),
(9, 'Télévision 4K', 'Télévision 55 pouces 4K', '599.99', 5, 'Sony'),
(10, 'Machine à laver', 'Machine à laver frontale', '399.99', 15, 'Whirlpool'),
(11, 'Table de cuisine', 'Table de cuisine en verre', '249.99', 25, 'Ikea'),
(12, 'Fauteuil relax', 'Fauteuil avec repose-pieds', '199.99', 35, 'La-Z-Boy'),
(13, 'Bureau d\'ordinateur', 'Bureau d\'ordinateur en métal', '149.99', 45, 'Office Depot'),
(14, 'Aspirateur sans sac', 'Aspirateur Dyson V11', '599.99', 55, 'Dyson'),
(15, 'Table basse', 'Table basse en verre trempé', '89.99', 65, 'Wayfair'),
(16, 'Buffet de cuisine', 'Buffet avec rangements', '299.99', 75, 'Ikea'),
(17, 'Armoire penderie', 'Armoire à portes coulissantes', '399.99', 85, 'Home Depot'),
(18, 'Lit double', 'Lit double avec rangement', '349.99', 95, 'Ikea'),
(19, 'Canapé-lit', 'Canapé-lit en tissu', '499.99', 105, 'Ashley Furniture'),
(20, 'Bibliothèque', 'Bibliothèque en chêne', '199.99', 115, 'Wayfair'),
(21, 'Climatiseur portable', 'Climatiseur 12000 BTU', '399.99', 125, 'LG'),
(22, 'Grille-pain', 'Grille-pain à 4 fentes', '49.99', 135, 'Breville'),
(23, 'Cafetière', 'Cafetière programmable 12 tasses', '79.99', 145, 'Keurig'),
(24, 'Blender', 'Blender haute puissance', '99.99', 155, 'Ninja'),
(25, 'Tablette', 'Tablette 10 pouces Android', '299.99', 165, 'Samsung'),
(26, 'Smartphone', 'Smartphone 5G', '799.99', 175, 'Apple'),
(27, 'Enceinte Bluetooth', 'Enceinte Bluetooth portable', '199.99', 185, 'Bose'),
(28, 'Montre connectée', 'Montre connectée GPS', '249.99', 195, 'Garmin'),
(29, 'Casque audio', 'Casque audio sans fil', '299.99', 205, 'Sony'),
(30, 'Barbecue', 'Barbecue à gaz 4 brûleurs', '399.99', 10, 'Weber'),
(31, 'Tondeuse à gazon', 'Tondeuse électrique sans fil', '349.99', 100, 'Greenworks');

COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
