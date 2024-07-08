import os
import shutil
import sys
from datetime import datetime

from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

import mysql.connector
# pyside6-rcc image.qrc -o image_rc.py
import image_rc

# ==> MAIN ADMIN WINDOW
from gui.ui_main_admin import Ui_Main_Admin
# ==> MAIN ADMIN WINDOW
from gui.ui_main_employee import Ui_Main_Employee
# ==> MAIN ADMIN WINDOW
from gui.ui_choose_sp import Ui_Choose_sp
# ==> CHANGE PASSWORD WINDOW
from gui.ui_change_pass import Ui_ChangePass
# ==> FORGOTPW WINDOW
# from gui.ui_forgotpw import Ui_ForgotPw
# ==> REPLACEPW WINDOW
# from gui.ui_replacepw import Ui_ReplacePw
# ==> SIGNIN WINDOW
from gui.ui_signin import Ui_Signin
# ==> LOGIN WINDOW
from gui.ui_login import Ui_Login
# ==> SPLASH WINDOW
from gui.ui_splash import Ui_Splash

# ==> GLOBALS
counter = 0

# MAINADMIN
class MainAdmin(QMainWindow):
    def __init__(self, username, email, profile_image, name):
        super().__init__()
        self.ui = Ui_Main_Admin()
        self.ui.setupUi(self)
        
        self.set_avatar(profile_image)
        self.ui.label_Username.setText(username)
        self.ui.label_Email.setText(email)
        self.name = name
        
        # Đưa window về trung tâm màn hình
        qr = self.frameGeometry()
        cp = self.screen().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
        
        ## XOÁ TITLEBAR
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        
        self.ui.label_Exit.mousePressEvent = self.close_window
        self.ui.label_Minimize.mousePressEvent = self.minimize_window
        self.ui.label_CPass.mousePressEvent = self.change_pw
        self.ui.label_Logout.mousePressEvent = self.logout
        
        self.ui.Btn_Pd.clicked.connect(lambda: self.change_page(0))
        self.ui.Btn_Nv.clicked.connect(lambda: self.change_page(1))
        self.ui.Btn_Inventory.clicked.connect(lambda: self.change_page(2))
        self.ui.Btn_Revenue.clicked.connect(lambda: self.change_page(3))
        self.ui.Btn_Pub.clicked.connect(lambda: self.change_page(4))
        self.ui.Btn_Auth.clicked.connect(lambda: self.change_page(5))
        self.ui.Btn_Genre.clicked.connect(lambda: self.change_page(6))
        
        
        self.change_page(0)

        # page 1 -----------------------------------------------------------------------------------
        self.ui.Btn_Add_Pd.clicked.connect(self.check_adding)
        self.ui.Btn_Del_Pd.clicked.connect(self.check_delete)
        self.ui.Btn_Update.clicked.connect(self.check_update)
        self.ui.Btn_SelectImage.clicked.connect(self.select_image)
        
        self.ui.Table_sanpham.setColumnCount(8)
        self.ui.Table_sanpham.setHorizontalHeaderLabels(["ID sản phẩm", "Thể Loại", "Nhà phát hành", "Tác giả", "Hình ảnh","Tên sản phẩm","Giá tiền","Trạng thái"])
        self.ui.Table_sanpham.verticalHeader().setVisible(False)  # Tắt số thứ tự đầu bảng
        # Thiết lập kích thước cột tự động theo tỉ lệ
        # self.ui.Table_sanpham.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.Table_sanpham.setSelectionBehavior(QAbstractItemView.SelectRows)  # type: ignore # Chọn cả dòng
        self.ui.Table_sanpham.verticalHeader().setDefaultSectionSize(100)  # Tăng chiều cao của dòng
        
        # Thiết lập kích thước cột cố định cho từng cột
        self.ui.Table_sanpham.setColumnWidth(0, 76)  # ID sản phẩm
        self.ui.Table_sanpham.setColumnWidth(1, 115)  # Thể Loại
        self.ui.Table_sanpham.setColumnWidth(2, 120)  # Nhà phát hành
        self.ui.Table_sanpham.setColumnWidth(3, 120)  # Tác giả
        self.ui.Table_sanpham.setColumnWidth(4, 120)  # Hình ảnh
        self.ui.Table_sanpham.setColumnWidth(5, 200)  # Tên sản phẩm
        self.ui.Table_sanpham.setColumnWidth(6, 110)  # Giá tiền
        self.ui.Table_sanpham.setColumnWidth(7, 110)  # Trạng thái
        
        self.load_data()
        self.ui.Table_sanpham.cellClicked.connect(self.select_product)
        
        self.load_genre()
        self.load_pub()
        self.load_auth()
        
        # page 2 -----------------------------------------------------------------------------------
        self.ui.Btn_Add_Nv.clicked.connect(self.check_adding_nv)
        self.ui.Btn_Del_Nv.clicked.connect(self.check_delete_nv)
        self.ui.Btn_Update_Nv.clicked.connect(self.check_update_nv)
        self.ui.Btn_SelectImage_Nv.clicked.connect(self.select_image_nv)
        
        self.ui.Table_nv.setColumnCount(6)
        self.ui.Table_nv.setHorizontalHeaderLabels(["Username","Password","Email","Tên","Avatar","Chức vụ"])
        self.ui.Table_nv.verticalHeader().setVisible(False)  # Tắt số thứ tự đầu bảng
        # Thiết lập kích thước cột tự động theo tỉ lệ
        self.ui.Table_nv.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.Table_nv.setSelectionBehavior(QAbstractItemView.SelectRows)  # Chọn cả dòng
        self.ui.Table_nv.verticalHeader().setDefaultSectionSize(100)  # Tăng chiều cao của dòng
        
        self.load_data_nv()
        self.ui.Table_nv.cellClicked.connect(self.select_nv)
        
        # page 3 -----------------------------------------------------------------------------------
        self.ui.Btn_Update_Inv.clicked.connect(self.check_update_inv)
        
        self.ui.Table_tonkho.setColumnCount(2)
        self.ui.Table_tonkho.setHorizontalHeaderLabels(["ID sản phẩm","Số lượng"])
        self.ui.Table_tonkho.verticalHeader().setVisible(False)  # Tắt số thứ tự đầu bảng
        # Thiết lập kích thước cột tự động theo tỉ lệ
        # self.ui.Table_tonkho.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.Table_tonkho.setSelectionBehavior(QAbstractItemView.SelectRows)  # Chọn cả dòng
        self.ui.Table_tonkho.verticalHeader().setDefaultSectionSize(100)  # Tăng chiều cao của dòng
        
        # Thiết lập kích thước cột cố định cho từng cột
        self.ui.Table_tonkho.setColumnWidth(0, 200)  # ID sản phẩm
        self.ui.Table_tonkho.setColumnWidth(1, 200)  # Số lượng
        
        self.load_data_inv()
        # self.ui.Table_tonkho.cellClicked.connect(self.select_inv)
        
        # page 4 -----------------------------------------------------------------------------------
        self.ui.Table_lshd.setColumnCount(3)
        self.ui.Table_lshd.setHorizontalHeaderLabels(["Tên","Username","Action"])
        self.ui.Table_lshd.verticalHeader().setVisible(False)  # Tắt số thứ tự đầu bảng
        # Thiết lập kích thước cột tự động theo tỉ lệ
        # self.ui.Table_lshd.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.Table_lshd.setSelectionBehavior(QAbstractItemView.SelectRows)  # Chọn cả dòng
        self.ui.Table_lshd.verticalHeader().setDefaultSectionSize(50)  # Tăng chiều cao của dòng
        
        # Thiết lập kích thước cột cố định cho từng cột
        self.ui.Table_lshd.setColumnWidth(0, 200)
        self.ui.Table_lshd.setColumnWidth(1, 200)
        self.ui.Table_lshd.setColumnWidth(2, 571)  
        
        self.load_rev()
        self.load_histories()
        
        # page 5 -----------------------------------------------------------------------------------
        self.ui.Btn_Add_Pub.clicked.connect(self.check_adding_nph)
        self.ui.Btn_Del_Pub.clicked.connect(self.check_delete_nph)
        self.ui.Btn_Update_Pub.clicked.connect(self.check_update_nph)
        
        self.ui.Table_NhaPh.setColumnCount(2)
        self.ui.Table_NhaPh.setHorizontalHeaderLabels(["ID","Nhà phát hành"])
        self.ui.Table_NhaPh.verticalHeader().setVisible(False)  # Tắt số thứ tự đầu bảng
        # Thiết lập kích thước cột tự động theo tỉ lệ
        self.ui.Table_NhaPh.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.Table_NhaPh.setSelectionBehavior(QAbstractItemView.SelectRows)  # Chọn cả dòng
        self.ui.Table_NhaPh.verticalHeader().setDefaultSectionSize(100)  # Tăng chiều cao của dòng
        
        self.load_data_nph()
        self.ui.Table_NhaPh.cellClicked.connect(self.select_nph)
        
        # page 6 -----------------------------------------------------------------------------------
        self.ui.Btn_Add_Auth.clicked.connect(self.check_adding_tg)
        self.ui.Btn_Del_Auth.clicked.connect(self.check_delete_tg)
        self.ui.Btn_Update_Auth.clicked.connect(self.check_update_tg)
        
        self.ui.Table_tacgia.setColumnCount(2)
        self.ui.Table_tacgia.setHorizontalHeaderLabels(["ID","Tên tác giả"])
        self.ui.Table_tacgia.verticalHeader().setVisible(False)  # Tắt số thứ tự đầu bảng
        # Thiết lập kích thước cột tự động theo tỉ lệ
        self.ui.Table_tacgia.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.Table_tacgia.setSelectionBehavior(QAbstractItemView.SelectRows)  # Chọn cả dòng
        self.ui.Table_tacgia.verticalHeader().setDefaultSectionSize(100)  # Tăng chiều cao của dòng
        
        self.load_data_tg()
        self.ui.Table_tacgia.cellClicked.connect(self.select_tg)
        
        # page 7 -----------------------------------------------------------------------------------
        self.ui.Btn_Add_Genre.clicked.connect(self.check_adding_tl)
        self.ui.Btn_Del_Genre.clicked.connect(self.check_delete_tl)
        self.ui.Btn_Update_Genre.clicked.connect(self.check_update_tl)
        
        self.ui.Table_theloai.setColumnCount(2)
        self.ui.Table_theloai.setHorizontalHeaderLabels(["ID","Thể loại"])
        self.ui.Table_theloai.verticalHeader().setVisible(False)  # Tắt số thứ tự đầu bảng
        # Thiết lập kích thước cột tự động theo tỉ lệ
        self.ui.Table_theloai.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.Table_theloai.setSelectionBehavior(QAbstractItemView.SelectRows)  # Chọn cả dòng
        self.ui.Table_theloai.verticalHeader().setDefaultSectionSize(100)  # Tăng chiều cao của dòng
        
        self.load_data_tl()
        self.ui.Table_theloai.cellClicked.connect(self.select_tl)

    def record_act_epl(self, username, name, action):
        try:
            connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="qlch"
            )
            cursor = connection.cursor()

            query = "INSERT INTO lshd (username, name, action) VALUES (%s, %s, %s)"
            cursor.execute(query, (username, name, action))

            connection.commit()
            cursor.close()
            connection.close()

        except mysql.connector.Error as err:
            print(f"Error: {err}")
        
    def close_window(self, event):
        self.close()
        
    def minimize_window(self, event):
        self.showMinimized()
        
    def set_avatar(self, image_path):
        if image_path is None:
            image_path = ":/image/resources/pic/icon.jpg"  # Đặt đường dẫn hình ảnh mặc định
        pixmap = QPixmap(image_path)
        rounded_pixmap = QPixmap(pixmap.size())
        rounded_pixmap.fill(Qt.transparent)
        mask_brush = QBrush(QColor(Qt.black))
        mask_brush.setStyle(Qt.SolidPattern)
        painter = QPainter(rounded_pixmap)
        painter.setBrush(mask_brush)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setPen(Qt.NoPen)
        painter.drawRoundedRect(0, 0, pixmap.width(), pixmap.height(), 50, 50)
        painter.end()
        pixmap.setMask(rounded_pixmap.mask())
        self.ui.Avatar.setPixmap(pixmap)
        self.ui.Avatar.setScaledContents(True)
        
    def change_pw(self, event):
        self.changepw = ChangePass(self.ui.label_Username.text())
        self.changepw.show()
        
    def logout(self, event):
        self.close()
        self.login_window = Login()
        self.login_window.show()
        self.ui.label_Username.setText("")
        self.ui.label_Email.setText("")
    
    def change_page(self, index):
        self.ui.stackedWidget.setCurrentIndex(index)
        # if index in range(1,7):
        #     self.choose_pd.hide()
        
        buttons = [
            self.ui.Btn_Pd, 
            self.ui.Btn_Nv, 
            self.ui.Btn_Inventory, 
            self.ui.Btn_Revenue, 
            self.ui.Btn_Pub, 
            self.ui.Btn_Auth,
            self.ui.Btn_Genre
        ]
        
        # Thiết lập lại styleSheet cho tất cả các nút
        for button in buttons:
            button.setStyleSheet('''
                QPushButton{
                    border: 2px solid rgb(0, 170, 127);
                    border-radius: 15px;
                }
                QPushButton:hover{
                    color: rgb(255, 255, 255);
                    background-color: rgb(0, 170, 127);
                }
            ''')
        
        # Đặt màu nền cho nút được chọn
        selected_button = buttons[index]
        selected_button.setStyleSheet('''
            QPushButton{
                color: rgb(255, 255, 255);
                border: 2px solid rgb(0, 170, 127);
                border-radius: 15px;
                background-color: rgb(0, 170, 127); /* Màu nền khi được chọn */
            }
            QPushButton:hover{
                color: rgb(255, 255, 255);
                background-color: rgb(0, 170, 127);
            }
        ''')
        
        # Đặt index cho stackedWidget
        self.ui.stackedWidget.setCurrentIndex(index)
        
    # phần của page1 -----------------------------------------------------------------------------------
    def load_genre(self):
        # Kết nối với cơ sở dữ liệu MySQL
        self.db_connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="qlch"
        )
        cursor = self.db_connection.cursor()
        # Thực hiện truy vấn để lấy dữ liệu từ bảng lớp học
        cursor.execute("SELECT ten_theloai FROM theloai")
        rows = cursor.fetchall()
        # Xóa dữ liệu cũ trong ComboBox trước khi thêm dữ liệu mới
        self.ui.Genre.clear()
        # Thêm dữ liệu vào ComboBox
        for row in rows:
            self.ui.Genre.addItem(row[0])
        cursor.close()
        
    def load_pub(self):
        # Kết nối với cơ sở dữ liệu MySQL
        self.db_connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="qlch"
        )
        cursor = self.db_connection.cursor()
        # Thực hiện truy vấn để lấy dữ liệu từ bảng lớp học
        cursor.execute("SELECT ten_nhaph FROM nhaphathanh")
        rows = cursor.fetchall()
        # Xóa dữ liệu cũ trong ComboBox trước khi thêm dữ liệu mới
        self.ui.Pub.clear()
        # Thêm dữ liệu vào ComboBox
        for row in rows:
            self.ui.Pub.addItem(row[0])
        cursor.close()
        
    def load_auth(self):
        # Kết nối với cơ sở dữ liệu MySQL
        self.db_connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="qlch"
        )
        cursor = self.db_connection.cursor()
        # Thực hiện truy vấn để lấy dữ liệu từ bảng lớp học
        cursor.execute("SELECT ten_tacgia FROM tacgia")
        rows = cursor.fetchall()
        # Xóa dữ liệu cũ trong ComboBox trước khi thêm dữ liệu mới
        self.ui.Author.clear()
        # Thêm dữ liệu vào ComboBox
        for row in rows:
            self.ui.Author.addItem(row[0])
        cursor.close()
    
    def load_data(self):
        try:
            connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="qlch"
            )

            cursor = connection.cursor()

            # Thực hiện truy vấn join để lấy thông tin từ các bảng thích hợp
            cursor.execute("""
                SELECT sp.product_id, tl.ten_theloai, nph.ten_nhaph, tg.ten_tacgia, sp.hinhanh, sp.tensanpham, sp.price, sp.status
                FROM sanpham sp
                LEFT JOIN theloai tl ON sp.genre_id = tl.genre_id
                LEFT JOIN nhaphathanh nph ON sp.pub_id = nph.pub_id
                LEFT JOIN tacgia tg ON sp.auth_id = tg.auth_id
            """)
            results = cursor.fetchall()

            self.ui.Table_sanpham.setRowCount(len(results))

            for row_num, row_data in enumerate(results):
                for col_num, data in enumerate(row_data):
                    if col_num == 4:  # Cột hình ảnh
                        # Hiển thị hình ảnh trong cột
                        pixmap = QPixmap(data)
                        item = QTableWidgetItem()
                        item.setData(Qt.DecorationRole, pixmap.scaledToHeight(100, Qt.SmoothTransformation))
                        item.setData(Qt.UserRole, data)  # Thêm đường dẫn vào UserRole
                    else:
                        item = QTableWidgetItem(str(data))
                    item.setFlags(item.flags() & ~Qt.ItemIsEditable)  # Đặt các ô không thể chỉnh sửa
                    self.ui.Table_sanpham.setItem(row_num, col_num, item)

            cursor.close()
            connection.close()

        except mysql.connector.Error as err:
            print(f"Lỗi: {err}")

    def select_product(self, row, column):
        self.ui.lineEdit_ProductID.setText(self.ui.Table_sanpham.item(row, 0).text())
        self.ui.Genre.setCurrentText(self.ui.Table_sanpham.item(row, 1).text())
        self.ui.Pub.setCurrentText(self.ui.Table_sanpham.item(row, 2).text())
        self.ui.Author.setCurrentText(self.ui.Table_sanpham.item(row, 3).text())
        self.ui.lineEdit_ProductName.setText(self.ui.Table_sanpham.item(row, 5).text())
        image_path = self.ui.Table_sanpham.item(row, 4).data(Qt.UserRole)  # Lấy đường dẫn từ UserRole
        self.ui.lineEdit_ImagePath.setText(image_path)
        self.ui.lineEdit_Price.setText(self.ui.Table_sanpham.item(row, 6).text())
        # status_text = self.ui.Table_sanpham.item(row, 7).text()
        
    def check_update(self):
        pd_id = self.ui.lineEdit_ProductID.text()
        pd_genre = self.ui.Genre.currentText()
        pd_pub = self.ui.Pub.currentText()
        pd_auth = self.ui.Author.currentText()
        pd_name = self.ui.lineEdit_ProductName.text()
        pd_price = self.ui.lineEdit_Price.text()
        pd_image = self.ui.lineEdit_ImagePath.text()
        
        row = self.ui.Table_sanpham.currentRow()
        if row == -1 or not all([pd_id, pd_genre, pd_pub, pd_auth, pd_name, pd_price, pd_image]):
            QMessageBox.critical(self, "Lỗi", "Chưa chọn sản phẩm cần cập nhật.")
            return

        selected_pd_id = self.ui.Table_sanpham.item(row, 0).text()
        current_image_path = self.ui.Table_sanpham.item(row, 4).data(Qt.UserRole)  # Lấy đường dẫn từ UserRole hiện tại

        # Thư mục đích để lưu hình ảnh
        dest_dir = r"E:\hoc\python\baitaplon\resources\pic\product_image"

        # Đảm bảo thư mục đích tồn tại
        if not os.path.exists(dest_dir):
            os.makedirs(dest_dir)

        # Hàm để tạo tên mới cho tập tin ảnh
        def get_new_image_name():
            existing_files = os.listdir(dest_dir)
            existing_numbers = [
                int(f[2:-4]) for f in existing_files if f.startswith("sp") and f.endswith(".jpg") and f[2:-4].isdigit()
            ]
            if existing_numbers:
                new_number = max(existing_numbers) + 1
            else:
                new_number = 1
            return f"sp{new_number}.jpg"

        # Chỉ đổi tên và di chuyển ảnh nếu đường dẫn ảnh mới khác với đường dẫn ảnh hiện tại
        if pd_image != current_image_path:
            new_image_name = get_new_image_name()  # Tạo tên mới cho tập tin ảnh
            new_image_path = os.path.join(dest_dir, new_image_name)  # Đường dẫn mới cho ảnh

            try:
                # Xóa ảnh cũ
                if os.path.exists(current_image_path):
                    os.remove(current_image_path)
                
                # Di chuyển và đổi tên ảnh mới
                shutil.copy(pd_image, new_image_path)
                # Cập nhật đường dẫn hình ảnh trong cơ sở dữ liệu
                pd_image = new_image_path
            except Exception as e:
                QMessageBox.critical(self, "Lỗi", str(e))
                return
        else:
            pd_image = current_image_path  # Giữ nguyên đường dẫn ảnh hiện tại nếu không thay đổi

        try:
            # Kết nối cơ sở dữ liệu và cập nhật thông tin sản phẩm
            connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="qlch"
            )

            cursor = connection.cursor()
            # Sử dụng new_product_id trong lệnh truy vấn UPDATE
            # Truy vấn để lấy genre_id từ tên thể loại
            cursor.execute("SELECT genre_id FROM theloai WHERE ten_theloai = %s", (pd_genre,))
            genre_id = cursor.fetchone()[0]

            # Truy vấn để lấy pub_id từ tên nhà phát hành
            cursor.execute("SELECT pub_id FROM nhaphathanh WHERE ten_nhaph = %s", (pd_pub,))
            pub_id = cursor.fetchone()[0]

            # Truy vấn để lấy auth_id từ tên tác giả
            cursor.execute("SELECT auth_id FROM tacgia WHERE ten_tacgia = %s", (pd_auth,))
            auth_id = cursor.fetchone()[0]
            
            query = """
                    UPDATE sanpham
                    SET product_id = %s, genre_id = %s, pub_id = %s, auth_id = %s, tensanpham = %s, hinhanh = %s, price = %s
                    WHERE product_id = %s
                    """
            cursor.execute(query, (pd_id, genre_id, pub_id, auth_id, pd_name, pd_image, pd_price, selected_pd_id))
            connection.commit()

            cursor.close()
            connection.close()

            self.load_data()  # Tải lại dữ liệu sau khi lưu
            self.load_data_inv()
            
            self.record_act_epl(self.ui.label_Username.text(), self.name, f'đã cập nhật sản phẩm {pd_name} với mã "{pd_id}"')
            
            self.ui.lineEdit_ProductID.setText("")
            self.ui.Genre.setCurrentIndex(-1)
            self.ui.Pub.setCurrentIndex(-1)
            self.ui.Author.setCurrentIndex(-1)
            self.ui.lineEdit_ProductName.setText("")
            self.ui.lineEdit_Price.setText("")
            self.ui.lineEdit_ImagePath.setText("")
            
            QMessageBox.information(self, "Thông báo", "Cập nhật thành công")

        except mysql.connector.Error as err:
            QMessageBox.critical(self, "Database Lỗi", f"Lỗi: {err}")
        except Exception as e:
            QMessageBox.critical(self, "Lỗi", str(e))

    def check_adding(self):
        pd_id = self.ui.lineEdit_ProductID.text()
        pd_genre = self.ui.Genre.currentText()
        pd_pub = self.ui.Pub.currentText()
        pd_auth = self.ui.Author.currentText()
        pd_name = self.ui.lineEdit_ProductName.text()
        pd_price = self.ui.lineEdit_Price.text()
        pd_image = self.ui.lineEdit_ImagePath.text()

        if not all([pd_id, pd_genre, pd_pub, pd_auth, pd_name, pd_price, pd_image]):
            QMessageBox.critical(self, "Lỗi", "Chưa điền đầy đủ thông tin sản phẩm cần thêm.")
            return
        
        # Thư mục đích để lưu hình ảnh
        dest_dir = r"E:\hoc\python\baitaplon\resources\pic\product_image"

        # Đảm bảo thư mục đích tồn tại
        if not os.path.exists(dest_dir):
            os.makedirs(dest_dir)

        # Đặt tên ảnh mới theo định dạng sp(n).jpg
        def get_new_image_name():
            existing_files = os.listdir(dest_dir)
            existing_numbers = [
                int(f[2:-4]) for f in existing_files if f.startswith("sp") and f.endswith(".jpg") and f[2:-4].isdigit()
            ]
            if existing_numbers:
                new_number = max(existing_numbers) + 1
            else:
                new_number = 1
            return f"sp{new_number}.jpg"

        new_image_name = get_new_image_name()
        new_image_path = os.path.join(dest_dir, new_image_name)

        try:
            
            # Di chuyển và đổi tên ảnh
            shutil.copy(pd_image, new_image_path)
            
            # Cập nhật đường dẫn hình ảnh trong cơ sở dữ liệu
            pd_image = new_image_path
            
            # Kết nối cơ sở dữ liệu
            connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="qlch"
            )

            cursor = connection.cursor()
            # kiểm tra xem sản phẩm đã tồn tại hay chưa
            query_check_name_exist = "SELECT COUNT(*) FROM sanpham WHERE tensanpham = %s"
            cursor.execute(query_check_name_exist, (pd_name,))
            result_name_check = cursor.fetchone()
            if result_name_check[0] > 0:  # Nếu sản phẩm đã tồn tại
                QMessageBox.critical(self, "Lỗi", "Tên sản phẩm đã tồn tại.")
                cursor.close()
                connection.close()
                return
            
            # Truy vấn để lấy genre_id từ tên thể loại
            cursor.execute("SELECT genre_id FROM theloai WHERE ten_theloai = %s", (pd_genre,))
            genre_id = cursor.fetchone()[0]

            # Truy vấn để lấy pub_id từ tên nhà phát hành
            cursor.execute("SELECT pub_id FROM nhaphathanh WHERE ten_nhaph = %s", (pd_pub,))
            pub_id = cursor.fetchone()[0]

            # Truy vấn để lấy auth_id từ tên tác giả
            cursor.execute("SELECT auth_id FROM tacgia WHERE ten_tacgia = %s", (pd_auth,))
            auth_id = cursor.fetchone()[0]
            
            query_product = """
                    INSERT INTO sanpham (product_id, genre_id, pub_id, auth_id, tensanpham, hinhanh, price, status)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                    """
            cursor.execute(query_product, (pd_id, genre_id, pub_id, auth_id, pd_name, pd_image, pd_price, 'còn hàng'))
            connection.commit()

            # Kiểm tra xem sản phẩm đã tồn tại trong bảng 'tonkho' chưa
            query_check_exist = "SELECT COUNT(*) FROM tonkho WHERE product_id = %s"
            cursor.execute(query_check_exist, (pd_id,))
            result = cursor.fetchone()
            if result[0] == 0:  # Nếu sản phẩm chưa tồn tại trong bảng 'tonkho', thêm mới với quantity mặc định là 1
                insert_tonkho = "INSERT INTO tonkho (product_id, quantity) VALUES (%s, 1)"
                cursor.execute(insert_tonkho, (pd_id,))
                connection.commit()

            cursor.close()
            connection.close()

            self.load_data()
            self.load_data_inv()
            
            self.record_act_epl(self.ui.label_Username.text(), self.name,f'đã thêm sản phẩm {pd_name} với mã "{pd_id}"')
            
            self.ui.lineEdit_ProductID.setText("")
            self.ui.Genre.setCurrentIndex(-1)
            self.ui.Pub.setCurrentIndex(-1)
            self.ui.Author.setCurrentIndex(-1)
            self.ui.lineEdit_ProductName.setText("")
            self.ui.lineEdit_Price.setText("")
            self.ui.lineEdit_ImagePath.setText("")
            
            QMessageBox.information(self, "Thông báo", "Thêm sản phẩm thành công")
            
            self.load_histories()
            
        except mysql.connector.Error as err:
            QMessageBox.critical(self, "Database Lỗi", f"Lỗi: {err}")

    def check_delete(self):
        pd_id = self.ui.lineEdit_ProductID.text()
        pd_genre = self.ui.Genre.currentText()
        pd_pub = self.ui.Pub.currentText()
        pd_auth = self.ui.Author.currentText()
        pd_name = self.ui.lineEdit_ProductName.text()
        pd_price = self.ui.lineEdit_Price.text()
        pd_image = self.ui.lineEdit_ImagePath.text()
        
        row = self.ui.Table_sanpham.currentRow()
        if row == -1 or not all([pd_id, pd_genre, pd_pub, pd_auth, pd_name, pd_price, pd_image]):
            QMessageBox.critical(self, "Lỗi", "Chưa chọn sản phẩm cần xoá.")
            return
        
        # Lấy thông tin sản phẩm
        pd_id = self.ui.Table_sanpham.item(row, 0).text()
        pd_image_path = self.ui.Table_sanpham.item(row, 4).data(Qt.UserRole)  # Lấy đường dẫn ảnh từ UserRole

        try:
            # Xóa ảnh từ thư mục
            if os.path.exists(pd_image_path):
                os.remove(pd_image_path)

            # Xóa sản phẩm từ cơ sở dữ liệu
            connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="qlch"
            )

            cursor = connection.cursor()
            query1 = "DELETE FROM sanpham WHERE product_id = %s"
            cursor.execute(query1, (pd_id,))
            connection.commit()
            
            query2 = "DELETE FROM tonkho WHERE product_id = %s"
            cursor.execute(query2, (pd_id,))
            connection.commit()

            cursor.close()
            connection.close()

            self.load_data()
            self.load_inv()
            
            self.record_act_epl(self.ui.label_Username.text(), self.name,f'đã xoá sản phẩm {pd_name} với mã "{pd_id}"')
            
            self.ui.lineEdit_ProductID.setText("")
            self.ui.Genre.setCurrentIndex(-1)
            self.ui.Pub.setCurrentIndex(-1)
            self.ui.Author.setCurrentIndex(-1)
            self.ui.lineEdit_ProductName.setText("")
            self.ui.lineEdit_Price.setText("")
            self.ui.lineEdit_ImagePath.setText("")
            
            QMessageBox.information(self, "Thông báo", "Xóa sản phẩm thành công")

            self.load_histories()
            
        except mysql.connector.Error as err:
            QMessageBox.critical(self, "Database Lỗi", f"Lỗi: {err}")
        except Exception as e:
            QMessageBox.critical(self, "Lỗi", str(e))

    def select_image(self):
        # Thực hiện chức năng chọn hình ảnh từ hệ thống
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file_path, _ = QFileDialog.getOpenFileName(self, "Chọn ảnh", "", "Image Files (*.png *.jpg *.jpeg *.bmp *.gif)", options=options)
        if file_path:
            self.ui.lineEdit_ImagePath.setText(file_path)
    
    # phần của page2 -----------------------------------------------------------------------------------
    def load_data_nv(self):
        try:
            connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="qlch"
            )

            cursor = connection.cursor()
            cursor.execute("SELECT username, password, email, name, profile_image, role FROM users WHERE role IN ('Admin', 'Nhân viên')")
            results = cursor.fetchall()

            self.ui.Table_nv.setRowCount(len(results))

            for row_num, row_data in enumerate(results):
                for col_num, data in enumerate(row_data):
                    if col_num == 4:  # Cột hình ảnh
                        if data is not None and data != '':
                            # Hiển thị hình ảnh trong cột
                            pixmap = QPixmap(data)
                            item = QTableWidgetItem()
                            item.setData(Qt.DecorationRole, pixmap.scaledToHeight(100, Qt.SmoothTransformation))
                            item.setData(Qt.UserRole, data)  # Thêm đường dẫn vào UserRole
                        else:
                            # Xử lý trường hợp không có hình ảnh
                            item = QTableWidgetItem("No Image")
                    else:
                        item = QTableWidgetItem(str(data))
                    item.setFlags(item.flags() & ~Qt.ItemIsEditable)  # Đặt các ô không thể chỉnh sửa
                    self.ui.Table_nv.setItem(row_num, col_num, item)

            cursor.close()
            connection.close()

        except mysql.connector.Error as err:
            print(f"Lỗi: {err}")
            
    def select_nv(self, row, column):
        
        self.ui.lineEdit_NvUsername.setText(self.ui.Table_nv.item(row, 0).text())
        self.ui.lineEdit_NvPass.setText(self.ui.Table_nv.item(row, 1).text())
        self.ui.lineEdit_NvEmail.setText(self.ui.Table_nv.item(row, 2).text())
        self.ui.lineEdit_NvName.setText(self.ui.Table_nv.item(row, 3).text())
        image_path_nv = self.ui.Table_nv.item(row, 4).data(Qt.UserRole)  # Lấy đường dẫn từ UserRole
        self.ui.lineEdit_ImagePath_2.setText(image_path_nv)
        status_text_nv = self.ui.Table_nv.item(row, 5).text()
        status_index_nv = self.ui.Status_Nv.findText(status_text_nv)
        if status_index_nv != -1:
            self.ui.Status_Nv.setCurrentIndex(status_index_nv)
        else:
            self.ui.Status_Nv.setCurrentIndex(-1)
            
    def check_update_nv(self):
        nv_name = self.ui.lineEdit_NvName.text()
        nv_pass = self.ui.lineEdit_NvPass.text()
        nv_username = self.ui.lineEdit_NvUsername.text()
        nv_email = self.ui.lineEdit_NvEmail.text()
        nv_image = self.ui.lineEdit_ImagePath_2.text()
        nv_role = self.ui.Status_Nv.currentText()
        
        row = self.ui.Table_nv.currentRow()
        if row == -1 or not all([nv_name, nv_pass, nv_username, nv_email, nv_image, nv_role]):
            QMessageBox.critical(self, "Lỗi", "Chưa chọn nhân viên để cập nhật thông tin.")
            return

        current_image_path = self.ui.Table_nv.item(row, 4).data(Qt.UserRole)  # Lấy đường dẫn từ UserRole hiện tại

        # Thư mục đích để lưu hình ảnh
        dest_dir = r"E:\hoc\python\baitaplon\resources\pic\profile_image"

        # Đảm bảo thư mục đích tồn tại
        if not os.path.exists(dest_dir):
            os.makedirs(dest_dir)

        # Hàm để tạo tên mới cho tập tin ảnh
        def get_new_image_name():
            existing_files = os.listdir(dest_dir)
            existing_numbers = [
                int(f[2:-4]) for f in existing_files if f.startswith("pf") and f.endswith(".jpg") and f[2:-4].isdigit()
            ]
            if existing_numbers:
                new_number = max(existing_numbers) + 1
            else:
                new_number = 1
            return f"pf{new_number}.jpg"

        # Chỉ đổi tên và di chuyển ảnh nếu đường dẫn ảnh mới khác với đường dẫn ảnh hiện tại
        if nv_image != current_image_path:
            new_image_name = get_new_image_name()  # Tạo tên mới cho tập tin ảnh
            new_image_path_nv = os.path.join(dest_dir, new_image_name)  # Đường dẫn mới cho ảnh

            try:
                # Xóa ảnh cũ
                if os.path.exists(current_image_path):
                    os.remove(current_image_path)
                
                # Di chuyển và đổi tên ảnh mới
                shutil.copy(nv_image, new_image_path_nv)
                # Cập nhật đường dẫn hình ảnh trong cơ sở dữ liệu
                nv_image = new_image_path_nv
            except Exception as e:
                QMessageBox.critical(self, "Lỗi", str(e))
                return
        else:
            nv_image = current_image_path  # Giữ nguyên đường dẫn ảnh hiện tại nếu không thay đổi

        try:
            # Kết nối cơ sở dữ liệu và cập nhật thông tin người dùng
            connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="qlch"
            )

            cursor = connection.cursor()
            # Sử dụng nv_username trong lệnh truy vấn UPDATE
            query = """
                    UPDATE users 
                    SET username = %s, email = %s, name = %s, password = %s, profile_image = %s, role = %s 
                    WHERE username = %s
                    """
            cursor.execute(query, (nv_username, nv_email, nv_name, nv_pass, nv_image, nv_role, nv_username))
            connection.commit()

            cursor.close()
            connection.close()

            self.load_data_nv()  # Tải lại dữ liệu sau khi lưu
            self.load_rev()
            
            self.record_act_epl(self.ui.label_Username.text(), self.name,f'đã cập nhật nhân viên {nv_name}')
            
            self.ui.lineEdit_NvName.setText("")
            self.ui.lineEdit_NvUsername.setText("")
            self.ui.lineEdit_NvEmail.setText("")
            self.ui.lineEdit_NvPass.setText("")
            self.ui.lineEdit_ImagePath_2.setText("")
            self.ui.Status_Nv.setCurrentIndex(-1)
            
            QMessageBox.information(self, "Thông báo", "Cập nhật thành công")
            
            self.load_histories()
            
        except mysql.connector.Error as err:
            QMessageBox.critical(self, "Database Lỗi", f"Lỗi: {err}")
        except Exception as e:
            QMessageBox.critical(self, "Lỗi", str(e))

    def check_adding_nv(self):
        nv_name = self.ui.lineEdit_NvName.text()
        nv_pass = self.ui.lineEdit_NvPass.text()
        nv_username = self.ui.lineEdit_NvUsername.text()
        nv_email = self.ui.lineEdit_NvEmail.text()
        nv_image = self.ui.lineEdit_ImagePath_2.text()
        nv_role = self.ui.Status_Nv.currentText()
        
        if not all([nv_name, nv_pass, nv_username, nv_email, nv_image, nv_role]):
            QMessageBox.critical(self, "Lỗi", "Chưa điền thông tin nhân viên cần thêm.")
            return
        
        # Thư mục đích để lưu hình ảnh
        dest_dir = r"E:\hoc\python\baitaplon\resources\pic\profile_image"

        # Đảm bảo thư mục đích tồn tại
        if not os.path.exists(dest_dir):
            os.makedirs(dest_dir)

        # Đặt tên ảnh mới theo định dạng sp(n).jpg
        def get_new_image_name():
            existing_files = os.listdir(dest_dir)
            existing_numbers = [
                int(f[2:-4]) for f in existing_files if f.startswith("pf") and f.endswith(".jpg") and f[2:-4].isdigit()
            ]
            if existing_numbers:
                new_number = max(existing_numbers) + 1
            else:
                new_number = 1
            return f"pf{new_number}.jpg"

        new_image_name = get_new_image_name()
        new_image_path = os.path.join(dest_dir, new_image_name)

        try:
            
            # Di chuyển và đổi tên ảnh
            shutil.copy(nv_image, new_image_path)
            
            # Cập nhật đường dẫn hình ảnh trong cơ sở dữ liệu
            nv_image = new_image_path
            
            # Kết nối cơ sở dữ liệu
            connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="qlch"
            )

            cursor = connection.cursor()
            query_check_name_exist = "SELECT COUNT(*) FROM users WHERE username = %s"
            cursor.execute(query_check_name_exist, (nv_username,))
            result_name_check = cursor.fetchone()
            if result_name_check[0] > 0:  # Nếu sản phẩm đã tồn tại
                QMessageBox.critical(self, "Lỗi", "Tên người dùng này đã tồn tại.")
                cursor.close()
                connection.close()
                return
            
            query = """
                    INSERT INTO users (username, email, name, password, profile_image, role)
                    VALUES (%s, %s, %s, %s, %s, %s)
                    """
            cursor.execute(query, (nv_username, nv_email, nv_name, nv_pass, nv_image, nv_role))
            connection.commit()

            cursor.close()
            connection.close()

            self.load_data_nv()
            self.load_rev()
            
            self.record_act_epl(self.ui.label_Username.text(), self.name,f'đã thêm nhân viên {nv_name}')
            
            self.ui.lineEdit_NvName.setText("")
            self.ui.lineEdit_NvUsername.setText("")
            self.ui.lineEdit_NvEmail.setText("")
            self.ui.lineEdit_NvPass.setText("")
            self.ui.lineEdit_ImagePath_2.setText("")
            self.ui.Status_Nv.setCurrentIndex(-1)
            
            QMessageBox.information(self, "Thông báo", "Thêm nhân viên thành công")

            self.load_histories()
            
        except mysql.connector.Error as err:
            QMessageBox.critical(self, "Database Lỗi", f"Lỗi: {err}")
        except Exception as e:
            QMessageBox.critical(self, "Lỗi", f"Lỗi: {str(e)}")

    def check_delete_nv(self):
        nv_name = self.ui.lineEdit_NvName.text()
        nv_pass = self.ui.lineEdit_NvPass.text()
        nv_username = self.ui.lineEdit_NvUsername.text()
        nv_email = self.ui.lineEdit_NvEmail.text()
        nv_image = self.ui.lineEdit_ImagePath_2.text()
        nv_role = self.ui.Status_Nv.currentText()
        
        row = self.ui.Table_nv.currentRow()
        if row == -1 or not all([nv_name, nv_pass, nv_username, nv_email, nv_image, nv_role]):
            QMessageBox.critical(self, "Lỗi", "Chưa chọn nhân viên cần xoá.")
            return
        
        # Lấy thông tin sản phẩm
        nv_user = self.ui.Table_nv.item(row, 0).text()
        user_image_path = self.ui.Table_nv.item(row, 4).data(Qt.UserRole)  # Lấy đường dẫn ảnh từ UserRole

        try:
            # Xóa ảnh từ thư mục
            if os.path.exists(user_image_path):
                os.remove(user_image_path)

            # Xóa sản phẩm từ cơ sở dữ liệu
            connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="qlch"
            )

            cursor = connection.cursor()
            query = "DELETE FROM users WHERE username = %s"
            cursor.execute(query, (nv_user,))
            connection.commit()

            cursor.close()
            connection.close()

            self.load_data_nv()  # Tải lại dữ liệu sau khi xóa
            self.load_rev()
            
            self.record_act_epl(self.ui.label_Username.text(), self.name,f'đã xoá nhân viên {nv_name}')
            
            self.ui.lineEdit_NvName.setText("")
            self.ui.lineEdit_NvUsername.setText("")
            self.ui.lineEdit_NvEmail.setText("")
            self.ui.lineEdit_NvPass.setText("")
            self.ui.lineEdit_ImagePath_2.setText("")
            self.ui.Status_Nv.setCurrentIndex(-1)
            
            QMessageBox.information(self, "Thông báo", "Xóa nhân viên thành công")

            self.load_histories()
            
        except mysql.connector.Error as err:
            QMessageBox.critical(self, "Database Lỗi", f"Lỗi: {err}")
        except Exception as e:
            QMessageBox.critical(self, "Lỗi", str(e))
            
    def select_image_nv(self):
        # Thực hiện chức năng chọn hình ảnh từ hệ thống
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file_path_nv, _ = QFileDialog.getOpenFileName(self, "Chọn ảnh", "", "Image Files (*.png *.jpg *.jpeg *.bmp *.gif)", options=options)
        if file_path_nv:
            self.ui.lineEdit_ImagePath_2.setText(file_path_nv)

    # phần của page3 -----------------------------------------------------------------------------------
    
    def load_data_inv(self):
        try:
            connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="qlch"
            )

            cursor = connection.cursor()
            cursor.execute("""
                SELECT sp.tensanpham, tk.quantity
                FROM tonkho tk
                LEFT JOIN sanpham sp ON tk.product_id = sp.product_id
            """)
            results = cursor.fetchall()

            self.ui.Table_tonkho.setRowCount(len(results))

            for row_num, row_data in enumerate(results):
                for col_num, data in enumerate(row_data):
                    item = QTableWidgetItem(str(data))
                    item.setFlags(item.flags() & ~Qt.ItemIsEditable)  # Đặt các ô không thể chỉnh sửa
                    self.ui.Table_tonkho.setItem(row_num, col_num, item)

            cursor.close()
            connection.close()

        except mysql.connector.Error as err:
            print(f"Lỗi: {err}")
            
    # def select_inv(self, row, column):
    #     self.ui.lineEdit_Quantt.setText(self.ui.Table_tonkho.item(row, 1).text())

    def check_update_inv(self):
        row = self.ui.Table_tonkho.currentRow()
        
        tk_sl = self.ui.lineEdit_Quantt.text()
        tk_name = self.ui.Table_tonkho.item(row, 0).text()
        
        if row == -1 or not tk_sl:
            QMessageBox.warning(self,"Lỗi","Chưa chọn sản phẩm cần tăng số lượng.")
            return

        try:
            # Kết nối cơ sở dữ liệu và cập nhật thông tin sản phẩm
            connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="qlch"
            )

            cursor = connection.cursor()
            
            cursor.execute("SELECT product_id FROM sanpham WHERE tensanpham = %s", (tk_name,))
            product_id = cursor.fetchone()[0]

            # Cập nhật số lượng trong bảng tonkho
            query1 = " UPDATE tonkho SET product_id = %s, quantity = quantity + %s WHERE product_id = %s "
            cursor.execute(query1, (product_id, tk_sl, product_id))
            connection.commit()

            cursor.close()
            connection.close()

            self.load_data_inv()
            self.load_data()
            
            self.record_act_epl(self.ui.label_Username.text(), self.name,f'đã thêm số lượng là {tk_sl} của sản phẩm "{tk_name}"')
            
            self.ui.lineEdit_Quantt.setText("")
            
            QMessageBox.information(self, "Thông báo", "Cập nhật thành công")
            
            self.load_histories()
            
        except mysql.connector.Error as err:
            QMessageBox.critical(self, "Database Lỗi", f"Lỗi: {err}")
        except Exception as e:
            QMessageBox.critical(self, "Lỗi", str(e))

    # phần của page4 -----------------------------------------------------------------------------------
    def load_rev(self):
        try:
            connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="qlch"
            )

            cursor = connection.cursor()
            cursor.execute("""
                        SELECT COUNT(cus_name) AS pdCount, SUM(total_amount) AS ttAmount 
                        FROM hoadon
                        """)
            result = cursor.fetchone()
            
            cursor.execute("""
                        SELECT 
                            COUNT(role) AS userCount
                        FROM users
                        WHERE role = 'Nhân viên'
                        """)
            mem_result = cursor.fetchone()
            
            cursor.execute("""
                        SELECT 
                            SUM(quantity) AS buySum
                        FROM chitiethoadon
                        WHERE transaction_type = 'Mua'
                        """)
            sell_result = cursor.fetchone()
            
            cursor.execute("""
                        SELECT SUM(quantity) AS renSum
                        FROM chitiethoadon
                        WHERE transaction_type = 'Thuê'
                        """)
            rent_count = cursor.fetchone()
            
            pd_count = str(result[0]) if result and result[0] is not None else "0"
            tt_amount = str(result[1]) if result and result[1] is not None else "0"
            mber = str(mem_result[0]) if mem_result and mem_result[0] is not None else "0"
            qtt_rent = str(rent_count[0]) if rent_count and rent_count[0] is not None else "0"
            qtt_sell = str(sell_result[0]) if sell_result and sell_result[0] is not None else "0"            
                        
            font = QFont()
            font.setFamilies([u"Agbalumo"])
            font.setPointSize(20)
                
            self.ui.tt_price.setFont(font)
            self.ui.tt_price.setText(f"{tt_amount} VND")
                
            self.ui.mber.setFont(font)
            self.ui.mber.setText(mber)
                
            self.ui.qtt_sell.setFont(font)
            self.ui.qtt_sell.setText(qtt_sell)
                
            self.ui.qtt_rent.setFont(font)
            self.ui.qtt_rent.setText(qtt_rent)
                
            self.ui.qtt_order.setFont(font)
            self.ui.qtt_order.setText(pd_count)
            
            # if result:
            #     # Lấy giá trị đầu tiên từ tuple và chuyển thành chuỗi
            #     pd_count = str(result[0])
            #     tt_amount = str(result[1])
            #     qtt_rent = str(rent_count[0])
            #     qtt_sell = str(sell_result[0])
            #     mber = str(mem_result[0])
                
            #     font = QFont()
            #     font.setFamilies([u"Agbalumo"])
            #     font.setPointSize(20)
                
            #     self.ui.tt_price.setFont(font)
            #     self.ui.tt_price.setText(f"{tt_amount} VND")
                
            #     self.ui.mber.setFont(font)
            #     self.ui.mber.setText(mber)
                
            #     self.ui.qtt_sell.setFont(font)
            #     self.ui.qtt_sell.setText(qtt_sell)
                
            #     self.ui.qtt_rent.setFont(font)
            #     self.ui.qtt_rent.setText(qtt_rent)
                
            #     self.ui.qtt_order.setFont(font)
            #     self.ui.qtt_order.setText(pd_count)
            # else:
                # self.ui.tt_price.setText("0")
                # self.ui.mber.setText("0")
                # self.ui.qtt_sell.setText("0")
                # self.ui.qtt_rent.setText("0")
                # self.ui.qtt_order.setText("0")

            cursor.close()
            connection.close()

        except mysql.connector.Error as err:
            print(f"Lỗi: {err}")

    def load_histories(self):
        try:
            connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="qlch"
            )

            cursor = connection.cursor()
            cursor.execute("SELECT name, username, action FROM lshd")
            results = cursor.fetchall()

            self.ui.Table_lshd.setRowCount(len(results))

            for row_num, row_data in enumerate(results):
                for col_num, data in enumerate(row_data):
                    item = QTableWidgetItem(str(data))
                    item.setFlags(item.flags() & ~Qt.ItemIsEditable)  # Đặt các ô không thể chỉnh sửa
                    self.ui.Table_lshd.setItem(row_num, col_num, item)

            cursor.close()
            connection.close()

        except mysql.connector.Error as err:
            print(f"Lỗi: {err}")
                    
    # phần của page5 -----------------------------------------------------------------------------------
    def load_data_nph(self):
        try:
            connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="qlch"
            )

            cursor = connection.cursor()
            cursor.execute("SELECT pub_id, ten_nhaph FROM nhaphathanh")
            results = cursor.fetchall()

            self.ui.Table_NhaPh.setRowCount(len(results))

            for row_num, row_data in enumerate(results):
                for col_num, data in enumerate(row_data):
                    item = QTableWidgetItem(str(data))
                    item.setFlags(item.flags() & ~Qt.ItemIsEditable)  # Đặt các ô không thể chỉnh sửa
                    self.ui.Table_NhaPh.setItem(row_num, col_num, item)

            cursor.close()
            connection.close()

        except mysql.connector.Error as err:
            print(f"Lỗi: {err}")

    def select_nph(self, row, column):
        self.ui.lineEdit_PubID.setText(self.ui.Table_NhaPh.item(row, 0).text())
        self.ui.lineEdit_PubName.setText(self.ui.Table_NhaPh.item(row, 1).text())

    def check_update_nph(self):
        pub_id = self.ui.lineEdit_PubID.text()
        pub_name = self.ui.lineEdit_PubName.text()
        
        row = self.ui.Table_NhaPh.currentRow()
        if row == -1 or not all([pub_id, pub_name]):
            QMessageBox.warning(self, "Lỗi", "Chưa chọn NPH cần cập nhật.")
            return
        
        selected_pub_id = self.ui.Table_NhaPh.item(row, 0).text()

        try:
            # Kết nối cơ sở dữ liệu và cập nhật thông tin sản phẩm
            connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="qlch"
            )

            cursor = connection.cursor()
            # Sử dụng new_product_id trong lệnh truy vấn UPDATE
            query = """
                    UPDATE nhaphathanh
                    SET pub_id = %s, ten_nhaph = %s
                    WHERE pub_id = %s
                    """
            cursor.execute(query, (pub_id, pub_name, selected_pub_id))
            connection.commit()
            connection.commit()

            cursor.close()
            connection.close()

            self.load_data_nph()
            
            self.record_act_epl(self.ui.label_Username.text(), self.name,f'đã cập nhật nph tên {pub_name} với mã "{pub_id}"')
            
            self.ui.lineEdit_PubID.setText("")
            self.ui.lineEdit_PubName.setText("")
            
            QMessageBox.information(self, "Thông báo", "Cập nhật thành công")
            
            self.load_histories()

        except mysql.connector.Error as err:
            QMessageBox.critical(self, "Database Lỗi", f"Lỗi: {err}")
        except Exception as e:
            QMessageBox.critical(self, "Lỗi", str(e))

    def check_adding_nph(self):
        pub_id = self.ui.lineEdit_PubID.text()
        pub_name = self.ui.lineEdit_PubName.text()
        
        if not all([pub_id, pub_name]):
            QMessageBox.warning(self, "Lỗi", "Chưa điền thông tin NPH cần thêm.")
            return

        try:
            # Kết nối cơ sở dữ liệu
            connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="qlch"
            )

            cursor = connection.cursor()
            query_check_name_exist = "SELECT COUNT(*) FROM nhaphathanh WHERE ten_nhaph = %s"
            cursor.execute(query_check_name_exist, (pub_name,))
            result_name_check = cursor.fetchone()
            if result_name_check[0] > 0:  # Nếu sản phẩm đã tồn tại
                QMessageBox.critical(self, "Lỗi", "Nhà phát hành này đã tồn tại.")
                cursor.close()
                connection.close()
                return
            
            query = """
                    INSERT INTO nhaphathanh (pub_id, ten_nhaph)
                    VALUES (%s, %s)
                    """
            cursor.execute(query, (pub_id, pub_name))
            connection.commit()

            cursor.close()
            connection.close()

            self.load_data_nph()
            
            self.record_act_epl(self.ui.label_Username.text(), self.name,f'đã thêm nph tên {pub_name} với mã "{pub_id}"')
            
            self.ui.lineEdit_PubID.setText("")
            self.ui.lineEdit_PubName.setText("")
            
            QMessageBox.information(self, "Thông báo", "Thêm NPH thành công")
            
            self.load_histories()
            
        except mysql.connector.Error as err:
            QMessageBox.critical(self, "Database Lỗi", f"Lỗi: {err}")

    def check_delete_nph(self):
        pub_id = self.ui.lineEdit_PubID.text()
        pub_name = self.ui.lineEdit_PubName.text()
        
        row = self.ui.Table_NhaPh.currentRow()
        if row == -1 or not all([pub_id, pub_name]):
            QMessageBox.warning(self, "Lỗi", "Chưa chọn NPH cần xoá.")
            return
        
        try:
            # Xóa sản phẩm từ cơ sở dữ liệu
            connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="qlch"
            )

            cursor = connection.cursor()
            query = "DELETE FROM nhaphathanh WHERE pub_id = %s"
            cursor.execute(query, (pub_id,))
            connection.commit()

            cursor.close()
            connection.close()

            self.load_data_nph()
            
            self.record_act_epl(self.ui.label_Username.text(), self.name,f'đã xoá nph tên {pub_name} với mã "{pub_id}"')
            
            self.ui.lineEdit_PubID.setText("")
            self.ui.lineEdit_PubName.setText("")

            QMessageBox.information(self, "Thông báo", "Xóa NPH thành công")
            
            self.load_histories()
            
        except mysql.connector.Error as err:
            QMessageBox.critical(self, "Database Lỗi", f"Lỗi: {err}")
        except Exception as e:
            QMessageBox.critical(self, "Lỗi", str(e))
    
    # phần của page6 -----------------------------------------------------------------------------------
    def load_data_tg(self):
        try:
            connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="qlch"
            )

            cursor = connection.cursor()
            cursor.execute("SELECT auth_id, ten_tacgia FROM tacgia")
            results = cursor.fetchall()

            self.ui.Table_tacgia.setRowCount(len(results))

            for row_num, row_data in enumerate(results):
                for col_num, data in enumerate(row_data):
                    item = QTableWidgetItem(str(data))
                    item.setFlags(item.flags() & ~Qt.ItemIsEditable)  # Đặt các ô không thể chỉnh sửa
                    self.ui.Table_tacgia.setItem(row_num, col_num, item)

            cursor.close()
            connection.close()

        except mysql.connector.Error as err:
            print(f"Lỗi: {err}")

    def select_tg(self, row, column):
        self.ui.lineEdit_AuthID.setText(self.ui.Table_tacgia.item(row, 0).text())
        self.ui.lineEdit_AuthN.setText(self.ui.Table_tacgia.item(row, 1).text())

    def check_update_tg(self):
        auth_id = self.ui.lineEdit_AuthID.text()
        auth_name = self.ui.lineEdit_AuthN.text()
        
        row = self.ui.Table_tacgia.currentRow()
        if row == -1 or not all([auth_id, auth_name]):
            QMessageBox.warning(self, "Lỗi", "Chưa chọn tác giả cần cập nhật.")
            return
        
        selected_auth_id = self.ui.Table_tacgia.item(row, 0).text()

        try:
            # Kết nối cơ sở dữ liệu và cập nhật thông tin sản phẩm
            connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="qlch"
            )

            cursor = connection.cursor()
            # Sử dụng new_product_id trong lệnh truy vấn UPDATE
            query = """
                    UPDATE tacgia
                    SET auth_id = %s, ten_tacgia = %s
                    WHERE auth_id = %s
                    """
            cursor.execute(query, (auth_id, auth_name, selected_auth_id))
            connection.commit()
            connection.commit()

            cursor.close()
            connection.close()

            self.load_data_tg()
            
            self.record_act_epl(self.ui.label_Username.text(), self.name,f'đã cập nhật tác giả tên {auth_name} với mã "{auth_id}"')
            
            self.ui.lineEdit_AuthID.setText("")
            self.ui.lineEdit_AuthN.setText("")
            
            QMessageBox.information(self, "Thông báo", "Cập nhật thành công")
            
            self.load_histories()
            
        except mysql.connector.Error as err:
            QMessageBox.critical(self, "Database Lỗi", f"Lỗi: {err}")
        except Exception as e:
            QMessageBox.critical(self, "Lỗi", str(e))

    def check_adding_tg(self):
        auth_id = self.ui.lineEdit_AuthID.text()
        auth_name = self.ui.lineEdit_AuthN.text()
        
        if not all([auth_id, auth_name]):
            QMessageBox.warning(self, "Lỗi", "Không có dữ liệu tác giả cần thêm.")
            return

        try:
            # Kết nối cơ sở dữ liệu
            connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="qlch"
            )

            cursor = connection.cursor()
            query_check_name_exist = "SELECT COUNT(*) FROM tacgia WHERE ten_tacgia = %s"
            cursor.execute(query_check_name_exist, (auth_name,))
            result_name_check = cursor.fetchone()
            if result_name_check[0] > 0:  # Nếu sản phẩm đã tồn tại
                QMessageBox.critical(self, "Lỗi", "Tên người dùng này đã tồn tại.")
                cursor.close()
                connection.close()
                return
            query = """
                    INSERT INTO tacgia (auth_id, ten_tacgia)
                    VALUES (%s, %s)
                    """
            cursor.execute(query, (auth_id, auth_name))
            connection.commit()

            cursor.close()
            connection.close()

            self.load_data_tg()
            
            self.record_act_epl(self.ui.label_Username.text(), self.name,f'đã thêm tác giả tên {auth_name} với mã "{auth_id}"')
            
            self.ui.lineEdit_PubID.setText("")
            self.ui.lineEdit_PubName.setText("")
            
            QMessageBox.information(self, "Thông báo", "Thêm tác giả thành công")
            
        except mysql.connector.Error as err:
            QMessageBox.critical(self, "Database Lỗi", f"Lỗi: {err}")

    def check_delete_tg(self):
        auth_id = self.ui.lineEdit_AuthID.text()
        auth_name = self.ui.lineEdit_AuthN.text()
        
        row = self.ui.Table_tacgia.currentRow()
        if row == -1 or not all([auth_id, auth_name]):
            QMessageBox.warning(self, "Lỗi", "Chưa chọn tác giả cần xoá.")
            return
        
        # Lấy thông tin sản phẩm
        auth_id = self.ui.Table_tacgia.item(row, 0).text()

        try:
            # Xóa sản phẩm từ cơ sở dữ liệu
            connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="qlch"
            )

            cursor = connection.cursor()
            query = "DELETE FROM tacgia WHERE auth_id = %s"
            cursor.execute(query, (auth_id,))
            connection.commit()

            cursor.close()
            connection.close()

            self.load_data_tg()
            
            self.record_act_epl(self.ui.label_Username.text(), self.name,f'đã xoá tác giả tên {auth_name} với mã "{auth_id}"')
            
            self.ui.lineEdit_AuthID.setText("")
            self.ui.lineEdit_AuthN.setText("")

            QMessageBox.information(self, "Thông báo", "Xóa tác giả thành công")
            
            self.load_histories()
            
        except mysql.connector.Error as err:
            QMessageBox.critical(self, "Database Lỗi", f"Lỗi: {err}")
        except Exception as e:
            QMessageBox.critical(self, "Lỗi", str(e))

    # phần của page7 -----------------------------------------------------------------------------------
    def load_data_tl(self):
        try:
            connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="qlch"
            )

            cursor = connection.cursor()
            cursor.execute("SELECT genre_id, ten_theloai FROM theloai")
            results = cursor.fetchall()

            self.ui.Table_theloai.setRowCount(len(results))

            for row_num, row_data in enumerate(results):
                for col_num, data in enumerate(row_data):
                    item = QTableWidgetItem(str(data))
                    item.setFlags(item.flags() & ~Qt.ItemIsEditable)  # Đặt các ô không thể chỉnh sửa
                    self.ui.Table_theloai.setItem(row_num, col_num, item)

            cursor.close()
            connection.close()

        except mysql.connector.Error as err:
            print(f"Lỗi: {err}")

    def select_tl(self, row, column):
        self.ui.lineEdit_GenreID.setText(self.ui.Table_theloai.item(row, 0).text())
        self.ui.lineEdit_GenreN.setText(self.ui.Table_theloai.item(row, 1).text())

    def check_update_tl(self):
        genre_id = self.ui.lineEdit_GenreID.text()
        genre_name = self.ui.lineEdit_GenreN.text()
        
        row = self.ui.Table_theloai.currentRow()
        if row == -1 or not all([genre_name, genre_id]):
            QMessageBox.warning(self, "Lỗi", "Chưa chọn thể loại cần cập nhật.")
            return
        
        selected_genre_id = self.ui.Table_theloai.item(row, 0).text()

        try:
            # Kết nối cơ sở dữ liệu và cập nhật thông tin sản phẩm
            connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="qlch"
            )

            cursor = connection.cursor()
            # Sử dụng new_product_id trong lệnh truy vấn UPDATE
            query = """
                    UPDATE theloai
                    SET genre_id = %s, ten_theloai = %s
                    WHERE genre_id = %s
                    """
            cursor.execute(query, (genre_id, genre_name, selected_genre_id))
            connection.commit()
            connection.commit()

            cursor.close()
            connection.close()

            self.load_data_tl()
            
            self.record_act_epl(self.ui.label_Username.text(), self.name,f'đã cập nhật thể loại tên {genre_name} với mã "{genre_id}"')
            
            self.ui.lineEdit_GenreID.setText("")
            self.ui.lineEdit_GenreN.setText("")

            QMessageBox.information(self, "Thông báo", "Cập nhật thành công")
            
            self.load_histories()
            
        except mysql.connector.Error as err:
            QMessageBox.critical(self, "Database Lỗi", f"Lỗi: {err}")
        except Exception as e:
            QMessageBox.critical(self, "Lỗi", str(e))

    def check_adding_tl(self):
        genre_id = self.ui.lineEdit_GenreID.text()
        genre_name = self.ui.lineEdit_GenreN.text()
        
        if not all([genre_name, genre_id]):
            QMessageBox.warning(self, "Lỗi", "Chưa điền thông tin thể loại cần thêm.")
            return

        try:
            # Kết nối cơ sở dữ liệu
            connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="qlch"
            )

            cursor = connection.cursor()
            
            query_check_name_exist = "SELECT COUNT(*) FROM theloai WHERE ten_theloai = %s"
            cursor.execute(query_check_name_exist, (genre_name,))
            result_name_check = cursor.fetchone()
            if result_name_check[0] > 0:  # Nếu sản phẩm đã tồn tại
                QMessageBox.critical(self, "Lỗi", "Thể loại này đã tồn tại.")
                cursor.close()
                connection.close()
                return
            
            query = """
                    INSERT INTO theloai (genre_id, ten_theloai)
                    VALUES (%s, %s)
                    """
            cursor.execute(query, (genre_id, genre_name))
            connection.commit()

            cursor.close()
            connection.close()

            self.load_data_tl()
            
            self.record_act_epl(self.ui.label_Username.text(), self.name,f'đã thêm thể loại tên {genre_name} với mã "{genre_id}"')
            
            self.ui.lineEdit_GenreID.setText("")
            self.ui.lineEdit_GenreN.setText("")

            QMessageBox.information(self, "Thông báo", "Thêm thể loại thành công")
            
            self.load_histories()
            
        except mysql.connector.Error as err:
            QMessageBox.critical(self, "Database Lỗi", f"Lỗi: {err}")

    def check_delete_tl(self):
        genre_id = self.ui.lineEdit_GenreID.text()
        genre_name = self.ui.lineEdit_GenreN.text()
        
        row = self.ui.Table_theloai.currentRow()
        if row == -1 or not all([genre_name, genre_id]):
            QMessageBox.warning(self, "Lỗi", "Chưa điền thông tin thể loại cần thêm.")
            return
        
        # Lấy thông tin sản phẩm
        genre_id = self.ui.Table_theloai.item(row, 0).text()

        try:
            # Xóa sản phẩm từ cơ sở dữ liệu
            connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="qlch"
            )

            cursor = connection.cursor()
            query = "DELETE FROM theloai WHERE genre_id = %s"
            cursor.execute(query, (genre_id,))
            connection.commit()

            cursor.close()
            connection.close()

            self.load_data_tl()  # Tải lại dữ liệu sau khi xóa
            
            self.record_act_epl(self.ui.label_Username.text(), self.name,f'đã xoá thể loại tên {genre_name} với mã "{genre_id}"')
            
            self.ui.lineEdit_GenreID.setText("")
            self.ui.lineEdit_GenreN.setText("")

            QMessageBox.information(self, "Thông báo", "Xóa thể loại thành công")
            
            self.load_histories()
            
            # Xóa nội dung của các lineEdit
            
        except mysql.connector.Error as err:
            QMessageBox.critical(self, "Database Lỗi", f"Lỗi: {err}")
        except Exception as e:
            QMessageBox.critical(self, "Lỗi", str(e))

# MAINEMPLOYEE
class MainEmpl(QMainWindow):
    def __init__(self,  username, email, profile_image, name, choose_pd):
        super().__init__()
        self.ui = Ui_Main_Employee()
        self.ui.setupUi(self)
        
        self.set_avatar(profile_image)
        self.ui.label_Username.setText(username)
        self.ui.label_Email.setText(email)
        self.ui.label_Name.setText(name)
        
        self.choose_pd = choose_pd
        # self.choose_pd = Choose_Pd()
        # self.login = Login()
        
        # Đưa window về trung tâm màn hình
        qr = self.frameGeometry()
        cp = self.screen().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
        
        ## XOÁ TITLEBAR
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        
        self.ui.label_Exit.mousePressEvent = self.close_window
        self.ui.label_Minimize.mousePressEvent = self.minimize_window
        self.ui.label_CPass.mousePressEvent = self.change_pw
        self.ui.label_Logout.mousePressEvent = self.logout
        
        self.ui.Btn_Td.clicked.connect(lambda: self.change_page(0))
        self.ui.Btn_Pd.clicked.connect(lambda: self.change_page(1))
        self.ui.Btn_Bkeeping.clicked.connect(lambda: self.change_page(2))
        self.ui.Btn_Sell.clicked.connect(lambda: self.change_page(3))
        self.ui.Btn_Rent.clicked.connect(lambda: self.change_page(4))
        self.ui.Btn_Report.clicked.connect(lambda: self.change_page(5))
        
        self.change_page(0)
        
        # page 1 -----------------------------------------------------------------------------------
        self.ui.Tt_price.setReadOnly(True)
        self.ui.Tt_price.setFocusPolicy(Qt.NoFocus)
        
        self.ui.Btn_Edit_Kh.clicked.connect(self.check_update_kh)
        self.ui.Btn_Clr.clicked.connect(self.clear)
        self.ui.Btn_Del_Hd.clicked.connect(self.check_delete_hd)
        self.ui.Btn_Save.clicked.connect(self.slt_date_to_tb_sp)
        
        self.ui.Rent_End.setCalendarPopup(True)
        self.ui.Rent_End.setCalendarWidget(self.ui.cld_return)
        self.ui.cld_return.selectionChanged.connect(self.updateSelectedDate)
        
        current_date = QDate.currentDate()
        day_date = current_date.addDays(3)
        
        self.ui.cld_return.setMaximumDate(day_date)
        self.ui.Rent_St.setDate(current_date)
        self.ui.Rent_End.setDate(day_date)
        
        self.ui.label_st.hide()
        self.ui.label_end.hide()
        self.ui.Rent_St.hide()
        self.ui.Rent_End.hide()
        self.ui.Btn_Save.hide()
        
        # Table_Sp ---------------------------------------------------------------------------------
        self.ui.Table_Sp.setColumnCount(7)
        self.ui.Table_Sp.setHorizontalHeaderLabels(["ID","Sản phẩm","Loại","Số lượng","Giá", "Ngày mượn", "Ngày trả"])
        self.ui.Table_Sp.verticalHeader().setVisible(False)  # Tắt số thứ tự đầu bảng
        # Thiết lập kích thước cột tự động theo tỉ lệ
        self.ui.Table_Sp.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.Table_Sp.setSelectionBehavior(QAbstractItemView.SelectRows)  # Chọn cả dòng
        self.ui.Table_Sp.verticalHeader().setDefaultSectionSize(50)  # Tăng chiều cao của dòng
        
        self.ui.Table_Sp.cellClicked.connect(self.select_tb_sp)
        
        # Table_Hd ---------------------------------------------------------------------------------
        
        self.ui.Btn_Paym_Kh.clicked.connect(self.payment)
        
        self.ui.Table_Hd.setColumnCount(5)
        self.ui.Table_Hd.setHorizontalHeaderLabels(["Tên khách","Số điện thoại","Địa chỉ","Ngày","Tổng tiền"])
        self.ui.Table_Hd.verticalHeader().setVisible(False)  # Tắt số thứ tự đầu bảng
        # Thiết lập kích thước cột tự động theo tỉ lệ
        self.ui.Table_Hd.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.Table_Hd.setSelectionBehavior(QAbstractItemView.SelectRows)  # Chọn cả dòng
        self.ui.Table_Hd.verticalHeader().setDefaultSectionSize(50)  # Tăng chiều cao của dòng
        
        self.load_hd()
        self.ui.Table_Hd.cellClicked.connect(self.select)
        self.ui.Btn_re_prt_bill.clicked.connect(self.re_prt_bill)
        
        # Table_Hd_2 -------------------------------------------------------------------------------
        
        self.ui.Table_Hd_2.setColumnCount(4)
        self.ui.Table_Hd_2.setHorizontalHeaderLabels(["Sản phẩm","Số lượng","Loại","Giá"])
        self.ui.Table_Hd_2.verticalHeader().setVisible(False)  # Tắt số thứ tự đầu bảng
        # Thiết lập kích thước cột tự động theo tỉ lệ
        self.ui.Table_Hd_2.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.Table_Hd_2.setSelectionBehavior(QAbstractItemView.SelectRows)  # Chọn cả dòng
        self.ui.Table_Hd_2.verticalHeader().setDefaultSectionSize(50)  # Tăng chiều cao của dòng
        
        # self.load_data_kh()
        # self.ui.Table_Hd_2.cellClicked.connect(self.select_kh)
        
        # page 2 -----------------------------------------------------------------------------------
        # Kết nối các nút điều hướng với các hàm xử lý tương ứng
        self.ui.Btn_Del_Pd.clicked.connect(self.check_delete)
        self.ui.Btn_Update.clicked.connect(self.check_update)
        self.ui.Btn_SelectImage.clicked.connect(self.select_image)
        
        self.ui.Table_sanpham.setColumnCount(8)
        self.ui.Table_sanpham.setHorizontalHeaderLabels(["ID sản phẩm", "Thể Loại", "Nhà phát hành", "Tác giả", "Hình ảnh","Tên sản phẩm","Giá tiền","Trạng thái"])
        self.ui.Table_sanpham.verticalHeader().setVisible(False)  # Tắt số thứ tự đầu bảng
        # Thiết lập kích thước cột tự động theo tỉ lệ
        # self.ui.Table_sanpham.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.Table_sanpham.setSelectionBehavior(QAbstractItemView.SelectRows)  # Chọn cả dòng
        self.ui.Table_sanpham.verticalHeader().setDefaultSectionSize(100)  # Tăng chiều cao của dòng
        
        # Thiết lập kích thước cột cố định cho từng cột
        self.ui.Table_sanpham.setColumnWidth(0, 76)  # ID sản phẩm
        self.ui.Table_sanpham.setColumnWidth(1, 115)  # Thể Loại
        self.ui.Table_sanpham.setColumnWidth(2, 120)  # Nhà phát hành
        self.ui.Table_sanpham.setColumnWidth(3, 120)  # Tác giả
        self.ui.Table_sanpham.setColumnWidth(4, 120)  # Hình ảnh
        self.ui.Table_sanpham.setColumnWidth(5, 200)  # Tên sản phẩm
        self.ui.Table_sanpham.setColumnWidth(6, 110)  # Giá tiền
        self.ui.Table_sanpham.setColumnWidth(7, 110)  # Trạng thái
        
        self.load_data()
        self.ui.Table_sanpham.cellClicked.connect(self.select_product)
        
        self.load_genre()
        self.load_pub()
        self.load_auth()
        
        # page 3 ---------------------------------------------------------------------------------
        self.ui.Btn_bk_update.clicked.connect(self.check_update_bk)
        
        self.ui.Table_b_keeping.setColumnCount(2)
        self.ui.Table_b_keeping.setHorizontalHeaderLabels(["Tên sản phẩm","Số lượng"])
        self.ui.Table_b_keeping.verticalHeader().setVisible(False)  # Tắt số thứ tự đầu bảng
        # Thiết lập kích thước cột tự động theo tỉ lệ
        # self.ui.Table_b_keeping.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.Table_b_keeping.setSelectionBehavior(QAbstractItemView.SelectRows)  # Chọn cả dòng
        self.ui.Table_b_keeping.verticalHeader().setDefaultSectionSize(100)  # Tăng chiều cao của dòng
        
        # Thiết lập kích thước cột cố định cho từng cột
        self.ui.Table_b_keeping.setColumnWidth(0, 200)  # ID sản phẩm
        self.ui.Table_b_keeping.setColumnWidth(1, 200)  # Số lượng
        
        self.load_data_bk()
        # self.ui.Table_b_keeping.cellClicked.connect(self.select_bk)
        
        # page 4 ---------------------------------------------------------------------------------
        self.ui.Table_sell.setColumnCount(4)
        self.ui.Table_sell.setHorizontalHeaderLabels(["ID sản phẩm","Tên sản phẩm","Số lượng","Giá"])
        self.ui.Table_sell.verticalHeader().setVisible(False)  # Tắt số thứ tự đầu bảng
        # Thiết lập kích thước cột tự động theo tỉ lệ
        self.ui.Table_sell.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.Table_sell.setSelectionBehavior(QAbstractItemView.SelectRows)  # Chọn cả dòng
        self.ui.Table_sell.verticalHeader().setDefaultSectionSize(50)  # Tăng chiều cao của dòng
        
        self.load_sell()
        
        # page 5 ---------------------------------------------------------------------------------
        self.ui.Rent_st.setCurrentIndex(-1)
        self.ui.Btn_Upd_Rent.clicked.connect(self.upd_rent)
        
        self.ui.Table_rent.setColumnCount(7)
        self.ui.Table_rent.setHorizontalHeaderLabels(["Mã đơn","Tên sản phẩm","Số lượng","Giá", "Ngày mượn", "Hạn trả", "Trạng thái"])
        self.ui.Table_rent.verticalHeader().setVisible(False)  # Tắt số thứ tự đầu bảng
        # Thiết lập kích thước cột tự động theo tỉ lệ
        self.ui.Table_rent.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.Table_rent.setSelectionBehavior(QAbstractItemView.SelectRows)  # Chọn cả dòng
        self.ui.Table_rent.verticalHeader().setDefaultSectionSize(50)  # Tăng chiều cao của dòng
        
        self.load_rent()
        self.ui.Table_rent.cellClicked.connect(self.select_rent)
        
        # page 6 ---------------------------------------------------------------------------------

    def record_act_epl(self, username, name, action):
        try:
            connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="qlch"
            )
            cursor = connection.cursor()

            query = "INSERT INTO lshd (username, name, action) VALUES (%s, %s, %s)"
            cursor.execute(query, (username, name, action))

            connection.commit()
            cursor.close()
            connection.close()

        except mysql.connector.Error as err:
            print(f"Error: {err}")
               
    def close_window(self, event):
        self.close()
    
    def closeEvent(self, event):
        if self.choose_pd.isVisible():
            self.choose_pd.close()
        event.accept()
        
    def minimize_window(self, event):
        self.showMinimized()
        
    def set_avatar(self, image_path):
        if image_path is None:
            image_path = ":/image/resources/pic/icon.jpg"  # Đặt đường dẫn hình ảnh mặc định
        pixmap = QPixmap(image_path)
        rounded_pixmap = QPixmap(pixmap.size())
        rounded_pixmap.fill(Qt.transparent)
        mask_brush = QBrush(QColor(Qt.black))
        mask_brush.setStyle(Qt.SolidPattern)
        painter = QPainter(rounded_pixmap)
        painter.setBrush(mask_brush)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setPen(Qt.NoPen)
        painter.drawRoundedRect(0, 0, pixmap.width(), pixmap.height(), 50, 50)
        painter.end()
        pixmap.setMask(rounded_pixmap.mask())
        self.ui.Avatar.setPixmap(pixmap)
        self.ui.Avatar.setScaledContents(True)
        
    def change_pw(self, event):
        self.changepw = ChangePass(self.ui.label_Username.text())
        self.changepw.show()
        
    def logout(self, event):
        self.close()
        self.login_window = Login()
        self.login_window.show()
        self.ui.label_Username.setText("")
        self.ui.label_Email.setText("")
    
    def change_page(self, index):
        self.ui.stackedWidget.setCurrentIndex(index)
        # if index in range(1,7):
        #     self.choose_pd.hide()
        
        buttons = [
            self.ui.Btn_Td, 
            self.ui.Btn_Pd, 
            self.ui.Btn_Bkeeping, 
            self.ui.Btn_Sell, 
            self.ui.Btn_Rent, 
            self.ui.Btn_Report
        ]
        
        # Thiết lập lại styleSheet cho tất cả các nút
        for button in buttons:
            button.setStyleSheet('''
                QPushButton{
                    border: 2px solid rgb(0, 170, 127);
                    border-radius: 15px;
                }
                QPushButton:hover{
                    color: rgb(255, 255, 255);
                    background-color: rgb(0, 170, 127);
                }
            ''')
        
        # Đặt màu nền cho nút được chọn
        selected_button = buttons[index]
        selected_button.setStyleSheet('''
            QPushButton{
                color: rgb(255, 255, 255);
                border: 2px solid rgb(0, 170, 127);
                border-radius: 15px;
                background-color: rgb(0, 170, 127); /* Màu nền khi được chọn */
            }
            QPushButton:hover{
                color: rgb(255, 255, 255);
                background-color: rgb(0, 170, 127);
            }
        ''')
        
        # Đặt index cho stackedWidget
        self.ui.stackedWidget.setCurrentIndex(index)
        
    # phần của page1 -----------------------------------------------------------------------------------
    def updateSelectedDate(self):
        # Lấy ngày được chọn từ QCalendarWidget và đặt vào QDateEdit chọn ngày
        slt_date = self.ui.cld_return.selectedDate()
        self.ui.Rent_End.setDate(slt_date)
    
    def slt_date_to_tb_sp(self):
        row = self.ui.Table_Sp.currentRow()
        if row == -1:
            print("No row selected.")
            return

        date_start = self.ui.Rent_St.date().toString("dd-MM-yyyy")  # Lấy ngày từ QDateEdit
        item_st = QTableWidgetItem(date_start)  # Tạo một QTableWidgetItem với ngày vừa lấy
        self.ui.Table_Sp.setItem(row, 5, item_st)  # Đặt QTableWidgetItem vào ô của tableWidget
        # print(f"Set Rent Start Date: {date_start} at row {row}, column 5")

        current_date = QDate.currentDate()
        slt_date = self.ui.Rent_End.date()
        if slt_date < current_date:
            self.ui.Rent_End.setDate(current_date)

        date_return = self.ui.Rent_End.date().toString("dd-MM-yyyy")  # Lấy ngày từ QDateEdit
        item_rt = QTableWidgetItem(date_return)  # Tạo một QTableWidgetItem với ngày vừa lấy
        self.ui.Table_Sp.setItem(row, 6, item_rt)  # Đặt QTableWidgetItem vào ô của tableWidget
        # print(f"Set Rent End Date: {date_return} at row {row}, column 6")
        
    def update_table_sp(self, products):
        self.ui.Table_Sp.setRowCount(len(products))
        for row_num, product in enumerate(products):
            for col_num, data in enumerate(product):
                item = QTableWidgetItem(str(data))
                item.setFlags(item.flags() & ~Qt.ItemIsEditable)
                self.ui.Table_Sp.setItem(row_num, col_num, item)
                
    def update_total_price(self, total_price):
        font = QFont()
        font.setFamilies([u"Agbalumo"])
        font.setPointSize(14)
        self.ui.Tt_price.setText(f" {total_price} VND")
        self.ui.Tt_price.setFont(font)

    def load_hd(self):
        try:
            connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="qlch"
            )

            cursor = connection.cursor()

            # Thực hiện truy vấn join để lấy thông tin từ các bảng thích hợp
            cursor.execute("""
                SELECT cus_name, phone_num, addr, invoice_date, total_amount
                FROM hoadon
            """)
            results = cursor.fetchall()

            self.ui.Table_Hd.setRowCount(len(results))

            for row_num, row_data in enumerate(results):
                for col_num, data in enumerate(row_data):
                    item = QTableWidgetItem(str(data))
                    item.setFlags(item.flags() & ~Qt.ItemIsEditable)  # Đặt các ô không thể chỉnh sửa
                    self.ui.Table_Hd.setItem(row_num, col_num, item)

            cursor.close()
            connection.close()

        except mysql.connector.Error as err:
            print(f"Lỗi: {err}")

    def select(self, row, column):
        self.ui.Kh_name.setText(self.ui.Table_Hd.item(row, 0).text())
        self.ui.Kh_phone.setText(self.ui.Table_Hd.item(row, 1).text())
        self.ui.Kh_Addr.setText(self.ui.Table_Hd.item(row, 2).text())
        
        cus_name = self.ui.Table_Hd.item(row, 0).text()
        
        try:
            connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="qlch"
            )

            cursor = connection.cursor()
            
            # Truy vấn để lấy chi tiết hóa đơn dựa trên tên khách hàng
            query = """
                SELECT cthd.pd_name, cthd.quantity, cthd.transaction_type, cthd.price
                FROM chitiethoadon cthd
                JOIN hoadon hd ON cthd.invoice_id = hd.invoice_id
                WHERE hd.cus_name = %s
            """
            cursor.execute(query, (cus_name,))
            results = cursor.fetchall()
            
            self.ui.Table_Hd_2.setRowCount(len(results))
            for row_num, row_data in enumerate(results):
                for col_num, data in enumerate(row_data):
                    item = QTableWidgetItem(str(data))
                    item.setFlags(item.flags() & ~Qt.ItemIsEditable)  # Đặt các ô không thể chỉnh sửa
                    self.ui.Table_Hd_2.setItem(row_num, col_num, item)

            cursor.close()
            connection.close()

        except mysql.connector.Error as err:
            print(f"Lỗi: {err}")

    def select_tb_sp(self, row, column):
        row = self.ui.Table_Sp.currentRow()
        if row == -1:
            return
        
        # Lấy giá trị từ ô trong bảng
        # item = self.ui.Table_Sp.item(row, 5)
        # if item is not None and item.text() != '':
        #     date_str = item.text()  # Lấy chuỗi ngày/tháng/năm từ QTableWidgetItem
        #     date = QDate.fromString(date_str, "dd-MM-yyyy")  # Chuyển đổi chuỗi thành QDate
            
        #     # Đặt ngày vào QDateEdit Rent_St và Rent_End
        #     self.ui.Rent_St.setDate(date)
        #     self.ui.Rent_End.setDate(date)
        # else:
        #     # Nếu ô không có dữ liệu, bạn có thể xử lý ở đây, ví dụ như pass hoặc thực hiện một hành động khác
        #     pass
        
        ld_item = self.ui.Table_Sp.item(row, 2)
        if ld_item is not None and ld_item.text() == 'Thuê':
            self.ui.label_st.show()
            self.ui.label_end.show()
            self.ui.Rent_St.show()
            self.ui.Rent_End.show()
            self.ui.Btn_Save.show()
        else:
            self.ui.label_st.hide()
            self.ui.label_end.hide()
            self.ui.Rent_St.hide()
            self.ui.Rent_End.hide()
            self.ui.Btn_Save.hide()
    
    def payment(self):
        products = []

        kh_name = self.ui.Kh_name.text()
        kh_phone = self.ui.Kh_phone.text()
        kh_addr = self.ui.Kh_Addr.text()

        if not kh_name or not kh_phone or not kh_addr:
            QMessageBox.warning(self, "Thiếu thông tin", "Hãy điền đầy đủ tên khách hàng")
            return

        for row in range(self.ui.Table_Sp.rowCount()):
            product = []
            for col in range(self.ui.Table_Sp.columnCount()):
                item = self.ui.Table_Sp.item(row, col)
                if item is not None:
                    product.append(item.text())
                else:
                    product.append("")
            print(f"Row {row}: {product}")  # In ra dữ liệu từng hàng
            products.append(product)

        try:
            connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="qlch"
            )
            cursor = connection.cursor()

            current_dt = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

            total_amount = int(self.ui.Tt_price.text().split()[0])

            query = ("INSERT INTO hoadon (cus_name, phone_num, addr, invoice_date, total_amount) VALUES (%s, %s, %s, %s, %s)")
            cursor.execute(query, (kh_name, kh_phone, kh_addr, current_dt, total_amount))

            invoice_id = cursor.lastrowid

            for row, product in enumerate(products):
                product_id, product_name, action, quantity, price = product[:5]
                quantity = int(quantity)

                if action == 'Thuê':
                    rent_st_item = self.ui.Table_Sp.item(row, 5) 
                    rent_end_item = self.ui.Table_Sp.item(row, 6)

                    rent_st = rent_end = None
                    
                    if rent_st_item is not None:
                        rent_st = rent_st_item.text()
                        rent_st = datetime.strptime(rent_st, "%d-%m-%Y").date()
                        rent_st = rent_st.strftime("%Y-%m-%d")

                    if rent_end_item is not None:
                        rent_end = rent_end_item.text()
                        rent_end = datetime.strptime(rent_end, "%d-%m-%Y").date()
                        rent_end = rent_end.strftime("%Y-%m-%d")
                        
                    if rent_st is None or rent_end is None:
                        QMessageBox.warning(self, "Thiếu thông tin", "Thiếu ngày hẹn trả sản phẩm")
                        return

                    query2 = ("INSERT INTO chitiethoadon (invoice_id, product_id, pd_name, transaction_type, quantity, price, borrow_date, return_date, status_sp) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)")
                    cursor.execute(query2, (invoice_id, product_id, product_name, action, quantity, price, rent_st, rent_end, 'Đang mượn'))
                else:
                    rent_st = rent_end = None
                    
                    query2 = ("INSERT INTO chitiethoadon (invoice_id, product_id, pd_name, transaction_type, quantity, price, borrow_date, return_date, status_sp) VALUES (%s, %s, %s, %s, %s, %s, NULL, NULL, NULL)")
                    cursor.execute(query2, (invoice_id, product_id, product_name, action, quantity, price))

                update_quantity_query = ("UPDATE tonkho SET quantity = quantity - %s WHERE product_id = %s")
                cursor.execute(update_quantity_query, (quantity, product_id))

            connection.commit()
            cursor.close()
            connection.close()
            
            self.record_act_epl(self.ui.label_Username.text(), self.name, f'Thanh toán hoá đơn {invoice_id}')

            reply = QMessageBox.question(self, 'In hóa đơn', 'Bạn có muốn in hóa đơn không?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

            if reply == QMessageBox.Yes:
                with open(f'invoice_{invoice_id}.txt', 'w', encoding='utf-8') as f:
                    f.write(f"Hóa đơn số: {invoice_id}\n")
                    f.write(f"Tên khách hàng: {kh_name}\n")
                    f.write(f"Số điện thoại: {kh_phone}\n")
                    f.write(f"Địa chỉ: {kh_addr}\n")
                    f.write(f"Ngày hóa đơn: {current_dt}\n")
                    f.write(f"Tổng số tiền: {total_amount}\n\n")
                    f.write("Danh sách sản phẩm:\n")
                    f.write(f"{'Mã SP':<10}{'Tên SP':<30}{'Hành động':<15}{'Số lượng':<10}{'Giá':<10}\n")
                    for product in products:
                        product_id, product_name, action, quantity, price = product[:5]
                        f.write(f"{product_id:<10}{product_name:<30}{action:<15}{quantity:<10}{price:<10}\n")

            self.ui.Table_Sp.setRowCount(0)
            self.choose_pd.cl_tb_choosed()
            self.ui.Tt_price.clear()

            self.ui.Kh_name.setText("")
            self.ui.Kh_phone.setText("")
            self.ui.Kh_Addr.setText("")

            self.load_hd()
            self.load_sell()
            self.load_rent()
            self.choose_pd.load_data()

            QMessageBox.information(self, "Thông báo", "Thanh toán thành công.")

        except mysql.connector.Error as err:
            QMessageBox.critical(self, "Lỗi", f"Đã xảy ra lỗi: {err}")
        
    def re_prt_bill(self):
        row = self.ui.Table_Hd.currentRow()
        
        # kh_name = self.ui.Table_Hd.item(row, 0).text()
        # kh_phone = self.ui.Table_Hd.item(row, 1).text()
        # kh_addr = self.ui.Table_Hd.item(row, 2).text()
        kh_name = self.ui.Kh_name.text()
        kh_phone = self.ui.Kh_phone.text()
        kh_addr = self.ui.Kh_Addr.text()
        
        
        if row == -1 or not kh_name or not kh_phone or not kh_addr:
            QMessageBox.warning(self, "Lỗi", "Bạn chưa chọn hóa đơn cần in",)
            return
        
        invoice_date = self.ui.Table_Hd.item(row, 3).text()
        tt_amount = self.ui.Table_Hd.item(row, 4).text()
        
        try:
            
            connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="qlch"
            )
            cursor = connection.cursor()

            query_invoice = ("SELECT invoice_id FROM hoadon WHERE cus_name = %s AND phone_num = %s AND addr = %s AND invoice_date = %s AND total_amount = %s")
            cursor.execute(query_invoice, (kh_name, kh_phone, kh_addr, invoice_date, tt_amount))
            result = cursor.fetchone()

            if not result:
                QMessageBox.warning(self, "Không tìm thấy", "Không tìm thấy hóa đơn với thông tin đã nhập")
                return

            invoice_id = result[0]

            query_products = "SELECT product_id, pd_name, transaction_type, quantity, price FROM chitiethoadon WHERE invoice_id = %s"
            cursor.execute(query_products, (invoice_id,))
            products = cursor.fetchall()

            cursor.close()
            connection.close()

            with open(f'invoice_{invoice_id}.txt', 'w', encoding='utf-8') as f:
                f.write(f"Hóa đơn số: {invoice_id}\n")
                f.write(f"Tên khách hàng: {kh_name}\n")
                f.write(f"Số điện thoại: {kh_phone}\n")
                f.write(f"Địa chỉ: {kh_addr}\n")
                f.write(f"Ngày hóa đơn: {invoice_date}\n")
                f.write(f"Tổng số tiền: {tt_amount}\n\n")
                f.write("Danh sách sản phẩm:\n")
                f.write(f"{'Mã SP':<10}{'Tên SP':<30}{'Hành động':<15}{'Số lượng':<10}{'Giá':<10}\n")
                for product in products:
                    product_id, product_name, action, quantity, price = product
                    f.write(f"{product_id:<10}{product_name:<30}{action:<15}{quantity:<10}{price:<10}\n")
                    
            self.record_act_epl(self.ui.label_Username.text(), self.ui.label_Name.text(), f'In lại hoá đơn {invoice_id}')
            
            self.choose_pd.load_data()        
            QMessageBox.information(self, "Thông báo", f"Hóa đơn đã được in lại thành công.")
            
        except mysql.connector.Error as err:
            QMessageBox.critical(self, "Lỗi", f"Đã xảy ra lỗi: {err}")

    def check_update_kh(self):
        row = self.ui.Table_Hd.currentRow()
        
        kh_name_old = self.ui.Table_Hd.item(row, 0).text()
        kh_name = self.ui.Kh_name.text()
        kh_phone = self.ui.Kh_phone.text()
        kh_addr = self.ui.Kh_Addr.text()
        
        if row == -1 or not kh_name or not kh_phone or not kh_addr:
            QMessageBox.warning(self, "Lỗi", "Không có thông tin để thay đổi")
            return

        try:
            connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="qlch"
            )
            cursor = connection.cursor()

            cursor.execute("""
                        UPDATE hoadon 
                        SET cus_name = %s, phone_num = %s, addr = %s 
                        WHERE cus_name = %s
                        """, (kh_name, kh_phone, kh_addr, kh_name_old))
            connection.commit()

            cursor.close()
            connection.close()
            
            self.ui.Kh_name.setText("")
            self.ui.Kh_phone.setText("")
            self.ui.Kh_Addr.setText("")

            self.load_hd()
            self.load_sell()
            self.load_rent()
            
            self.record_act_epl(self.ui.label_Username.text(), self.ui.label_Name.text(), 'Đã cập nhật thông tin khách hàng ')
            
            QMessageBox.information(self, "Thông báo", "Cập nhật thành công")

        except mysql.connector.Error as err:
            QMessageBox.critical(self, "Database Lỗi", f"Lỗi: {err}")
        except Exception as e:
            QMessageBox.critical(self, "Lỗi", str(e))

    def check_delete_hd(self):
        row = self.ui.Table_Hd.currentRow()
        
        kh_name = self.ui.Table_Hd.item(row, 0).text()
        kh_phone = self.ui.Table_Hd.item(row, 1).text()
        kh_addr = self.ui.Table_Hd.item(row, 2).text()
        invoice_date = self.ui.Table_Hd.item(row, 3).text()
        total_amount = self.ui.Table_Hd.item(row, 4).text()
        
        if row == -1 or not kh_name or not kh_phone or not kh_addr:
            QMessageBox.critical(self, "Lỗi", "Vui lòng chọn đơn để xóa.")
            return
        
        try:
            # Xóa sản phẩm từ cơ sở dữ liệu
            connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="qlch"
            )

            cursor = connection.cursor()
            
            query1 = ("SELECT invoice_id FROM hoadon WHERE cus_name = %s AND phone_num = %s AND addr = %s AND invoice_date = %s AND total_amount = %s")
            cursor.execute(query1, (kh_name, kh_phone, kh_addr, invoice_date, total_amount))
            result = cursor.fetchone()
            
            if not result:
                QMessageBox.critical(self, "Lỗi", "Không tìm thấy hóa đơn.")
                cursor.close()
                connection.close()
                return

            invoice_id = result[0]
                
            query2 = "DELETE FROM hoadon WHERE invoice_id = %s"
            cursor.execute(query2, (invoice_id,))
            connection.commit()


            cursor.close()
            connection.close()

            self.load_hd()
            self.load_sell()
            self.load_rent()
            self.ui.Table_Hd_2.setRowCount(0)
            self.choose_pd.load_data()
            
            self.record_act_epl(self.ui.label_Username.text(), self.ui.label_Name.text(), f'Đã xoá hoá đơn {invoice_id}')
            
            QMessageBox.information(self, "Thông báo", "Xóa đơn hàng thành công")
            
            self.ui.Kh_name.setText("")
            self.ui.Kh_phone.setText("")
            self.ui.Kh_Addr.setText("")

        except mysql.connector.Error as err:
            QMessageBox.critical(self, "Database Lỗi", f"Lỗi: {err}")
        except Exception as e:
            QMessageBox.critical(self, "Lỗi", str(e))

    def clear(self):
        self.ui.Table_Hd_2.setRowCount(0)
        self.ui.Table_Sp.setRowCount(0)
        self.choose_pd.cl_tb_choosed()
        self.ui.Tt_price.clear()
        
        self.ui.Kh_name.setText("")
        self.ui.Kh_phone.setText("")
        self.ui.Kh_Addr.setText("")
        
        self.ui.label_st.hide()
        self.ui.label_end.hide()
        self.ui.Rent_St.hide()
        self.ui.Rent_End.hide()   
        self.ui.Btn_Save.hide()
        
    # phần của page2 -----------------------------------------------------------------------------------
    def load_genre(self):
        # Kết nối với cơ sở dữ liệu MySQL
        self.db_connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="qlch"
        )
        cursor = self.db_connection.cursor()
        # Thực hiện truy vấn để lấy dữ liệu từ bảng lớp học
        cursor.execute("SELECT ten_theloai FROM theloai")
        rows = cursor.fetchall()
        # Xóa dữ liệu cũ trong ComboBox trước khi thêm dữ liệu mới
        self.ui.Genre.clear()
        # Thêm dữ liệu vào ComboBox
        for row in rows:
            self.ui.Genre.addItem(row[0])
        cursor.close()
        
    def load_pub(self):
        # Kết nối với cơ sở dữ liệu MySQL
        self.db_connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="qlch"
        )
        cursor = self.db_connection.cursor()
        # Thực hiện truy vấn để lấy dữ liệu từ bảng lớp học
        cursor.execute("SELECT ten_nhaph FROM nhaphathanh")
        rows = cursor.fetchall()
        # Xóa dữ liệu cũ trong ComboBox trước khi thêm dữ liệu mới
        self.ui.Pub.clear()
        # Thêm dữ liệu vào ComboBox
        for row in rows:
            self.ui.Pub.addItem(row[0])
        cursor.close()
        
    def load_auth(self):
        # Kết nối với cơ sở dữ liệu MySQL
        self.db_connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="qlch"
        )
        cursor = self.db_connection.cursor()
        # Thực hiện truy vấn để lấy dữ liệu từ bảng lớp học
        cursor.execute("SELECT ten_tacgia FROM tacgia")
        rows = cursor.fetchall()
        # Xóa dữ liệu cũ trong ComboBox trước khi thêm dữ liệu mới
        self.ui.Author.clear()
        # Thêm dữ liệu vào ComboBox
        for row in rows:
            self.ui.Author.addItem(row[0])
        cursor.close()
    
    def load_data(self):
        try:
            connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="qlch"
            )

            cursor = connection.cursor()

            # Thực hiện truy vấn join để lấy thông tin từ các bảng thích hợp
            cursor.execute("""
                SELECT sp.product_id, tl.ten_theloai, nph.ten_nhaph, tg.ten_tacgia, sp.hinhanh, sp.tensanpham, sp.price, sp.status
                FROM sanpham sp
                LEFT JOIN theloai tl ON sp.genre_id = tl.genre_id
                LEFT JOIN nhaphathanh nph ON sp.pub_id = nph.pub_id
                LEFT JOIN tacgia tg ON sp.auth_id = tg.auth_id
            """)
            results = cursor.fetchall()

            self.ui.Table_sanpham.setRowCount(len(results))

            for row_num, row_data in enumerate(results):
                for col_num, data in enumerate(row_data):
                    if col_num == 4:  # Cột hình ảnh
                        # Hiển thị hình ảnh trong cột
                        pixmap = QPixmap(data)
                        item = QTableWidgetItem()
                        item.setData(Qt.DecorationRole, pixmap.scaledToHeight(100, Qt.SmoothTransformation))
                        item.setData(Qt.UserRole, data)  # Thêm đường dẫn vào UserRole
                    else:
                        item = QTableWidgetItem(str(data))
                    item.setFlags(item.flags() & ~Qt.ItemIsEditable)  # Đặt các ô không thể chỉnh sửa
                    self.ui.Table_sanpham.setItem(row_num, col_num, item)

            cursor.close()
            connection.close()

        except mysql.connector.Error as err:
            print(f"Lỗi: {err}")

    def select_product(self, row, column):
        self.ui.lineEdit_ProductID.setText(self.ui.Table_sanpham.item(row, 0).text())
        self.ui.Genre.setCurrentText(self.ui.Table_sanpham.item(row, 1).text())
        self.ui.Pub.setCurrentText(self.ui.Table_sanpham.item(row, 2).text())
        self.ui.Author.setCurrentText(self.ui.Table_sanpham.item(row, 3).text())
        self.ui.lineEdit_ProductName.setText(self.ui.Table_sanpham.item(row, 5).text())
        image_path = self.ui.Table_sanpham.item(row, 4).data(Qt.UserRole)  # Lấy đường dẫn từ UserRole
        self.ui.lineEdit_ImagePath.setText(image_path)
        self.ui.lineEdit_Price.setText(self.ui.Table_sanpham.item(row, 6).text())
        # status_text = self.ui.Table_sanpham.item(row, 7).text()
        
    def check_update(self):
        pd_id = self.ui.lineEdit_ProductID.text()
        pd_genre = self.ui.Genre.currentText()
        pd_pub = self.ui.Pub.currentText()
        pd_auth = self.ui.Author.currentText()
        pd_name = self.ui.lineEdit_ProductName.text()
        pd_price = self.ui.lineEdit_Price.text()
        pd_image = self.ui.lineEdit_ImagePath.text()
        
        row = self.ui.Table_sanpham.currentRow()
        if row == -1 or not all([pd_id, pd_genre, pd_pub, pd_auth, pd_name, pd_price, pd_image]):
            QMessageBox.critical(self, "Lỗi", "Chưa chọn sản phẩm cần cập nhật.")
            return

        selected_pd_id = self.ui.Table_sanpham.item(row, 0).text()
        current_image_path = self.ui.Table_sanpham.item(row, 4).data(Qt.UserRole)  # Lấy đường dẫn từ UserRole hiện tại

        # Thư mục đích để lưu hình ảnh
        dest_dir = r"E:\hoc\python\baitaplon\resources\pic\product_image"

        # Đảm bảo thư mục đích tồn tại
        if not os.path.exists(dest_dir):
            os.makedirs(dest_dir)

        # Hàm để tạo tên mới cho tập tin ảnh
        def get_new_image_name():
            existing_files = os.listdir(dest_dir)
            existing_numbers = [
                int(f[2:-4]) for f in existing_files if f.startswith("sp") and f.endswith(".jpg") and f[2:-4].isdigit()
            ]
            if existing_numbers:
                new_number = max(existing_numbers) + 1
            else:
                new_number = 1
            return f"sp{new_number}.jpg"

        # Chỉ đổi tên và di chuyển ảnh nếu đường dẫn ảnh mới khác với đường dẫn ảnh hiện tại
        if pd_image != current_image_path:
            new_image_name = get_new_image_name()  # Tạo tên mới cho tập tin ảnh
            new_image_path = os.path.join(dest_dir, new_image_name)  # Đường dẫn mới cho ảnh

            try:
                # Xóa ảnh cũ
                if os.path.exists(current_image_path):
                    os.remove(current_image_path)
                
                # Di chuyển và đổi tên ảnh mới
                shutil.copy(pd_image, new_image_path)
                # Cập nhật đường dẫn hình ảnh trong cơ sở dữ liệu
                pd_image = new_image_path
            except Exception as e:
                QMessageBox.critical(self, "Lỗi", str(e))
                return
        else:
            pd_image = current_image_path  # Giữ nguyên đường dẫn ảnh hiện tại nếu không thay đổi

        try:
            # Kết nối cơ sở dữ liệu và cập nhật thông tin sản phẩm
            connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="qlch"
            )

            cursor = connection.cursor()
            # Sử dụng new_product_id trong lệnh truy vấn UPDATE
            # Truy vấn để lấy genre_id từ tên thể loại
            cursor.execute("SELECT genre_id FROM theloai WHERE ten_theloai = %s", (pd_genre,))
            genre_id = cursor.fetchone()[0]

            # Truy vấn để lấy pub_id từ tên nhà phát hành
            cursor.execute("SELECT pub_id FROM nhaphathanh WHERE ten_nhaph = %s", (pd_pub,))
            pub_id = cursor.fetchone()[0]

            # Truy vấn để lấy auth_id từ tên tác giả
            cursor.execute("SELECT auth_id FROM tacgia WHERE ten_tacgia = %s", (pd_auth,))
            auth_id = cursor.fetchone()[0]
            
            query = """
                    UPDATE sanpham
                    SET product_id = %s, genre_id = %s, pub_id = %s, auth_id = %s, tensanpham = %s, hinhanh = %s, price = %s
                    WHERE product_id = %s
                    """
            cursor.execute(query, (pd_id, genre_id, pub_id, auth_id, pd_name, pd_image, pd_price, selected_pd_id))
            connection.commit()

            cursor.close()
            connection.close()

            self.load_data()  # Tải lại dữ liệu sau khi lưu
            self.load_data_inv()
            
            self.ui.lineEdit_ProductID.setText("")
            self.ui.Genre.setCurrentIndex(-1)  # Đặt thể loại về trạng thái không có mục nào được chọn
            self.ui.Pub.setCurrentIndex(-1)
            self.ui.Author.setCurrentIndex(-1)
            self.ui.lineEdit_ProductName.setText("")
            self.ui.lineEdit_Price.setText("")
            self.ui.lineEdit_ImagePath.setText("")
            
            self.record_act_epl(self.ui.label_Username.text(), self.ui.label_Name.text(),f'cập nhật sản phẩm {pd_name} với mã "{pd_id}"')
            
            QMessageBox.information(self, "Thông báo", "Cập nhật thành công")
            
        except mysql.connector.Error as err:
            QMessageBox.critical(self, "Database Lỗi", f"Lỗi: {err}")
        except Exception as e:
            QMessageBox.critical(self, "Lỗi", str(e))

    def check_delete(self):
        pd_id = self.ui.lineEdit_ProductID.text()
        pd_genre = self.ui.Genre.currentText()
        pd_pub = self.ui.Pub.currentText()
        pd_auth = self.ui.Author.currentText()
        pd_name = self.ui.lineEdit_ProductName.text()
        pd_price = self.ui.lineEdit_Price.text()
        pd_image = self.ui.lineEdit_ImagePath.text()
        
        row = self.ui.Table_sanpham.currentRow()
        if row == -1 or not all([pd_id, pd_genre, pd_pub, pd_auth, pd_name, pd_price, pd_image]):
            QMessageBox.critical(self, "Lỗi", "Chưa chọn sản phẩm cần xoá.")
            return
        
        # Lấy thông tin sản phẩm
        pd_id = self.ui.Table_sanpham.item(row, 0).text()
        pd_image_path = self.ui.Table_sanpham.item(row, 4).data(Qt.UserRole)  # Lấy đường dẫn ảnh từ UserRole

        try:
            # Xóa ảnh từ thư mục
            if os.path.exists(pd_image_path):
                os.remove(pd_image_path)

            # Xóa sản phẩm từ cơ sở dữ liệu
            connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="qlch"
            )

            cursor = connection.cursor()
            query1 = "DELETE FROM sanpham WHERE product_id = %s"
            cursor.execute(query1, (pd_id,))
            connection.commit()
            
            query2 = "DELETE FROM tonkho WHERE product_id = %s"
            cursor.execute(query2, (pd_id,))
            connection.commit()

            cursor.close()
            connection.close()

            self.load_data()  # Tải lại dữ liệu sau khi xóa
            
            self.ui.lineEdit_ProductID.setText("")
            self.ui.Genre.setCurrentIndex(-1)  # Đặt thể loại về trạng thái không có mục nào được chọn
            self.ui.Pub.setCurrentIndex(-1)
            self.ui.Author.setCurrentIndex(-1)
            self.ui.lineEdit_ProductName.setText("")
            self.ui.lineEdit_Price.setText("")
            self.ui.lineEdit_ImagePath.setText("")

            QMessageBox.information(self, "Thông báo", "Xóa sản phẩm thành công")
            
        except mysql.connector.Error as err:
            QMessageBox.critical(self, "Database Lỗi", f"Lỗi: {err}")
        except Exception as e:
            QMessageBox.critical(self, "Lỗi", str(e))

    def select_image(self):
        # Thực hiện chức năng chọn hình ảnh từ hệ thống
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file_path, _ = QFileDialog.getOpenFileName(self, "Chọn ảnh", "", "Image Files (*.png *.jpg *.jpeg *.bmp *.gif)", options=options)
        if file_path:
            self.ui.lineEdit_ImagePath.setText(file_path)

    # phần của page3 -----------------------------------------------------------------------------------    
    def load_data_bk(self):
        try:
            connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="qlch"
            )

            cursor = connection.cursor()
            cursor.execute("""
                SELECT sp.tensanpham, tk.quantity
                FROM tonkho tk
                LEFT JOIN sanpham sp ON tk.product_id = sp.product_id
            """)
            results = cursor.fetchall()

            self.ui.Table_b_keeping.setRowCount(len(results))

            for row_num, row_data in enumerate(results):
                for col_num, data in enumerate(row_data):
                    item = QTableWidgetItem(str(data))
                    item.setFlags(item.flags() & ~Qt.ItemIsEditable)  # Đặt các ô không thể chỉnh sửa
                    self.ui.Table_b_keeping.setItem(row_num, col_num, item)

            cursor.close()
            connection.close()

        except mysql.connector.Error as err:
            print(f"Lỗi: {err}")
    
    #thêm nếu muốn hiện số ở thanh số lượng 
    # def select_bk(self, row, column):
    #     self.ui.Bk_sl.setText(self.ui.Table_b_keeping.item(row, 1).text())

    def check_update_bk(self):
        tk_sl = self.ui.Bk_sl.text()
        
        row = self.ui.Table_b_keeping.currentRow()
        if row == -1 or not all([tk_sl]):
            QMessageBox.warning(self,"Thiếu","Chưa chọn và thêm số lượng sản phẩm.")
            return
        
        tk_id = self.ui.Table_b_keeping.item(row, 0).text()
        
        try:
            # Kết nối cơ sở dữ liệu và cập nhật thông tin sản phẩm
            connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="qlch"
            )

            cursor = connection.cursor()
            # Sử dụng new_product_id trong lệnh truy vấn UPDATE
            cursor.execute("SELECT product_id FROM sanpham WHERE tensanpham = %s", (tk_id,))
            product_id = cursor.fetchone()[0]

            # Cập nhật số lượng trong bảng tonkho
            query1 = """UPDATE tonkho SET product_id = %s, quantity = quantity + %s WHERE product_id = %s """
            cursor.execute(query1, (product_id, tk_sl, product_id))
            connection.commit()

            cursor.close()
            connection.close()

            self.load_data_bk()
            self.load_data()
            self.choose_pd.load_data()
            self.ui.Bk_sl.setText("")
            
            self.record_act_epl(self.ui.label_Username.text(), self.ui.label_Name.text(), f'Đã thêm {tk_sl} cuốn của "{tk_id}"')
            
            QMessageBox.information(self, "Thông báo", "Cập nhật thành công")
            
        except mysql.connector.Error as err:
            QMessageBox.critical(self, "Database Lỗi", f"Lỗi: {err}")
        except Exception as e:
            QMessageBox.critical(self, "Lỗi", str(e))
    
    # phần của page4 -----------------------------------------------------------------------------------
    def load_sell(self):
        try:
            connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="qlch"
            )

            cursor = connection.cursor()
            cursor.execute("SELECT product_id, pd_name, quantity, price, transaction_type FROM chitiethoadon WHERE transaction_type IN ('Mua')")
            results = cursor.fetchall()

            self.ui.Table_sell.setRowCount(len(results))

            for row_num, row_data in enumerate(results):
                for col_num, data in enumerate(row_data):
                    item = QTableWidgetItem(str(data))
                    item.setFlags(item.flags() & ~Qt.ItemIsEditable)  # Đặt các ô không thể chỉnh sửa
                    self.ui.Table_sell.setItem(row_num, col_num, item)

            cursor.close()
            connection.close()

        except mysql.connector.Error as err:
            print(f"Lỗi: {err}")
            
    # phần của page5 -----------------------------------------------------------------------------------
    def select_rent(self, row, column):
        status = self.ui.Table_rent.item(row, 6).text()
        if status == "Đã trả":
            self.ui.Rent_st.setCurrentText("Đã trả")
        else:
            self.ui.Rent_st.setCurrentIndex(-1)

    def load_rent(self):
        try:
            connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="qlch"
            )

            cursor = connection.cursor()
            cursor.execute("SELECT invoice_id, pd_name, quantity, price, borrow_date, return_date, status_sp, transaction_type FROM chitiethoadon WHERE transaction_type IN ('Thuê')")
            results = cursor.fetchall()

            self.ui.Table_rent.setRowCount(len(results))

            for row_num, row_data in enumerate(results):
                for col_num, data in enumerate(row_data):
                    item = QTableWidgetItem(str(data))
                    item.setFlags(item.flags() & ~Qt.ItemIsEditable)  # Đặt các ô không thể chỉnh sửa
                    self.ui.Table_rent.setItem(row_num, col_num, item)

            cursor.close()
            connection.close()

        except mysql.connector.Error as err:
            print(f"Lỗi: {err}")

    def upd_rent(self):
        stt_rent = self.ui.Rent_st.currentText()
        
        row = self.ui.Table_rent.currentRow()
        if row == -1 or stt_rent == -1:
            QMessageBox.warning(self,"Lỗi", "Chưa cập nhật trạng thái")
            return
        
        try:
            # Kết nối cơ sở dữ liệu và cập nhật thông tin sản phẩm
            connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="qlch"
            )
            cursor = connection.cursor()
            
            invoice_id = self.ui.Table_rent.item(row, 0).text()
            
            cursor.execute("SELECT detail_id, product_id, quantity, status_sp, transaction_type FROM chitiethoadon WHERE invoice_id = %s AND transaction_type = 'Thuê'", (invoice_id,))
            results = cursor.fetchall()
            
            if results:
                for result in results:
                    detail_id = result[0]
                    product_id = result[1]
                    quantity = result[2]
                    status_sp = result[3]
                    
                    if status_sp == 'Đã trả':
                        continue
                    
                    query1 = """
                            UPDATE chitiethoadon
                            SET status_sp = %s
                            WHERE detail_id = %s AND transaction_type = 'Thuê'
                            """
                    cursor.execute(query1, (stt_rent, detail_id))
                    
                    query2 = """
                            UPDATE tonkho
                            SET quantity = quantity + %s
                            WHERE product_id = %s
                            """
                    cursor.execute(query2, (quantity, product_id))
                    connection.commit()
            
            cursor.close()
            connection.close()

            self.load_rent()
            self.ui.Rent_st.setCurrentIndex(-1)
            self.choose_pd.load_data()
            
            self.record_act_epl(self.ui.label_Username.text(), self.ui.label_Name.text(), f'Cập nhật trạng thái "{stt_rent}" của đơn chi tiết số "{invoice_id}"')
            
            QMessageBox.information(self, "Thông báo", "Cập nhật thành công")

        except mysql.connector.Error as err:
            QMessageBox.critical(self, "Database Lỗi", f"Lỗi: {err}")
        except Exception as e:
            QMessageBox.critical(self, "Lỗi", str(e))
        
    # phần của page6 -----------------------------------------------------------------------------------
    # ------------------------------------hiện tại chưa có phần báo cáo---------------------------------
    
# CHOOSEPD
class Choose_Pd(QMainWindow):
    def __init__(self, mainepl):
        super().__init__()
        self.ui = Ui_Choose_sp()
        self.ui.setupUi(self)
        
        self.mainepl = mainepl
        self.all_products = []
        self.selected_products = []

        # Ẩn các widget khi khởi động
        self.ui.pd_buy_rent.hide()
        self.ui.spinBox_quantity.hide()
        self.ui.pd_name.hide()
        self.ui.pd_price.hide()
        self.ui.pd_del.hide()

        # Bảng 1
        self.ui.Search.textChanged.connect(self.search_pd)
        self.ui.Btn_Buy.clicked.connect(lambda: self.buy_or_rent("Mua"))
        self.ui.Btn_Rent.clicked.connect(lambda: self.buy_or_rent("Thuê"))
        
        self.ui.tb_choose.setColumnCount(2)
        self.ui.tb_choose.horizontalHeader().setVisible(False)
        self.ui.tb_choose.verticalHeader().setVisible(False)
        self.ui.tb_choose.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.ui.tb_choose.verticalHeader().setDefaultSectionSize(100)
        
        # Bảng 2
        self.ui.tb_choosed.setColumnCount(1)
        self.ui.tb_choosed.horizontalHeader().setVisible(False)
        self.ui.tb_choosed.verticalHeader().setVisible(False)
        self.ui.tb_choosed.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.ui.tb_choosed.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.tb_choosed.verticalHeader().setDefaultSectionSize(100)  # Tăng chiều cao của dòng
        
        self.ui.tb_choose.setColumnWidth(0, 255)
        self.ui.tb_choose.setColumnWidth(1, 252)
        
        self.load_data()
        
    def closeEvent(self, event):
        if self.mainepl.isVisible():
            self.mainepl.close()
        event.accept()

    def check_inventory(self, product_id, quantity):
        try:
            connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="qlch"
            )
            cursor = connection.cursor()

            # Truy vấn số lượng tồn kho
            cursor.execute("""
                SELECT quantity 
                FROM tonkho 
                WHERE product_id = %s
            """, (product_id,))
            result = cursor.fetchone()

            cursor.close()
            connection.close()

            if result and result[0] >= quantity:
                return True
            else:
                return False

        except mysql.connector.Error as err:
            print(f"Lỗi: {err}")
            return False

    # def update_inventory(self, product_id, quantity_change):
    #     try:
    #         connection = mysql.connector.connect(
    #             host="localhost",
    #             user="root",
    #             password="",
    #             database="qlch"
    #         )
    #         cursor = connection.cursor()

    #         # Trừ số lượng tồn kho
    #         cursor.execute("""
    #             UPDATE tonkho 
    #             SET quantity = quantity - %s 
    #             WHERE product_id = %s
    #         """, (quantity_change, product_id))

    #         connection.commit()

    #         cursor.close()
    #         connection.close()

    #     except mysql.connector.Error as err:
    #         print(f"Lỗi: {err}")    
    
    def load_data(self):
        try:
            connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="qlch"
            )
            cursor = connection.cursor()

            cursor.execute("""
                SELECT sp.product_id, tl.ten_theloai, nph.ten_nhaph, tg.ten_tacgia, sp.hinhanh, sp.tensanpham, sp.price, sp.status, tk.quantity
                FROM sanpham sp
                LEFT JOIN theloai tl ON sp.genre_id = tl.genre_id
                LEFT JOIN nhaphathanh nph ON sp.pub_id = nph.pub_id
                LEFT JOIN tacgia tg ON sp.auth_id = tg.auth_id
                LEFT JOIN tonkho tk ON sp.product_id = tk.product_id
            """)
            results = cursor.fetchall()
            self.all_products = results

            self.update_tb(results)

            cursor.close()
            connection.close()

        except mysql.connector.Error as err:
            print(f"Lỗi: {err}")

    def update_tb(self, products):
        self.ui.tb_choose.clearContents()
        self.ui.tb_choose.setRowCount(len(products))

        if not products:
            self.ui.tb_choose.setRowCount(1)
            no_result_item = QTableWidgetItem("Không có sản phẩm với tên bạn tìm kiếm")
            no_result_item.setTextAlignment(Qt.AlignCenter)
            self.ui.tb_choose.setItem(0, 0, no_result_item)
            self.ui.tb_choose.setSpan(0, 0, 1, 2)
        else:
            self.ui.tb_choose.setSpan(0, 0, 1, 1)
            self.ui.tb_choose.setSpan(0, 1, 1, 1)
            
            for row_num, row_data in enumerate(products):
                product_info = (
                    f"Tên sản phẩm: {row_data[5]}\n"
                    f"Mã sản phẩm: {row_data[0]}\n"
                    f"Tên tác giả: {row_data[3]}\n"
                    f"Thể loại: {row_data[1]}\n"
                    f"Số lượng: {row_data[8]}\n"
                    f"Nhà phát hành: {row_data[2]}\n"
                    f"Giá: {row_data[6]} VND"
                )
                info_item = QTableWidgetItem(product_info)
                info_item.setFlags(info_item.flags() & ~Qt.ItemIsEditable)
                self.ui.tb_choose.setItem(row_num, 0, info_item)

                image_path = row_data[4]
                pixmap = QPixmap(image_path)
                image_item = QTableWidgetItem()
                image_item.setData(Qt.DecorationRole, pixmap.scaledToHeight(100, Qt.SmoothTransformation))
                image_item.setData(Qt.UserRole, image_path)
                image_item.setFlags(image_item.flags() & ~Qt.ItemIsEditable)
                self.ui.tb_choose.setItem(row_num, 1, image_item)

    def search_pd(self):
        search_text = self.ui.Search.text().lower()
        filtered_products = [
            product for product in self.all_products
            if search_text in product[5].lower()
            or search_text in product[3].lower()
            or search_text in product[2].lower()
        ]
        self.update_tb(filtered_products)

    # def buy_or_rent(self, action):
    #     selected_items = self.ui.tb_choose.selectedItems()
    #     if selected_items:
    #         selected_row = selected_items[0].row()
    #         product_info = self.ui.tb_choose.item(selected_row, 0).text()
    #         product_id = self.all_products[selected_row][0]
    #         product_price = self.all_products[selected_row][6]
    #         available_quantity = self.all_products[selected_row][8]  # Số lượng tồn kho

    #         # Kiểm tra số lượng tồn kho
    #         if available_quantity > 0:
    #             self.ui.pd_buy_rent.setText(f"Loại giao dịch: {action}")
    #             self.ui.pd_buy_rent.show()

    #             self.ui.pd_name.setText(f"Tên sản phẩm: {product_info.splitlines()[0].split(': ')[1]}")
    #             self.ui.pd_name.show()

    #             self.ui.pd_price.setText(f"Giá: {product_price} VND")
    #             self.ui.pd_price.show()

    #             self.ui.spinBox_quantity.setMaximum(available_quantity)
    #             self.ui.spinBox_quantity.setValue(1)
    #             self.ui.spinBox_quantity.show()

    #             self.ui.sl_choose.setValue(1)

    #             # Thêm sản phẩm vào bảng tb_choosed ngay lập tức
    #             self.add_pd_to_choosed(action, product_id, 1)

    #             # Ẩn các widget sau khi thêm sản phẩm vào bảng tb_choosed
    #             self.ui.pd_buy_rent.hide()
    #             self.ui.spinBox_quantity.hide()
    #             self.ui.pd_name.hide()
    #             self.ui.pd_price.hide()

    #             # Tính và hiển thị tổng số tiền
    #             self.updt_total_price()
    #         else:
    #             QMessageBox.warning(self, "Hết hàng", "Sản phẩm này đã hết hàng. Vui lòng chọn sản phẩm khác.")   
    
    def buy_or_rent(self, action):
        selected_items = self.ui.tb_choose.selectedItems()
        if selected_items:
            selected_row = selected_items[0].row()
            product_info = self.ui.tb_choose.item(selected_row, 0).text()
            product_id = self.all_products[selected_row][0]
            product_price = self.all_products[selected_row][6]

            # Kiểm tra số lượng tồn kho
            if not self.check_inventory(product_id, 1):
                QMessageBox.warning(self, "Thông báo", "Sản phẩm đã hết hàng, vui lòng chọn sản phẩm khác.")
                return

            self.ui.pd_buy_rent.setText(f"Loại giao dịch: {action}")
            self.ui.pd_buy_rent.show()

            self.ui.pd_name.setText(f"Tên sản phẩm: {product_info.splitlines()[0].split(': ')[1]}")
            self.ui.pd_name.show()

            self.ui.pd_price.setText(f"Giá: {product_price} VND")
            self.ui.pd_price.show()

            self.ui.spinBox_quantity.setValue(self.ui.sl_choose.value())
            self.ui.spinBox_quantity.show()
            
            self.ui.sl_choose.setValue(1)

            # Thêm sản phẩm vào bảng tb_choosed ngay lập tức
            self.add_pd_to_choosed(action, product_id)

            # Ẩn các widget sau khi thêm sản phẩm vào bảng tb_choosed
            self.ui.pd_buy_rent.hide()
            self.ui.spinBox_quantity.hide()
            self.ui.pd_name.hide()
            self.ui.pd_price.hide()

            # Tính và hiển thị tổng số tiền
            self.updt_total_price()             

    def add_pd_to_choosed(self, action, product_id):
        product_name = self.ui.pd_name.text().split(': ')[1]
        product_price = int(self.ui.pd_price.text().split(': ')[1].split()[0])
        quantity = self.ui.spinBox_quantity.value()

        found_existing = False

        # Kiểm tra nếu sản phẩm đã tồn tại trong bảng tb_choosed
        for row in range(self.ui.tb_choosed.rowCount()):
            frame = self.ui.tb_choosed.cellWidget(row, 0)
            if frame:
                pd_name = frame.findChild(QLabel, "pd_name").text().split(': ')[1]
                pd_id = frame.findChild(QLabel, "pd_id").text().split(': ')[1]
                pd_buy_rent = frame.findChild(QLabel, "pd_buy_rent").text().split(': ')[1]
                if pd_name == product_name and pd_buy_rent == action and pd_id == product_id:
                    spinBox_quantity = frame.findChild(QSpinBox, "spinBox_quantity")
                    existing_quantity = spinBox_quantity.value()
                    new_quantity = existing_quantity + quantity
                    spinBox_quantity.setValue(new_quantity)
                    total_price = product_price * new_quantity
                    frame.findChild(QLabel, "pd_price").setText(f"Giá: {total_price} VND")
                    found_existing = True
                    break

        # Nếu sản phẩm chưa tồn tại, thêm mới vào bảng tb_choosed
        if not found_existing:
            total_price = product_price * quantity
            self.add_to_choosed_tb(product_name, quantity, action, product_price, total_price, product_id)

        # Sau khi thêm sản phẩm, cập nhật tổng số tiền
        self.updt_total_price()

    def add_to_choosed_tb(self, product_name, quantity, action, product_price, total_price, product_id):
        row_position = self.ui.tb_choosed.rowCount()
        self.ui.tb_choosed.insertRow(row_position)

        frame = QFrame(self.ui.tb_choosed)
        frame.setFrameShape(QFrame.StyledPanel)
        frame.setFrameShadow(QFrame.Raised)
        frame.setStyleSheet(u"#frame.QFrame{\n"
                            "background-color: white; border: 1px solid #00C957;\n"
                            "}")
        grid_layout = QGridLayout(frame)

        pd_name = QLabel(frame)
        pd_name.setObjectName("pd_name")
        pd_name.setText(f"Tên sản phẩm: {product_name}")
        grid_layout.addWidget(pd_name, 0, 0)
        
        pd_id = QLabel(frame)
        pd_id.setObjectName("pd_id")
        pd_id.setText(f"   Mã SP: {product_id}")
        pd_id.setStyleSheet(u"#pd_id.QLabel{\n"
                            "border-left: 1px solid black;\n"
                            "}")
        grid_layout.addWidget(pd_id, 0, 1)

        pd_del = QPushButton(frame)
        pd_del.setObjectName("pd_del")
        pd_del.setIcon(QIcon(":/icon/resources/icon-pack/exit_icon.png"))  # Đặt icon cho nút xoá
        pd_del.setCursor(Qt.PointingHandCursor)
        pd_del.setFixedSize(21, 21)
        pd_del.setStyleSheet("QPushButton#pd_del { border: none; }")
        pd_del.clicked.connect(lambda: self.delete_pd(frame))  # Kết nối sự kiện click của nút xoá với phương thức delete_pd
        grid_layout.addWidget(pd_del, 0, 2)

        pd_buy_rent = QLabel(frame)
        pd_buy_rent.setObjectName("pd_buy_rent")
        pd_buy_rent.setText(f"Loại giao dịch: {action}")
        grid_layout.addWidget(pd_buy_rent, 1, 0, 1, 3)

        pd_price = QLabel(frame)
        pd_price.setObjectName("pd_price")
        pd_price.setText(f"Giá: {total_price} VND")
        grid_layout.addWidget(pd_price, 2, 0)

        spinBox_quantity = QSpinBox(frame)
        spinBox_quantity.setObjectName("spinBox_quantity")
        spinBox_quantity.setValue(quantity)
        spinBox_quantity.setFixedSize(61, 21)  # Thêm dòng này để chỉnh kích thước
        spinBox_quantity.valueChanged.connect(lambda: self.updt_pd_price(frame, product_price))
        spinBox_quantity.setStyleSheet(
            "QSpinBox {"
            "   border: 1px solid rgb(0, 170, 127);"
            "   padding: 2px;"
            "}"
            "QSpinBox::up-button {"
            "   subcontrol-origin: border;"
            "   subcontrol-position: top right;"
            "   width: 16px;"
            "}"
            "QSpinBox::down-button {"
            "   subcontrol-origin: border;"
            "   subcontrol-position: bottom right;"
            "   width: 16px;"
            "}"
            "QSpinBox::up-button:hover, QSpinBox::down-button:hover {"
            "   background: none;"
            "}"
        )
        grid_layout.addWidget(spinBox_quantity, 2, 1)

        frame.setLayout(grid_layout)
        self.ui.tb_choosed.setCellWidget(row_position, 0, frame)

        self.updt_total_price()
        self.update_table_sp()

    def updt_pd_price(self, frame, product_price):
        spinBox_quantity = frame.findChild(QSpinBox, "spinBox_quantity")
        quantity = spinBox_quantity.value()
        if quantity == 0:
            self.delete_pd(frame)
        else:
            total_price = product_price * quantity
            frame.findChild(QLabel, "pd_price").setText(f"Giá: {total_price} VND")
            self.updt_total_price()
            self.update_table_sp()

    def updt_total_price(self):
        total_price = 0
        for row in range(self.ui.tb_choosed.rowCount()):
            frame = self.ui.tb_choosed.cellWidget(row, 0)
            if frame:
                pd_price = frame.findChild(QLabel, "pd_price").text()
                total_price += int(pd_price.split(': ')[1].split()[0])

        self.ui.sum_price.setText(f"{total_price} VND")
        
        self.mainepl.update_total_price(total_price)

    def delete_pd(self, frame):
        for row in range(self.ui.tb_choosed.rowCount()):
            if self.ui.tb_choosed.cellWidget(row, 0) == frame:
                self.ui.tb_choosed.removeRow(row)
                break
        self.updt_total_price()
        self.update_table_sp()

    def update_table_sp(self):
        products = []
        for row in range(self.ui.tb_choosed.rowCount()):
            frame = self.ui.tb_choosed.cellWidget(row, 0)
            if frame:
                product_name = frame.findChild(QLabel, "pd_name").text().split(': ')[1]
                product_id = frame.findChild(QLabel, "pd_id").text().split(': ')[1]
                quantity = frame.findChild(QSpinBox, "spinBox_quantity").value()
                action = frame.findChild(QLabel, "pd_buy_rent").text().split(': ')[1]
                price = frame.findChild(QLabel, "pd_price").text().split(': ')[1].split()[0]
                products.append([product_id ,product_name, action, quantity, price])

        self.mainepl.update_table_sp(products)
        
    def cl_tb_choosed(self):
        self.ui.tb_choosed.setRowCount(0)
        self.ui.sum_price.clear()
              
# CHANGE PASS
class ChangePass(QWidget):
    def __init__(self, username):
        super().__init__()
        self.ui = Ui_ChangePass()
        self.ui.setupUi(self)
        
        self.username = username
        
        # Đưa window về trung tâm màn hình
        qr = self.frameGeometry()
        cp = self.screen().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
        
        ## XOÁ TITLEBAR
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        
        self.ui.label_Exit.mousePressEvent = self.close_window
        self.ui.pushButton.clicked.connect(self.change_password)
        
    def close_window(self, event):
        self.close()
        
    def change_password(self):
        current_password = self.ui.lineEdit.text()
        new_password = self.ui.lineEdit_2.text()
        confirm_new_password = self.ui.lineEdit_3.text()
        
        if not current_password or not new_password or not confirm_new_password:
            QMessageBox.warning(self, "Lỗi", "Nhập đầy đủ thông tin.")
            return

        try:
            connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="qlch"
            )

            cursor = connection.cursor()
            query = "SELECT password FROM users WHERE username = %s"
            cursor.execute(query, (self.username,))
            result = cursor.fetchone()

            if result:
                current_db_password = result[0]
                if current_password == current_db_password:
                    if new_password == confirm_new_password:
                        update_query = "UPDATE users SET password = %s WHERE username = %s"
                        cursor.execute(update_query, (new_password, self.username))
                        connection.commit()
                        QMessageBox.information(self, "Success", "Mật khẩu đã được cập nhật thành công!")
                        self.close()
                    else:
                        QMessageBox.warning(self, "Lỗi", "Mật khẩu mới không khớp!")
                else:
                    QMessageBox.warning(self, "Lỗi", "Mật khẩu hiện tại không đúng!")
            else:
                QMessageBox.warning(self, "Lỗi", "Người dùng không tồn tại!")

            cursor.close()
            connection.close()

        except mysql.connector.Error as err:
            QMessageBox.critical(self, "Lỗi Cơ sở dữ liệu", f"Lỗi: {err}")
        except Exception as e:
            QMessageBox.critical(self, "Lỗi", str(e))
            
        # # Kết nối đến cơ sở dữ liệu
        # self.connection = mysql.connector.connect(
        #     host="localhost",
        #     user="your_username",
        #     password="your_password",
        #     database="qlch"
        # )
        # self.cursor = self.connection.cursor()

        # # Kiểm tra mật khẩu hiện tại
        # query = "SELECT password FROM users WHERE username = %s"
        # self.cursor.execute(query, (self.username,))
        # result = self.cursor.fetchone()

        # if result:
        #     current_db_password = result[0]
        #     if current_password == current_db_password:
        #         if new_password == confirm_new_password:
        #             # Cập nhật mật khẩu mới vào cơ sở dữ liệu
        #             update_query = "UPDATE users SET password = %s WHERE username = %s"
        #             self.cursor.execute(update_query, (new_password, self.username))
        #             self.connection.commit()
        #             QMessageBox.information(self, "Success", "Password updated successfully!")
        #         else:
        #             QMessageBox.warning(self, "Warning", "New passwords do not match!")
        #     else:
        #         QMessageBox.warning(self, "Warning", "Incorrect current password!")
        # else:
        #     QMessageBox.warning(self, "Warning", "User not found!")

        # self.close()

# REPLACEPW
# class ReplacePass(QMainWindow):
#     def __init__(self, username):
#         super().__init__()
#         self.ui = Ui_ReplacePw()
#         self.ui.setupUi(self)
#         self.username = username
        
#         ## XOÁ TITLEBAR
#         self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
#         self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        
#         self.ui.label_Exit.mousePressEvent = self.close_window
#         self.ui.Btn_rplpw.clicked.connect(self.change_password)
    
#     def close_window(self, event):
#         self.close()
        
#     def change_password(self):
#         new_password = self.ui.lineEdit.text()
#         cfpassword = self.ui.lineEdit_2.text()
        
#         if not new_password or not cfpassword:
#             QMessageBox.warning(self, "Lỗi", "Vui lòng nhập mật khẩu mới.")
#             return
#         elif new_password != cfpassword:
#             QMessageBox.warning(self, "Lỗi", "Mật khẩu không khớp.")
#             return
        
#         try:
#             connection = mysql.connector.connect(
#                 host="localhost",
#                 user="root",
#                 password="",
#                 database="qlch"
#             )

#             cursor = connection.cursor()

#             query_update_password = """
#                 UPDATE users SET password = %s WHERE username = %s
#             """
#             cursor.execute(query_update_password, (new_password, self.username))
#             connection.commit()

#             cursor.close()
#             connection.close()

#             QMessageBox.information(self, "Thông báo", "Đổi mật khẩu thành công.")
#             self.close()
#             self.login_window = Login()
#             self.login_window.show()

#         except mysql.connector.Error as err:
#             QMessageBox.critical(self, "Database Lỗi", f"Lỗi: {err}")
#         except Exception as e:
#             QMessageBox.critical(self, "Lỗi", f"Lỗi: {str(e)}")

# FORGOTPW
# class FogotPass(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.ui = Ui_ForgotPw()
#         self.ui.setupUi(self)
        
#         ## XOÁ TITLEBAR
#         self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
#         self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        
#         self.ui.label_Return.mousePressEvent = self.return_login
#         self.ui.label_Exit.mousePressEvent = self.close_window
#         self.ui.label_Login.mousePressEvent = self.return_login
        
#         self.ui.Btn_fgpw.clicked.connect(self.check_forgotpw)
        
#     def close_window(self, event):
#         self.close()
        
#     def return_login(self, event):
#         # self.hide()
#         self.close()
#         self.login_window = Login()
#         self.login_window.show()
        
#     def check_forgotpw(self):
#         forgotpw = self.ui.lineEdit.text()
        
#         if not forgotpw:
#             QMessageBox.warning(self, "Lỗi", "Thiếu thông tin")
#             return
        
#         try:
#             # Kết nối cơ sở dữ liệu
#             connection = mysql.connector.connect(
#                 host="localhost",
#                 user="root",
#                 password="",
#                 database="qlch"
#             )

#             cursor = connection.cursor()

#             query_check_user = """
#                 SELECT username FROM users WHERE username = %s OR email = %s
#             """
#             cursor.execute(query_check_user, (forgotpw, forgotpw))
#             result = cursor.fetchone()

#             if result:
#                 username = result[0]
#                 self.close()
#                 self.rpl_pass_window = ReplacePass(username)
#                 self.rpl_pass_window.show()
            
#             cursor.close()
#             connection.close()

#         except mysql.connector.Error as err:
#             QMessageBox.critical(self, "Database Lỗi", f"Lỗi: {err}")
#         except Exception as e:
#             QMessageBox.critical(self, "Lỗi", f"Lỗi: {str(e)}")
        
# SIGNIN
class Signin(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Signin()
        self.ui.setupUi(self)
        
        ## XOÁ TITLEBAR
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        
        self.ui.label_Return.mousePressEvent = self.return_login
        self.ui.label_Exit.mousePressEvent = self.close_window
        self.ui.lineEdit_3.setEchoMode(QLineEdit.EchoMode.Password)
        self.ui.lineEdit_4.setEchoMode(QLineEdit.EchoMode.Password)
        self.ui.label_Login.mousePressEvent = self.return_login
        self.ui.Btn_Signin.clicked.connect(self.check_signin)
        
    def close_window(self, event):
        self.close()
        
    def return_login(self, event):
        # self.hide()
        self.close()
        self.login_window = Login()
        self.login_window.show()
        
    def check_signin(self):
        email = self.ui.lineEdit.text()
        username = self.ui.lineEdit_2.text()
        password = self.ui.lineEdit_3.text()
        cfpassword = self.ui.lineEdit_4.text()
        
        if not email or not username or not password or not cfpassword:
            QMessageBox.warning(self, "Lỗi", "Thiếu thông tin")
            return
        elif password != cfpassword:
            QMessageBox.warning(self, "Lỗi", "Mật khẩu không khớp")
            return
        
        try:
            # Kết nối cơ sở dữ liệu
            connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="qlch"
            )

            cursor = connection.cursor()
            
            query_check_name_exist = "SELECT COUNT(*) FROM users WHERE username = %s"
            cursor.execute(query_check_name_exist, (username,))
            result_name_check = cursor.fetchone()
            if result_name_check[0] > 0:  # Nếu sản phẩm đã tồn tại
                QMessageBox.critical(self, "Lỗi", "Tên người dùng này đã tồn tại.")
                cursor.close()
                connection.close()
                return
            
            query = """
                    INSERT INTO users (username, email, password, role)
                    VALUES (%s, %s, %s, %s)
                    """
            cursor.execute(query, (username, email, password, 'Khách'))
            connection.commit()

            cursor.close()
            connection.close()

            QMessageBox.information(self, "Thông báo", "Đăng ký thành công")

        except mysql.connector.Error as err:
            QMessageBox.critical(self, "Database Lỗi", f"Lỗi: {err}")
        except Exception as e:
            QMessageBox.critical(self, "Lỗi", f"Lỗi: {str(e)}")

# LOGIN
class Login(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Login()
        self.ui.setupUi(self)
        
        self.ui.Rem_ckBox.hide()
        self.ui.label_ForgotPw.hide()
        # self.ui.label_Signin.hide()
        
        ## XOÁ TITLEBAR
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        
        self.ui.label_Exit.mousePressEvent = self.close_window
        self.ui.lineEdit_2.setEchoMode(QLineEdit.EchoMode.Password)
        self.ui.label_Signin.mousePressEvent = self.signin_window
        # self.ui.label_ForgotPw.mousePressEvent = self.forgotpw_window
        self.ui.pushButton.clicked.connect(self.check_login)
        
        k_enter = QShortcut(QKeySequence(Qt.Key_Return), self)
        k_enter.activated.connect(self.check_login)

        k_return = QShortcut(QKeySequence(Qt.Key_Enter), self)
        k_return.activated.connect(self.check_login)
        
    def close_window(self, event):
        self.close()
        
    def signin_window(self, event):
        self.hide()
        self.close()
        self.sigin_window = Signin()
        self.sigin_window.show()
        
    # def forgotpw_window(self, event):
    #     self.hide()
    #     self.close()
    #     self.forgot_window = FogotPass()
    #     self.forgot_window.show()
        
    def check_login(self):
        username_or_email = self.ui.lineEdit.text()
        password = self.ui.lineEdit_2.text()

        if not username_or_email or not password:
            QMessageBox.warning(self, "Đầu vào lỗi", "Nhập đầy đủ username/email và password.")
            return

        try:
            connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="qlch"
            )

            cursor = connection.cursor()
            query = """
            SELECT username, email, profile_image, role, name FROM users 
            WHERE (username = %s OR email = %s) AND password = %s
            """
            cursor.execute(query, (username_or_email, username_or_email, password))
            result = cursor.fetchone()

            if result:
                username, email, profile_image, role, name = result
                self.hide()
                
                if role == 'Admin':
                    self.main = MainAdmin(username, email, profile_image, name)
                elif role == 'Nhân viên':
                    self.main2 = Choose_Pd(None)
                    delay_timer = QTimer()
                    delay_timer.singleShot(2000, self.main2.show)
                    self.main = MainEmpl(username, email, profile_image, name, self.main2)
                    self.main2.mainepl = self.main
                self.main.show()
            else:
                QMessageBox.warning(self, "Đăng nhập thất bại", "Username/email hoặc mật khẩu không đúng.")
                self.ui.lineEdit_2.setText("")
                self.show()
                
            cursor.close()
            connection.close()

        except mysql.connector.Error as err:
            QMessageBox.critical(self, "Database Lỗi", f"Lỗi: {err}")
        except Exception as e:
            QMessageBox.critical(self, "Lỗi", str(e))

# SPLASH
class Splash(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Splash()
        self.ui.setupUi(self)

        ## UI ==> INTERFACE CODES
        ########################################################################

        ## XOÁ TITLEBAR
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        ## DROP SHADOW EFFECT
        self.shadow = QtWidgets.QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 60))
        self.ui.dropShadowFrame.setGraphicsEffect(self.shadow)

        ## QTIMER ==> START
        self.timer = QTimer()
        self.timer.timeout.connect(self.progress)
        # TIMER IN MILLISECONDS
        self.timer.start(35)

        ## SHOW ==> MAIN WINDOW
        ########################################################################
        self.show()
        ## ==> END ##

    ## ==> APP FUNCTIONS
    ########################################################################
    def progress(self):

        global counter

        # SET VALUE TO PROGRESS BAR
        self.ui.progressBar.setValue(counter)

        # CLOSE SPLASH SCREE AND OPEN APP
        if counter > 100:
            # STOP TIMER
            self.timer.stop()

            # SHOW MAIN WINDOW
            # self.main = Main()
            self.main.show()

            # CLOSE SPLASH SCREEN
            self.close()

        # INCREASE COUNTER
        counter += 1

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Login()
    window.show()
    sys.exit(app.exec())