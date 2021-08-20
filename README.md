# D2L Login

1. Install requirements
``python3 -m pip install -r requirements.txt``

2. Create a file named ``login.yml`` that contains your login info
```
➜  ~ cat login.yml
user:
  email: youremail.com
  password: 'Your super cool password'
  url: 'hxxps://yourschool.com'
  url2: 'msteams://teams.microsoft.com/xxx'
  ```
3. Download the ChromeDriver
From here ➜ https://sites.google.com/a/chromium.org/chromedriver/downloads

4. Run
``python3 main.py``

>I wrote this program to automatically log me into the D2L platform that >uses Microsoft SSO on the backend and also open and join my Teams meeting >for class :)

* D2L platform ➜ https://www.d2l.com
