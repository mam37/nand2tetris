class WriterMixin:
    def write(self, lines):
        self.outfile.writelines(map(lambda str: str + "\n", lines))
