d_t <- expression((2*cos(t) - 2)^2 + (sin(t) - 1)^2) 
dd_t <- D(d_t,'t')
print(dd_t)