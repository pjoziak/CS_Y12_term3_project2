TASK:
write 2 applications:
- application 1 would expose `/validate` endpoint, accepting `POST` requests, and would expect 
```json
{"login": ..., "password": ...}``` 
input. It would validate the login/password pair, and if it is ok, reply with 200, otherwise, reply with 403 (user/password invalid) or 422 (request not properly formatted)
- application 2 would be simple interface: ask the user to provide login and password (`input` method) and send it over to application 1 to validate. If it is validated properly, will show "Login successful", otherwise it will show "Invalid login/password"