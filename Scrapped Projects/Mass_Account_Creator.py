import time
import bs4
import random
import requests

from selenium import webdriver

my_mail = None
my_Password = None

def GetEmail():
    browser = webdriver.Edge()

    browser.get("https://tempmailto.org/")

    source = browser.page_source
    prettied_code = bs4.BeautifulSoup(source, 'html.parser')

    for div in prettied_code.find_all('div', class_="block appearance-none w-full bg-white text-white py-4 px-5 pr-8 bg-opacity-10 rounded-md cursor-pointer focus:outline-none select-none"):
        email = div.get_text(strip=True)
        return email



def GeneratePassword():
    password = ""
    password_length = random.randint(10, 20)

    choices = {
        "chars" : [],
        "numbers" : [],
        "special_chars" : [],
    }

    choices["chars"].extend("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    choices["numbers"].extend("0123456789")
    choices["special_chars"].extend(r"!£$%^&()_+-=[]#';./,.")

    for i in range(password_length):
        what_list = random.randint(1,3)
        what_list -= 1
        true_index = 0

        for index, nil in choices.items():
            if true_index == what_list:
                needed_list = nil
                if type(needed_list) == list:
                    random_index = random.randint(0, len(needed_list) - 1)

                    new_value = needed_list[random_index]
                    password += new_value
            else:
                true_index += 1
    return password
    


def SendSignRequest(email, password, username):
    url = "https://discord.com/api/v9/auth/register"

    headers = {
        "Host": "discord.com",
        "Content-Type": "application/json",  # Assuming JSON payload
    }

    payload = {
        "email":email,
        "username":username,
        "global_name":"a",
        "password":password,
        "invite":None,
        "consent":True,
        "date_of_birth":"1998-12-05",
        "gift_code_sku_id":None,
        "promotional_email_opt_in":False
    }

    first_request = requests.post(url=url, headers=headers, json=payload)

    if int(first_request.status_code) == 200:
        print("Success!!")
    else:
        print(first_request.status_code)
        print(first_request._content)


my_mail = GetEmail()
my_Password = GeneratePassword()

SendSignRequest(my_mail, my_Password, "NeuralBot14")
