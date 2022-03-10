import requests


def get_age(name):
    age_query = f"https://api.agify.io?name={name}"
    my_age = requests.get(age_query).json()
    return my_age["age"]


def get_gender(name):
    gender_query = f"https://api.genderize.io?name={name}"
    my_gender = requests.get(gender_query).json()
    return my_gender["gender"]


