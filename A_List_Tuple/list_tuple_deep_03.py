import copy

original = [
        [10, 20],
        [30, 40]
]


print(f"Original: {original}")

shallow = original.copy()
deep = copy.deepcopy(original)

shallow[0][0] = 999
deep[1][1] = 777

print(f"Shallow: {shallow}")
print(f"Deep: {deep}")
print(f"Original: {original}")
