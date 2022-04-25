#!/bin/python3
import re


def take_data():
    print("\nYou can print: mail, name, date(dd-mm-yyy), phone number...")
    print("gen! - finish")
    text = input("> ").strip()
    return text


def generate_pass(text, numbers):
    separators = ["", "_", "-", " "]
    passwords = []

    for t in text:
        for n in numbers:
            for sep in separators:
                passwords.append(t + sep + n)
                passwords.append(n + sep + t)
        for t2 in text:
            for sep in separators:
                passwords.append(t + sep + t2)
    
    return passwords
                

def processing(data_list):
    text = []
    numbers = []

    for data in data_list:
        # number
        if data.isdigit():
            for i in range(1, len(data) + 1):
                numbers.append(data[:i])
            for i in range(1, len(data)):
                numbers.append(data[i:])
        # data
        elif re.findall(r"\d\d-\d\d-\d\d\d\d", data):
            numbers = numbers + data.split("-")
            numbers.append(data[-2:])
        # name
        else:
            text.append(data)
            text.append(data.lower())
            text.append(data.upper())
            text.append(data.title())
            for i in range(3, len(data)):
                strip_data = data[:i]
    return text, numbers


def write_pass(passwords):
    with open("pass.txt", "w") as f:
        for i in passwords:
            f.write(i + "\n")


# main
data_list = []
try:
    while True:
        data = take_data()
        if data == "gen!":
            text, numbers = processing(data_list)
            print("\nGenerating...")
            passwords = generate_pass(text, numbers)
            write_pass(list(set(passwords)))
            print(len(passwords), "passwords was generated!")
            break
        if data:
            data_list.append(data)
except KeyboardInterrupt:
    pass
    
