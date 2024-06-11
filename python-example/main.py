import requests

# Disable SSL warnings
requests.packages.urllib3.disable_warnings()


def get_data():
    response = requests.get("https://api.chucknorris.io/jokes/random", verify=False)
    return response.json()["value"]


def main():
    data = get_data()
    print("")
    print("Chuck Norris joke:")
    print(data)
    print("")


if __name__ == "__main__":
    main()
