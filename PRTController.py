from PRTEntry import PRTEntry
from collections import defaultdict


class PRTController(object):

    def __init__(self, prt):
        self.prt_file = prt
        self.runs = defaultdict(list)

    def set_dims(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def add_runs(self, term):
        '''searches for term and creates PRTEntry for all data in term'''
        opened = open(self.prt_file)
        for line in opened:
            if line.strip().startswith(term):
                temp = PRTEntry(self.x, self.y, self.z)
                temp.read_type_info(line)

                self._skip_lines(opened, term)
                temp.read_cell_info(opened)

                self.runs[term] += [temp]
                print(temp.name+" at "+str(temp.time)+" read.")
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
