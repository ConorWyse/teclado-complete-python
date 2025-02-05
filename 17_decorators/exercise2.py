from functools import wraps

admin_level = 0
user_level = 1
guest_level = 2


def get_current_user_role() -> int:
    # return the current user's role, represented by an int
    # for example, 0 - admin, 1 - user, 2 - guest
    # You don't need to change this function, we will replace it with a real function that returns the user's role
    return 0


def access_control(access_level: int):
    def my_decorator(func):
        @wraps(func)
        def secure_func(*args, **kwargs):
            if get_current_user_role() <= access_level:
                print("You da man!")
                return func(*args, **kwargs)
            else:
                raise PermissionError("You do not have the proper access level.")
        return secure_func
    return my_decorator


# Test decorator on function that takes a parameter
@access_control(user_level)
def delete_some_file(filename):
    # perform the deletion operation
    print('{} is deleted!'.format(filename))


delete_some_file('temp.txt')


# Test decorator on function that doesn't take a parameter
@access_control(admin_level)
def delete_MBR():
    print('Master Boot Record is deleted!')

delete_MBR()
