from pathlib import Path

__par_dir = Path(__file__).parent
open_file = lambda path, mode: open(__par_dir.joinpath(path), mode, encoding="utf-8")

if __name__ == "__main__":
	# test module here
	from word_changer import get_base_word as gbw
	line = input()
	while line:
		print(gbw(line))
		print()
		line = input()