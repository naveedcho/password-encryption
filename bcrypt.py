import bcrypt
import time

if __name__ == '__main__':
    f1 = open("swift-passwords.txt", "r")
    f2 = open("swift-bcrypthashes-12.txt", "wb")

    start_time = time.time()

    for password in f1:
        salt = bcrypt.gensalt(12)
        hashed = bcrypt.hashpw(b'password', salt)
        f2.write(hashed)
        f2.write(b'\n')

    print("%s seconds" % (time.time() - start_time))