import requests

un = input('Please enter your user username: \n')
pw = input('Please enter your password: \n')

data = {
  "login": un,
  "password": pw,
}

resp = requests.post('http://127.0.0.1:21370/login', json=data)
print(resp)
