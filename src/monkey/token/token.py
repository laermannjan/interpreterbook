from dataclasses import dataclass
from enum import Enum

TokenType = str


@dataclass
class Token:
    type: TokenType
    literal: str

    def __eq__(self, other) -> bool:
        if isinstance(other, Token):
            if self.type == other.type and self.literal == other.literal:
                return True
        return False


class Tokens(TokenType, Enum):
    ILLEGAL = "ILLEGAL"
    EOF = "EOF"

    # // Identifiers + literals
    IDENT = "IDENT"  # add, foobar, x, y, ...
    INT = "INT"  # 1343456

    # // Operators
    ASSIGN = "="
    PLUS = "+"

    # // Delimiters
    COMMA = ","
    SEMICOLON = ";"

    LPAREN = "("
    RPAREN = ")"
    LBRACE = "{"
    RBRACE = "}"

    # // Keywords
    FUNCTION = "FUNCTION"
    LET = "LET"
