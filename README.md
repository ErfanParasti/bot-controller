# Bot-controller


```markdown
# Telegram Bot UI

A modern, feature-rich Telegram bot control panel built using Python and PyQt5. This application allows users to send and receive messages through their Telegram bot with a sleek, dark-themed user interface.

## Features

- **Token & Chat ID Management**: Easily input and save your bot token and chat ID.
- **Dark Mode UI**: Stylish and intuitive interface with responsive design.
- **Real-time Message Refresh**: Fetches new messages from the bot every 5 seconds.
- **Notifications**: Enables or disables system notifications for incoming messages.
- **Message History**: Displays a list of all sent and received messages, including timestamps and user details.
- **Interactive Table**: Scrollable table to view message details.
- **Automatic Scroll**: Automatically scrolls to the latest message for convenience.
- **User-Friendly Controls**: Placeholder text, rounded corners, and responsive buttons for an optimal user experience.

## Requirements

Before you begin, ensure you have the following installed:

- Python 3.8 or higher
- `PyQt5` for GUI components
- `requests` for API communication
- `plyer` for notifications

Install required packages via pip:

```bash
pip install PyQt5 requests plyer
```

## File Structure

- **`bot.json`**: A configuration file saved in the user's `Documents` folder. It stores the bot token, chat ID, and notification preferences.

## How to Run

1. Clone the repository or download the source code.
2. Install the required packages using the command mentioned above.
3. Run the application:

   ```bash
   python main.py
   ```

4. Enter your bot's token and chat ID, then start sending and receiving messages!

## Configuration File

The application automatically creates a `bot.json` file in your `Documents` directory to save:

- **Token**: Your bot's API token.
- **Chat ID**: The chat ID for sending messages.
- **Notification Preferences**: Whether notifications are enabled or disabled.

Example `bot.json`:

```json
{
    "token": "your-telegram-bot-token",
    "chat_id": "your-chat-id",
    "notifications_enabled": true
}
```

## Screenshots

![UI Screenshot](path/to/screenshot.png)  
_Add a screenshot here showcasing the UI._

## Usage Instructions

### Sending a Message
1. Enter your message in the input field at the bottom.
2. Click "ارسال" or press `Enter`.

### Receiving Messages
The application fetches new messages every 5 seconds. Notifications are displayed if enabled.

### Replacing Token and Chat ID
1. Update the token or chat ID fields.
2. Click **جایگزینی توکن** to save changes.

### Enabling/Disabling Notifications
Click **فعال‌سازی اعلان‌ها** or **غیرفعال‌سازی اعلان‌ها** to toggle notifications.

## Contribution

Contributions are welcome! If you have suggestions or encounter issues, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
```

### Notes:
- Replace `path/to/screenshot.png` with an actual image path if you include a screenshot.
- Add instructions or examples for advanced configurations if necessary.
