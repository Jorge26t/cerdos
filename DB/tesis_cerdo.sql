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

 Date: 07/10/2022 11:07:39
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for alimentacion
-- ----------------------------
DROP TABLE IF EXISTS `alimentacion`;
CREATE TABLE `alimentacion`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `alimento_id` int NULL DEFAULT NULL,
  `tipo_id` int NULL DEFAULT NULL,
  `usuario_id` int NULL DEFAULT NULL,
  `fecha` date NULL DEFAULT NULL,
  `cantidad` int NULL DEFAULT NULL,
  `observacion` varchar(255) CHARACTER SET utf8 COLLATE utf8_spanish_ci NULL DEFAULT NULL,
  `estado` int NULL DEFAULT 1,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `alimento_id`(`alimento_id`) USING BTREE,
  INDEX `tipo_id`(`tipo_id`) USING BTREE,
  INDEX `usuario_id`(`usuario_id`) USING BTREE,
  CONSTRAINT `alimentacion_ibfk_1` FOREIGN KEY (`alimento_id`) REFERENCES `alimento` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `alimentacion_ibfk_2` FOREIGN KEY (`tipo_id`) REFERENCES `tipo_alimentcion` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `alimentacion_ibfk_3` FOREIGN KEY (`usuario_id`) REFERENCES `usuario` (`usuario_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE = InnoDB AUTO_INCREMENT = 14 CHARACTER SET = utf8 COLLATE = utf8_spanish_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of alimentacion
-- ----------------------------
INSERT INTO `alimentacion` VALUES (9, 3, 1, 1, '2022-09-27', 1, 'Observación', 1);
INSERT INTO `alimentacion` VALUES (10, 1, 2, 1, '2022-09-27', 8, 'Observación de alimentacion', 1);
INSERT INTO `alimentacion` VALUES (11, 3, 2, 1, '2022-09-28', 1, 'LA CRIAR CERDITOS', 1);
INSERT INTO `alimentacion` VALUES (12, 3, 1, 1, '2022-10-06', 3, 'Observación', 1);
INSERT INTO `alimentacion` VALUES (13, 2, 1, 1, '2022-10-06', 2, 'Observación engorda', 1);

-- ----------------------------
-- Table structure for alimento
-- ----------------------------
DROP TABLE IF EXISTS `alimento`;
CREATE TABLE `alimento`  (
  `id` int NOT NULL AUTO_INCREMENT COMMENT 'Primary Key',
  `codigo` char(50) CHARACTER SET utf8 COLLATE utf8_spanish_ci NULL DEFAULT NULL,
  `nombre` varchar(255) CHARACTER SET utf8 COLLATE utf8_spanish_ci NULL DEFAULT NULL,
  `tipo_id` int NULL DEFAULT NULL,
  `marca_id` int NULL DEFAULT NULL,
  `cantidad` int NULL DEFAULT 1,
  `precio` decimal(10, 2) NULL DEFAULT NULL,
  `peso` decimal(10, 2) NULL DEFAULT NULL,
  `detalle` text CHARACTER SET utf8 COLLATE utf8_spanish_ci NULL,
  `foto` varchar(100) CHARACTER SET utf8 COLLATE utf8_spanish_ci NULL DEFAULT NULL,
  `estado` int NULL DEFAULT 1,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `tipo_id`(`tipo_id`) USING BTREE,
  INDEX `marca_id`(`marca_id`) USING BTREE,
  CONSTRAINT `alimento_ibfk_1` FOREIGN KEY (`tipo_id`) REFERENCES `tipo_alimento` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `alimento_ibfk_2` FOREIGN KEY (`marca_id`) REFERENCES `marca_alimento` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE = InnoDB AUTO_INCREMENT = 4 CHARACTER SET = utf8 COLLATE = utf8_spanish_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of alimento
-- ----------------------------
INSERT INTO `alimento` VALUES (1, '808715633', 'DON CHANCHO', 3, 2, 10, 100.20, 3.40, ' ALIMENTO PARA ENGORDA DEL CERDO Y PARA CRECIMIENTO', '20220923200226_prod-5.jpg', 1);
INSERT INTO `alimento` VALUES (2, '157962197', 'NUEVO ALIMENTO editaado', 2, 3, 14, 321.00, 3.00, ' Detalle del saco de alimento del cerdo editado ', '20220923203750AdminLTELogo.png', 1);
INSERT INTO `alimento` VALUES (3, '888408884', 'Repuestos AlmaZull', 2, 3, 0, 23.00, 34.00, ' Detalle del saco de alimento del cerdo', 'alimento.jpg', 1);

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
INSERT INTO `cerdo` VALUES (2, '964664411', 'pepe pig dos editado', 'Macho', 3, '110', 'Origen del cerdo editado', '2022-09-01', ' Detalle del cerdo editado', '20220912121337user.png', 1, 'si');

-- ----------------------------
-- Table structure for compra_alimento
-- ----------------------------
DROP TABLE IF EXISTS `compra_alimento`;
CREATE TABLE `compra_alimento`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `usuario_id` int NULL DEFAULT NULL,
  `proveedor_id` int NULL DEFAULT NULL,
  `fecha` date NULL DEFAULT NULL,
  `numero_compra` char(50) CHARACTER SET utf8 COLLATE utf8_spanish_ci NULL DEFAULT NULL,
  `documento` char(50) CHARACTER SET utf8 COLLATE utf8_spanish_ci NULL DEFAULT NULL,
  `iva` int NULL DEFAULT NULL,
  `subtotal` decimal(10, 2) NULL DEFAULT NULL,
  `impuesto` decimal(10, 2) NULL DEFAULT NULL,
  `total` decimal(10, 2) NULL DEFAULT NULL,
  `estado` int NULL DEFAULT 1,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `usuario_id`(`usuario_id`) USING BTREE,
  INDEX `proveedor_id`(`proveedor_id`) USING BTREE,
  CONSTRAINT `compra_alimento_ibfk_1` FOREIGN KEY (`usuario_id`) REFERENCES `usuario` (`usuario_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `compra_alimento_ibfk_2` FOREIGN KEY (`proveedor_id`) REFERENCES `proveedor` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE = InnoDB AUTO_INCREMENT = 16 CHARACTER SET = utf8 COLLATE = utf8_spanish_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of compra_alimento
-- ----------------------------
INSERT INTO `compra_alimento` VALUES (9, 1, 1, '2022-09-25', '20220605190629', 'Factura', 12, 421.20, 50.54, 471.74, 0);
INSERT INTO `compra_alimento` VALUES (10, 1, 1, '2022-09-25', '20220605200640', 'nota_venta', 0, 36688.80, 0.00, 36688.80, 0);
INSERT INTO `compra_alimento` VALUES (11, 1, 1, '2022-09-26', '20220702090749', 'Factura', 12, 41698.80, 5003.86, 46702.66, 0);
INSERT INTO `compra_alimento` VALUES (12, 1, 1, '2022-09-26', '20220605190633', 'Factura', 12, 2106.00, 252.72, 2358.72, 1);
INSERT INTO `compra_alimento` VALUES (13, 1, 1, '2022-09-26', '20220605200648', 'Factura', 12, 1605.00, 192.60, 1797.60, 0);
INSERT INTO `compra_alimento` VALUES (14, 1, 1, '2022-09-26', '20220702090740', 'Factura', 12, 200.40, 24.05, 224.45, 1);
INSERT INTO `compra_alimento` VALUES (15, 1, 1, '2022-09-26', '20220605190609', 'Factura', 12, 4412.00, 529.44, 4941.44, 1);

-- ----------------------------
-- Table structure for compra_insumo
-- ----------------------------
DROP TABLE IF EXISTS `compra_insumo`;
CREATE TABLE `compra_insumo`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `usuario_id` int NULL DEFAULT NULL,
  `proveedor_id` int NULL DEFAULT NULL,
  `fecha` date NULL DEFAULT NULL,
  `numero_compra` char(50) CHARACTER SET utf8 COLLATE utf8_spanish_ci NULL DEFAULT NULL,
  `documento` char(50) CHARACTER SET utf8 COLLATE utf8_spanish_ci NULL DEFAULT NULL,
  `iva` int NULL DEFAULT NULL,
  `subtotal` decimal(10, 2) NULL DEFAULT NULL,
  `impuesto` decimal(10, 2) NULL DEFAULT NULL,
  `total` decimal(10, 2) NULL DEFAULT NULL,
  `estado` int NULL DEFAULT 1,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `usuario_id`(`usuario_id`) USING BTREE,
  INDEX `proveedor_id`(`proveedor_id`) USING BTREE,
  CONSTRAINT `compra_insumo_ibfk_1` FOREIGN KEY (`usuario_id`) REFERENCES `usuario` (`usuario_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `compra_insumo_ibfk_2` FOREIGN KEY (`proveedor_id`) REFERENCES `proveedor` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE = InnoDB AUTO_INCREMENT = 10 CHARACTER SET = utf8 COLLATE = utf8_spanish_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of compra_insumo
-- ----------------------------
INSERT INTO `compra_insumo` VALUES (1, 1, 1, '2022-10-06', '20220605190634', 'Factura', 12, 321.00, 38.52, 359.52, 0);
INSERT INTO `compra_insumo` VALUES (2, 1, 1, '2022-10-06', '20220605190632', 'Factura', 12, 3318.00, 398.16, 3716.16, 0);
INSERT INTO `compra_insumo` VALUES (3, 1, 1, '2022-10-06', '20220605190609', 'Factura', 12, 3318.00, 398.16, 3716.16, 0);
INSERT INTO `compra_insumo` VALUES (4, 1, 1, '2022-10-06', '20220605190633', 'Factura', 12, 3330.00, 399.60, 3729.60, 0);
INSERT INTO `compra_insumo` VALUES (5, 1, 1, '2022-10-06', '20220605200640', 'Factura', 12, 3850.00, 462.00, 4312.00, 0);
INSERT INTO `compra_insumo` VALUES (6, 1, 1, '2022-10-06', '202206051906123', 'Factura', 12, 3318.00, 398.16, 3716.16, 0);
INSERT INTO `compra_insumo` VALUES (7, 1, 1, '2022-10-06', '20220605112345', 'Factura', 12, 333.00, 39.96, 372.96, 1);
INSERT INTO `compra_insumo` VALUES (8, 1, 1, '2022-10-06', '202206051954321', 'nota_venta', 0, 3330.00, 0.00, 3330.00, 1);
INSERT INTO `compra_insumo` VALUES (9, 1, 1, '2022-10-06', '202206052456', 'nota_venta', 0, 6993.00, 0.00, 6993.00, 1);

-- ----------------------------
-- Table structure for detalle_alimentacion
-- ----------------------------
DROP TABLE IF EXISTS `detalle_alimentacion`;
CREATE TABLE `detalle_alimentacion`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `id_alimentacion` int NULL DEFAULT NULL,
  `id_cerdo` int NULL DEFAULT NULL,
  `peso` decimal(10, 2) NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `id_alimentacion`(`id_alimentacion`) USING BTREE,
  INDEX `id_cerdo`(`id_cerdo`) USING BTREE,
  CONSTRAINT `detalle_alimentacion_ibfk_1` FOREIGN KEY (`id_alimentacion`) REFERENCES `alimentacion` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `detalle_alimentacion_ibfk_2` FOREIGN KEY (`id_cerdo`) REFERENCES `cerdo` (`id_cerdo`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE = InnoDB AUTO_INCREMENT = 11 CHARACTER SET = utf8 COLLATE = utf8_spanish_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of detalle_alimentacion
-- ----------------------------
INSERT INTO `detalle_alimentacion` VALUES (3, 9, 1, 123.00);
INSERT INTO `detalle_alimentacion` VALUES (4, 10, 1, 123.00);
INSERT INTO `detalle_alimentacion` VALUES (5, 10, 2, 100.00);
INSERT INTO `detalle_alimentacion` VALUES (6, 11, 1, 123.00);
INSERT INTO `detalle_alimentacion` VALUES (7, 12, 1, 123.00);
INSERT INTO `detalle_alimentacion` VALUES (8, 12, 2, 110.00);
INSERT INTO `detalle_alimentacion` VALUES (9, 13, 2, 110.00);
INSERT INTO `detalle_alimentacion` VALUES (10, 13, 1, 123.00);

-- ----------------------------
-- Table structure for detalle_compra_alimento
-- ----------------------------
DROP TABLE IF EXISTS `detalle_compra_alimento`;
CREATE TABLE `detalle_compra_alimento`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `compra_alimento_id` int NULL DEFAULT NULL,
  `alimento_id` int NULL DEFAULT NULL,
  `precio` decimal(10, 2) NULL DEFAULT NULL,
  `cantidad` int NULL DEFAULT NULL,
  `descuento` int NULL DEFAULT NULL,
  `total` decimal(10, 2) NULL DEFAULT NULL,
  `estado` int NULL DEFAULT 1,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `compra_alimento_id`(`compra_alimento_id`) USING BTREE,
  INDEX `alimento_id`(`alimento_id`) USING BTREE,
  CONSTRAINT `detalle_compra_alimento_ibfk_1` FOREIGN KEY (`compra_alimento_id`) REFERENCES `compra_alimento` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `detalle_compra_alimento_ibfk_2` FOREIGN KEY (`alimento_id`) REFERENCES `alimento` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE = InnoDB AUTO_INCREMENT = 14 CHARACTER SET = utf8 COLLATE = utf8_spanish_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of detalle_compra_alimento
-- ----------------------------
INSERT INTO `detalle_compra_alimento` VALUES (1, 9, 1, 100.20, 1, 0, 100.20, 1);
INSERT INTO `detalle_compra_alimento` VALUES (2, 9, 2, 321.00, 1, 0, 321.00, 1);
INSERT INTO `detalle_compra_alimento` VALUES (3, 10, 1, 100.20, 49, 0, 4909.80, 1);
INSERT INTO `detalle_compra_alimento` VALUES (4, 10, 2, 321.00, 99, 0, 31779.00, 1);
INSERT INTO `detalle_compra_alimento` VALUES (5, 11, 1, 100.20, 99, 0, 9919.80, 1);
INSERT INTO `detalle_compra_alimento` VALUES (6, 11, 2, 321.00, 99, 0, 31779.00, 1);
INSERT INTO `detalle_compra_alimento` VALUES (7, 12, 1, 100.20, 5, 0, 501.00, 1);
INSERT INTO `detalle_compra_alimento` VALUES (8, 12, 2, 321.00, 5, 0, 1605.00, 1);
INSERT INTO `detalle_compra_alimento` VALUES (9, 13, 2, 321.00, 5, 0, 1605.00, 1);
INSERT INTO `detalle_compra_alimento` VALUES (10, 14, 1, 100.20, 2, 0, 200.40, 1);
INSERT INTO `detalle_compra_alimento` VALUES (11, 15, 2, 321.00, 10, 5, 3205.00, 1);
INSERT INTO `detalle_compra_alimento` VALUES (12, 15, 3, 23.00, 10, 10, 220.00, 1);
INSERT INTO `detalle_compra_alimento` VALUES (13, 15, 1, 100.20, 10, 15, 987.00, 1);

-- ----------------------------
-- Table structure for detalle_compra_insumo
-- ----------------------------
DROP TABLE IF EXISTS `detalle_compra_insumo`;
CREATE TABLE `detalle_compra_insumo`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `compra_insumo_id` int NULL DEFAULT NULL,
  `insumo_id` int NULL DEFAULT NULL,
  `precio` decimal(10, 2) NULL DEFAULT NULL,
  `cantidad` int NULL DEFAULT NULL,
  `descuento` decimal(10, 2) NULL DEFAULT NULL,
  `total` decimal(10, 2) NULL DEFAULT NULL,
  `estado` int NULL DEFAULT 1,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `compra_insumo_id`(`compra_insumo_id`) USING BTREE,
  INDEX `insumo_id`(`insumo_id`) USING BTREE,
  CONSTRAINT `detalle_compra_insumo_ibfk_1` FOREIGN KEY (`compra_insumo_id`) REFERENCES `compra_insumo` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `detalle_compra_insumo_ibfk_2` FOREIGN KEY (`insumo_id`) REFERENCES `insumo` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE = InnoDB AUTO_INCREMENT = 14 CHARACTER SET = utf8 COLLATE = utf8_spanish_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of detalle_compra_insumo
-- ----------------------------
INSERT INTO `detalle_compra_insumo` VALUES (1, 3, 1, 321.00, 10, 0.00, 3210.00, 0);
INSERT INTO `detalle_compra_insumo` VALUES (2, 3, 2, 12.00, 9, 0.00, 108.00, 0);
INSERT INTO `detalle_compra_insumo` VALUES (3, 4, 1, 321.00, 10, 0.00, 3210.00, 0);
INSERT INTO `detalle_compra_insumo` VALUES (4, 4, 2, 12.00, 10, 0.00, 120.00, 0);
INSERT INTO `detalle_compra_insumo` VALUES (5, 5, 1, 321.00, 12, 2.00, 3850.00, 0);
INSERT INTO `detalle_compra_insumo` VALUES (6, 6, 2, 12.00, 9, 0.00, 108.00, 0);
INSERT INTO `detalle_compra_insumo` VALUES (7, 6, 1, 321.00, 10, 0.00, 3210.00, 1);
INSERT INTO `detalle_compra_insumo` VALUES (8, 7, 1, 321.00, 1, 0.00, 321.00, 1);
INSERT INTO `detalle_compra_insumo` VALUES (9, 7, 2, 12.00, 1, 0.00, 12.00, 1);
INSERT INTO `detalle_compra_insumo` VALUES (10, 8, 1, 321.00, 10, 0.00, 3210.00, 1);
INSERT INTO `detalle_compra_insumo` VALUES (11, 8, 2, 12.00, 10, 0.00, 120.00, 1);
INSERT INTO `detalle_compra_insumo` VALUES (12, 9, 1, 321.00, 21, 0.00, 6741.00, 1);
INSERT INTO `detalle_compra_insumo` VALUES (13, 9, 2, 12.00, 21, 0.00, 252.00, 1);

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
INSERT INTO `empresa` VALUES (1, 'Nombre de hacienda', '0985906677', '0940321854', 'elgamer-26@hotmail.com', '20220923203833cerdito.png', 'Encargado', 'Descripción de hacienda', 'Dirección');

-- ----------------------------
-- Table structure for enfermedad
-- ----------------------------
DROP TABLE IF EXISTS `enfermedad`;
CREATE TABLE `enfermedad`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(255) CHARACTER SET utf8 COLLATE utf8_spanish_ci NULL DEFAULT NULL,
  `descripcion` text CHARACTER SET utf8 COLLATE utf8_spanish_ci NULL,
  `estado` int NULL DEFAULT 1,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_spanish_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of enfermedad
-- ----------------------------
INSERT INTO `enfermedad` VALUES (1, 'RABIA editada', 'RABIA ES editada', 1);

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
INSERT INTO `galpon_cerdo` VALUES (6, 1, 1, '2022-09-23', 1);
INSERT INTO `galpon_cerdo` VALUES (7, 2, 2, '2022-09-20', 1);

-- ----------------------------
-- Table structure for insumo
-- ----------------------------
DROP TABLE IF EXISTS `insumo`;
CREATE TABLE `insumo`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `codigo` char(50) CHARACTER SET utf8 COLLATE utf8_spanish_ci NULL DEFAULT NULL,
  `nombre` varchar(255) CHARACTER SET utf8 COLLATE utf8_spanish_ci NULL DEFAULT NULL,
  `tipo_id` int NULL DEFAULT NULL,
  `cantidad` int NULL DEFAULT NULL,
  `precio` decimal(10, 2) NULL DEFAULT NULL,
  `detalle` text CHARACTER SET utf8 COLLATE utf8_spanish_ci NULL,
  `foto` varchar(255) CHARACTER SET utf8 COLLATE utf8_spanish_ci NULL DEFAULT NULL,
  `estado` int NULL DEFAULT 1,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `tipo_id`(`tipo_id`) USING BTREE,
  CONSTRAINT `insumo_ibfk_1` FOREIGN KEY (`tipo_id`) REFERENCES `tipo_insumo` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE = InnoDB AUTO_INCREMENT = 3 CHARACTER SET = utf8 COLLATE = utf8_spanish_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of insumo
-- ----------------------------
INSERT INTO `insumo` VALUES (1, '610998828', 'ALCOHOL editado', 2, 42, 321.00, 'Detalle del insumo ALCOHOL editado', '20221006095306AdminLTELogo.png', 1);
INSERT INTO `insumo` VALUES (2, '399055551', 'Nombre del insumo', 3, 33, 12.00, ' Detalle del insumo', '20221006095325insumo.jpg', 1);

-- ----------------------------
-- Table structure for marca_alimento
-- ----------------------------
DROP TABLE IF EXISTS `marca_alimento`;
CREATE TABLE `marca_alimento`  (
  `id` int NOT NULL AUTO_INCREMENT COMMENT 'Primary Key',
  `marca_alimento` varchar(255) CHARACTER SET utf8 COLLATE utf8_spanish_ci NULL DEFAULT NULL,
  `estado` int NULL DEFAULT 1,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 5 CHARACTER SET = utf8 COLLATE = utf8_spanish_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of marca_alimento
-- ----------------------------
INSERT INTO `marca_alimento` VALUES (1, 'CERDIL', 0);
INSERT INTO `marca_alimento` VALUES (2, 'cerdo editado', 1);
INSERT INTO `marca_alimento` VALUES (3, 'PORKI LO MEJOR', 1);
INSERT INTO `marca_alimento` VALUES (4, 'COENJO', 1);

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
) ENGINE = InnoDB AUTO_INCREMENT = 18 CHARACTER SET = utf8 COLLATE = utf8_spanish_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of movimientos
-- ----------------------------
INSERT INTO `movimientos` VALUES (15, 6, '2022-09-21', 'N°: 321 - Tipo: lote editado');
INSERT INTO `movimientos` VALUES (16, 6, '2022-09-21', 'N°: 123 - Tipo: lechones');
INSERT INTO `movimientos` VALUES (17, 6, '2022-09-23', 'N°: 321 - Tipo: lote editado');

-- ----------------------------
-- Table structure for peso_cerdo
-- ----------------------------
DROP TABLE IF EXISTS `peso_cerdo`;
CREATE TABLE `peso_cerdo`  (
  `peso_id` int NOT NULL AUTO_INCREMENT,
  `cerdo_id` int NULL DEFAULT NULL,
  `fecha` date NULL DEFAULT NULL,
  `metodo` char(50) CHARACTER SET utf8 COLLATE utf8_spanish_ci NULL DEFAULT NULL,
  `estado` char(50) CHARACTER SET utf8 COLLATE utf8_spanish_ci NULL DEFAULT NULL,
  `observacion` varchar(255) CHARACTER SET utf8 COLLATE utf8_spanish_ci NULL DEFAULT NULL,
  `peso_a` char(50) CHARACTER SET utf8 COLLATE utf8_spanish_ci NULL DEFAULT NULL,
  `peso_b` char(50) CHARACTER SET utf8 COLLATE utf8_spanish_ci NULL DEFAULT NULL,
  `p_t` char(50) CHARACTER SET utf8 COLLATE utf8_spanish_ci NULL DEFAULT NULL,
  `l_c` char(50) CHARACTER SET utf8 COLLATE utf8_spanish_ci NULL DEFAULT NULL,
  `p_v` char(40) CHARACTER SET utf8 COLLATE utf8_spanish_ci NULL DEFAULT NULL,
  `estado_` int NULL DEFAULT 1,
  PRIMARY KEY (`peso_id`) USING BTREE,
  INDEX `cerdo_id`(`cerdo_id`) USING BTREE,
  CONSTRAINT `peso_cerdo_ibfk_1` FOREIGN KEY (`cerdo_id`) REFERENCES `cerdo` (`id_cerdo`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE = InnoDB AUTO_INCREMENT = 7 CHARACTER SET = utf8 COLLATE = utf8_spanish_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of peso_cerdo
-- ----------------------------
INSERT INTO `peso_cerdo` VALUES (1, 2, '2022-09-29', 'vivo', 'd_flaco', 'llego tarde', '100', '', '12', '12', '0', 1);
INSERT INTO `peso_cerdo` VALUES (2, 2, '2022-09-29', 'exacto', 'd_flaco', 'Observación', '100', '110', '', '', '', 1);
INSERT INTO `peso_cerdo` VALUES (3, 2, '2022-09-29', 'exacto', 'gordo', 'ESTA GORO EL CERDO', '100', '150', '', '', '', 1);
INSERT INTO `peso_cerdo` VALUES (4, 1, '2022-09-29', 'vivo', 'd_gordo', 'ESTA MAS GORO', '123', '', '140', '120', '205', 1);
INSERT INTO `peso_cerdo` VALUES (5, 2, '2022-09-29', 'exacto', 'flaco', 'ESTA FLACO EL CERDO', '100', '110', '', '', '', 1);
INSERT INTO `peso_cerdo` VALUES (6, 2, '2022-09-29', 'exacto', 'd_flaco', 'NUEVA PESAAJE DEL CERO', '100', '110', '', '', '', 1);

-- ----------------------------
-- Table structure for proveedor
-- ----------------------------
DROP TABLE IF EXISTS `proveedor`;
CREATE TABLE `proveedor`  (
  `id` int NOT NULL AUTO_INCREMENT COMMENT 'Primary Key',
  `razon` varchar(255) CHARACTER SET utf8 COLLATE utf8_spanish_ci NULL DEFAULT NULL,
  `ruc` char(15) CHARACTER SET utf8 COLLATE utf8_spanish_ci NULL DEFAULT NULL,
  `telefono` char(15) CHARACTER SET utf8 COLLATE utf8_spanish_ci NULL DEFAULT NULL,
  `correo` varchar(150) CHARACTER SET utf8 COLLATE utf8_spanish_ci NULL DEFAULT NULL,
  `descripcion` text CHARACTER SET utf8 COLLATE utf8_spanish_ci NULL,
  `encargado` varchar(200) CHARACTER SET utf8 COLLATE utf8_spanish_ci NULL DEFAULT NULL,
  `telefono_en` char(15) CHARACTER SET utf8 COLLATE utf8_spanish_ci NULL DEFAULT NULL,
  `direccion` varchar(150) CHARACTER SET utf8 COLLATE utf8_spanish_ci NULL DEFAULT NULL,
  `estado` int NULL DEFAULT 1,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 2 CHARACTER SET = utf8 COLLATE = utf8_spanish_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of proveedor
-- ----------------------------
INSERT INTO `proveedor` VALUES (1, 'la granja de porki', '0940321854', '0987654321', 'elgamer@hotmail.com', ' LA MEJOR CALIDAD DE COMIDA Y DE CERDO', 'YO MISMO', '54321', 'milagro ', 1);

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
-- Table structure for tipo_alimentcion
-- ----------------------------
DROP TABLE IF EXISTS `tipo_alimentcion`;
CREATE TABLE `tipo_alimentcion`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `tipo` varchar(255) CHARACTER SET utf8 COLLATE utf8_spanish_ci NULL DEFAULT NULL,
  `estado` int NULL DEFAULT 1,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 3 CHARACTER SET = utf8 COLLATE = utf8_spanish_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of tipo_alimentcion
-- ----------------------------
INSERT INTO `tipo_alimentcion` VALUES (1, 'engorda editado', 1);
INSERT INTO `tipo_alimentcion` VALUES (2, 'crecimiento', 1);

-- ----------------------------
-- Table structure for tipo_alimento
-- ----------------------------
DROP TABLE IF EXISTS `tipo_alimento`;
CREATE TABLE `tipo_alimento`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `tipo_alimento` varchar(255) CHARACTER SET utf8 COLLATE utf8_spanish_ci NULL DEFAULT NULL,
  `estado` int NULL DEFAULT 1,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 5 CHARACTER SET = utf8 COLLATE = utf8_spanish_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of tipo_alimento
-- ----------------------------
INSERT INTO `tipo_alimento` VALUES (1, 'ENGORDA editado', 0);
INSERT INTO `tipo_alimento` VALUES (2, 'PAJA', 1);
INSERT INTO `tipo_alimento` VALUES (3, 'ARROZ', 1);
INSERT INTO `tipo_alimento` VALUES (4, 'balanceador', 1);

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
-- Table structure for tipo_insumo
-- ----------------------------
DROP TABLE IF EXISTS `tipo_insumo`;
CREATE TABLE `tipo_insumo`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `tipo` varchar(255) CHARACTER SET utf8 COLLATE utf8_spanish_ci NULL DEFAULT NULL,
  `estado` int NULL DEFAULT 1,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 4 CHARACTER SET = utf8 COLLATE = utf8_spanish_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of tipo_insumo
-- ----------------------------
INSERT INTO `tipo_insumo` VALUES (1, 'ALCOOHOL', 1);
INSERT INTO `tipo_insumo` VALUES (2, 'PAPEL', 1);
INSERT INTO `tipo_insumo` VALUES (3, 'NUEVO EDITADO', 1);

-- ----------------------------
-- Table structure for tipo_tratamiento
-- ----------------------------
DROP TABLE IF EXISTS `tipo_tratamiento`;
CREATE TABLE `tipo_tratamiento`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(255) CHARACTER SET utf8 COLLATE utf8_spanish_ci NULL DEFAULT NULL,
  `descripcion` text CHARACTER SET utf8 COLLATE utf8_spanish_ci NULL,
  `estado` int NULL DEFAULT 1,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_spanish_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of tipo_tratamiento
-- ----------------------------
INSERT INTO `tipo_tratamiento` VALUES (1, 'Tipo tratamiento', 'Descripción', 1);
INSERT INTO `tipo_tratamiento` VALUES (2, ' editado', ' Descripción editado', 1);

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
INSERT INTO `usuario` VALUES (1, 'PORKY', 'CERDO', 'admin', '123', 1, 'casa', '123', '20220924140704cerdito.png', 1);
INSERT INTO `usuario` VALUES (9, 'as', 'asa', 'asa', 'Jorge2´+', 1, 'asa', 'asas', '20220907195019avatar5.png', 1);
INSERT INTO `usuario` VALUES (10, 'aaaaaaaaaa', 'bbbbbbbb', 'ssssss', 'Jorgqwqw12´@', 2, 'ccccccccccc', '111111111', '20220907195131avatar3.png', 1);
INSERT INTO `usuario` VALUES (11, 'JORGE MOISES', 'RAMIREZ ZAVALA', 'Jorge', 'Jorge12q,.', 1, 'MILAGRO', '0987654321', '20220907195143avatar.png', 1);
INSERT INTO `usuario` VALUES (12, 'aaaaaaaaaaaa', 'ccccccccc', 'abc', 'AM112.,´q', 3, 'a121', '1212121', '20220907140512_IMG192202211510.png', 1);

-- ----------------------------
-- Table structure for veterinario
-- ----------------------------
DROP TABLE IF EXISTS `veterinario`;
CREATE TABLE `veterinario`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(255) CHARACTER SET utf8 COLLATE utf8_spanish_ci NULL DEFAULT NULL,
  `apellido` varchar(255) CHARACTER SET utf8 COLLATE utf8_spanish_ci NULL DEFAULT NULL,
  `documento` char(15) CHARACTER SET utf8 COLLATE utf8_spanish_ci NULL DEFAULT NULL,
  `telefono` char(15) CHARACTER SET utf8 COLLATE utf8_spanish_ci NULL DEFAULT NULL,
  `direccion` varchar(255) CHARACTER SET utf8 COLLATE utf8_spanish_ci NULL DEFAULT NULL,
  `sucursal` varchar(255) CHARACTER SET utf8 COLLATE utf8_spanish_ci NULL DEFAULT NULL,
  `estado` int NULL DEFAULT 1,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_spanish_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of veterinario
-- ----------------------------
INSERT INTO `veterinario` VALUES (1, 'Nombres', 'Apelllidos editado', '0940321855', '1234567890', 'Naranjito editado', 'SUPER CAT editado', 1);
INSERT INTO `veterinario` VALUES (2, 'BACILIO TONTO', 'AAAAAA BBBBBB', '0940321854', '0985906677', 'milagro', 'VANESUR', 1);

-- ----------------------------
-- Table structure for web
-- ----------------------------
DROP TABLE IF EXISTS `web`;
CREATE TABLE `web`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `foto1` varchar(255) CHARACTER SET utf8 COLLATE utf8_spanish_ci NULL DEFAULT NULL,
  `foto2` varchar(255) CHARACTER SET utf8 COLLATE utf8_spanish_ci NULL DEFAULT NULL,
  `foto3` varchar(255) CHARACTER SET utf8 COLLATE utf8_spanish_ci NULL DEFAULT NULL,
  `detalle1` varchar(255) CHARACTER SET utf8 COLLATE utf8_spanish_ci NULL DEFAULT NULL,
  `detalle2` varchar(255) CHARACTER SET utf8 COLLATE utf8_spanish_ci NULL DEFAULT NULL,
  `detalle3` varchar(255) CHARACTER SET utf8 COLLATE utf8_spanish_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 2 CHARACTER SET = utf8 COLLATE = utf8_spanish_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of web
-- ----------------------------
INSERT INTO `web` VALUES (1, '2022092618143620220924140704cerdito.png', '2022092613044120220907140512_IMG192202211510.png', '2022092613044920220907195019avatar5.png', 'Los mejores cerdos', 'la  mejor calidad de cerdo', 'los cerdos son cerdos');

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
