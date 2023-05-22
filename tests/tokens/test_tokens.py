import pytest
from monkey.tokens.tokens import Tokens, Token

from monkey.lexer.lexer import Lexer


@pytest.mark.parametrize(
    "input, expected_tokens",
    [
        (
            """let five = 5;
let ten = 10;

let add = fn(x, y) {
  x + y;
};

let result = add(five, ten);
!-/*5;
5 < 10 > 5;

if (5 < 10) {
    return true;
} else {
    return false;
}

10 == 10;
10 != 9;""",
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
                Token(Tokens.SEMICOLON, ";"),
                Token(Tokens.INT, "5"),
                Token(Tokens.LT, "<"),
                Token(Tokens.INT, "10"),
                Token(Tokens.GT, ">"),
                Token(Tokens.INT, "5"),
                Token(Tokens.SEMICOLON, ";"),
                Token(Tokens.IF, "if"),
                Token(Tokens.LPAREN, "("),
                Token(Tokens.INT, "5"),
                Token(Tokens.LT, "<"),
                Token(Tokens.INT, "10"),
                Token(Tokens.RPAREN, ")"),
                Token(Tokens.LBRACE, "{"),
                Token(Tokens.RETURN, "return"),
                Token(Tokens.TRUE, "true"),
                Token(Tokens.SEMICOLON, ";"),
                Token(Tokens.RBRACE, "}"),
                Token(Tokens.ELSE, "else"),
                Token(Tokens.LBRACE, "{"),
                Token(Tokens.RETURN, "return"),
                Token(Tokens.FALSE, "false"),
                Token(Tokens.SEMICOLON, ";"),
                Token(Tokens.RBRACE, "}"),
                Token(Tokens.INT, "10"),
                Token(Tokens.EQ, "=="),
                Token(Tokens.INT, "10"),
                Token(Tokens.SEMICOLON, ";"),
                Token(Tokens.INT, "10"),
                Token(Tokens.NOT_EQ, "!="),
                Token(Tokens.INT, "9"),
                Token(Tokens.SEMICOLON, ";"),
                Token(Tokens.EOF, ""),
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
