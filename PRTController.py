from PRTEntry import PRTEntry
from collections import defaultdict


class PRTController(object):

    def __init__(self, prt):
        self.prt_file = prt
        self.runs = defaultdict(list)

    def add_runs(self, term):
        opened = open(self.prt_file)
        i = 0
        for line in opened:
            if line.strip().startswith(term) and i > 5 and i < 11:
                temp = PRTEntry()
                temp.read_type_info(line)

                self._skip_lines(opened, term)
                temp.read_cell_info(opened)

                self.runs[term] += [temp]
            elif line.strip().startswith(term) and i <= 5:
                i += 1
            elif i == 11:
                break
        opened.close()

    def _skip_lines(self, f, term):
        for line in f:
            if line.strip().startswith(term):
                return

if __name__ == '__main__':
    from sys import argv

    test = PRTController(argv[1])
    test.add_runs()
    print(str(test.runs))
