from monkey.tokens.tokens import Token, Tokens, lookup_ident


def is_letter(char):
    return isinstance(char, str) and ("a" <= char <= "z" or "A" <= char <= "Z" or char == "_")


def is_digit(char):
    return isinstance(char, str) and ("0" <= char <= "9")


class Lexer:
    """The lexer class takes an input string and provides a
    `next_token` function to be iterated over by the parser.

    `self.char` contains the most recently read character in the input string
    `self.position` is the index of that character in the input string
    `self.read_position` is always ahead of `self.position` and points to the next character to be read
    """

    def __init__(self, input: str) -> None:
        self.input = input
        self.read_position = 0
        self._read_char()

    def _read_char(self):
        """Returns the next character (ASCII) in `self.input."""
        if self.read_position >= len(self.input):
            self.char = None
        else:
            self.char = self.input[self.read_position]

        self.position = self.read_position
        self.read_position += 1

    def _read_identifier(self):
        init_pos = self.position
        while is_letter(self.char):
            self._read_char()

        return self.input[init_pos : self.position]

    def _read_number(self):
        init_pos = self.position
        while is_digit(self.char):
            self._read_char()

        return self.input[init_pos : self.position]

    def _skip_whitespace(self):
        while self.char in [" ", "\t", "\n", "\r"]:
            self._read_char()

    def _peek_char(self):
        if self.read_position >= len(self.input):
            return None
        else:
            return self.input[self.read_position]

    def next_token(self):
        tok: Token

        self._skip_whitespace()

        match self.char:
            case "=":
                if self._peek_char() == "=":
                    first_char = self.char
                    self._read_char()
                    tok = Token(type=Tokens.EQ, literal=first_char + self.char)
                else:
                    tok = Token(type=Tokens.ASSIGN, literal=self.char)
            case "+":
                tok = Token(type=Tokens.PLUS, literal=self.char)
            case "-":
                tok = Token(type=Tokens.MINUS, literal=self.char)
            case "!":
                if self._peek_char() == "=":
                    first_char = self.char
                    self._read_char()
                    tok = Token(type=Tokens.NOT_EQ, literal=first_char + self.char)
                else:
                    tok = Token(type=Tokens.BANG, literal=self.char)
            case "/":
                tok = Token(type=Tokens.SLASH, literal=self.char)
            case "*":
                tok = Token(type=Tokens.ASTERISK, literal=self.char)
            case "<":
                tok = Token(type=Tokens.LT, literal=self.char)
            case ">":
                tok = Token(type=Tokens.GT, literal=self.char)
            case "(":
                tok = Token(type=Tokens.LPAREN, literal=self.char)
            case ")":
                tok = Token(type=Tokens.RPAREN, literal=self.char)
            case "{":
                tok = Token(type=Tokens.LBRACE, literal=self.char)
            case "}":
                tok = Token(type=Tokens.RBRACE, literal=self.char)
            case ",":
                tok = Token(type=Tokens.COMMA, literal=self.char)
            case ";":
                tok = Token(type=Tokens.SEMICOLON, literal=self.char)
            case None:
                tok = Token(type=Tokens.EOF, literal="")
            case _:
                if is_letter(self.char):
                    literal = self._read_identifier()
                    tok = Token(
                        type=lookup_ident(literal),
                        literal=literal,
                    )
                    return tok
                elif is_digit(self.char):
                    tok = Token(type=Tokens.INT, literal=self._read_number())
                    return tok
                else:
                    tok = Token(type=Tokens.ILLEGAL, literal=self.char)

        self._read_char()
        return tok
