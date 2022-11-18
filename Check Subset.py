class Farhad:
    def __init__(self,t):
        self.t=t
    def TakeInput(self):
        for i in range(0,self.t):
            self.a=int(input())
            self.b=set(list(map(int,input().split())))
            self.c=int(input())
            self.d=set(list(map(int,input().split())))
            print(self.b.issubset(self.d))
farhad=Farhad(t=int(input()))
farhad.TakeInput()
'''t=int(input())
for i in range(0,t):
    a=int(input())
    b=list(map(int,input().split()))
    b1=set(b)
    c=int(input())
    d=list(map(int,input().split()))
    d1=set(d)
    print(b1.issubset(d1))'''
