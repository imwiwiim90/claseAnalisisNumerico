from pylab import*

t=arange(-pi,2*pi,0.01)

r=2+cos(3*t)

polar(t,r)

grid(True)

show()


from sympy import*

t=Symbol('t')

f=2+cos(3*t)-(2-exp(t))

r=-1

df=diff(f)

r=r-float(f.subs(t,r))/float(df.subs(t,r))

r

r=r-float(f.subs(t,r))/float(df.subs(t,r))

r

r=r-float(f.subs(t,r))/float(df.subs(t,r))

r

r=r-float(f.subs(t,r))/float(df.subs(t,r))

r

r=r-float(f.subs(t,r))/float(df.subs(t,r))

r

r=r-float(f.subs(t,r))/float(df.subs(t,r))

r

r=r-float(f.subs(t,r))/float(df.subs(t,r))

r

2+cos(3*r)
