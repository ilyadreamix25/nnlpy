from sys import argv
from parser.tokenizer import NNLTokenizer
from utility.linq import try_item_at

if __name__ == "__main__":
    if fpath := try_item_at(argv, 1):
        with open(fpath, encoding="utf-8") as f:
            tokens = NNLTokenizer.tokenize(f.read())
            for token in tokens:
                print(f"{token.key} -> {token.value}")
    else:
        print(f"Cannot open file {fpath}")
