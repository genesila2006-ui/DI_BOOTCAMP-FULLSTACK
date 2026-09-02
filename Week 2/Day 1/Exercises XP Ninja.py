class Phone:
    def __init__(self, phone_number):
        self.phone_number = phone_number
        self.call_history = []
        self.messages = []

    def call(self, other_phone):
        call_log = f"{self.phone_number} called {other_phone.phone_number}"
        print(call_log)
        self.call_history.append(call_log)

    def show_call_history(self):
        print(f"\n--- Call History for {self.phone_number} ---")
        for log in self.call_history:
            print(log)

    def send_message(self, other_phone, content):
        message_data = {
            "to": other_phone.phone_number,
            "from": self.phone_number,
            "content": content
        }
        # Save message to both sender's and receiver's history
        self.messages.append(message_data)
        other_phone.messages.append(message_data)
        print(f"Message sent from {self.phone_number} to {other_phone.phone_number}")

    def show_outgoing_messages(self):
        print(f"\n--- Outgoing Messages from {self.phone_number} ---")
        outgoing = [msg for msg in self.messages if msg["from"] == self.phone_number]
        for msg in outgoing:
            print(f"To {msg['to']}: {msg['content']}")

    def show_incoming_messages(self):
        print(f"\n--- Incoming Messages for {self.phone_number} ---")
        incoming = [msg for msg in self.messages if msg["to"] == self.phone_number]
        for msg in incoming:
            print(f"From {msg['from']}: {msg['content']}")

    def show_messages_from(self, other_phone):
        print(f"\n--- Messages between {self.phone_number} and {other_phone.phone_number} ---")
        filtered = [
            msg for msg in self.messages 
            if (msg["from"] == other_phone.phone_number and msg["to"] == self.phone_number) or
               (msg["from"] == self.phone_number and msg["to"] == other_phone.phone_number)
        ]
        for msg in filtered:
            print(f"[{msg['from']} -> {msg['to']}]: {msg['content']}")


# --- Testing the Code ---

# Create phone instances
phone1 = Phone("123-456-7890")
phone2 = Phone("987-654-3210")
phone3 = Phone("555-555-5555")

# Test calls
phone1.call(phone2)
phone2.call(phone1)
phone1.show_call_history()

# Test sending messages
phone1.send_message(phone2, "Hey, how are you?")
phone2.send_message(phone1, "I'm good, thanks! How about you?")
phone3.send_message(phone1, "Hey phone1, call me back!")

# Test showing message logs
phone1.show_outgoing_messages()
phone1.show_incoming_messages()
phone1