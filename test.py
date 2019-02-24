class User:
    def __init__(self, name, email):
        self._name = name
        self._email = email

    def get_name(self):
        return self._name
        
    def get_email(self):
        return self._email

    def do_something(self):
        pass

    def __str__(self):
        return self._name + ", " + self._email

users = [ User("Testuser", "testmail@mail.com"), User("User2", "user2@mail.com")]

for user in users:
    user.do_something


def newmethon111():
    print('234')

newmethon111()

print('123')

# TODO 二月 24, 2019: 重构此文件代码！

msg = 'Hello World!'
print(msg)