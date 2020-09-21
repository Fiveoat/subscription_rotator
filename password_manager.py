import lastpass


class PasswordManager:
    def __init__(self):
        self.username = "fiveoat@gmail.com"
        self.password = ""

    def generate_new_password(self):
        pass

    def update_passwords(self):
        pass

    def get_current_passwords(self):
        vault = lastpass.Vault.open_remote(self.username, self.password)
        for i in vault.accounts:
            print(i.__dict__)


if __name__ == '__main__':
    pw_manager = PasswordManager()
    pw_manager.get_current_passwords()
