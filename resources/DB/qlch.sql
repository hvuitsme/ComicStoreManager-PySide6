-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Máy chủ: 127.0.0.1
-- Thời gian đã tạo: Th6 28, 2024 lúc 11:35 AM
-- Phiên bản máy phục vụ: 10.4.32-MariaDB
-- Phiên bản PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Cơ sở dữ liệu: `qlch`
--

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `chitiethoadon`
--

CREATE TABLE `chitiethoadon` (
  `detail_id` int(11) NOT NULL,
  `invoice_id` int(11) NOT NULL,
  `product_id` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `pd_name` varchar(255) NOT NULL,
  `quantity` int(11) NOT NULL,
  `price` int(11) NOT NULL,
  `transaction_type` enum('Mua','Thuê') NOT NULL,
  `status_sp` enum('Đã trả','Đang mượn','Quá hạn') DEFAULT NULL,
  `borrow_date` date DEFAULT NULL,
  `return_date` date DEFAULT NULL
) ;

--
-- Bẫy `chitiethoadon`
--
DELIMITER $$
CREATE TRIGGER `update_status_sp` BEFORE INSERT ON `chitiethoadon` FOR EACH ROW BEGIN
  IF NEW.status_sp != 'Đã trả' THEN
    IF NEW.return_date < CURDATE() THEN
      SET NEW.status_sp = 'Quá hạn';
    ELSE
      SET NEW.status_sp = 'Đang mượn';
    END IF;
  END IF;
END
$$
DELIMITER ;
DELIMITER $$
CREATE TRIGGER `update_status_sp_on_update` BEFORE UPDATE ON `chitiethoadon` FOR EACH ROW BEGIN
  IF NEW.status_sp != 'Đã trả' THEN
    IF NEW.return_date < CURDATE() THEN
      SET NEW.status_sp = 'Quá hạn';
    ELSE
      SET NEW.status_sp = 'Đang mượn';
    END IF;
  END IF;
END
$$
DELIMITER ;

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `hoadon`
--

CREATE TABLE `hoadon` (
  `invoice_id` int(11) NOT NULL,
  `cus_name` varchar(255) NOT NULL,
  `phone_num` varchar(20) NOT NULL,
  `addr` varchar(255) NOT NULL,
  `invoice_date` datetime NOT NULL,
  `total_amount` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `lshd`
--

CREATE TABLE `lshd` (
  `hst_id` int(11) NOT NULL,
  `username` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `name` varchar(255) NOT NULL,
  `action` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `nhaphathanh`
--

CREATE TABLE `nhaphathanh` (
  `pub_id` varchar(11) NOT NULL,
  `ten_nhaph` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Đang đổ dữ liệu cho bảng `nhaphathanh`
--

INSERT INTO `nhaphathanh` (`pub_id`, `ten_nhaph`) VALUES
('NPH001', 'NXB Kim Đồng'),
('NPH002', 'NXB Trẻ'),
('NPH003', 'NXB Văn Học'),
('NPH004', 'Shinchosha'),
('NPH005', 'Kodansha'),
('NPH006', 'Shogakukan');

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `sanpham`
--

CREATE TABLE `sanpham` (
  `product_id` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `tensanpham` varchar(255) NOT NULL,
  `hinhanh` text NOT NULL,
  `price` int(11) NOT NULL,
  `genre_id` varchar(11) NOT NULL,
  `pub_id` varchar(11) NOT NULL,
  `auth_id` varchar(11) NOT NULL,
  `status` enum('Còn hàng','Hết hàng') NOT NULL DEFAULT 'Còn hàng'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Đang đổ dữ liệu cho bảng `sanpham`
--

INSERT INTO `sanpham` (`product_id`, `tensanpham`, `hinhanh`, `price`, `genre_id`, `pub_id`, `auth_id`, `status`) VALUES
('SB20', 'Câu truyện thần thoại Hy Lạp', 'E:\\hoc\\python\\baitaplon\\resources\\pic\\product_image\\sp5.jpg', 80000, 'TL004', 'NPH005', 'TG005', 'Còn hàng'),
('SP32', 'Ngủ những giấc mơ trưa', 'E:\\hoc\\python\\baitaplon\\resources\\pic\\product_image\\sp1.jpg', 40000, 'TL005', 'NPH005', 'TG004', 'Còn hàng'),
('SS22', 'Tình yêu tuổi học trò', 'E:\\hoc\\python\\baitaplon\\resources\\pic\\product_image\\sp8.jpg', 40000, 'TL005', 'NPH001', 'TG002', 'Còn hàng');

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `tacgia`
--

CREATE TABLE `tacgia` (
  `auth_id` varchar(11) NOT NULL,
  `ten_tacgia` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Đang đổ dữ liệu cho bảng `tacgia`
--

INSERT INTO `tacgia` (`auth_id`, `ten_tacgia`) VALUES
('TG001', 'Nguyễn Nhật Ánh'),
('TG002', 'Trần Nhật Ánh'),
('TG003', 'Lê Thị Ánh'),
('TG004', 'Haruki Murakami'),
('TG005', 'Yukio Mishima'),
('TG006', 'Yoshimoto Banana');

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `theloai`
--

CREATE TABLE `theloai` (
  `genre_id` varchar(11) NOT NULL,
  `ten_theloai` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Đang đổ dữ liệu cho bảng `theloai`
--

INSERT INTO `theloai` (`genre_id`, `ten_theloai`) VALUES
('TL001', 'Tiểu thuyết'),
('TL002', 'Truyện tranh'),
('TL003', 'Kinh tế'),
('TL004', 'Khoa học'),
('TL005', 'Light Novel');

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `tonkho`
--

CREATE TABLE `tonkho` (
  `product_id` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `quantity` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Đang đổ dữ liệu cho bảng `tonkho`
--

INSERT INTO `tonkho` (`product_id`, `quantity`) VALUES
('SB20', 3),
('SP32', 4),
('SS22', 4);

--
-- Bẫy `tonkho`
--
DELIMITER $$
CREATE TRIGGER `update_product_status` AFTER UPDATE ON `tonkho` FOR EACH ROW BEGIN
    DECLARE product_count INT;
    SET product_count = (SELECT `quantity` FROM `tonkho` WHERE `product_id` = NEW.`product_id`);
    
    IF product_count <= 0 THEN
        UPDATE `sanpham`
        SET `status` = 'Hết hàng'
        WHERE `product_id` = NEW.`product_id`;
    ELSE
        UPDATE `sanpham`
        SET `status` = 'Còn hàng'
        WHERE `product_id` = NEW.`product_id`;
    END IF;
END
$$
DELIMITER ;

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `users`
--

CREATE TABLE `users` (
  `user_id` int(11) NOT NULL,
  `username` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `email` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `name` varchar(255) NOT NULL,
  `password` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `profile_image` text DEFAULT NULL,
  `role` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Đang đổ dữ liệu cho bảng `users`
--

INSERT INTO `users` (`user_id`, `username`, `email`, `name`, `password`, `profile_image`, `role`) VALUES
(7, 'admin', 'admin@example.com', 'Admin', '123', 'E:\\hoc\\python\\baitaplon\\resources\\pic\\profile_image\\pf3.jpg', 'Admin'),
(11, 'nhanvien1', 'nhanvien1@example.com', 'Trần Quỳnh Như', '123', 'E:\\hoc\\python\\baitaplon\\resources\\pic\\profile_image\\pf2.jpg', 'Nhân viên'),
(32, 'nhanvien2', 'nhanvien2@example.com', 'Trần Ngọc Tài', '123', 'E:\\hoc\\python\\baitaplon\\resources\\pic\\profile_image\\pf6.jpg', 'Nhân viên'),
(33, 'nhanvien3', 'nhanvien3@example.com', 'Thắng đần', '123', 'E:\\hoc\\python\\baitaplon\\resources\\pic\\profile_image\\pf8.jpg', 'Nhân viên');

--
-- Chỉ mục cho các bảng đã đổ
--

--
-- Chỉ mục cho bảng `chitiethoadon`
--
ALTER TABLE `chitiethoadon`
  ADD PRIMARY KEY (`detail_id`),
  ADD KEY `fk_chitiethoadon_invoice` (`invoice_id`),
  ADD KEY `fk_chitiethoadon_product` (`product_id`);

--
-- Chỉ mục cho bảng `hoadon`
--
ALTER TABLE `hoadon`
  ADD PRIMARY KEY (`invoice_id`);

--
-- Chỉ mục cho bảng `lshd`
--
ALTER TABLE `lshd`
  ADD PRIMARY KEY (`hst_id`);

--
-- Chỉ mục cho bảng `nhaphathanh`
--
ALTER TABLE `nhaphathanh`
  ADD PRIMARY KEY (`pub_id`);

--
-- Chỉ mục cho bảng `sanpham`
--
ALTER TABLE `sanpham`
  ADD PRIMARY KEY (`product_id`),
  ADD KEY `fk_sanpham_theloai` (`genre_id`),
  ADD KEY `fk_sanpham_tacgia` (`auth_id`),
  ADD KEY `fk_sanpham_nhaphathanh` (`pub_id`);

--
-- Chỉ mục cho bảng `tacgia`
--
ALTER TABLE `tacgia`
  ADD PRIMARY KEY (`auth_id`);

--
-- Chỉ mục cho bảng `theloai`
--
ALTER TABLE `theloai`
  ADD PRIMARY KEY (`genre_id`);

--
-- Chỉ mục cho bảng `tonkho`
--
ALTER TABLE `tonkho`
  ADD PRIMARY KEY (`product_id`);

--
-- Chỉ mục cho bảng `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`user_id`);

--
-- AUTO_INCREMENT cho các bảng đã đổ
--

--
-- AUTO_INCREMENT cho bảng `chitiethoadon`
--
ALTER TABLE `chitiethoadon`
  MODIFY `detail_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT cho bảng `hoadon`
--
ALTER TABLE `hoadon`
  MODIFY `invoice_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=123;

--
-- AUTO_INCREMENT cho bảng `lshd`
--
ALTER TABLE `lshd`
  MODIFY `hst_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=31;

--
-- AUTO_INCREMENT cho bảng `users`
--
ALTER TABLE `users`
  MODIFY `user_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=42;

--
-- Các ràng buộc cho các bảng đã đổ
--

--
-- Các ràng buộc cho bảng `chitiethoadon`
--
ALTER TABLE `chitiethoadon`
  ADD CONSTRAINT `fk_chitiethoadon_invoice` FOREIGN KEY (`invoice_id`) REFERENCES `hoadon` (`invoice_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `fk_chitiethoadon_product` FOREIGN KEY (`product_id`) REFERENCES `sanpham` (`product_id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Các ràng buộc cho bảng `sanpham`
--
ALTER TABLE `sanpham`
  ADD CONSTRAINT `fk_sanpham_nhaphathanh` FOREIGN KEY (`pub_id`) REFERENCES `nhaphathanh` (`pub_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `fk_sanpham_tacgia` FOREIGN KEY (`auth_id`) REFERENCES `tacgia` (`auth_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `fk_sanpham_theloai` FOREIGN KEY (`genre_id`) REFERENCES `theloai` (`genre_id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Các ràng buộc cho bảng `tonkho`
--
ALTER TABLE `tonkho`
  ADD CONSTRAINT `fk_tonkho_sanpham` FOREIGN KEY (`product_id`) REFERENCES `sanpham` (`product_id`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
