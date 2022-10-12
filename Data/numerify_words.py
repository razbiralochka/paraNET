import re, sys, pathlib
from collections import Counter

sys.path.append(pathlib.Path(__file__).parent.parent.__str__())

# Увы, vscode не переваривает данную архитектуру каталогов и работает с директорией не файла, а запуска vscode
__par_dir = pathlib.Path(__file__).parent
open_file = lambda path, mode: open(__par_dir.joinpath(path), mode, encoding="utf-8")

from WordSimplifier.word_changer import get_base_word as gbw

text_file = open_file("sentences.txt", "r")
word_lists = [
    [gbw(word) for word in re.split("[^а-яё]", line.lower()) if word]
    for line in text_file.readlines()
]  # [line][word]
text_file.close()

set_ = set(word for line in word_lists for word in line)
dict_ = dict((word, i) for i, word in enumerate(set_))

matrix = [[0] * len(set_) for _ in word_lists]
for i, line in enumerate(word_lists):
    for word, cnt in Counter(line).items():
        matrix[i][dict_[word]] = cnt

test = [" ".join(map(str, line)) for line in matrix]


new_file = open_file("numericWords.txt", "w")
new_file.writelines((" ".join(map(str, line)) + "\n" for line in matrix))
new_file.close()

print("Done!")
