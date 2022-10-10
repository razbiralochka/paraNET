from util import open_file
from difflib import get_close_matches as __gcm

__fl = open_file("10k_most_recent.txt", "r")
__lines = __fl.readlines()
__fl.close()


def get_base_word(word):
    res_list = __gcm(word, __lines, 1)
    return (res_list[0] if res_list else word).strip()
