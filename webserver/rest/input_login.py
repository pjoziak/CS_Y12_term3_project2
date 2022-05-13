import requests 

user_login = str(input("Login:"))
user_pass = str(input("Password:"))

json = {"login" : user_login,
    "password": user_pass
}
r = requests.post("http://localhost:22000/verify", json=json)

def process_response(response):
    if response.status_code == 200:
        print("Logged in")
    elif response.status_code == 403:
        print("something wrong")
    else:
        print("error") 


process_response(r)
