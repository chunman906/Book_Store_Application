import logging
class NameIsNotMatch(Exception):
    pass

class IntIsNotMatch(Exception):
    pass

class FileNotFound(Exception):
    pass

class PasswordIsNotMatch(Exception):
    pass


# logging setup
logging.basicConfig(filename='logfile.log', level=logging.DEBUG, format="%(asctime)s | %(levelname)s | %(name)s | %(message)s")

