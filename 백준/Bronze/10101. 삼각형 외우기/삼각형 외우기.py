def get_triangle_name(first, second, third):
    if (first + second + third) != 180:
        return 'Error'
    elif first == second and second == third:
        return 'Equilateral'
    elif first == second or second == third or first == third:
        return 'Isosceles'
    else:
        return 'Scalene'

first_degree = int(input())
second_degree = int(input())
third_degree = int(input())

result = get_triangle_name(first_degree, second_degree, third_degree)
print(result)