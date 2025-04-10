for dan in range(2, 10):
    print(f"#  {dan}단  #", end=" ")
print()

for i in range(1, 10):
    for dan in range(2, 10):
        print(f"{dan}X{i} = {dan*i:2}", end="  ")
    print()