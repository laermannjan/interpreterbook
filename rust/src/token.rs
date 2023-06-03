#[allow(dead_code)]
#[derive(Debug, PartialEq)]
pub enum Token {
    Illegal,
    Eof,

    Ident(String),
    Int(String),

    // Keywords
    Let,
    Function,

    // Operators
    Assign,
    Bang,
    Plus,
    Minus,
    Slash,
    Asterisk,
    Comma,
    Semicolon,

    // Comparators
    LessThan,
    GreaterThan,
    Equal,
    NotEqual,

    // Delimiters
    LParen,
    RParen,
    LBrace,
    RBrace,

    If,
    Else,
    Return,
    True,
    False,
}
