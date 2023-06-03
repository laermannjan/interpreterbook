from dataclasses import dataclass
from enum import Enum, auto


class TokenType(Enum):
    ILLEGAL = auto()
    EOF = auto()

    IDENT = auto()
    INT = auto()

    ASSIGN = auto()
    PLUS = auto()
    MINUS = auto()
    BANG = auto()
    ASTERISK = auto()
    SLASH = auto()

    LT = auto()
    GT = auto()
    EQ = auto()
    NOT_EQ = auto()

    LPAREN = auto()
    RPAREN = auto()
    LBRACE = auto()
    RBRACE = auto()
    COMMA = auto()
    SEMICOLON = auto()

    FN = auto()
    LET = auto()

    IF = auto()
    ELSE = auto()
    RETURN = auto()
    TRUE = auto()
    FALSE = auto()


@dataclass(frozen=True)
class Token:
    token_type: TokenType
    literal: str | None = None

    def __repr__(self) -> str:
        if self.literal is None:
            return f"Token({self.token_type})"
        return f"Token({self.token_type}, {self.literal})"


OPERATORS = {
    "=": TokenType.ASSIGN,
    "+": TokenType.PLUS,
    "-": TokenType.MINUS,
    "!": TokenType.BANG,
    "*": TokenType.ASTERISK,
    "/": TokenType.SLASH,
    "<": TokenType.LT,
    ">": TokenType.GT,
    "==": TokenType.EQ,
    "!=": TokenType.NOT_EQ,
}

DELIMITERS = {
    "(": TokenType.LPAREN,
    ")": TokenType.RPAREN,
    "{": TokenType.LBRACE,
    "}": TokenType.RBRACE,
    ",": TokenType.COMMA,
    ";": TokenType.SEMICOLON,
}

KEYWORDS = {
    "fn": TokenType.FN,
    "let": TokenType.LET,
    "return": TokenType.RETURN,
    "if": TokenType.IF,
    "else": TokenType.ELSE,
    "true": TokenType.TRUE,
    "false": TokenType.FALSE,
}
