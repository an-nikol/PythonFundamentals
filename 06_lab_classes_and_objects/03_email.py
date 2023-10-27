class Email:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"


emails = []

info = input()
while info != "Stop":
    command = info.split(" ")
    sender = command[0]
    receiver = command[1]
    content = command[2]
    # apply the class to the object
    email_object = Email(sender, receiver, content)
    emails.append(email_object)
    info = input()

# convert indices to integers
indexes = input().split(", ")
sent_emails = [int(num) for num in indexes]
for idx in sent_emails:
    # call the send method for each email object in the list
    emails[idx].send()

for email in emails:
    print(email.get_info())