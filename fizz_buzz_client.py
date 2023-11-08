import requests
import argparse

BASE_URL = "http://127.0.0.1:4000/api"

def get_values_between(start_range, end_range):
    params = {"start_range": start_range, "end_range": end_range}
    response = requests.get(f"{BASE_URL}/get_values_between", params=params)
    print(response.json())

def get_homepage_values():
    response = requests.get(f"{BASE_URL}/get_homepage_values")
    print(response.json())

def get_favourites():
    response = requests.get(f"{BASE_URL}/get_favourites")
    print(response.json())

def set_favourite(number, value):
    data = {"number": number, "value": value}
    response = requests.post(f"{BASE_URL}/set_favourite", json=data)
    print(response.json())

def delete_favourite(number):
    data = {"number": number}
    response = requests.delete(f"{BASE_URL}/delete_favourite", json=data)
    print(response.json())

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="API client for ElixirFizzBuzz API")
    parser.add_argument("action", choices=["get_values_between", "get_homepage_values", "get_favourites", "set_favourite", "delete_favourite"], help="The API action to perform")
    parser.add_argument("--start_range", type=int, help="The start range for the get_values_between action")
    parser.add_argument("--end_range", type=int, help="The end range for the get_values_between action")
    parser.add_argument("--number", type=int, help="The number for the set_favourite and delete_favourite actions")
    parser.add_argument("--value", help="The value for the set_favourite action")
    args = parser.parse_args()

    if args.action == "get_values_between":
        get_values_between(args.start_range, args.end_range)
    elif args.action == "get_homepage_values":
        get_homepage_values()
    elif args.action == "get_favourites":
        get_favourites()
    elif args.action == "set_favourite":
        set_favourite(args.number, args.value)
    elif args.action == "delete_favourite":
        delete_favourite(args.number)