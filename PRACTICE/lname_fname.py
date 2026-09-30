@property
def check(self,s):
    
    self.fname = s.split(" ")[0]
    self.lname = s.split(" ")[1]
    return f"{self.fname} or {self.lname}"
syt="hello ammar"
check(syt)