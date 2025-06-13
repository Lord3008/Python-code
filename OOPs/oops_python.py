class chatbook:
    def __init__(self):
        self.username = ""
        self.password = ""
        self.loggedin = False
        self.menu()
    
    def menu(self):
        user_input = input("""Enter 1. to signup, 
                                    2. to signinn, 
                                    3. to write a post, 
                                    4. msg a friend, 
                                    5. Anyother key to exit """)
        if user_input == "1":
            self.signup()
        elif user_input == "2":
            self.signin()
        elif user_input == "3":
            if self.loggedin:
                self.write_post()
            else:
                print("You need to be logged in to write a post.")
                self.menu()
        elif user_input == "4":
            if self.loggedin:
                self.msg_friend()
            else:
                print("You need to be logged in to message a friend.")
                self.menu()
        else:
            print("Exiting the application. Goodbye!")
            return
    
    def signup(self):
        self.username = input("Enter your username: ")
        self.password = input("Enter your password: ")
        print(f"User {self.username} signed up successfully!")
        print("\n")
        self.menu()
    
    def signin(self):
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        if username == self.username and password == self.password:
            self.loggedin = True
            print(f"User {self.username} signed in successfully!")
        else:
            print("Invalid credentials. Please try again.")
        print("\n")
        self.menu()
    
    def write_post(self):
        if not self.loggedin:
            print("You need to be logged in to write a post.")
            self.menu()
            return
        post_content = input("Write your post: ")
        print(f"Post created: {post_content}")
        print("\n")
        self.menu()
    
    def msg_friend(self):
        if not self.loggedin:
            print("You need to be logged in to message a friend.")
            self.menu()
            return
        friend_username = input("Enter the friend's username: ")
        message_content = input("Write your message: ")
        print(f"Message sent to {friend_username}: {message_content}")
        print("\n")
        self.menu()
    
#obj = chatbook()

