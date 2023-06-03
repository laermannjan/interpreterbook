from dataclasses import dataclass, field
from typing import Iterable
from monkey.lexer import Lexer
from monkey.token import Token, TokenType


@dataclass
class Repl:
    history: list[tuple[str, str]] = field(default_factory=list)

    def run(self) -> None:
        while True:
            line = input(">> ")
            if line == "exit":
                break
            elif line == "history":
                for i, (inp, out) in enumerate(self.history):
                    print(f"{i + 1}:\n{inp}\n{out}")
            else:
                output = "\n".join([repr(tok) for tok in self.tokenize(line)])
                self.history.append((line, output))
                print(output)

    def tokenize(self, input: str) -> Iterable[Token]:
        lexer = Lexer(input)
        while tok := lexer.next_token():
            yield tok
            if tok.token_type == TokenType.EOF:
                break
