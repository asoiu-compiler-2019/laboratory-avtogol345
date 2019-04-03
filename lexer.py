import token_types
import character_util as psh
from my_token import Token


class Lexer(object):
    # constructor
    def __init__(self, file):
        self.defined_keywords_list = token_types.defined_keywords_list
        self.supported_operators = token_types.supported_operators
        self.operators_KeyValue_list = token_types.operators_KeyValue_list

        self.array_index = 0
        self.token = Token()
        self.token_lst = []

        # read in input_file file
        with open(file, 'r') as pascal_testfile:
            self.input_file = pascal_testfile.read().lower()

    def token_builder(self, tempWord, keyValue):
        return Token.build_token(self.token, tempWord, token_types.defined_keywords_list.get(keyValue).upper())

    def op_token_builder(self, tempOperator):
        return Token.build_token(self.token, tempOperator,
                                 'TK_' + self.operators_KeyValue_list.get(tempOperator))

    def scan(self):
        while len(self.input_file) > self.array_index:

            if self.input_file[self.array_index].isalpha():
                self.token_lst.append(self.if_letter())
            elif self.input_file[self.array_index].isdigit():
                self.token_lst.append(self.if_number())
            elif self.input_file[self.array_index] in self.supported_operators:
                self.token_lst.append(self.if_operator())
            elif self.input_file[self.array_index] == " ":
                self.array_index += 1
                self.token.set_colNumber(self.token.get_colNumber() + 1)
            elif self.input_file[self.array_index] == "\n":
                self.array_index += 1
                self.token.set_rowNumber(self.token.get_rowNumber() + 1)
                self.token.set_colNumber(0)
            elif self.input_file[self.array_index] == "\'":
                self.token_lst.append(self.if_quote())
            else:
                raise TypeError("Can't identify char: " + self.input_file[self.array_index])

        eof = self.token.build_token("EOF", token_types.defined_keywords_list.get("eof").upper())
        self.token_lst.append(eof)

        return self.token_lst

    def if_letter(self):
        # Parameters
        # Returns: A token which was returned by the helper function

        word_infile = ""
        # Loop through each character
        for character in self.input_file[self.array_index:]:
            # create string
            if character.isalpha() or character.isdigit():
                word_infile += character
            else:
                return psh.help_caseLetter(self, word_infile)

    def if_number(self):
        # Parameters
        # Returns: A token which was returned by the helper function

        digit_infile = ""

        while self.array_index < len(self.input_file):
            # create string of numbers
            if self.input_file[self.array_index].isdigit() or \
                    self.input_file[self.array_index] == '.':
                digit_infile += self.input_file[self.array_index]
                self.array_index += 1
                self.token.set_colNumber(self.token.get_colNumber() + 1)
            else:
                return psh.help_caseNum(self, digit_infile)

    def if_operator(self):
        # Parameters
        # Returns: A token which was returned by one of the helper functions

        tempOperator = ""

        while self.array_index < len(self.input_file):

            tempOperator += self.input_file[self.array_index]

            # check if single colon or assignment
            if self.input_file[self.array_index] == ":":
                return psh.help_caseOperator(self, tempOperator, self.input_file[self.array_index + 1])

            # check if <, <=, or !=
            elif self.input_file[self.array_index] in "<!":
                return psh.check_lte_notequal(self, tempOperator, self.input_file[self.array_index + 1])

            # if greater than or gte
            elif self.input_file[self.array_index] == ">":
                return psh.help_caseOperator(self, tempOperator, self.input_file[self.array_index + 1])

            # check if a comment
            elif self.input_file[self.array_index] == "(":
                return psh.check_comment(self, tempOperator, self.input_file[self.array_index + 1])
            else:
                self.array_index += 1
                self.token.set_colNumber(self.token.get_colNumber() + 1)

                return self.op_token_builder(tempOperator)

    def if_comment(self, current, next):
        # Parameters
        # Returns: A comment token

        curr_comment = ""
        curr_comment += current + next
        self.array_index += 2
        self.token.set_colNumber(self.token.get_colNumber() + 2)

        while self.array_index < len(self.input_file) and \
                self.input_file[self.array_index] != "*" and self.input_file[self.array_index + 1] != ")":
            curr_comment += self.input_file[self.array_index]
            psh.help_caseComment(self)

        if self.array_index >= len(self.input_file):
            return "Comment never completed"

        curr_comment += self.input_file[self.array_index] + self.input_file[self.array_index + 1]
        self.array_index += 2
        self.token.set_colNumber(self.token.get_colNumber() + 2)
        return self.token.build_token(curr_comment, token_types.defined_keywords_list.get("comment").upper())

    def if_quote(self):
        # Parameters
        # Returns: A token of type string which was returned by the helper function

        built_string = ""

        built_string += self.input_file[self.array_index]
        self.array_index += 1
        self.token.set_colNumber(self.token.get_colNumber() + 1)

        while self.array_index < len(self.input_file):
            psh.help_caseQuote(self, built_string, self.input_file[self.array_index])

        # throw an error if the file ends before the string is completed
        if self.array_index >= len(self.input_file):
            return "String never completed"
