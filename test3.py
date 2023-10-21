# # # import subprocess
# from pywinauto.application import Application
# import time


# # # # subprocess.run(r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\iTunes\iTunes.lnk")


# # import subprocess


# # # Mở iTunes bằng subprocess
# # # subprocess.run(r"C:\Program Files\iTunes\iTunes.exe")
# # app=Application(backend='uia').start(r"C:\Program Files\iTunes\iTunes.exe").connect(title='iTunes')
# # app.iTunes.print_control_identifiers()
# # # print("zzzzzzz: {app}")




import sys
from io import StringIO
from contextlib import redirect_stdout
from pywinauto import Application
import pywinauto
import pyautogui
import time
# Tạo một đối tượng StringIO để lưu trữ đầu ra
output = StringIO()


from pywinauto import Application
import time

class iTunesApp:
    def __init__(self):
        self.app = Application(backend='uia').start(r"C:\Program Files\iTunes\iTunes.exe").connect(title='iTunes', timeout =5)


    def account(self):
        try:
            return self.app.top_window().child_window(title="Account", control_type="MenuItem").wrapper_object()
        except Exception as e:
            print("Không tìm thấy:",e)
            return None   
    def view_my_account(self):
        try:
            return self.app.top_window().child_window(title="View My Account…", control_type="MenuItem").wrapper_object()
        except Exception as e:
            print("Không tìm thấy:",e)
            return None           
    def nhap_ID(self):
        try:    
            return self.app.top_window().child_window(title="Apple ID:", control_type="Edit").wrapper_object()
        except Exception as e:
            print("Không tìm thấy:",e)
            return None         
        
    # def print_control_identifiers(self):
    #     self.app.top_window().print_control_identifiers()
    def print_email(self):
        try:
            email_edit = self.app.top_window().child_window(auto_id="2", control_type="MenuItem").wrapper_object()
            email_title = email_edit.window_text()
            return email_title
        except Exception as e:
            print("Không tìm thấy icloud")
            return None

    def auto_ct(self, title, control_type, ctrl):
        try:
            control = self.app.top_window().child_window(title=title, control_type=control_type).wrapper_object()
            ctrl(control)  # Gọi hàm set_text_func để thiết lập giá trị cho control
            return control
        except Exception as e:
            print("Không tìm thấy:", e)
            return None
        
    def auto_id(self, auto_id, control_type, ctrl):
        try:
            control = self.app.top_window().child_window(auto_id=auto_id, control_type=control_type).wrapper_object()
            ctrl(control)  # Gọi hàm set_text_func để thiết lập giá trị cho control
            return control
        except Exception as e:
            print("Không tìm thấy:", e)
            return None
        
    def print_control_identifiers(self):
        top_window = self.app.top_window()
        for child_window in top_window.descendants():
            print(child_window.window_text())
            print(child_window.print_control_identifiers())
    
    

itunes_app = iTunesApp()


# itunes_app.print_control_identifiers()



# # text = itunes_app.auto_ct(title="OK", control_type="Button", ctrl=lambda control: control.window_text()) #OK k co mang
# print("Văn bản của cửa sổ là:", text)

# if text is not None and 'Make sure your network connection is active and try again' in text:
#     print("OK")
# elif text is None:
#     print("Giá trị text là None")
# else:
#     print("Chuỗi không tồn tại trong văn bản của cửa sổ")

# text = itunes_app.auto_id(auto_id="105", control_type="Text", ctrl=lambda control: control.window_text())

# if text and 'Make sure your network connection is active and try again' in text.window_text():
#     print("Mạng lõ")
#     itunes_app.auto_ct(title="OK", control_type="Button", ctrl=lambda control: control.click_input())
# else:
#     print("Chuỗi không tồn tại trong văn bản của cửa sổ")


# itunes_app.auto_ct(title="Continue", control_type="Button", ctrl=lambda control: control.click_input()) #AutomationId	-2092416608
# itunes_app.auto_ct(title="Account", control_type="MenuItem", ctrl=lambda control: control.click_input())
# print("Email trên itune là:", itunes_app.print_email())
# itunes_app.auto_ct(title="View My Account…", control_type="MenuItem", ctrl=lambda control: control.click_input())
# itunes_app.auto_ct(title="Apple ID:", control_type="Edit", ctrl=lambda control: control.set_edit_text("ozellalloyd1806@icloud.com"))
# itunes_app.auto_ct(title="Password:", control_type="Edit", ctrl=lambda control: control.set_edit_text("Zxcv1231233"))
# itunes_app.auto_ct(title="Sign In", control_type="Button", ctrl=lambda control: control.click_input())
itunes_app.auto_ct(title="Edit", control_type="Edit", ctrl=lambda control: control.click_input())











# itunes_app = iTunesApp()
# if itunes_app.account() is not None:
#     itunes_app.account().click_input()
# # time.sleep(2)
# if itunes_app.view_my_account() is not None:
#     itunes_app.view_my_account().click_input()
# # itunes_app.print_control_identifiers()
# ## itunes_app.nhap_ID().type_keys("ZASDSAJsads@icloud.com")
# # time.sleep(2)
# if itunes_app.nhap_ID() is not None:
#     itunes_app.nhap_ID().set_edit_text("ozellalloyd1806@icloud.com")
# app = Application(backend='uia').start(r"C:\Program Files\iTunes\iTunes.exe").connect(title='iTunes', timeout =10)

print("xong")
# print("Email trên itune là:", itunes_app.print_email())
# ...


# # for child in app.top_window().child_window().children():
# #     print(child)

# new_window = app.window(title='iTunes')  # Provide the actual title of the new window
# for child in new_window.children():
#     print(child)
# view_my_account_element = itunes_app.view_my_account()
# if view_my_account_element.exists():
#     # Nếu tồn tại, thực hiện click và in ra thông báo
#     view_my_account_element.click_input()
#     print("Đã click vào View My Account")
# else:
#     # Nếu không tồn tại, in ra thông báo
#     print("Không tìm thấy phần tử View My Account")


# main_window = app.window(title='iTunes')

# account.click_input()
# print("1")
# time.sleep(2)
# view_my_account.click_input()
# time.sleep(2)
# nhap_ID.type_keys("ZASDSAJsads@icloud.com")


# main_window = account

# with redirect_stdout(output):
#     main_window.print_control_identifiers()

# with open('itune1.txt', 'w') as f:
#     f.write(output.getvalue())

# print("Đã ghi đầu ra vào tệp itune1.txt")



# # import cv2
# # from pytesseract import pytesseract

# # pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

# # img = cv2.imread("img/temp.png")

# # words_in_image = pytesseract.image_to_string(img)

# # print(words_in_image)


# Khởi động hoặc kết nối với ứng dụng iTunes
# app = Application(backend='uia').connect(path=r"C:\Program Files\iTunes\iTunes.exe")

# # Đợi cho cửa sổ iTunes hiển thị
# main_window = app.window(title='iTunes')
# main_window.wait('visible', timeout=10)  # Đợi cho cửa sổ hiển thị trong 10 giây

# # Tìm và bấm vào MenuItem "Account"
# account_menu = main_window.child_window(title="Account", control_type="MenuItem")
# account_menu.click_input()



