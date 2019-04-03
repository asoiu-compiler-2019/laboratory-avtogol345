class Token(object):
    def __init__(self):
        self.row_number = 1
        self.col_number = 1

    def get_rowNumber(self):
        return self.row_number

    def set_rowNumber(self, num):
        self.row_number = num

    def set_colNumber(self, num):
        self.col_number = num

    def get_colNumber(self):
        return self.col_number

    def build_token(self, value, tok_type):
        return value, tok_type, self.row_number, self.col_number
