# our simple user passes test permission

# create a function
# takes in a user
# checks to if the role is teacher
def is_teacher(user):
    # return a boolean.
    return user.role == "Teacher"