mod lexer;
mod repl;
mod token;

use crate::repl::run_repl;
use std::io;

fn main() -> io::Result<()> {
    run_repl()
}
