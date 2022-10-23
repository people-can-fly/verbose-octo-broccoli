Hodges: int = 14


def isHarshad(num: int) -> bool:
    num_str_list = [int(x) for x in str(num)]
    return num % sum(num_str_list) == 0


def isSiete(num: int) -> bool:
    num_str = str(num)
    return len(num_str) >= 2 and num_str[-2] == '7'
