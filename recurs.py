def u(a):
    if a == 0:

        return 1
    else:
        return a*u(a-1)

print(u(5))
exec(input(">>>"))
exec(input(">>>"))
