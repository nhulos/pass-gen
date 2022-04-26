#!/bin/python3
import re


# get data from user: mail, name, date, phone number...
def get_data():
    print("\nYou can print: mail, name, date(dd-mm-yyy), phone number...")
    print("gen! - finish")
    text = input("> ").strip()
    return text


# incput int data
def input_num(input_text):
    while True:
        data = input(input_text).strip()
        if data.isdigit() and int(data) > 0:
            return int(data)
        print("Incorrect!")


# passwords category
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


# generate combinations
def generate_pass(text, numbers, min_len, max_len):
    separators = ["", "_", "-", " "]
    passwords = []

    # add passwords to list
    def add_pass(password):
        if not password in passwords and min_len <= len(password) <= max_len:
            passwords.append(password)

    for sep in separators:
        for t in text:
            # text + number
            for n in numbers:
                add_pass(t + sep + n)
                add_pass(n + sep + t)
            # text + text
            for t2 in text:
                add_pass(t + sep + t2)

        # number + number
        for n in numbers:
            for n2 in numbers:
                add_pass(n + sep + n2)

    return passwords


# write passwords to file
def write_pass(passwords):
    with open("pass.txt", "w") as f:
        for i in passwords:
            f.write(i + "\n")


def main():
    data_list = []
    while True:
        input_data = get_data()
        # generation passwords
        if input_data == "gen!":
            # min and max lenght
            min_len = input_num("min len: ")
            max_len = input_num("max len: ")
            text, numbers = processing(data_list)  # categorys
            print("\nGenerating...")
            passwords = generate_pass(
                text, numbers, min_len, max_len)  # generate
            write_pass(passwords)  # write to file
            print(len(passwords), "passwords was generated!")
            break
        # input data
        if input_data:
            data_list.append(input_data)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass
