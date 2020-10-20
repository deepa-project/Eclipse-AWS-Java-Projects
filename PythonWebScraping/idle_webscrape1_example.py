Python 3.8.3 (tags/v3.8.3:6f8c832, May 13 2020, 22:37:02) [MSC v.1924 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from urllib.request import urlopen
>>> url = "http://olympus.realpython.org/profiles/aphrodite"
>>> page = urlopen(url)
>>> page
<http.client.HTTPResponse object at 0x0000013DA6B144F0>
>>> html_bytes = page.read()
>>> html = html_bytes.decode("utf-8")
>>> html
'<html>\n<head>\n<title>Profile: Aphrodite</title>\n</head>\n<body bgcolor="yellow">\n<center>\n<br><br>\n<img src="/static/aphrodite.gif" />\n<h2>Name: Aphrodite</h2>\n<br><br>\nFavorite animal: Dove\n<br><br>\nFavorite color: Red\n<br><br>\nHometown: Mount Olympus\n</center>\n</body>\n</html>\n'
>>> html = html_bytes.decode("utf-8")
>>> print(html)
<html>
<head>
<title>Profile: Aphrodite</title>
</head>
<body bgcolor="yellow">
<center>
<br><br>
<img src="/static/aphrodite.gif" />
<h2>Name: Aphrodite</h2>
<br><br>
Favorite animal: Dove
<br><br>
Favorite color: Red
<br><br>
Hometown: Mount Olympus
</center>
</body>
</html>

>>> 