# Gmail Sender Application

A command-line utility for sending emails through Gmail using Python. This tool provides a simple interface to compose and send emails with optional clipboard support.

## Features

- 📧 **Gmail Integration**: Sends emails directly through Gmail's SMTP server
- 📝 **Multi-line Email Body**: Compose email bodies line by line
- 📋 **Clipboard Support**: Optional clipboard paste functionality with `pyperclip`
- ✉️ **Custom Headers**: Set sender name, recipient name, and email subject
- 🔐 **Secure Authentication**: Uses Gmail App Passwords for security
- ✔️ **Email Validation**: Validates recipient email format
- ⏱️ **Smart Timeout**: Dynamically adjusts timeout based on email body size
- 🛡️ **Error Handling**: Comprehensive error handling for authentication and connection issues

## Requirements

- Python 3.6+
- Gmail account with 2-factor authentication enabled
- Required libraries:
  - `smtplib` (built-in)
  - `email.mime` (built-in)
  - `pyperclip` (optional, for clipboard support)

## Installation

1. Clone or download this repository
2. Install optional dependency for clipboard support:
```bash
pip install pyperclip
```

3. Set up Gmail App Password:
   - Go to: https://myaccount.google.com/security
   - Enable 2-factor authentication if not already enabled
   - Go to "App Passwords" (appears only with 2FA enabled)
   - Select "Mail" and "Windows Computer"
   - Generate a 16-character App Password
   - Save it securely

## Usage

Run the script:
```bash
python send\ gmail.py
```

The program will guide you through several prompts:

### 1. Enter Your Gmail Account
```
Input your account
your.email@gmail.com
```

### 2. Enter App Password
```
app password(not password)
xxxx xxxx xxxx xxxx
```
- Use the 16-character App Password (not your Gmail password)
- Remove spaces when entering

### 3. Enter Recipient Email
```
to who do you want to send?
recipient@example.com
```
- Must be a valid email format (contains @ and .)
- Must be between 6-30 characters

### 4. Compose Email Body
```
Please write the body(write stope to stop or pastee to paste).
Do not use Ctrl + v to paste:
> This is the first line
> This is the second line
> stope
```
- Type each line and press Enter
- Type `stope` to finish composing
- Type `pastee` to paste from clipboard (if pyperclip is installed)

### 5. Set Recipient Display Name
```
How you want to call him?
> John Doe
```

### 6. Set Email Subject
```
what is the subject of email:
> Meeting Tomorrow
```

### 7. Send!
- Email is sent automatically
- You'll see "sent!" on success
- Program exits after 5 seconds

## Technical Details

### Gmail SMTP Configuration
- **Server**: smtp.gmail.com
- **Port**: 587
- **Security**: STARTTLS
- **Email Format**: MIME Text with UTF-8 encoding

### Timeout Calculation
```
timeout = max(20, int(body_length / 50) + 20) seconds
```
- Minimum timeout: 20 seconds
- Scales with email body size

### Email Validation
Recipient email must:
- ✓ Contain exactly one @ symbol
- ✓ Contain at least one . (dot)
- ✓ Be 6-30 characters long

## Examples

### Example 1: Simple Email
```bash
Input your account: your.email@gmail.com
app password(not password): abcd efgh ijkl mnop
to who do you want to send?: friend@example.com
Please write the body(write stope to stop):
> Hi Friend!
> How are you doing?
> Let's catch up soon.
> stope
How you want to call him?: Friend
what is the subject of email: Catching Up
sent!
```

### Example 2: Long Email with Clipboard
```bash
Input your account: sender@gmail.com
app password(not password): wxyz abcd efgh ijkl
to who do you want to send?: boss@company.com
Please write the body(write stope to stop or pastee to paste):
> Meeting Notes:
> pastee
> stope
How you want to call him?: Boss
what is the subject of email: Q1 Business Review
sent!
```

## Error Messages

| Error | Cause | Solution |
|-------|-------|----------|
| "Failed...Please check the app password" | Invalid authentication | Verify App Password is correct (16 chars) |
| "Bad input" | Invalid email format | Email must contain @ and . and be 6-30 chars |
| "Error: [details]. Not sent" | Connection or other error | Check internet and that Gmail allows SMTP access |

## Important Notes

⚠️ **Security Reminders:**
- Never share your App Password
- Don't use your regular Gmail password
- Store credentials securely
- Don't commit credentials to version control
- Consider using environment variables for credentials in production

## Clipboard Support

### With pyperclip (recommended)
- Install: `pip install pyperclip`
- In email body, type `pastee` to paste from clipboard
- Don't use `Ctrl + V` as it won't work in terminal

### Without pyperclip
- The `pastee` command will be treated as regular text
- Type your content line by line instead

## Limitations

- Gmail accounts only (requires SMTP support)
- No file attachment support
- Plain text emails only (no rich formatting)
- No scheduling capability
- No draft saving
- Recipient email must be validated on the fly

## Troubleshooting

**"Failed...Please check the app password"**
- Verify you're using the 16-character App Password, not your Gmail password
- Ensure 2-factor authentication is enabled on your Gmail account
- Check that you selected "Mail" and "Windows Computer" when generating the App Password
- Regenerate the App Password if needed

**"Bad input" on email address**
- Email must contain exactly one @ symbol
- Email must contain at least one . (dot)
- Email length must be between 6-30 characters
- Check for typos

**No "pastee" option appearing**
- pyperclip is not installed
- Install with: `pip install pyperclip`
- Or continue typing lines normally without clipboard

**Connection timeout**
- Check your internet connection
- Gmail might be blocking login from less secure apps
- Try generating a new App Password
- Ensure port 587 is not blocked by firewall

**Email not received**
- Check spam/junk folder
- Verify recipient address is correct
- Some corporate firewalls may block emails
- Try sending to a different email first to test

## Advanced Usage

### Automating Credentials (Development Only)
```python
# For development/testing only - NOT for production
sender = "your.email@gmail.com"
app_password = "xxxx xxxx xxxx xxxx"
```

### Using Environment Variables (Recommended)
```python
import os
sender = os.getenv('GMAIL_ADDRESS')
app_password = os.getenv('GMAIL_APP_PASSWORD')
```

## Performance

- Email sending time: 2-10 seconds (depending on content and connection)
- Timeout automatically scales with email size
- No network cleanup needed; connection handles gracefully

## Code Structure

1. **Imports**: SMTP, email formatting, and optional clipboard support
2. **Configuration**: Gmail SMTP settings hardcoded for simplicity
3. **Input Handling**: Prompts for credentials, recipient, and content
4. **Email Composition**: Builds MIME message with proper encoding
5. **Sending**: Establishes secure connection and sends email
6. **Error Handling**: Catches authentication and general errors

---

**Disclaimer**: This tool is for personal use. Ensure you comply with Gmail's Terms of Service and applicable regulations when sending emails.
