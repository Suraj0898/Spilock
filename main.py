from src.authentication.rfid_auth import rfid_auth
from src.authentication.voice_auth import voice_auth


def start(name):
    print(f'Hello, {name}')
    if rfid_auth():
        print("Loading....")
        voice_auth()

if __name__ == '__main__':
    start('Welcome to the Security Locking System!')
