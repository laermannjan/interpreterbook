from monkey.lexer.lexer import Lexer

from monkey.tokens.tokens import Tokens


PROMPT = ">>> "


def start_repl():
    while inp := input(PROMPT):
        lexer = Lexer(inp)
        while tok := lexer.next_token():
            if tok.type == Tokens.EOF:
                break
            print(tok)
