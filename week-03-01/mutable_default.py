# Mutable Default Argument Bug

def f(x, cache=[]):
    cache.append(x)
    return cache

print("Before fixing:")
print(f(10))
print(f(20))
print(f(30))

# Fixed version
def f_fixed(x, cache=None):
    if cache is None:
        cache = []

    cache.append(x)
    return cache

print("\nAfter fixing:")
print(f_fixed(10))
print(f_fixed(20))
print(f_fixed(30))