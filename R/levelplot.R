
#
#  Using base graphics
#
levelplot <- function(xgrid, ygrid, FUN){
  zgrid <- apply(expand.grid(xgrid, ygrid), 1, FUN)
  
  image(x=xgrid, y=ygrid, z=matrix(zgrid, nrow=length(xgrid)))
}
levelplot(seq(-10, 10, length.out=100), seq(-10, 10, length.out=100), max)


#
#  Using lattice
#
levelplot <- function(xgrid, ygrid, FUN){
  require(lattice)
  df <- expand.grid(xgrid, ygrid)
  names(df) <- c('x', 'y')
  df$z <- apply(df, 1, FUN)
  lattice::levelplot(z ~ x * y, data=df,
                     col.regions=heat.colors(length(xgrid)/5))
}
levelplot(seq(-10, 10, length.out=100), seq(-10, 10, length.out=100), max)


#
#  Using ggplot2
#
levelplot <- function(xgrid, ygrid, FUN){
  require(ggplot2)
  df <- expand.grid(xgrid, ygrid)
  names(df) <- c('x', 'y')
  df$z <- apply(df, 1, FUN)
  ggplot(df, aes(x, y, fill=z)) +
    geom_tile()
}
levelplot(seq(-10, 10, length.out=100), seq(-10, 10, length.out=100), max)
