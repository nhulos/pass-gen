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


# answer yes/no
def answer(text, default):
    result = input(text).strip().lower()
    if result == "":
        return default
    elif result == "y":
        return True
    else:
        return False


# randomization some numbers
def rand_one_int(numbers_list):
    result = []
    for num in numbers_list:
        num = str(num)
        for random_num in range(10):
            for i in range(len(num)):
                result.append(num[:i] + str(random_num) + num[i+1:])
    return result


# passwords category
def processing(data_list):
    text = []
    numbers = []

    for data in data_list:
        # number
        if data.isdigit():
            if len(data) > 4:
                for i in range(1, len(data) + 1):
                    numbers.append(data[:i])
                for i in range(1, len(data)):
                    numbers.append(data[i:])
            else:
                numbers.append(data)
        # data
        elif re.findall(r"\d\d-\d\d-\d\d\d\d", data):
            numbers = numbers + data.split("-")
            numbers.append(data[-2:])
        # name
        else:
            data_types = (data, data.lower(), data.upper(), data.title())
            for word in data_types:
                text.append(word)
            for i in range(3, len(data)):
                text.append(data[:i])

    return text, numbers


# generate combinations
def generate_pass(text, numbers, min_len, max_len, num_and_num):
    separators = ["", "_", "-", " "]

    # add passwords to list
    def write_pass(password):
        if min_len <= len(password) <= max_len:
            with open("pass.txt", "a") as f:
                f.write(password + "\n")

    for sep in separators:
        for t in text:
            # text + number
            for n in numbers:
                write_pass(t + sep + n)
                write_pass(n + sep + t)
            # text + text
            for t2 in text:
                write_pass(t + sep + t2)

        # number + number
        if num_and_num:
            for n in numbers:
                for n2 in numbers:
                    write_pass(n + sep + n2)


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
            # random one number
            if answer("Generate combinations with one random number replace[y/N]: ", False):
                numbers += rand_one_int(numbers)
            # num + num
            if answer("Generate num + num combinations[y/N]: ", False):
                num_and_num = True
            else:
                num_and_num = False
            print("\nGenerating...")
            # generate
            generate_pass(text, numbers, min_len, max_len, num_and_num)
            print(sum(1 for line in open('pass.txt', 'r')),
                  "passwords was generated!")
            break
        # input data
        if input_data:
            data_list.append(input_data)


# clear pass.txt
def clear_file():
    with open("pass.txt", "w") as f:
        pass


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass
