from src.app import app

#def main() -> None:
#    sum(4, 10)
HOST = "localhost"
PORT = 4000
DEBUG = True

if __name__ == '__main__':
    app.run(HOST,PORT,DEBUG)
