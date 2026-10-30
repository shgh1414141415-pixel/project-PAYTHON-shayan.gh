n = int(input(" خط  "))

triangle = []

for i in range(n):
    خط = [1]

    for j in range(1, i):
       خط .append(triangle[i-1][j-1] + triangle[i-1][j])

    if i > 0:
        خط .append(1)

    triangle.append( خط )

for خط  in triangle:
    print( خط )