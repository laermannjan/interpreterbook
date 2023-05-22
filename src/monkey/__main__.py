import os

from monkey.repl.repl import start_repl


def main():
    user = os.environ.get("USER", os.environ.get("USERNAME"))
    print(f"Hello {user}! This is the Monkey programming language")
    print("Feel free to type in commands")
    start_repl()


if __name__ == "__main__":
    main()
