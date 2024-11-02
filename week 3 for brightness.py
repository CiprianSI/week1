print("what level of brightness required?")
brightness_level = int(input())
for brightness in range(2,brightness_level+1, 2):
    print(f"brightness level is : {'*' * brightness }")