from monkey.token import TokenType, Token

from monkey.lexer import Lexer


def test_int():
    input = "5"
    lexer = Lexer(input)
    tok = lexer.next_token()
    assert (
        tok.token_type == TokenType.INT
    ), f"Token type wrong. expected={TokenType.INT}, got={tok}"
    assert tok.literal == "5", f"Token literal wrong. expected={5}, got={tok}"


def test_next_token():
    input = """let five = 5;
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
10 != 9;"""

    expected_tokens = (
        Token(TokenType.LET),
        Token(TokenType.IDENT, "five"),
        Token(TokenType.ASSIGN),
        Token(TokenType.INT, "5"),
        Token(TokenType.SEMICOLON),
        Token(TokenType.LET),
        Token(TokenType.IDENT, "ten"),
        Token(TokenType.ASSIGN),
        Token(TokenType.INT, "10"),
        Token(TokenType.SEMICOLON),
        Token(TokenType.LET),
        Token(TokenType.IDENT, "add"),
        Token(TokenType.ASSIGN),
        Token(TokenType.FN),
        Token(TokenType.LPAREN),
        Token(TokenType.IDENT, "x"),
        Token(TokenType.COMMA),
        Token(TokenType.IDENT, "y"),
        Token(TokenType.RPAREN),
        Token(TokenType.LBRACE),
        Token(TokenType.IDENT, "x"),
        Token(TokenType.PLUS),
        Token(TokenType.IDENT, "y"),
        Token(TokenType.SEMICOLON),
        Token(TokenType.RBRACE),
        Token(TokenType.SEMICOLON),
        Token(TokenType.LET),
        Token(TokenType.IDENT, "result"),
        Token(TokenType.ASSIGN),
        Token(TokenType.IDENT, "add"),
        Token(TokenType.LPAREN),
        Token(TokenType.IDENT, "five"),
        Token(TokenType.COMMA),
        Token(TokenType.IDENT, "ten"),
        Token(TokenType.RPAREN),
        Token(TokenType.SEMICOLON),
        Token(TokenType.BANG),
        Token(TokenType.MINUS),
        Token(TokenType.SLASH),
        Token(TokenType.ASTERISK),
        Token(TokenType.INT, "5"),
        Token(TokenType.SEMICOLON),
        Token(TokenType.INT, "5"),
        Token(TokenType.LT),
        Token(TokenType.INT, "10"),
        Token(TokenType.GT),
        Token(TokenType.INT, "5"),
        Token(TokenType.SEMICOLON),
        Token(TokenType.IF),
        Token(TokenType.LPAREN),
        Token(TokenType.INT, "5"),
        Token(TokenType.LT),
        Token(TokenType.INT, "10"),
        Token(TokenType.RPAREN),
        Token(TokenType.LBRACE),
        Token(TokenType.RETURN),
        Token(TokenType.TRUE),
        Token(TokenType.SEMICOLON),
        Token(TokenType.RBRACE),
        Token(TokenType.ELSE),
        Token(TokenType.LBRACE),
        Token(TokenType.RETURN),
        Token(TokenType.FALSE),
        Token(TokenType.SEMICOLON),
        Token(TokenType.RBRACE),
        Token(TokenType.INT, "10"),
        Token(TokenType.EQ),
        Token(TokenType.INT, "10"),
        Token(TokenType.SEMICOLON),
        Token(TokenType.INT, "10"),
        Token(TokenType.NOT_EQ),
        Token(TokenType.INT, "9"),
        Token(TokenType.SEMICOLON),
        Token(TokenType.EOF),
    )
    lexer = Lexer(input)
    for t in expected_tokens:
        tok = lexer.next_token()
        assert (
            tok.token_type == t.token_type
        ), f"Token type wrong. expected={t}, got={tok}"
        assert tok.literal == t.literal, f"Token literal wrong. expected={t}, got={tok}"
