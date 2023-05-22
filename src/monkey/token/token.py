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
    MINUS = "-"
    BANG = "!"
    ASTERISK = "*"
    SLASH = "/"

    LT = "<"
    GT = ">"

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
    TRUE = "TRUE"
    FALSE = "FALSE"
    IF = "IF"
    ELSE = "ELSE"
    RETURN = "RETURN"


KEYWORDS = {
    "fn": Tokens.FUNCTION,
    "let": Tokens.LET,
    "true": Tokens.TRUE,
    "false": Tokens.FALSE,
    "if": Tokens.IF,
    "else": Tokens.ELSE,
    "return": Tokens.RETURN,
}


def lookup_ident(ident: str) -> TokenType:
    return KEYWORDS.get(ident, Tokens.IDENT)
