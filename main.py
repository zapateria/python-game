import sys
from Player import Player

def main() -> int:
    name = input("Your name: ")
    player = Player(name)
    print(f"Hello {player.name}..")

    while True:
        cmd = player.prompt()
        if cmd == "quit":
            return 0

if __name__ == "__main__":
    sys.exit(main())

