# create a class
class Comment:
    # create the constructor
    def __init__(self, username, content, likes=0):
        self.username = username
        self.content = content
        self.likes = likes


# apply the constructor to an object

comment = Comment("user1", "I like this book")
print(comment.username)
print(comment.content)
print(comment.likes)
