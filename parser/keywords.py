class NNLKeywords:
    CONSTANT = "const"
    VARIABLE = "var"
    
    INCLUDE = "include"
    USING = "using"
    
    FUNCTION = "fn"
    RETURN = "return"
    
    IF = "if"
    ELSE = "else"
    FOR = "for"
    WHILE = "while"
    TRUE = "true"
    FALSE = "false"
    
    ALL = [
        CONSTANT, VARIABLE,
        INCLUDE, USING,
        FUNCTION, RETURN,
        IF, ELSE, WHILE, TRUE, FALSE
    ]
    