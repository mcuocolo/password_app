import secrets
import string


""" Password class with options as variables and method
    

This class generates a password using parameters to initialize a long string.
Once the long string is generate, characters are randomly selected from it.
Selected characters are removed or not depending if duplicates are allowed in generate password.

This script requires that "pyperclip" to copy generated password to the clipboard.

"""

similar_char = "iI1loO0"


class Password:
    """
    A class used to generate a password

    ...

    Attributes
    ----------
    allow_numbers : Bool
        the parameter that specifies if numbers are to be included in the long string
        numbers are : "0123456789"
        default value = True,

    allow_symbols : Bool
        the parameter that specifies if symbols are to be included in the long string
        symbols are : "!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"
        default value = True,

    allow_lowercase : Bool
        the parameter that specifies if lowercase letters are to be included in the long string
        lowercase letters are : "abcdefghijklmnopqrstuvwxyz"
        default value = True,

    allow_uppercase : Bool
        the parameter that specifies if numbers are to be included in the long string
        uppercase letters are : "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        default value = True,

    allow_similar : Bool
        the parameter that specifies if similar characters that can generate confusion or errors when copied
        are to be included in the long string if not similar characters are removed from long string generation
        similar characters are : "iI1loO0"
        default value = True,

    allow_duplicates : Bool
        the parameter that specifies if duplicate characters are allowed in final generate password
        if not each select char is removed from long string generation
        default value = True,

    length : int
        User input value that specifies the length of generate password string
        default value = True,


    _long_string : str
        The concatenated value of all the approved strings among :
                    - numbers,
                    - symbols,
                    - lowercase letters,
                    - uppercase letters,
        Doesn't include similar characters if allow_similar is False
        default value = ""

    psw : str
        The string containing the generated password

    message : str
        Final message for output to user

    success = Bool
        A bool returning True if password successfully generated, False if not

    Methods
    -------
    _generate_long_string()
    _long_string_length_ok()
    generate_psw()

    """
    # default user_input dict
    def __init__(self):
        self.allow_numbers = True,
        self.allow_symbols = True,
        self.allow_lowercase = True,
        self.allow_uppercase = True,
        self.allow_similar = True,
        self.allow_duplicates = True,

        self.length = 12

        self._long_string = ""
        self.psw = ""

        self.message = ""
        self.success = False

    def _generate_long_string(self):
        """ define long string for psw generation based on selected options
        NB: Generated long string can be empty if all options are set to False """

        if self.allow_numbers:
            self._long_string += string.digits
        if self.allow_symbols:
            self._long_string += string.punctuation
        if self.allow_uppercase:
            self._long_string += string.ascii_uppercase
        if self.allow_lowercase:
            self._long_string += string.ascii_lowercase
        if not self.allow_similar:
            for char in similar_char:
                self._long_string = self._long_string.replace(char, "")

    def _long_string_length_ok(self):
        """ Checks if length of long string can generate password in case allow_duplicates is True"""
        if self.allow_duplicates:
            return True
        elif len(self._long_string) > self.length:
            return True
        else:
            return False

    def generate_psw(self):
        """ A function generating a password based by random selection from the long string
        returns a tuple (success, message, psw)
        and copies generated password to the clipboard """

        string = ""
        self._generate_long_string()

        # check string length if allow duplicates == False
        if self._long_string_length_ok():
            chars = []
            for i in range(self.length):
                char = secrets.choice(self._long_string)
                chars.append(char)
                if not self.allow_duplicates:
                    string = string.replace(char, "")
            self.psw = "".join(chars)
            self.message = f"Generated password : {self.psw}"
            self.success = True
        else:
            self.message = "No password generated, allow duplicates or add possible characters to password generator." \
                           
        return self.success, self.message, self.psw
