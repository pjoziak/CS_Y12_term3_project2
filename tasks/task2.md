TASK:
have a look on weblogin sub-project. It consits of:
- an application, exposing `/login` endpoint, accepting `POST` requests, and would expect 
```json
{
  "login": "user", 
  "password": "user-password"
}
``` 
input. It validates the login/password pair, and if it is ok, reply with 200, otherwise, reply with 403 (user/password invalid) or 422 (request not properly formatted)
- HTML + JavaScript, that renders in a browser and communicates with the application and allowing to log in, if proper credentials are sent.

Extend it to support also "sign up" option.