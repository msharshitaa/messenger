import re

class MessageApp:
    def send_message(self):
        pass

class SmsService(MessageApp):
    def send_message(self, message, number):
        print(f"Message sent to {number} successfully.")

class EmailService(MessageApp):
    def send_message(self, message, email):
        print(f"Message sent to {email} successfully.")

class WhatsappService(MessageApp):
    def send_message(self, message, number):
        print(f"Message sent to {number} successfully.")

class Validator:
    def is_valid_number(self, num):
        pattern = re.compile("^[6-9]\d{9}$")
        return pattern.match(num)

    def is_valid_email(self, email):
        pattern = r'[^@]+@[^@]+\.[a-z]+'
        return re.match(pattern, email)

sms_service = SmsService()
email_service = EmailService()
whatsapp_service = WhatsappService()
validator = Validator()

while True:
    print("Select an option:")
    print("1. Send SMS")
    print("2. Send Email")
    print("3. Send WhatsApp")
    print("4. Quit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        number = input("Enter the recipient's phone number: ")
        if validator.is_valid_number(number):
            message = input("Enter the message to send: ")
            sms_service.send_message(message, number)
        else:
            print("Invalid phone number.")
    elif choice == 2:
        email = input("Enter the recipient's email address: ")
        if validator.is_valid_email(email):
            message = input("Enter the message to send: ")
            email_service.send_message(message, email)
        else:
            print("Invalid email address.")
    elif choice == 3:
        number = input("Enter the recipient's phone number: ")
        if validator.is_valid_number(number):
            message = input("Enter the message to send: ")
            whatsapp_service.send_message(message, number)
        else:
            print("Invalid phone number.")
    elif choice == 4:
        print("Thank you!")
        break
    else:
        print("Invalid choice.")
