import pytest
from monkey.token.token import Tokens, Token

from monkey.lexer.lexer import Lexer


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
        (
            """let five = 5;
let ten = 10;

let add = fn(x, y) {
  x + y;
};

let result = add(five, ten);""",
            [
                Token(Tokens.LET, "let"),
                Token(Tokens.IDENT, "five"),
                Token(Tokens.ASSIGN, "="),
                Token(Tokens.INT, "5"),
                Token(Tokens.SEMICOLON, ";"),
                Token(Tokens.LET, "let"),
                Token(Tokens.IDENT, "ten"),
                Token(Tokens.ASSIGN, "="),
                Token(Tokens.INT, "10"),
                Token(Tokens.SEMICOLON, ";"),
                Token(Tokens.LET, "let"),
                Token(Tokens.IDENT, "add"),
                Token(Tokens.ASSIGN, "="),
                Token(Tokens.FUNCTION, "fn"),
                Token(Tokens.LPAREN, "("),
                Token(Tokens.IDENT, "x"),
                Token(Tokens.COMMA, ","),
                Token(Tokens.IDENT, "y"),
                Token(Tokens.RPAREN, ")"),
                Token(Tokens.LBRACE, "{"),
                Token(Tokens.IDENT, "x"),
                Token(Tokens.PLUS, "+"),
                Token(Tokens.IDENT, "y"),
                Token(Tokens.SEMICOLON, ";"),
                Token(Tokens.RBRACE, "}"),
                Token(Tokens.SEMICOLON, ";"),
                Token(Tokens.LET, "let"),
                Token(Tokens.IDENT, "result"),
                Token(Tokens.ASSIGN, "="),
                Token(Tokens.IDENT, "add"),
                Token(Tokens.LPAREN, "("),
                Token(Tokens.IDENT, "five"),
                Token(Tokens.COMMA, ","),
                Token(Tokens.IDENT, "ten"),
                Token(Tokens.RPAREN, ")"),
                Token(Tokens.SEMICOLON, ";"),
            ],
        ),
        (
            """let five = 5;
let ten = 10;

let add = fn(x, y) {
  x + y;
};

let result = add(five, ten);
!-/*5""",
            [
                Token(Tokens.LET, "let"),
                Token(Tokens.IDENT, "five"),
                Token(Tokens.ASSIGN, "="),
                Token(Tokens.INT, "5"),
                Token(Tokens.SEMICOLON, ";"),
                Token(Tokens.LET, "let"),
                Token(Tokens.IDENT, "ten"),
                Token(Tokens.ASSIGN, "="),
                Token(Tokens.INT, "10"),
                Token(Tokens.SEMICOLON, ";"),
                Token(Tokens.LET, "let"),
                Token(Tokens.IDENT, "add"),
                Token(Tokens.ASSIGN, "="),
                Token(Tokens.FUNCTION, "fn"),
                Token(Tokens.LPAREN, "("),
                Token(Tokens.IDENT, "x"),
                Token(Tokens.COMMA, ","),
                Token(Tokens.IDENT, "y"),
                Token(Tokens.RPAREN, ")"),
                Token(Tokens.LBRACE, "{"),
                Token(Tokens.IDENT, "x"),
                Token(Tokens.PLUS, "+"),
                Token(Tokens.IDENT, "y"),
                Token(Tokens.SEMICOLON, ";"),
                Token(Tokens.RBRACE, "}"),
                Token(Tokens.SEMICOLON, ";"),
                Token(Tokens.LET, "let"),
                Token(Tokens.IDENT, "result"),
                Token(Tokens.ASSIGN, "="),
                Token(Tokens.IDENT, "add"),
                Token(Tokens.LPAREN, "("),
                Token(Tokens.IDENT, "five"),
                Token(Tokens.COMMA, ","),
                Token(Tokens.IDENT, "ten"),
                Token(Tokens.RPAREN, ")"),
                Token(Tokens.SEMICOLON, ";"),
                Token(Tokens.BANG, "!"),
                Token(Tokens.MINUS, "-"),
                Token(Tokens.SLASH, "/"),
                Token(Tokens.ASTERISK, "*"),
                Token(Tokens.INT, "5"),
            ],
        ),
    ],
)
def test_next_token(input, expected_tokens):
    lexer = Lexer(input)
    # lexer = input
    for t in expected_tokens:
        tok = lexer.next_token()
        assert tok.type == t.type, f"Token type wrong. expected={t}, got={tok}"
        assert tok.literal == t.literal, f"Token literal wrong. expected={t}, got={tok}"
