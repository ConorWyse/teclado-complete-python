import functools

# User identity dictionary
user = {
    'id': 1,
    'name': 'jose',
    'role': 'admin'
}


# Define a check_permission() decorator:
def check_permission(required_role):
    def check_permission_decorator(func):
        @functools.wraps(func)
        def secure_func():
            if user.get('role') == required_role:
                return func()
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


delete_database()

# print(delete_database.__name__)
# print(delete_database.__doc__)
