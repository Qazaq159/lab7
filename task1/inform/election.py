def election(x: bool, y: bool, z: bool) -> bool:
    return (x and y) or (x and z) or (y and z)


x, y, z = map(int, input().split())
print(election(x, y, x))

