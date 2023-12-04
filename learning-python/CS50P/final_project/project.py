import base64
from email.mime.text import MIMEText
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from requests import HTTPError
import re
import sys
import random
import os

emails = {}
secret_santa_assignments = {}

def main():
    SCOPES = ["https://www.googleapis.com/auth/gmail.send"]
    script_dir = os.path.dirname(os.path.abspath(__file__))
    credentials_path = os.path.join(script_dir, "credentials.json")

    if os.path.exists(credentials_path):
        flow = InstalledAppFlow.from_client_secrets_file(credentials_path, SCOPES)
        creds = flow.run_local_server(port=0)
    else:
        creds = None

    service = build("gmail", "v1", credentials=creds)

    try:
        for participant, santa in secret_santa_assignments.items():
            message = MIMEText(f"Congratulations!\nYou are so lucky to be the Secret Santa for {participant}!")
            message["to"] = emails[santa]
            message["subject"] = "Hohoho dear Santa"
            create_message = {'raw': base64.urlsafe_b64encode(message.as_bytes()).decode()}
            message = service.users().messages().send(userId="me", body=create_message).execute()
            print("Message sent successfully")
        print("All messages sent successfully")
    except HTTPError as error:
        print(f"An error occurred: {error}")
        message = None


def random_render(emails):
    participants = list(emails.keys())
    secret_santas = participants.copy()

    while True:
        random.shuffle(secret_santas)
        if all(participant != santa for participant, santa in zip(participants, secret_santas)):
            break

    secret_santa_dict = {participant: santa for participant, santa in zip(participants, secret_santas)}
    return secret_santa_dict

def validate_email(user_input):
    try:
        email = re.match(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", user_input)
        if email:
            if email.group() not in emails:
                return email.group()
            else:
                print("Email already introduced")
                return None
        else:
            print("Input does not match the email format. Please enter a valid email address.")
            return None
    except ValueError:
        print("Input a valid email address please")
        return None

def validate_name(user_input):
        if user_input not in emails:
            return user_input
        else:
            print("Name already introduced")
            return None


def exited(input):
    if input == "exit":
        print("Program exited")
        sys.exit(1)
    else:
        return False

def get_email():
    print("HoHoHoooo ))\n Could you please help Santa know how many people were kind this year")
    while True:
        try:
            n = (input("Input a number, please (type 'exit' to exit): ")).strip().lower()
            if not exited(n):
                n = int(n)
                break
        except ValueError:
            print("Oopsie Doopsie, that was not a number ((")

    for i in range(1, n + 1):
        person_email = None
        person_name = None
        while person_name is None:
            person_name = input(f"Person {i} name (Type 'exit' to exit): ").strip().lower()
            if not exited(person_name):
                person_name = person_name.title()
                person_name = validate_name(person_name)
        while person_email is None:
            person_email = input(f"Person {i} email (Type 'exit' to exit): ").strip().lower()
            if not exited(person_email):
                person_email = validate_email(person_email)
                if person_email and person_name:
                    emails[person_name] = person_email

    print("Collected emails:")
    for name, email in emails.items():
        print(f"  {name}: {email}")

if __name__ == "__main__":
    get_email()
    secret_santa_assignments = random_render(emails)
    print("\nSecret Santa Assignments:")
    for participant, santa in secret_santa_assignments.items():
        print(f"  {participant} is the Secret Santa for {santa}")
    main()