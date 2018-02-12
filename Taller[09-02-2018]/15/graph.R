d_t <-function(t)((5*t)-exp(t)+1)
dd_t <- function(t) {}
body(dd_t) <- D(body(d_t),'t')


png("d_t.png")
curve(d_t,-3,3)


