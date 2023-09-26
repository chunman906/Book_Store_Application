import csv
# Class based context manager for handling files
class FileManager:
    def __init__(self, file_name, mode):
        self.file_name = file_name
        self.mode = mode
        self.newline = ''

    def __enter__(self):
        self.file = open(self.file_name, self.mode, newline=self.newline)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()
