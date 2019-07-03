class FileReader:
    def __init__(self, filename=None):
        self.filename = filename

    def read(self):
        try:
            f = open(self.filename, 'r')
            content = f.read()
            f.close()
            return ''.join(content.splitlines())
        except IOError:
            print('Error')
            return ''


if __name__ == '__main__':
    reader = FileReader('../../example.txt')
    print(reader.read())
