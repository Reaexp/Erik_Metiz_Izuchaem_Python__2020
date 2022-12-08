s = "123123"

var = s[::-1].replace('2', 'x', 1)[::-1]
var_2 = var[::-1].replace('3','я',1)[::-1]
print(var_2)
