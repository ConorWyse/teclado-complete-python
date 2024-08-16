# Use "generators" to mimic threads

from collections import deque

friends = deque(('Rolf', 'Jose', 'Charlie', 'Jen', 'Anna'))

# This is really just a generator but it's called a coroutine because it takes in data and can be suspended
def friend_upper():
    while friends:
        friend = friends.popleft().upper()
        greeting = yield
        print(f'{greeting} {friend}')


def greet(g):
    yield from g
    # 'yield from g' is the same as these 4 lines:
    # g.send(None)
    # while True:
    #     greeting = yield
    #     g.send(greeting)


greeter = greet(friend_upper())
greeter.send(None)      # Prime the generator
greeter.send('Yo')      # Outputs: Yo ROLF
greeter.send('Hello')   # Outputs: Hello JOSE
greeter.send('Cheers')  # Outputs: Cheers CHARLIE

#   Note: instead of doing:
# greeter = greet(friend_upper())
#   We could have skipped a level and been more direct. That also works. That is, this:
# greeter = friend_upper()
#   So why use the indirect route? We'll see why in the 'async_await' example.
