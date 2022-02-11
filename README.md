# D2L Login

I made this program to automatically log me into the D2L platform that uses Microsoft SSO on the backend,

and then also opens and joins my Teams meeting for class <span style='font-size:50px;'>&#9786;</span>

- D2L platform ➜ https://www.d2l.com

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

3. Download the ChromeDriver From here ➜ <a href="https://sites.google.com/chromium.org/driver/" target="_blank">ChromeDriver</a>

4. Run
``python3 main.py``
