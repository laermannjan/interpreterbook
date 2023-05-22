import pytest
from monkey.token.token import Tokens, Token


@pytest.mark.parametrize(
    "input, expected_tokens",
    [
        (
            "=+(){},;",
            [
                Token(Tokens.ASSIGN, "="),
                Token(Tokens.PLUS, "+"),
                Token(Tokens.LPAREN, "("),
                Token(Tokens.RPAREN, ")"),
                Token(Tokens.LBRACE, "{"),
                Token(Tokens.RBRACE, "}"),
                Token(Tokens.COMMA, ","),
                Token(Tokens.SEMICOLON, ";"),
            ],
        ),
    ],
)
def test_next_token(input, expected_tokens):
    # lexer = Lexer(input)
    lexer = input
    for t in expected_tokens:
        tok = lexer.next_token()
        assert (
            tok.type == t.type
        ), f"Token type wrong. expected={t.type}, got={tok.type}"
        assert (
            tok.literal == t.literal
        ), f"Token literal wrong. expected={t.literal}, got={tok.literal}"
