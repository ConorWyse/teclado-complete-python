import functools

# User identity dictionary
user = {
    'id': 1,
    'name': 'jose',
    'role': 'badmin'
}


# Define a check_permission() decorator:
def check_permission(func):
    @functools.wraps(func)
    def secure_func():
        if user.get('role') == 'admin':
            return func()
        else:
            return PermissionError
    return secure_func


@check_permission
def delete_database():
    """
    Will __doc__ show this or something from 'secure_func'?
    """
    print('Database deleted!')


delete_database()

print(delete_database.__name__)
print(delete_database.__doc__)
