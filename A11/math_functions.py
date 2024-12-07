def pow(num, exp):
    return num ** exp

def div(num, deno):
    if deno == 0:
        raise ValueError("Error. 0 cannot be devided")
    return num / deno
