import sys
import raylibpy


class InputService:
    """Detects player input. The responsibility of the class of objects is to detect player keypresses and translate them into a point representing a direction (or velocity).

    Stereotype: 
        Service Provider

    Attributes:
        _screen (Screen): An Asciimatics screen.
    """

    def __init__(self):
        """The class constructor.

        Args:
            self (InputService): An instance of InputService.
        """

    # def get_letter(self):
    #     """Gets the letter that was typed. If the enter key was pressed returns an asterisk.

    #     Args:
    #         self (InputService): An instance of InputService.

    #     Returns:
    #         string: The letter that was typed.
    #     """
    #     result = ""
    #     event = self._screen.get_key()
    #     if not event is None:
    #         if event == 27:
    #             sys.exit()
    #         elif event == 10:
    #             result = "*"
    #         elif event >= 97 and event <= 122:
    #             result = chr(event)
    #     return result

    def get_letter(self):
        key_int = raylibpy.get_key_pressed()

        key_string = None

        if key_int != -1:
            key_string = chr(key_int)

        return key_string

    def get_letter_pressed(self, letter_list):

        key_int = raylibpy.get_key_pressed()
        if key_int != -1:
            letter_list.append(chr(key_int))
            return letter_list
