-- phpMyAdmin SQL Dump
-- version 4.9.5deb2
-- https://www.phpmyadmin.net/
--
-- Servidor: localhost:3306
-- Tiempo de generación: 10-06-2022 a las 14:45:03
-- Versión del servidor: 8.0.29-0ubuntu0.20.04.3
-- Versión de PHP: 7.4.3

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `escodisco`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `Clients`
--

CREATE TABLE `Clients` (
  `ID` int NOT NULL,
  `Nom` varchar(20) COLLATE utf32_spanish_ci NOT NULL,
  `Cognoms` varchar(40) COLLATE utf32_spanish_ci NOT NULL,
  `DNI` varchar(9) CHARACTER SET utf32 COLLATE utf32_spanish_ci NOT NULL,
  `Sexe` varchar(255) CHARACTER SET utf32 COLLATE utf32_spanish_ci NOT NULL,
  `Edat` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf32 COLLATE=utf32_spanish_ci;

--
-- Volcado de datos para la tabla `Clients`
--

INSERT INTO `Clients` (`ID`, `Nom`, `Cognoms`, `DNI`, `Sexe`, `Edat`) VALUES
(1, 'Nil', 'Saborit Gilabert', '79279241N', 'A vegades', 29),
(2, 'Biel', 'Clos Roset', '34554333Q', 'Gei', 19),
(3, 'Eric', 'Porcuna Rodriguez', '12332111Q', '69', 20),
(4, 'Gheorg', 'Dumitru', 'No en te', 'Zoofilic', 29);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `Consumicions`
--

CREATE TABLE `Consumicions` (
  `Article` varchar(20) COLLATE utf32_spanish_ci NOT NULL,
  `Quant` int NOT NULL,
  `Preu_Unitat` int NOT NULL,
  `Client` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf32 COLLATE=utf32_spanish_ci;

--
-- Volcado de datos para la tabla `Consumicions`
--

INSERT INTO `Consumicions` (`Article`, `Quant`, `Preu_Unitat`, `Client`) VALUES
('Combinat', 10, 8, 1),
('Combinat', 4, 8, 2),
('Aigua', 2, 4, 4),
('Combinat', 5, 8, 3),
('Xupito', 3, 3, 1);

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `Clients`
--
ALTER TABLE `Clients`
  ADD PRIMARY KEY (`ID`);

--
-- Indices de la tabla `Consumicions`
--
ALTER TABLE `Consumicions`
  ADD KEY `Client` (`Client`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `Clients`
--
ALTER TABLE `Clients`
  MODIFY `ID` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `Consumicions`
--
ALTER TABLE `Consumicions`
  ADD CONSTRAINT `Consumicions_ibfk_1` FOREIGN KEY (`Client`) REFERENCES `Clients` (`ID`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
