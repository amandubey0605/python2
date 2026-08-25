# WAP to find out whether a given post is talking about"aman" or not.
Post=input("Enter the post: ")

if("aman".lower() in Post.lower()):
    print("this is talking about: ",Post)
else:
    print("post is not talking about post")    