from collections import deque
from types import coroutine

friends = deque(('Rolf', 'Jose', 'Charlie', 'Jen', 'Anna'))


@coroutine
def friend_upper():
    while friends:
        friend = friends.popleft().upper()
        greeting = yield
        print(f'{greeting} {friend}')


async def greet(g):
    # 'yield from g' ==> 'await g'; we need to use '@coroutine'  and 'async'
    await g



greeter = greet(friend_upper())
greeter = friend_upper()
greeter.send(None)
greeter.send('Yo')
greeter.send('Hello')
greeter.send('Cheers')
