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