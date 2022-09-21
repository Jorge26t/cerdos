/*
 Navicat Premium Data Transfer

 Source Server         : Mysql
 Source Server Type    : MySQL
 Source Server Version : 80028
 Source Host           : localhost:3306
 Source Schema         : tesis_cerdo

 Target Server Type    : MySQL
 Target Server Version : 80028
 File Encoding         : 65001

 Date: 21/09/2022 11:21:33
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for cerdo
-- ----------------------------
DROP TABLE IF EXISTS `cerdo`;
CREATE TABLE `cerdo`  (
  `id_cerdo` int NOT NULL AUTO_INCREMENT,
  `codigo` char(25) CHARACTER SET utf8 COLLATE utf8_spanish_ci NULL DEFAULT NULL,
  `nombre` varchar(255) CHARACTER SET utf8 COLLATE utf8_spanish_ci NULL DEFAULT NULL,
  `sexo` char(15) CHARACTER SET utf8 COLLATE utf8_spanish_ci NULL DEFAULT NULL,
  `raza` int NULL DEFAULT NULL,
  `peso` char(30) CHARACTER SET utf8 COLLATE utf8_spanish_ci NULL DEFAULT NULL,
  `origen` text CHARACTER SET utf8 COLLATE utf8_spanish_ci NULL,
  `fecha` date NULL DEFAULT NULL,
  `detalle` text CHARACTER SET utf8 COLLATE utf8_spanish_ci NULL,
  `foto` varchar(255) CHARACTER SET utf8 COLLATE utf8_spanish_ci NULL DEFAULT NULL,
  `estado` int NULL DEFAULT 1,
  `galpon` varchar(255) CHARACTER SET utf8 COLLATE utf8_spanish_ci NULL DEFAULT 'no',
  PRIMARY KEY (`id_cerdo`) USING BTREE,
  INDEX `raza`(`raza`) USING BTREE,
  CONSTRAINT `cerdo_ibfk_1` FOREIGN KEY (`raza`) REFERENCES `raza` (`id_raza`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE = InnoDB AUTO_INCREMENT = 3 CHARACTER SET = utf8 COLLATE = utf8_spanish_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of cerdo
-- ----------------------------
INSERT INTO `cerdo` VALUES (1, '964664418', 'pepe pig', 'Hembra', 2, '123', 'de la tev', '2022-10-02', ' en una cerdo bien sucia', '20220912121318user2-160x160.jpg', 1, 'si');
INSERT INTO `cerdo` VALUES (2, '964664411', 'pepe pig dos editado', 'Hembra', 3, '100', 'Origen del cerdo editado', '2022-09-01', ' Detalle del cerdo editado', '20220912121337user.png', 1, 'si');

-- ----------------------------
-- Table structure for empresa
-- ----------------------------
DROP TABLE IF EXISTS `empresa`;
CREATE TABLE `empresa`  (
  `id_hacienda` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(255) CHARACTER SET utf8 COLLATE utf8_spanish_ci NULL DEFAULT NULL,
  `ruc` varchar(255) CHARACTER SET utf8 COLLATE utf8_spanish_ci NULL DEFAULT NULL,
  `telefono` char(15) CHARACTER SET utf8 COLLATE utf8_spanish_ci NULL DEFAULT NULL,
  `correo` varchar(255) CHARACTER SET utf8 COLLATE utf8_spanish_ci NULL DEFAULT NULL,
  `foto` varchar(255) CHARACTER SET utf8 COLLATE utf8_spanish_ci NULL DEFAULT NULL,
  `encargado` varchar(255) CHARACTER SET utf8 COLLATE utf8_spanish_ci NULL DEFAULT NULL,
  `descripcion` text CHARACTER SET utf8 COLLATE utf8_spanish_ci NULL,
  `direccion` varchar(255) CHARACTER SET utf8 COLLATE utf8_spanish_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id_hacienda`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 2 CHARACTER SET = utf8 COLLATE = utf8_spanish_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of empresa
-- ----------------------------
INSERT INTO `empresa` VALUES (1, 'Nombre de hacienda', '0985906677', '0940321854', 'elgamer-26@hotmail.com', '20220908103851AdminLTELogo.png', 'Encargado', 'Descripción de hacienda', 'Dirección');

-- ----------------------------
-- Table structure for galpon
-- ----------------------------
DROP TABLE IF EXISTS `galpon`;
CREATE TABLE `galpon`  (
  `id_galpon` int NOT NULL AUTO_INCREMENT,
  `numero` char(15) CHARACTER SET utf8 COLLATE utf8_spanish_ci NULL DEFAULT NULL,
  `id_tipo` int NULL DEFAULT NULL,
  `capacidad` int NULL DEFAULT NULL,
  `observacion` varchar(255) CHARACTER SET utf8 COLLATE utf8_spanish_ci NULL DEFAULT NULL,
  `estado` int NULL DEFAULT 1,
  PRIMARY KEY (`id_galpon`) USING BTREE,
  INDEX `id_tipo`(`id_tipo`) USING BTREE,
  CONSTRAINT `galpon_ibfk_1` FOREIGN KEY (`id_tipo`) REFERENCES `tipo_galpon` (`id_tipo`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE = InnoDB AUTO_INCREMENT = 3 CHARACTER SET = utf8 COLLATE = utf8_spanish_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of galpon
-- ----------------------------
INSERT INTO `galpon` VALUES (1, '123', 2, 3, 'para criar chancho', 1);
INSERT INTO `galpon` VALUES (2, '321', 1, 5, 'aaa', 1);

-- ----------------------------
-- Table structure for galpon_cerdo
-- ----------------------------
DROP TABLE IF EXISTS `galpon_cerdo`;
CREATE TABLE `galpon_cerdo`  (
  `id_galpon_cerdo` int NOT NULL AUTO_INCREMENT,
  `id_galpon` int NULL DEFAULT NULL,
  `id_cerdo` int NULL DEFAULT NULL,
  `fecha` date NULL DEFAULT NULL,
  `estado` int NULL DEFAULT 1,
  PRIMARY KEY (`id_galpon_cerdo`) USING BTREE,
  INDEX `id_galpon`(`id_galpon`) USING BTREE,
  INDEX `id_cerdo`(`id_cerdo`) USING BTREE,
  CONSTRAINT `galpon_cerdo_ibfk_1` FOREIGN KEY (`id_galpon`) REFERENCES `galpon` (`id_galpon`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `galpon_cerdo_ibfk_2` FOREIGN KEY (`id_cerdo`) REFERENCES `cerdo` (`id_cerdo`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE = InnoDB AUTO_INCREMENT = 8 CHARACTER SET = utf8 COLLATE = utf8_spanish_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of galpon_cerdo
-- ----------------------------
INSERT INTO `galpon_cerdo` VALUES (6, 1, 1, '2022-09-21', 1);
INSERT INTO `galpon_cerdo` VALUES (7, 2, 2, '2022-09-20', 1);

-- ----------------------------
-- Table structure for movimientos
-- ----------------------------
DROP TABLE IF EXISTS `movimientos`;
CREATE TABLE `movimientos`  (
  `id_m` int NOT NULL AUTO_INCREMENT,
  `id_g_c` int NULL DEFAULT NULL,
  `fecha` date NULL DEFAULT NULL,
  `hasta` varchar(255) CHARACTER SET utf8 COLLATE utf8_spanish_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id_m`) USING BTREE,
  INDEX `id_g_c`(`id_g_c`) USING BTREE,
  CONSTRAINT `movimientos_ibfk_1` FOREIGN KEY (`id_g_c`) REFERENCES `galpon_cerdo` (`id_galpon_cerdo`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_spanish_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of movimientos
-- ----------------------------
INSERT INTO `movimientos` VALUES (15, 6, '2022-09-21', 'N°: 321 - Tipo: lote editado');

-- ----------------------------
-- Table structure for raza
-- ----------------------------
DROP TABLE IF EXISTS `raza`;
CREATE TABLE `raza`  (
  `id_raza` int NOT NULL AUTO_INCREMENT,
  `raza` varchar(255) CHARACTER SET utf8 COLLATE utf8_spanish_ci NULL DEFAULT NULL,
  `estado` int NULL DEFAULT 1,
  PRIMARY KEY (`id_raza`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 8 CHARACTER SET = utf8 COLLATE = utf8_spanish_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of raza
-- ----------------------------
INSERT INTO `raza` VALUES (1, 'gordo editao', 1);
INSERT INTO `raza` VALUES (2, 'lote', 1);
INSERT INTO `raza` VALUES (3, 'a', 1);
INSERT INTO `raza` VALUES (4, 's', 0);
INSERT INTO `raza` VALUES (5, 'aw', 0);
INSERT INTO `raza` VALUES (6, 'ss', 0);
INSERT INTO `raza` VALUES (7, 'asde dita', 0);

-- ----------------------------
-- Table structure for rol
-- ----------------------------
DROP TABLE IF EXISTS `rol`;
CREATE TABLE `rol`  (
  `rol_id` int NOT NULL AUTO_INCREMENT,
  `rol` varchar(255) CHARACTER SET utf8 COLLATE utf8_spanish_ci NULL DEFAULT NULL,
  `estado` int NULL DEFAULT 1,
  PRIMARY KEY (`rol_id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 7 CHARACTER SET = utf8 COLLATE = utf8_spanish_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of rol
-- ----------------------------
INSERT INTO `rol` VALUES (1, 'administrador', 1);
INSERT INTO `rol` VALUES (2, 'bodega edita', 1);
INSERT INTO `rol` VALUES (3, 'alimentador', 1);
INSERT INTO `rol` VALUES (4, 'trabajador', 1);
INSERT INTO `rol` VALUES (5, 'CHANCHO', 0);
INSERT INTO `rol` VALUES (6, 'nuevo rol', 0);

-- ----------------------------
-- Table structure for tipo_galpon
-- ----------------------------
DROP TABLE IF EXISTS `tipo_galpon`;
CREATE TABLE `tipo_galpon`  (
  `id_tipo` int NOT NULL AUTO_INCREMENT,
  `tipo_galpon` varchar(255) CHARACTER SET utf8 COLLATE utf8_spanish_ci NULL DEFAULT NULL,
  `estado` int NULL DEFAULT 1,
  PRIMARY KEY (`id_tipo`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 3 CHARACTER SET = utf8 COLLATE = utf8_spanish_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of tipo_galpon
-- ----------------------------
INSERT INTO `tipo_galpon` VALUES (1, 'lote editado', 1);
INSERT INTO `tipo_galpon` VALUES (2, 'lechones', 1);

-- ----------------------------
-- Table structure for usuario
-- ----------------------------
DROP TABLE IF EXISTS `usuario`;
CREATE TABLE `usuario`  (
  `usuario_id` int NOT NULL AUTO_INCREMENT,
  `nombres` varchar(255) CHARACTER SET utf8 COLLATE utf8_spanish_ci NULL DEFAULT NULL,
  `apellidos` varchar(255) CHARACTER SET utf8 COLLATE utf8_spanish_ci NULL DEFAULT NULL,
  `usuario` varchar(255) CHARACTER SET utf8 COLLATE utf8_spanish_ci NULL DEFAULT NULL,
  `passwordd` varchar(255) CHARACTER SET utf8 COLLATE utf8_spanish_ci NULL DEFAULT NULL,
  `rol_id` int NULL DEFAULT NULL,
  `domicilio` varchar(200) CHARACTER SET utf8 COLLATE utf8_spanish_ci NULL DEFAULT NULL,
  `telefono` varchar(200) CHARACTER SET utf8 COLLATE utf8_spanish_ci NULL DEFAULT NULL,
  `foto` varchar(255) CHARACTER SET utf8 COLLATE utf8_spanish_ci NULL DEFAULT NULL,
  `estado` int NULL DEFAULT 1,
  PRIMARY KEY (`usuario_id`) USING BTREE,
  INDEX `rol_id`(`rol_id`) USING BTREE,
  CONSTRAINT `usuario_ibfk_1` FOREIGN KEY (`rol_id`) REFERENCES `rol` (`rol_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE = InnoDB AUTO_INCREMENT = 13 CHARACTER SET = utf8 COLLATE = utf8_spanish_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of usuario
-- ----------------------------
INSERT INTO `usuario` VALUES (1, 'JORGE MOISES', 'RAMIREZ ZAVALA', 'admin', '123', 1, 'casa', '123', '20220908132642user3-128x128.jpg', 1);
INSERT INTO `usuario` VALUES (9, 'as', 'asa', 'asa', 'Jorge2´+', 1, 'asa', 'asas', '20220907195019avatar5.png', 1);
INSERT INTO `usuario` VALUES (10, 'aaaaaaaaaa', 'bbbbbbbb', 'ssssss', 'Jorgqwqw12´@', 2, 'ccccccccccc', '111111111', '20220907195131avatar3.png', 1);
INSERT INTO `usuario` VALUES (11, 'JORGE MOISES', 'RAMIREZ ZAVALA', 'Jorge', 'Jorge12q,.', 1, 'MILAGRO', '0987654321', '20220907195143avatar.png', 1);
INSERT INTO `usuario` VALUES (12, 'aaaaaaaaaaaa', 'ccccccccc', 'abc', 'AM112.,´q', 3, 'a121', '1212121', '20220907140512_IMG192202211510.png', 1);

-- ----------------------------
-- Procedure structure for sp_capacidad_disponible
-- ----------------------------
DROP PROCEDURE IF EXISTS `sp_capacidad_disponible`;
delimiter ;;
CREATE PROCEDURE `sp_capacidad_disponible`(in id int)
BEGIN
DECLARE uno int;
DECLARE dos int;

SELECT
	COUNT(id_cerdo) AS cerdos INTO uno
FROM
	galpon
	INNER JOIN galpon_cerdo ON galpon.id_galpon = galpon_cerdo.id_galpon 
WHERE
	galpon_cerdo.id_galpon = id;

SELECT capacidad INTO dos from galpon WHERE id_galpon = id;

SELECT uno, dos;

END
;;
delimiter ;

SET FOREIGN_KEY_CHECKS = 1;
