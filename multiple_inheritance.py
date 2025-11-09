class A:
    def __init__(self):
        print("parent consturctor")
class B:
    def __init__(self):
        print("2nd parent constructor")
class C(A,B):
    def __init__(self):
        B.__init__(self)
        super().__init__()
        print("child constructor")

obj = C()
# 
class A:
    def f1(self):
        print("f1 parent consturctor")
class B:
    def f1(self):
        print("f1 2nd parent constructor")
class C(A,B):
    def f1(self):
        # B.f1(self)
        # super().f1()
        print("f1 child constructor")

obj = C()
obj.f1()
# eg 
class device:
    def __init__(self,brand,battery):
        self.brand = brand
        self.battery = battery
    def show_device_info(self):
        print("device brand:",self.brand)
        print("battery level:",self.battery)
    def use_battery(self,use):
        self.used_battery = use
        self.u = self.battery-self.used_battery
        print("battery used",self.u)
class network_enabled:
    def __init__(self):
        self.ip_address = "127:0:0:0"
        self.conected = False
    def connect(self):
        if self.conected ==False:
            self.conected =True
            print(f"connected to network:{self.ip_address}")
        else:
            self.conected =False
    def sync(self):
        if(self.conected == True):
            print("your data successfully sync")
class smarthealth(device,network_enabled):   
    def __init__(self,a,b):
        super().__init__(a,b)
        network_enabled.__init__(self)
        self.steps = 0
        self.heart_rate = 72
    def track_steps(self,ste):
        self.steps=ste
        self.steps+=ste
    def measure_rate(self,hea):
         self.heart_rate=hea
         self.heart_rate+=hea
    def health_summary(self):
        print("steps walked:",self.steps)
        print("heart rate updated:",self.heart_rate)
print(" ")
print("_____SMART HEALTH WATCH_____")
obj=smarthealth("apple",100)
obj.show_device_info()
obj.connect()
print(" ")
print("____INFORMATION AFTER CONNECTION_____")
print("======================================")
obj.track_steps(100)
obj.measure_rate(20)
obj.use_battery(30)
obj.health_summary()
obj.sync()

