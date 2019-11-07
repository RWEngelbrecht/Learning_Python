'''
    vars:   bio, interests[tags], pics, sexual_pref, fame_rating
    methods:   - modify: username, password;
               - find_geo
               -
'''

class User:

    def __init__(self, email, first_name, last_name, username):
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.username = username

    def mark(self, ques, ans):
        if ques == 1:
            if ans == "b":
                return 1
        if ques == 2:
            if ans == "c":
                return 1
        if ques == 3:
            if ans == "c":
                return 1
        return 0
