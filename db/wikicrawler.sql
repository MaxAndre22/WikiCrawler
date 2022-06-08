-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Server version:               10.6.8-MariaDB - mariadb.org binary distribution
-- Server OS:                    Win64
-- HeidiSQL Version:             11.3.0.6295
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- Dumping database structure for wikicrawler
CREATE DATABASE IF NOT EXISTS `wikicrawler` /*!40100 DEFAULT CHARACTER SET utf8mb3 */;
USE `wikicrawler`;

-- Dumping structure for table wikicrawler.article
CREATE TABLE IF NOT EXISTS `article` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(100) NOT NULL,
  `text` longtext NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb3;

-- Data exporting was unselected.

-- Dumping structure for table wikicrawler.article_stats
CREATE TABLE IF NOT EXISTS `article_stats` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `titles` int(11) NOT NULL,
  `words_body` int(11) NOT NULL,
  `words_titles` int(11) NOT NULL,
  `words_subtitles` int(11) NOT NULL,
  `images_w_alt` int(11) NOT NULL,
  `images_dw_alt` int(11) NOT NULL,
  `article_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_article_stats_article` (`article_id`),
  CONSTRAINT `fk_article_stats_article` FOREIGN KEY (`article_id`) REFERENCES `article` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb3;

-- Data exporting was unselected.

-- Dumping structure for table wikicrawler.common_word
CREATE TABLE IF NOT EXISTS `common_word` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `is_title` bit(1) NOT NULL,
  `word_id` int(11) NOT NULL,
  `article_stat_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_common_word_word` (`word_id`),
  KEY `fk_common_word_article_stat` (`article_stat_id`) USING BTREE,
  CONSTRAINT `fk_common_word_article_stat` FOREIGN KEY (`article_stat_id`) REFERENCES `article_stats` (`id`),
  CONSTRAINT `fk_common_word_word` FOREIGN KEY (`word_id`) REFERENCES `word` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb3;

-- Data exporting was unselected.

-- Dumping structure for table wikicrawler.reference
CREATE TABLE IF NOT EXISTS `reference` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `reference` text NOT NULL,
  `has_link` bit(1) NOT NULL,
  `active` bit(1) NOT NULL,
  `count` int(11) NOT NULL,
  `article_stat_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_reference_article_stats` (`article_stat_id`) USING BTREE,
  CONSTRAINT `fk_reference_article_stats` FOREIGN KEY (`article_stat_id`) REFERENCES `article_stats` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb3;

-- Data exporting was unselected.

-- Dumping structure for table wikicrawler.tag
CREATE TABLE IF NOT EXISTS `tag` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `tag` varchar(5) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb3;

-- Data exporting was unselected.

-- Dumping structure for table wikicrawler.tag_x_word_x_article
CREATE TABLE IF NOT EXISTS `tag_x_word_x_article` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `count` int(11) NOT NULL,
  `percent` int(11) NOT NULL,
  `tag_id` int(11) NOT NULL,
  `word_x_article_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_tag_x_word_x_article_tag` (`tag_id`),
  KEY `fk_tag_x_word_x_article_word_x_article` (`word_x_article_id`),
  CONSTRAINT `fk_tag_x_word_x_article_tag` FOREIGN KEY (`tag_id`) REFERENCES `tag` (`id`),
  CONSTRAINT `fk_tag_x_word_x_article_word_x_article` FOREIGN KEY (`word_x_article_id`) REFERENCES `word_x_article` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb3;

-- Data exporting was unselected.

-- Dumping structure for table wikicrawler.word
CREATE TABLE IF NOT EXISTS `word` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `word` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb3;

-- Data exporting was unselected.

-- Dumping structure for table wikicrawler.word_x_article
CREATE TABLE IF NOT EXISTS `word_x_article` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `count` int(11) NOT NULL,
  `percentage` int(11) NOT NULL,
  `article_id` int(11) NOT NULL,
  `word_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_word_x_article_article` (`article_id`),
  KEY `fk_word_x_article_word` (`word_id`),
  CONSTRAINT `fk_word_x_article_article` FOREIGN KEY (`article_id`) REFERENCES `article` (`id`),
  CONSTRAINT `fk_word_x_article_word` FOREIGN KEY (`word_id`) REFERENCES `word` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb3;

-- Data exporting was unselected.

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
