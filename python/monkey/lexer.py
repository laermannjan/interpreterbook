from dataclasses import dataclass
from monkey.token import Token, TokenType, OPERATORS, DELIMITERS, KEYWORDS


@dataclass
class Lexer:
    input: str
    position: int = 0
    read_position: int = 0
    ch: str = ""

    def __post_init__(self):
        self.read_char()

    def read_char(self) -> None:
        if self.read_position >= len(self.input):
            self.ch = ""
        else:
            self.ch = self.input[self.read_position]
        self.position = self.read_position
        self.read_position += 1

    def peek_char(self) -> str:
        if self.read_position >= len(self.input):
            return ""
        else:
            return self.input[self.read_position]

    def next_token(self) -> Token:
        self.skip_whitespace()
        tok: Token

        if self.ch in DELIMITERS:
            tok = Token(DELIMITERS[self.ch])

        elif self.ch in OPERATORS:
            if self.ch == "=" and self.peek_char() == "=":
                ch = self.ch
                self.read_char()
                literal = ch + self.ch
                tok = Token(OPERATORS[literal])
            elif self.ch == "!" and self.peek_char() == "=":
                ch = self.ch
                self.read_char()
                literal = ch + self.ch
                tok = Token(OPERATORS[literal])
            else:
                tok = Token(OPERATORS[self.ch])

        elif self.ch == "":
            tok = Token(TokenType.EOF)

        else:
            if self.ch.isalpha():
                literal = self.read_identifier()
                if literal in KEYWORDS:
                    tok = Token(KEYWORDS[literal])
                else:
                    tok = Token(TokenType.IDENT, literal)
                return tok
            elif self.ch.isdigit():
                literal = self.read_number()
                tok = Token(TokenType.INT, literal)
                return tok
            else:
                tok = Token(TokenType.ILLEGAL, self.ch)
            raise ValueError(f"unkown token encountered {self.ch=}")

        self.read_char()
        return tok

    def read_identifier(self) -> str:
        start = self.position
        while self.ch.isalpha():
            self.read_char()
        return self.input[start : self.position]

    def read_number(self) -> str:
        start = self.position
        while self.ch.isdigit():
            self.read_char()
        return self.input[start : self.position]

    def skip_whitespace(self) -> None:
        while self.ch in (" ", "\t", "\n", "\r"):
            self.read_char()
