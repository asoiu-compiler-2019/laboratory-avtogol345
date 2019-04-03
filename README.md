# Compiler
Compiler written in python without external dependencies

# BNF
```
program = "program", identifier, ";", block, ".";
functions = {"function", identifier, "(", var_dec, ")", ";", block};
block = [functions], ["var", var_dec], [statements];
var_dec = (identifier, {,",", identifier}, ":", type, ";")+
statements = "begin", statement, {";", statement}, "end";
statement = attribution | statements | print | if | while;
attribution = identifier, "=", (expression | read);
print = "print", "(", expression, ")";
read = "read", "(", ")";
if = "if", rel_expression, "then", statement, ["else" statement"];
while = "while", rel_expression, "do", statement;
rel_expression = expression, {comp, expression};
expression = term, { ("+"|"-"|"or"), term, };
term = factor, { ("*" | "/" | "and"), factor };
factor = ("+" | "-" | "not"), (factor | number | boolean | ("(" expression ")") | identifier | func_call);
func_call = identifier, "(", [expression, {",", expression}], ")";
identifier = letter, {letter | digit | "_" };
comp = ">" | "<" | "==" | "!=";
number = digit+;
boolean = "true" | "false";
type = "int" | "boolean";
letter = [a-zA-Z];
digit = [0-9];
```
# Lexical Analyzer
The main task of lexical analysis is to read input characters in the code and produce tokens.

Lexical analyzer scans the entire source code of the program. It identifies each token one by one. 
Scanners are usually implemented to produce tokens only when requested by a parser. Here is how this works:
![Alt Text](https://www.guru99.com/images/1/020819_1105_LexicalAnal1.png)
1. "Get next token" is a command which is sent from the parser to the lexical analyzer.
1. On receiving this command, the lexical analyzer scans the input until it finds the next token.
1. It returns the token to Parser.

Lexical Analyzer skips whitespaces and comments while creating these tokens. If any error
is present, then Lexical analyzer will correlate that error with the source file and line number.
# Parser
The parser is a compiler component that breaks down data into smaller elements for easy translation into another language. The parser accepts 
input data in the form of a sequence of tokens or program instructions and usually builds the data structure in the form
of a parse tree or an abstract syntax tree.
## Syntax diagrams
### program
![GitHub Logo](/images/program.png)
### block
![GitHub Logo](/images/block.png)
### functions
![GitHub Logo](/images/functions.png)
### declaration
![GitHub Logo](/images/declaration.png)
### statements
![GitHub Logo](/images/statements.png)
### statement
![GitHub Logo](/images/statement.png)
## Stack Machine
In computer science, computer engineering and programming language implementations, a stack machine is a type of computer. In some cases, the term refers to a software scheme that simulates a stack machine. The main difference from other computers is that most of its instructions operate on a pushdown stack of numbers rather than numbers in registers. Most computer systems implement a stack in some form to pass parameters and link to subroutines. This does not make these computers stack machines.

### Operations codes
```
    push = 1
    pushi = 2
    halt = 3
    pop = 4
    print_int = 5
    print_char = 6
    print_bool = 7
    print_real = 8
    newline = 9
    logical_not = 10
    add = 11
    xchg = 12
    cvr = 13
    fadd = 14
    sub = 15
    fsub = 16
    divide = 17
    multiply = 18
    fmultiply = 19
    logical_or = 20
    greater_than = 21
    less_than = 22
    equal = 23
    not_equal = 24
    gte = 25
    lte = 26
    jfalse = 27
    jump = 28
    put = 29
    get = 30
    array_print = 31
```
### Compress bytes to save operation in stack
```
def compress_bytes(initial):
    shift_one = int(initial) >> 24
    shift_two = int(initial) >> 16
    shift_three = int(initial) >> 8
    shift_four = int(initial) >> 0

    f = 0xFF

    return shift_one & f, shift_two & f, shift_three & f, shift_four & f
```
### Decompress bytes to execute operation from stack
```
def decompress_bytes(compressed_version):
    shift_one = compressed_version[0] << 24
    shift_two = compressed_version[1] << 16
    shift_three = compressed_version[2] << 8
    shift_four = compressed_version[3] << 0

    return shift_one | shift_two | shift_three | shift_four
```

# Examples
## if else
##### Code
```
program testIf;

var
   a, b, max : integer;
begin
   a = 1;
   b = 5;

   if a > b then
        max = a;
   else
        max = b;

   print(max)

end.
```
##### Result
```
5
```

## for
##### Code
```
program forLoop;
var
   n: integer;

begin

   (* For loop example *)
   for n = 1  to 3 do
   begin
      print(n);
   end;
end.
```
##### Result
```
1
2
3
```

## while
##### Code
```
program whileLoop;

var
   a : integer;
begin
   a = 1;

   (* Example of while loop *)
   while  a != 3  do
   begin
      print(a);
      a = a + 1;
   end;

end.
```
##### Result
```
1
2
```

## array 
##### Code
```
program arrays;

var
    n: array [1..20] of integer;
var
    i, sum: integer;
var
    avg : real;

begin
    sum = 0;

    for i = 1 to 10 do
    begin
        n[ i ] = i;

        sum = sum + n[ i ];
    end;

    avg = sum / 20.0;
    print(avg);
end.
```
##### Result
```
2.75
```
