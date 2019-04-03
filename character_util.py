def help_caseLetter(lexer, temp_word):
    lexer.token.set_colNumber(lexer.token.get_colNumber() + len(temp_word))
    lexer.array_index += len(temp_word)

    # check if the string is a reserved keyword
    if temp_word in lexer.defined_keywords_list:
        return lexer.token_builder(temp_word, temp_word)
    # if not then it's a string literal
    else:
        return lexer.token_builder(temp_word, "id")


def help_caseNum(lexer, digit):
    if "." in digit:
        temp_index = digit.find(".")

        if digit.count('.') == 1:
            real_number = float(digit)
            return lexer.token_builder(real_number, "real")
        elif digit.count('.') == 2:
            return lexer.token_builder(digit, "range")
        else:
            return "Invalid number format"
    # if not a real number or a range then it has to be an integer
    else:
        real_number = int(digit)
        return lexer.token_builder(real_number, "integer")


def help_caseOperator(lexer, tempOperator, nextOperator):
    if nextOperator == "=":
        tempOperator += nextOperator
        lexer.array_index += 2
        lexer.token.set_colNumber(lexer.token.get_colNumber() + 2)
        return lexer.op_token_builder(tempOperator)
    else:
        lexer.array_index += 1
        lexer.token.set_colNumber(lexer.token.get_colNumber() + 1)
        return lexer.op_token_builder(tempOperator)


def check_lte_notequal(lexer, tempOperator, nextOperator):
    if nextOperator == ">":
        tempOperator += nextOperator
        lexer.array_index += 2
        lexer.token.set_colNumber(lexer.token.get_colNumber() + 2)
        return lexer.op_token_builder(tempOperator)
    elif nextOperator == "=":
        tempOperator += nextOperator
        lexer.array_index += 2
        lexer.token.set_colNumber(lexer.token.get_colNumber() + 2)
        return lexer.op_token_builder(tempOperator)
    else:
        lexer.array_index += 1
        lexer.token.set_colNumber(lexer.token.get_colNumber() + 1)
        return lexer.op_token_builder(tempOperator)


def check_comment(lexer, tempOperator, nextChar):
    if nextChar == "*":
        return lexer.if_comment(tempOperator, nextChar)
    else:
        lexer.array_index += 1
        lexer.token.set_colNumber(lexer.token.get_colNumber() + 1)
        return lexer.op_token_builder(tempOperator)


def help_caseQuote(lexer, tempString, current):
    # Check if it is the closing '
    if current == "\'":
        tempString += current
        lexer.array_index += 1
        lexer.token.set_colNumber(lexer.token.get_colNumber() + 1)
        return lexer.token_builder(tempString, "string")
    # else it is just another char
    else:
        tempString += current
        if current == "\n":
            lexer.token.set_colNumber(0)
            lexer.token.set_rowNumber(lexer.token.get_rowNumber() + 1)
        else:
            lexer.token.set_colNumber(lexer.token.get_colNumber() + 1)

        lexer.array_index += 1


def help_caseComment(lexer):
    # Parameters

    if lexer.input_file[lexer.array_index] == "\n":
        lexer.token.set_colNumber(lexer.token.get_colNumber() + 0)
        lexer.token.set_rowNumber(lexer.token.get_rowNumber() + 1)
    else:
        lexer.token.set_colNumber(lexer.token.get_colNumber() + 1)

    lexer.array_index += 1
