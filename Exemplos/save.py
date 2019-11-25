# standard python libraries
import os


class Saver:
    def __init__(self, path):
        self.path = path

        if not os.path.exists(self.path):
            os.makedirs(self.path)


    def exists(self, username):
        path = os.path.join(self.path, username + '.txt')

        return os.path.exists(path)


    def save(self, username, name, alter_usernames):
        path = os.path.join(self.path, username + '.txt')

        mode = 'a' if os.path.exists(path) else 'w'
        with open(path, mode, encoding='iso-8859-1') as file:
            file.write(name + '\n')

            for alter_username in alter_usernames:
                file.write(alter_username + '\n')

        file.close()

       # print(username)
