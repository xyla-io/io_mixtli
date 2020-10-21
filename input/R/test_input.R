args <- commandArgs(trailingOnly = TRUE)
df <- read.csv(args[1])

cat('{"output": "The data frame has been processed"}')