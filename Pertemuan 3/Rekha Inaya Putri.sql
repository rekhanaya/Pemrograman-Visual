-- Nama: Rekha Inaya Putri
-- Nim: 2022071044
-- Mata Kuliah: Basis Data
-- Database: `akademik`

-- Table structure for database `akademik`

CREATE TABLE `mahasiswa` (
  `Nim` varchar(9) NOT NULL,
  `Nama_Mhs` varchar(25) NOT NULL,
  `Tgl_Lahir` date NOT NULL,
  `Alamat` varchar(50) NOT NULL,
  `Jenis_Kelamin` enum('Laki-laki','Perempuan') NOT NULL,
  `hobi` varchar(100) DEFAULT NULL -- Kondisi setelah ditambahkan Alter Add tabel 
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Insert data 
--
INSERT INTO `mahasiswa` (`Nim`, `Nama_Mhs`, `Tgl_Lahir`, `Alamat`, `Jenis_Kelamin`) VALUES
('202207104', 'Rekha Inaya Putri', '0000-00-00', 'Kebayoran Lama', 'Perempuan');

--
-- Update data
--
UPDATE `mahasiswa` SET `Tgl_Lahir`='2004-05-07' WHERE 1

--
-- Delete data
--
DELETE FROM mahasiswa WHERE Nama_Mhs='Rita Zahara';

--
-- Alter Add data
--
ALTER TABLE mahasiswa ADD hobi VARCHAR(100);

--
-- Alter Change atau Ubah nama tabel pada data
--
ALTER TABLE mahasiswa CHANGE alamat alamat_mahasiswa VARCHAR(100);

--
-- Alter Rename atau Mengganti nama tabel pada data
--
RENAME TABLE mahasiswa TO mhs;

--
-- Drop database
--
DROP DATABASE mahasiswa;

--
-- Membuat index 
--
CREATE INDEX mhs ON mhs (Nama_Mhs);

--
-- Drop index 
--
DROP INDEX mhs ON mhs;

--
-- Show
--
SHOW CREATE DATABASE; --perintah ini tidak dapat dijalankan pada XAMPP atau PHP My Admin
SHOW TABLES;
SHOW CREATE TABLE perkuliahan;
SHOW CREATE TABLE; --perintah ini tidak dapat dijalankan pada XAMPP atau PHP My Admin
SHOW COLUMNS FROM dosen;

-- Table structure for database `seimbang`
-- ========================================================== PERINTAH SQL TIPE DDL ==========================================================
-- Membuat skema database baru
CREATE SCHEMA `seimbang_db` ;

-- Menghapus database yang ada
DROP DATABASE `seimbang_db`;

-- Membuat skema database baru (setelah menghapus yang lama)
CREATE SCHEMA `seimbang_db` ;

-- Menggunakan skema yang baru dibuat
USE seimbang_db;

-- Membuat tabel untuk menyimpan informasi pengguna
CREATE TABLE `seimbang_db`.`users` (
  `user_id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `username` VARCHAR(255) NOT NULL,
  `password` VARCHAR(255) NOT NULL,
  `email` VARCHAR(255) NOT NULL,
  `nama lengkap` VARCHAR(255) NOT NULL,
  `tgl_lahir` DATE NOT NULL,
  PRIMARY KEY (`user_id`),
  UNIQUE INDEX `username_UNIQUE` (`username` ASC) VISIBLE,
  UNIQUE INDEX `email_UNIQUE` (`email` ASC) VISIBLE
);

-- Membuat tabel untuk menyimpan konten cinta seperti artikel dan video
CREATE TABLE `seimbang_db`.`konten_love` (
  `konten_id` INT NOT NULL AUTO_INCREMENT,
  `user_id` INT UNSIGNED NOT NULL,
  `judul_konten` VARCHAR(255) NOT NULL,
  `link_konten` VARCHAR(255) NOT NULL,
  `konten_kategori` ENUM('makanan_sehat_keluarga', 'olahraga') NOT NULL,
  PRIMARY KEY (`konten_id`),
  FOREIGN KEY (`user_id`) REFERENCES `users` (`user_id`)
);

-- Membuat tabel untuk menyimpan jenis-jenis aktivitas yang tersedia
CREATE TABLE `seimbang_db`.`jenis_aktivitas` (
  `jenis_aktivitas_id` INT NOT NULL AUTO_INCREMENT,
  `nama_jenis_aktivitas` VARCHAR(255) NOT NULL,
  PRIMARY KEY (`jenis_aktivitas_id`),
  UNIQUE INDEX `nama_jenis_aktivitas_UNIQUE` (`nama_jenis_aktivitas` ASC) VISIBLE
);

-- Membuat tabel untuk menyimpan informasi aktivitas yang direncanakan
CREATE TABLE `seimbang_db`.`aktivitas` (
  `aktivitas_id` INT NOT NULL AUTO_INCREMENT,
  `user_id` INT UNSIGNED NOT NULL,
  `nama_aktivitas` VARCHAR(255) NOT NULL,
  `jam_mulai` TIME NOT NULL,
  `jam_akhir` TIME NOT NULL,
  `waktu_pengingat` TIME NULL,
  `jenis_aktivitas_id` INT NOT NULL,
  PRIMARY KEY (`aktivitas_id`),
  FOREIGN KEY (`user_id`) REFERENCES `users` (`user_id`),
  FOREIGN KEY (`jenis_aktivitas_id`) REFERENCES `jenis_aktivitas` (`jenis_aktivitas_id`)
);

-- Memberikan komentar pada tabel-tabel yang telah dibuat
ALTER TABLE users COMMENT = 'Tabel untuk menyimpan informasi pengguna';
ALTER TABLE konten_love COMMENT = 'Tabel untuk menyimpan konten cinta seperti artikel dan video';
ALTER TABLE jenis_aktivitas COMMENT = 'Tabel untuk menyimpan jenis-jenis aktivitas yang tersedia';
ALTER TABLE aktivitas COMMENT = 'Tabel untuk menyimpan informasi aktivitas yang direncanakan';

-- Mengganti nama tabel untuk membuat pengepala sementara baru agar lebih mudah mengganti nama tabel
RENAME TABLE users TO new_users;
RENAME TABLE konten_love TO new_konten_love;
RENAME TABLE jenis_aktivitas TO new_jenis_aktivitas;
RENAME TABLE aktivitas TO new_aktivitas;

-- Mengganti nama tabel sementara kembali ke nama aslinya
RENAME TABLE new_users TO users;
RENAME TABLE new_konten_love TO konten_love;
RENAME TABLE new_jenis_aktivitas TO jenis_aktivitas;
RENAME TABLE new_aktivitas TO aktivitas;
-- ========================================================== PERINTAH SQL TIPE DML ==========================================================

-- Menyisipkan data pengguna
INSERT INTO `seimbang_db`.`users` (`username`, `password`, `email`, `nama lengkap`, `tgl_lahir`) 
VALUES 
('john_doe', 'password123', 'john@example.com', 'John Doe', '1990-01-01'),
('jane_smith', 'abc123', 'jane@example.com', 'Jane Smith', '1995-05-15'),
('michael_johnson', 'pass456', 'michael@example.com', 'Michael Johnson', '1988-09-20');

-- Menyisipkan data konten cinta
INSERT INTO `seimbang_db`.`konten_love` (`user_id`, `judul_konten`, `link_konten`, `konten_kategori`) 
VALUES 
(1, 'Resep Salad Sehat', 'https://resepsaladsehat.com', 'makanan_sehat_keluarga'),
(2, 'Tips Berolahraga di Rumah', 'https://tipsberolahragadiRumah.com', 'olahraga'),
(3, 'Manfaat Tidur yang Cukup', 'https://manfaattidur.com', 'olahraga');

-- Menyisipkan jenis-jenis aktivitas
INSERT INTO `seimbang_db`.`jenis_aktivitas` (`nama_jenis_aktivitas`) 
VALUES 
('family time'),
('me time'),
('cook'),
('work');

-- Menyisipkan data aktivitas yang direncanakan dengan waktu pengingat otomatis 5 menit sebelum jam mulai
INSERT INTO `seimbang_db`.`aktivitas` (`user_id`, `nama_aktivitas`, `jam_mulai`, `jam_akhir`, `waktu_pengingat`, `jenis_aktivitas_id`) 
VALUES 
(1, 'Berjalan pagi', '07:00:00', '08:00:00', '06:55:00', 1),
(2, 'Yoga sore', '17:00:00', '18:00:00', '16:55:00', 2),
(3, 'Membuat masakan baru', '12:00:00', '13:00:00', '11:55:00', 3);

-- Update nama pengguna (username) pengguna dengan ID tertentu
UPDATE `seimbang_db`.`users`
SET `username` = 'new_username'
WHERE `user_id` = 1;

-- Update email pengguna dengan nama pengguna tertentu
UPDATE `seimbang_db`.`users`
SET `email` = 'new_email@example.com'
WHERE `username` = 'john_doe';

-- Update judul konten cinta untuk konten dengan ID tertentu
UPDATE `seimbang_db`.`konten_love`
SET `judul_konten` = 'New Title'
WHERE `konten_id` = 1;

-- Update jenis aktivitas dengan ID tertentu
UPDATE `seimbang_db`.`jenis_aktivitas`
SET `nama_jenis_aktivitas` = 'New Activity'
WHERE `jenis_aktivitas_id` = 1;

-- Update nama aktivitas untuk aktivitas dengan ID tertentu
UPDATE `seimbang_db`.`aktivitas`
SET `nama_aktivitas` = 'New Activity Name'
WHERE `aktivitas_id` = 1;

-- Menghapus konten cinta dengan ID tertentu
DELETE FROM `seimbang_db`.`konten_love`
WHERE `konten_id` = 1;
ROLLBACK;

-- Menghapus aktivitas dengan ID tertentu
DELETE FROM `seimbang_db`.`aktivitas`
WHERE `aktivitas_id` = 1;
ROLLBACK;

-- Menghapus semua konten cinta
DELETE FROM `seimbang_db`.`konten_love`;
ROLLBACK;

-- Menghapus semua aktivitas
DELETE FROM `seimbang_db`.`aktivitas`;
ROLLBACK;

-- Mengunci tabel-tabel untuk operasi tulis
LOCK TABLES 
    `seimbang_db`.`users` WRITE,
    `seimbang_db`.`konten_love` WRITE,
    `seimbang_db`.`jenis_aktivitas` WRITE,
    `seimbang_db`.`aktivitas` WRITE;

-- Penguncian dilakukan untuk menghindari akses bersamaan ke tabel selama operasi yang memengaruhi integritas data sedang berlangsung.

-- Melakukan operasi INSERT, jika ada duplikasi pada kunci utama, maka lakukan UPDATE
INSERT INTO `seimbang_db`.`users` (`user_id`, `username`, `password`, `email`, `nama lengkap`, `tgl_lahir`)
VALUES 
    (1, 'john_doe', 'password123', 'john@example.com', 'John Doe', '1990-01-01'),
    (2, 'jane_smith', 'abc123', 'jane@example.com', 'Jane Smith', '1995-05-15'),
    (3, 'michael_johnson', 'pass456', 'michael@example.com', 'Michael Johnson', '1988-09-20')
ON DUPLICATE KEY UPDATE
    `username` = VALUES(`username`),
    `password` = VALUES(`password`),
    `email` = VALUES(`email`),
    `nama lengkap` = VALUES(`nama lengkap`),
    `tgl_lahir` = VALUES(`tgl_lahir`);

-- Penguncian dilakukan untuk menghindari akses bersamaan ke tabel selama operasi yang memengaruhi integritas data sedang berlangsung.

-- Pastikan untuk melepaskan kunci setelah selesai operasi.
UNLOCK TABLES;
-- ========================================================== PERINTAH SQL TIPE DQL ==========================================================
-- Menampilkan semua data dari tabel `users`
SELECT * FROM `seimbang_db`.`users`;

-- Menampilkan data pengguna berdasarkan nama pengguna tertentu
SELECT * FROM `seimbang_db`.`users` WHERE `username` = 'nama_pengguna';

-- Menampilkan data pengguna berdasarkan alamat email tertentu
SELECT * FROM `seimbang_db`.`users` WHERE `email` = 'email@contoh.com';

-- Menampilkan konten cinta berdasarkan kategori tertentu
SELECT * FROM `seimbang_db`.`konten_love` WHERE `konten_kategori` = 'makanan_sehat_keluarga';

-- Menampilkan semua jenis aktivitas yang tersedia
SELECT * FROM `seimbang_db`.`jenis_aktivitas`;

-- Menampilkan aktivitas berdasarkan jenis aktivitas tertentu
SELECT * FROM `seimbang_db`.`aktivitas` 
JOIN `seimbang_db`.`jenis_aktivitas` 
ON `aktivitas`.`jenis_aktivitas_id` = `jenis_aktivitas`.`jenis_aktivitas_id` 
WHERE `nama_jenis_aktivitas` = 'nama_jenis_aktivitas';

-- Menampilkan aktivitas yang dimulai pada atau setelah waktu tertentu
SELECT * FROM `seimbang_db`.`aktivitas` WHERE `jam_mulai` >= 'waktu_tertentu';

-- Menampilkan aktivitas yang memiliki waktu pengingat ditetapkan
SELECT * FROM `seimbang_db`.`aktivitas` WHERE `waktu_pengingat` IS NOT NULL;

-- Menampilkan aktivitas berdasarkan rentang waktu tertentu
SELECT * FROM `seimbang_db`.`aktivitas` WHERE `jam_mulai` BETWEEN 'waktu_awal' AND 'waktu_akhir';

-- Menampilkan semua data pengguna bersama dengan aktivitas yang terkait
SELECT * FROM `seimbang_db`.`users` 
LEFT JOIN `seimbang_db`.`aktivitas` 
ON `users`.`user_id` = `aktivitas`.`user_id`;