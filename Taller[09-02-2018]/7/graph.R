d_t <- function(t) ((2*cos(t) - 2)^2 + (sin(t) - 1)^2) 
dd_t <- function(t) {}
body(dd_t) <- D(body(d_t),'t')

pdf("d'(t).pdf")
curve(dd_t,0,2*pi)
dev.off()