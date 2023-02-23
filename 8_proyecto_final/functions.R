## FUNCTIONS ##

# cols returns a dataframe that summarizes: the column name, the number of unique values, the empty/false or na values, and the repeated values in each column.

cols <- function(df){
  #initialize summary columns
  nc <- ncol(df)
  type <- character(nc)
  unique_values <- integer(nc)
  nas <- integer(nc)
  empty <- integer(nc)
  
  #save aggregated values:
  for (i in 1:nc){
    type[i] <- typeof(df[[i]])
    unique_values[i] <- length(unique(df[[i]]))
    if(type[i]=="character"){
      empty[i] <- sum(nchar(df[[i]], keepNA=F) == 0)
    }
    else if(type[i] =="logical"){
      empty[i] <- sum(!df[[i]])
    }
    else{
      empty[i] <- sum(is.na(df[[i]]))
    }
  }
  #calculate repeated values
  repeated=nrow(df)-unique_values-empty
  
  #return summary df
  data.frame("column"=colnames(df), unique_values, type, empty, repeated)
}