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
(1, 'Produit 1', 'Description produit 1', '19.99', 50, 'Fournisseur 1'),
(2, 'Produit 2', 'Description produit 2', '29.99', 30, 'Fournisseur 2'),
(3, 'Produit 3', 'Description produit 3', '9.99', 100, 'Fournisseur 3'),
(5, 'Produit 5', 'Description produit 5', '24.99', 70, 'Fournisseur 5'),
(6, 'Produit 6', 'Description produit 6', '34.99', 20, 'Fournisseur 6'),
(7, 'Produit 7', 'Description produit 7', '4.99', 200, 'Fournisseur 7'),
(8, 'Produit 8', 'Description produit 8', '39.99', 10, 'Fournisseur 8'),
(9, 'Produit 9', 'Description produit 9', '49.99', 5, 'Fournisseur 9'),
(10, 'Produit 10', 'Description produit 10', '59.99', 15, 'Fournisseur 10'),
(11, 'Produit 11', 'Description produit 11', '69.99', 25, 'Fournisseur 11'),
(12, 'Produit 12', 'Description produit 12', '79.99', 35, 'Fournisseur 12'),
(13, 'Produit 13', 'Description produit 13', '89.99', 45, 'Fournisseur 13'),
(14, 'Produit 14', 'Description produit 14', '99.99', 55, 'Fournisseur 14'),
(15, 'Produit 15', 'Description produit 15', '109.99', 65, 'Fournisseur 15'),
(16, 'Produit 16', 'Description produit 16', '119.99', 75, 'Fournisseur 16'),
(17, 'Produit 17', 'Description produit 17', '129.99', 85, 'Fournisseur 17'),
(18, 'Produit 18', 'Description produit 18', '139.99', 95, 'Fournisseur 18'),
(19, 'Produit 19', 'Description produit 19', '149.99', 105, 'Fournisseur 19'),
(20, 'Produit 20', 'Description produit 20', '159.99', 115, 'Fournisseur 20'),
(21, 'Produit 21', 'Description produit 21', '169.99', 125, 'Fournisseur 21'),
(22, 'Produit 22', 'Description produit 22', '179.99', 135, 'Fournisseur 22'),
(23, 'Produit 23', 'Description produit 23', '189.99', 145, 'Fournisseur 23'),
(24, 'Produit 24', 'Description produit 24', '199.99', 155, 'Fournisseur 24'),
(25, 'Produit 25', 'Description produit 25', '209.99', 165, 'Fournisseur 25'),
(26, 'Produit 26', 'Description produit 26', '219.99', 175, 'Fournisseur 26'),
(27, 'Produit 27', 'Description produit 27', '229.99', 185, 'Fournisseur 27'),
(28, 'Produit 28', 'Description produit 28', '239.99', 195, 'Fournisseur 28'),
(29, 'Produit 29', 'Description produit 29', '249.99', 205, 'Fournisseur 29'),
(30, 'New nom produit MAJ', 'New Description', '14.99', 10, 'Fournisseur XYZ'),
(31, 'Nouveau Produit', 'Description du nouveau produit', '10.99', 100, 'Fournisseur XYZ');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
