def try_char_at(input: str, index: int) -> str | None:
    try:
        return input[index]
    except:
        return None

def try_item_at(input: list, index: int):
    try:
        return input[index]
    except:
        return None
    
