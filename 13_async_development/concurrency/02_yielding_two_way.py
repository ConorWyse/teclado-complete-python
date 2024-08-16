from collections import deque

friends = deque(('Rolf', 'Jose', 'Charlie', 'Jen', 'Anna'))


def get_friend():
    yield from friends


# Use a generator to greet friends
def greet(g):
    while True:
        try:
            friend = next(g)
            yield f'Hello {friend}'
        except StopIteration:
            pass


fg = get_friend()
g = greet(fg)

print(next(g))
print(next(g))



# print(next(fg))
# print(next(fg))
# print(next(get_friend()))
# print(next(fg))
# print(next(get_friend()))
