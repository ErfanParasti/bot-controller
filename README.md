# Telegram Bot Controller | کنترلر ربات تلگرام

**Version 2.1.0** | **نسخه ۲.۱.۰**

---

## 🌍 English Version

### 🔍 About the Project
The **Telegram Bot Controller** is a feature-rich, user-friendly **GUI-based application** designed to control a Telegram bot with ease. Built using **Python & PyQt5**, it enables users to **send and receive messages, manage tokens, view chat history, and get notifications** in a sleek **dark-themed UI**.

> ⚠️ **Disclaimer:** This tool is developed **for legal and ethical use only**. The developer is not responsible for any misuse or unauthorized actions performed using this application.

### 🚀 Features
- **Easy Token & Chat ID Management**
- **Dark Mode Interface**
- **Real-time Message Retrieval (every 5 seconds)**
- **Send & Receive Messages**
- **Message Auto-scroll for Convenience**
- **Desktop Notifications for New Messages**
- **Message History Storage**

---

### 🛠 Installation & Setup
#### 📌 Prerequisites
Ensure you have:
- **Python 3.8+**
- Required dependencies (**install via pip**):

```bash
pip install PyQt5 requests plyer
```

#### 📌 Running the Application
1. Clone the repository or download the source code.
2. Install dependencies (see above).
3. Run the script:

   ```bash
   python main.py
   ```

4. Enter your **bot token** and **chat ID** to start sending and receiving messages.

---

### 📌 Configuration File (`bot.json`)
The app automatically creates a configuration file (`bot.json`) in the **Documents** folder:

```json
{
    "token": "your-telegram-bot-token",
    "chat_id": "your-chat-id",
    "notifications_enabled": true
}
```

---

### 📸 Screenshot
![UI Screenshot](https://i.pinimg.com/1200x/91/59/81/91598100adaec3923f0440c5fa2046ec.jpg)

---

## 🇮🇷 نسخه فارسی

### 🔍 درباره پروژه
**کنترلر ربات تلگرام** یک برنامه **دارای رابط کاربری گرافیکی (GUI)** برای مدیریت ربات تلگرام است. این ابزار با **Python و PyQt5** توسعه داده شده و به کاربران اجازه می‌دهد که **پیام‌ها را ارسال و دریافت کنند، توکن و چت آیدی را مدیریت کنند، تاریخچه پیام‌ها را ببینند و نوتیفیکیشن دریافت کنند** – همه این‌ها در یک **رابط کاربری مدرن و دارک**.

> ⚠️ **سلب مسئولیت:** این ابزار فقط برای **استفاده قانونی و اخلاقی** توسعه داده شده است. توسعه‌دهنده هیچ مسئولیتی در قبال سوءاستفاده یا اقدامات غیرمجاز ندارد.

### 🚀 ویژگی‌ها
- **مدیریت آسان توکن و چت آیدی**
- **رابط کاربری دارک و مدرن**
- **دریافت پیام‌های جدید هر ۵ ثانیه**
- **ارسال و دریافت پیام**
- **اسکرول خودکار پیام‌ها**
- **نوتیفیکیشن دسکتاپ برای پیام‌های جدید**
- **ذخیره تاریخچه پیام‌ها**

---

### 🛠 نصب و اجرا
#### 📌 پیش‌نیازها
- **پایتون ۳.۸+**
- نصب وابستگی‌ها:

```bash
pip install PyQt5 requests plyer
```

#### 📌 نحوه اجرا
1. پروژه را کلون کنید یا فایل‌های آن را دانلود کنید.
2. وابستگی‌ها را نصب کنید (طبق دستور بالا).
3. اسکریپت را اجرا کنید:

   ```bash
   python main.py
   ```

4. **توکن ربات** و **چت آیدی** خود را وارد کنید و مدیریت پیام‌ها را شروع کنید!

---

### 📌 فایل تنظیمات (`bot.json`)
برنامه به‌صورت خودکار یک فایل تنظیمات (`bot.json`) در پوشه **Documents** ایجاد می‌کند:

```json
{
    "token": "توکن ربات شما",
    "chat_id": "چت آیدی شما",
    "notifications_enabled": true
}
```

---

### 📸 اسکرین‌شات
![UI Screenshot](https://i.pinimg.com/1200x/91/59/81/91598100adaec3923f0440c5fa2046ec.jpg)

---

## 📜 License | مجوز
This project is licensed under the **Apache 2.0 License**. See the `LICENSE` file for details.

---

💻 Developed by **Your Friend** | نسخه **۲.۱.۰**