from dataclasses import dataclass
from enum import StrEnum

TokenType = str


@dataclass
class Token:
    type: TokenType
    literal: str


class Tokens(StrEnum):
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
