
class User:
    """create a class User """
    users = []

    def create(self, username, role, email, password):
        """create a user """
        new_user = {
            "user_id": len(User.users) + 1,
            "username": username,
            "role": role,
            "email":email,
            "password":password
            }
        User.users.append(new_user)  # save user

    def get_all_users(self):
        """ get all users """
        return User.users

    def get_one_users(self, user_id):
        """ get single user """
        for one_user in User.users:
            if one_user['user_id'] == "user_id":
                return one_user

            return False
