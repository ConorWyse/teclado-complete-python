import functools

# User identity dictionary
user = {
    'id': 1,
    'name': 'jose',
    'role': 'badmin'
}


# Define a check_permission() decorator:
def check_permission(required_role):
    def check_permission_decorator(func):
        @functools.wraps(func)
        def secure_func(*args, **kwargs):
            if user.get('role') == required_role:
                return func(*args, **kwargs)
            else:
                return PermissionError
        return secure_func
    return check_permission_decorator


@check_permission('admin')
def delete_database():
    """
    Will __doc__ show this or something from 'secure_func'?
    """
    print('Database deleted!')


@check_permission('admin')
def something_silly(msg):
    """
    This is 'something_silly'
    """
    print(f"{msg} You must be an admin to see this message.")


delete_database()
something_silly('woot!')


print(delete_database.__name__)
print(delete_database.__doc__)
print(something_silly.__name__)
print(something_silly.__doc__)
