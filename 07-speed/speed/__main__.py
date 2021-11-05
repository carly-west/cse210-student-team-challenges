from game.output_service import OutputService
from game.input_service import InputService
from game.director import Director
import random
import raylibpy
# import os
# os.environ['RAYLIB_BIN_PATH'] = '.'


# def main(screen):
#     input_service = InputService(screen)
#     output_service = OutputService(screen)
#     director = Director(input_service, output_service)
#     director.start_game()


# Screen.wrapper(main)

def main():
    input_service = InputService()
    output_service = OutputService()
    director = Director(input_service, output_service)
    director.start_game()


if __name__ == "__main__":
    main()
