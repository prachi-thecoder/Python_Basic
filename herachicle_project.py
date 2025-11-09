class user:
    def __init__(self,username,email):
        self.username = username
        self.email = email
    def display_info(self):
        print(self.username)
        print(self.email)
class custmer(user):
    def __init__(self,username,name):
        super().__init__(username,name)
        self.cart=[]
    def add_to_cart(self):
        self.item=input("enter a elements:")
        self.cart.append(self.item)
        print(f"{self.item} added to prachi 's cart")
    def display(self):
        print(self.cart)
        print(f"prachi s cart:{self.cart}")
class seller(user):
    def __init__(self,username,email):
        super().__init__(username,email)
        self.inventory=[]
    def add_product(self):
        self.item_inventory=input("enter a inventor elements:")
        self.inventory.append(self.item_inventory)
    def display_productinfo(self):
        print(self.inventory)
class admin(user):
    def __init__(self,username,email):
        super().__init__(username,email)
        self.permi=[]
    def permission(self):
        self.permi.append("manage_users")
        self.permi.append("manage_site")
        self.permi.append("view_report ")
    def display_permission(self):
        print(self.permi)

obj = seller("prajakta","prajakta21@gmail.com")
obj.display_info()
obj1 = custmer("prachi","prachi12@gmail.com")
obj1.add_to_cart()
obj1.display()
obj.add_product()
obj.display_productinfo()
obj2 = admin("praxii","praxi12@gmail.com")
obj2.display_info()
obj2.permission()
obj2.display_permission()


