import sys
import os
import json
import requests
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QTableWidget, QTableWidgetItem, QPushButton, QLineEdit, QMessageBox, QHeaderView
from PyQt5.QtCore import Qt, QTimer
from datetime import datetime
from plyer import notification

json_file_path = os.path.join(os.path.expanduser("~"), "Documents", "bot.json")


class TelegramBotUI(QWidget):
    def __init__(self):
        super().__init__()
        self.load_bot_info()
        self.initUI()
        self.last_update_id = None
        self.timer = QTimer()
        self.timer.timeout.connect(self.refresh_messages)
        self.timer.start(5000)

    def load_bot_info(self):
        try:
            with open(json_file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                self.token = data.get('token', "")
                self.chat_id = data.get('chat_id', "")
                self.notifications_enabled = data.get('notifications_enabled', True)
        except (FileNotFoundError, KeyError):
            self.token = ""
            self.chat_id = ""
            self.notifications_enabled = True

    def save_bot_info(self):
        data = {
            'token': self.token,
            'chat_id': self.chat_id,
            'notifications_enabled': self.notifications_enabled
        }
        with open(json_file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    def initUI(self):
        self.setWindowTitle("Telegram Bot UI")
        self.setGeometry(100, 100, 900, 500)
        self.setStyleSheet("background-color: #0d1117; color: #c9d1d9; font-family: 'Tahoma';")

        layout = QVBoxLayout()
        input_layout = QHBoxLayout()

        self.token_entry = QLineEdit(self.token)
        self.token_entry.setPlaceholderText("توکن بات")
        self.token_entry.setStyleSheet("QLineEdit { background-color: #333333; color: #ffffff; border-radius: 5px; padding: 5px; }")

        self.chat_id_entry = QLineEdit(self.chat_id)
        self.chat_id_entry.setPlaceholderText("Chat ID")
        self.chat_id_entry.setStyleSheet("QLineEdit { background-color: #333333; color: #ffffff; border-radius: 5px; padding: 5px; }")
        self.chat_id_entry.setFixedWidth(150)

        self.replace_token_button = QPushButton("جایگزینی توکن")
        self.replace_token_button.clicked.connect(self.replace_token)
        self.replace_token_button.setStyleSheet("background-color: #2C97F4; color: #ffffff; border-radius: 5px; padding: 5px;")

        self.notification_toggle_button = QPushButton("غیرفعال‌سازی اعلان‌ها" if self.notifications_enabled else "فعال‌سازی اعلان‌ها")
        self.notification_toggle_button.setStyleSheet("background-color: #2C97F4; color: #ffffff; border-radius: 5px; padding: 5px;")
        self.notification_toggle_button.clicked.connect(self.toggle_notifications)

        input_layout.addWidget(self.token_entry)
        input_layout.addWidget(self.chat_id_entry)
        input_layout.addWidget(self.replace_token_button)
        input_layout.addWidget(self.notification_toggle_button)

        self.message_entry = QLineEdit()
        self.message_entry.setPlaceholderText("پیام")
        self.message_entry.setStyleSheet("QLineEdit { background-color: #333333; color: #ffffff; border-radius: 5px; padding: 5px; }")
        self.message_entry.returnPressed.connect(self.send_message)

        self.send_button = QPushButton("ارسال")
        self.send_button.clicked.connect(self.send_message)
        self.send_button.setStyleSheet("background-color: #2C97F4; color: #ffffff; border-radius: 5px; padding: 5px;")

        button_layout = QHBoxLayout()
        button_layout.addWidget(self.message_entry)
        button_layout.addWidget(self.send_button)

        layout.addLayout(input_layout)
        layout.addLayout(button_layout)

        self.message_table = QTableWidget()
        self.message_table.setColumnCount(4)
        self.message_table.setHorizontalHeaderLabels(["Chat ID", "نام و نام خانوادگی", "زمان", "متن پیام"])
        self.message_table.horizontalHeader().setSectionResizeMode(3, QHeaderView.Stretch)
        self.message_table.setStyleSheet("QTableWidget { background-color: #2E323A; color: #ffffff; border: 1px solid #30363d; } QHeaderView::section { background-color: #161b22; color: #c9d1d9; padding: 5px; border: none; } QTableWidget::item { padding: 10px; border: none; text-align: right; }")
        self.message_table.setLayoutDirection(Qt.RightToLeft)

        layout.addWidget(self.message_table)
        self.setLayout(layout)

    def replace_token(self):
        self.token = self.token_entry.text()
        self.chat_id = self.chat_id_entry.text()
        self.message_table.setRowCount(0)
        self.last_update_id = None
        self.save_bot_info()
        self.refresh_messages()

    def toggle_notifications(self):
        self.notifications_enabled = not self.notifications_enabled
        self.notification_toggle_button.setText("فعال‌سازی اعلان‌ها" if not self.notifications_enabled else "غیرفعال‌سازی اعلان‌ها")
        self.save_bot_info()

    def send_message(self):
        chat_id = self.chat_id_entry.text()
        token = self.token_entry.text()
        message = self.message_entry.text()

        if chat_id and token and message:
            url = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={message}'
            response = requests.get(url)

            if response.status_code == 200:
                time_sent = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                self.message_table.insertRow(self.message_table.rowCount())
                self.message_table.setItem(self.message_table.rowCount() - 1, 0, QTableWidgetItem(chat_id))
                self.message_table.setItem(self.message_table.rowCount() - 1, 1, QTableWidgetItem("نام و نام خانوادگی فرستنده"))
                self.message_table.setItem(self.message_table.rowCount() - 1, 2, QTableWidgetItem(time_sent))
                self.message_table.setItem(self.message_table.rowCount() - 1, 3, QTableWidgetItem(message))
                self.message_entry.clear()
                self.scroll_to_bottom()
            else:
                QMessageBox.critical(self, "خطا", "خطا در ارسال پیام!")
        else:
            QMessageBox.warning(self, "هشدار", "لطفاً همه فیلدها را پر کنید.")

    def scroll_to_bottom(self):
        self.message_table.scrollToBottom()

    def refresh_messages(self):
        if not self.token:
            return

        url = f'https://api.telegram.org/bot{self.token}/getUpdates'
        response = requests.get(url)
        data = response.json()

        if data.get('ok'):
            for update in data['result']:
                if 'message' in update and update['message'].get('text'):
                    message = update['message']['text']
                    chat_id = str(update['message']['chat']['id'])
                    username = update['message']['from'].get('username', 'کاربر ناشناخته')
                    first_name = update['message']['from'].get('first_name', 'نام ناشناخته')
                    last_name = update['message']['from'].get('last_name', 'نام خانوادگی ناشناخته')
                    sender_name = f"{first_name} {last_name}"
                    message_id = update['update_id']

                    # فقط برای آخرین پیام یا پیام‌های دارای /start
                    if self.notifications_enabled and (self.last_update_id is None or message_id > self.last_update_id):
                        time_received = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

                        # اگر /start ارسال شده بود، اطلاعات کاربر را به متن پیام اضافه کن
                        if "/start" in message:
                            message_content = f"/start\n\nاطلاعات کاربر:\nChat ID: {chat_id}\nUsername: {username}\nنام: {first_name}\nنام خانوادگی: {last_name}"
                        else:
                            message_content = message

                        self.message_table.insertRow(self.message_table.rowCount())
                        self.message_table.setItem(self.message_table.rowCount() - 1, 0, QTableWidgetItem(chat_id))
                        self.message_table.setItem(self.message_table.rowCount() - 1, 1, QTableWidgetItem(sender_name))
                        self.message_table.setItem(self.message_table.rowCount() - 1, 2, QTableWidgetItem(time_received))
                        self.message_table.setItem(self.message_table.rowCount() - 1, 3, QTableWidgetItem(message_content))
                        self.scroll_to_bottom()

                        # نمایش اعلان فقط برای پیام‌های جدید
                        if self.last_update_id is None or "/start" in message:
                            notification.notify(
                                title=f"پیام جدید از {sender_name}",
                                message=message_content,
                                timeout=5
                            )
                        notification.notify(
                                title=f"پیام جدید از {sender_name}",
                                message=message_content,
                                timeout=5
                        )
                        self.last_update_id = message_id

    def closeEvent(self, event):
        self.save_bot_info()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    bot_ui = TelegramBotUI()
    bot_ui.show()
    sys.exit(app.exec_())
