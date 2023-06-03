use crate::lexer::Lexer;
use crate::token::Token;
use std::io::{stdin, Result, Write};

pub fn run_repl() -> Result<()> {
    print_prompt();
    for line in stdin().lines() {
        let input = line.unwrap();
        let mut lexer = Lexer::new(input);
        loop {
            let tok = lexer.next_token().unwrap();
            println!("{:?}", tok);
            if tok == Token::Eof {
                break;
            }
        }
        print_prompt();
    }
    Ok(())
}

fn print_prompt() {
    print!(">> ");
    std::io::stdout().flush().unwrap();
}
