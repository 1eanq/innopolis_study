global_variable = 10


def outer_function(outer_variable):
    local_variable = 5
    sum_result = global_variable + outer_variable + local_variable
    return sum_result


result = outer_function(15)
print(result)
