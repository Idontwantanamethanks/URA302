import math

# ------------------ Question 1 ------------------
class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def dist(self,other):
        return math.sqrt((other.x-self.x)**2+(other.y-self.y)**2)
    def mid(self,other):
        return ((self.x+other.x)/2,(self.y+other.y)/2)
    def line(self,other):
        if other.x==self.x:
            return "x="+str(self.x)
        m=(other.y-self.y)/(other.x-self.x)
        c=self.y-m*self.x
        return (m,c)
    def reflect(self,A,B):
        dx=B.x-A.x
        dy=B.y-A.y
        t=((self.x-A.x)*dx+(self.y-A.y)*dy)/(dx*dx+dy*dy)
        Px=A.x+t*dx
        Py=A.y+t*dy
        return (2*Px-self.x,2*Py-self.y)

# ------------------ Question 2 ------------------
class Vec:
    def __init__(self,i,j):
        self.i=i
        self.j=j
    def add(self,b,c):
        return (self.i+b.i+c.i,self.j+b.j+c.j)
    def mag(self):
        return math.sqrt(self.i**2+self.j**2)
    def dot(self,other):
        return self.i*other.i+self.j*other.j
    def angle(self,other):
        d=self.dot(other)
        m1=self.mag()
        m2=other.mag()
        return math.degrees(math.acos(d/(m1*m2)))
    def proj(self,other):
        d=self.dot(other)
        m2=other.i**2+other.j**2
        k=d/m2
        return (k*other.i,k*other.j)

# ------------------ Question 3 ------------------
class Segment:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def dist(self,other):
        return math.sqrt((other.x-self.x)**2+(other.y-self.y)**2)
    def proj(self,E,P):
        dx=E.x-self.x
        dy=E.y-self.y
        t=((P.x-self.x)*dx+(P.y-self.y)*dy)/(dx*dx+dy*dy)
        t=max(0,min(1,t))
        qx=self.x+t*dx
        qy=self.y+t*dy
        return Segment(qx,qy)
    def proj_dist(self,E,P):
        Q=self.proj(E,P)
        return P.dist(Q)

# ------------------ Question 4 ------------------
class Line:
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
    def intersection(self,other):
        d=self.a*other.b-other.a*self.b
        if d==0:
            if self.a*other.c==other.a*self.c and self.b*other.c==other.b*self.c:
                return "Lines are parallel or coincident"
            else:
                return "Lines are parallel or coincident"
        x=(self.b*other.c-other.b*self.c)/d
        y=(self.c*other.a-other.c*self.a)/d
        return (x,y)

A=Point(1,2)
B=Point(4,6)
C=Point(3,5)

print(A.dist(B))
print(A.mid(B))
print(A.line(B))
print(C.reflect(A,B))

v1=Vec(1,2)
v2=Vec(3,4)
v3=Vec(5,6)

print(v1.add(v2,v3))
print(v1.mag(),v2.mag(),v3.mag())
print(v1.dot(v2),v1.dot(v3),v2.dot(v3))
print(v1.angle(v2),v1.angle(v3),v2.angle(v3))
print(v1.proj(v2))

S=Segment(1,1)
E=Segment(5,4)
P=Segment(3,2)

print(S.dist(E))
Q=S.proj(E,P)
print((Q.x,Q.y))
print(S.proj_dist(E,P))

L1=Line(2,3,6)
L2=Line(1,-1,2)

print(Line.intersection(L1,L2))
