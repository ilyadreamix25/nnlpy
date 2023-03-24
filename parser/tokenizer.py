"""
NoNameLanguage tokenizer
Copyright (c) 2023 IlyaDreamix
"""

from nnl.errors import UnclosedStringException
from nnl.primitives import NNLPrimitives

from parser.keywords import *
from parser.operators import *
from parser.spacers import *
from parser.special_symbols import *

from utility.linq import try_char_at


NEXT_WORD_IDS = [
    NNLSpecialSymbols.SEMICOLON,
    NNLSpecialSymbols.COLON,
    NNLSpecialSymbols.START_BLOCK,
    NNLSpecialSymbols.END_BLOCK,
    NNLSpecialSymbols.START_EXPRESSION,
    NNLSpecialSymbols.END_EXPRESSION,
    NNLSpecialSymbols.DOT,
    NNLSpacers.NEW_LINE,
    NNLSpacers.SPACE,
]
EMPTY_WORD = ""


class NNLToken:
    key: str
    value: str
    
    def __init__(self, key: str, value: str) -> None:
        self.key = key
        self.value = value
        
    SPECIAL_SYMBOL = "special_symbol"
    OPERATOR = "operator"
    VALUE = "value"
    KEYWORD = "keyword"
    NUMBER = "number"
    STRING = "string"
    PRIMITIVE = "primitive"


class NNLTokenizer:
    @staticmethod
    def tokenize(input: str) -> list[NNLToken]:
        """
        Translate NoNameLanguage code to the tokens for NNL parser
        
        :param input: Input code
        :return: Parsed tokens
        """
        
        word = EMPTY_WORD
        tokens = []
        
        for index, char in enumerate(input):
            next_char = try_char_at(input, index + 1)
            
            if char in NNLSpacers.ALL:
                continue
            
            if char in NNLSpecialSymbols.ALL and char != NNLSpecialSymbols.STRING:
                tokens.append(NNLToken(NNLToken.SPECIAL_SYMBOL, char))
                continue
            elif char == NNLSpecialSymbols.STRING:
                string_result = NNLTokenizer.parse_string(input, index)
                tokens.append(NNLToken(NNLToken.STRING, string_result[0]))
                
                new_input = input[string_result[1] + index:]
                tokens += NNLTokenizer.tokenize(new_input)
                
                break
            
            if char in NNLOperators.ALL:
                tokens.append(NNLToken(NNLToken.OPERATOR, char))
                continue
            
            word += char
            
            if next_char in NEXT_WORD_IDS:
                if word in NNLKeywords.ALL:
                    tokens.append(NNLToken(NNLToken.KEYWORD, word))
                elif word in NNLPrimitives.ALL:
                    tokens.append(NNLToken(NNLToken.PRIMITIVE, word))
                else:
                    tokens.append(NNLToken(NNLToken.VALUE, word))
                    
                word = EMPTY_WORD
        
        return tokens
    
    
    @staticmethod
    def parse_string(input: str, start: int) -> tuple[str, int]:  
        """
        Parse string from input that starts at ``start``
        
        :param input: Input code
        :param start: String start
        :return: Parsed string
        """
        
        chars_from_start = input[start + 1:]
        string = EMPTY_WORD
        string_end_index = start
        
        for index, char in enumerate(chars_from_start):
            if char == NNLSpecialSymbols.STRING:
                string_end_index = index
                break
            elif char == input[len(input) - 1]:
                raise UnclosedStringException
            else:
                string += char
            
            string_end_index = index
        
        return string, string_end_index + 2 # Add 2 because of ""-symbols skip
    