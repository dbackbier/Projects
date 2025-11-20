for (x in 1:10) {
  print(x)
}

num1 <- 5
num2 <- 10
num1 + num2

name <- "John"
age <- 40
name
age

text1 <- "R is"
text2 <- "awesome"
paste(text1, text2)

var1 <- var2 <- var3 <- "Orange"
var1
var2
var3

# numeric
x <- 10.5
class(x)

# integer
x <- 1000L
class(x)

# complex
x <- 9i + 3
class(x)

# character/string
x <- "R is exciting"
class(x)

# logical/boolean
x <- TRUE
class(x)

x <- 1L # integer
y <- 2 # numeric

# convert from integer to numeric:
a <- as.numeric(x)

# convert from numeric to integer:
b <- as.integer(y)

# print values of x and y
x
y

# print the class name of a and b
class(a)
class(b)

2 > 1 # returns true
2 < 1 # returns false

a <- 100
b <- 50

if (b > a) {
  print("b is greater than a")
} else if (a == b) {
  print("a is equal to b")
} else {
  print("a is greater than b")
}

x <- 41
if (x > 10) {
  print("above ten")
  if (x > 20) {
    print("and also above 20")
  } else {
    print("but not above 20")
  }
} else {
  print("below ten")
}

a <- 200
b <- 100
c <- 300
if (a > b & c > a) {
  "both conditions are true"
}
if (a > b | c > a) {
  "at least one of the conditions are true"
}

i <- 1
while (i < 6) {
  print(i)
  i <- i + 1
}

i <- 1
while (i < 6) {
  print(i)
  i <- i + 1
  if (i == 4) {
    break
  }
}

i <- 0
while (i < 6) {
  i <- i + 1
  if (i == 3) {
    next
  }
  print(i)
}

fruits <- list("apple", "banana", "orange")
for (x in fruits) {
  print(x)
}

dice <- c(1, 2, 3, 4, 5, 6)
for (x in dice) {
  print(x)
}

fruits <- list("apple", "banana", "cherry")
for (x in fruits) {
  if (x == "cherry") {
    break
  }
  print(x)
}

fruits <- list("apple", "banana", "orange")
for (x in fruits) {
  if (x == "banana") {
    next
  }
  print(x)
}

dice <- 1:6
for (x in dice) {
  if (x == 6) {
    print(paste("The dice number is", x, "Yahtzee!"))
  } else {
    print(paste("The dice number is", x, "not Yahtzee!"))
  }
}

adj <- list("red", "big", "tasty")
fruits <- list("apple", "banana", "cherry")
for (x in adj) {
  for (y in fruits) {
    print(paste(x, y))
  }
}

my_function <- function() {
  print("Hello World")
}

my_function()

my_function <- function(fname) {
  paste(fname, "Griffin")
}

my_function("Peter")
my_function("Lois")
my_function("Stewie")

my_function <- function(fname, lname) {
  paste(fname, lname)
}
my_function("Peter", "Griffin")

my_function <- function(country = "Norway") {
  paste("I am from", country)
}

my_function("USA")
my_function("Canada")
my_function()
my_function("India")

my_function <- function(x = 1) {
  return (x * 3)
}

my_function()
my_function(2)
my_function(3)

nested_function <- function(x, y) {
  a <- x + y
  return(a)
}

nested_function(nested_function(2, 2), nested_function(3, 3))

outer_func <- function(x) {
  inner_func <- function(y) {
    a <- x + y
    return(a)
  }
  return(inner_func)
}

output <- outer_func(3)
output(5)

tri_recursion <- function(k) {
  if (k > 0) {
    res <- k + tri_recursion(k - 1)
    print(res)
  } else {
    res <- 0
    return(res)
  }
}
tri_recursion(8)

txt <- "global variable"
my_function <- function() {
  txt <- "fantastic"
  paste("R is", txt)
}
my_function()
txt

my_function <- function() {
  txt <<- "fantastic"
  paste("R is", txt)
}
my_function()
txt

fruits <- c("banana", "apple", "cherry")
fruits
length(fruits)

numbers <- c(1, 2, 3)
numbers
length(numbers)

numbers <- 1:10
numbers
length(numbers)

nums1 <- 1.5:6.5
nums1
length(nums1)

nums2 <- 1.5:6.3
nums2
length(nums2)

log_values <- c(TRUE, FALSE, FALSE, TRUE)
log_values
length(log_values)

fruits <- c("banana", "apple", "orange", "mango", "lemon")
numbers <- c(13, 3, 5, 7, 20, 2)

sort(fruits)
sort(numbers)

fruits <- c("banana", "apple", "orange")
fruits[1]

fruits <- c("banana", "apple", "orange", "mango", "lemon")
fruits[c(1,3)]
fruits[-1]
fruits[1] <- "pear"
fruits[1]

repeat_each <- rep(c(1,2,3), each = 3)
repeat_each

repeat_times <- rep(c(1,2,3), times = 3)
repeat_times

repeat_indepent <- rep(c(1,2,3), times = c(5,2,1))
repeat_indepent

numbers <- seq(from = 0, to = 100, by = 20)
numbers

thislist <- list("apple", "banana", "cherry")
thislist
"apple" %in% thislist
append(thislist, "orange")

thislist <- list("apple", "banana", "cherry")
thislist[1] <- "blackcurrant"
thislist
length(thislist)
"apple" %in% thislist
append(thislist, "orange", after = 2)

thislist <- list("apple", "banana", "cherry")
newlist <- thislist[-1]
newlist

thislist <- list("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
(thislist)[2:5]

thislist <- list("apple", "banana", "cherry")
for (x in thislist) {
  print(x)
}

list1 <- list("a", "b", "c")
list2 <- list(1,2,3)
list3 <- c(list1,list2)

list3

thismatrix <- matrix(c(1,2,3,4,5,6), nrow = 2, ncol = 3)
thismatrix

thismatrix <- matrix(c("apple", "banana", "cherry", "orange"), nrow = 2, ncol = 2)
thismatrix
thismatrix[1, 2]
thismatrix[2,]
thismatrix[,2]
thismatrix[1,]
thismatrix[,1]

thismatrix <- matrix(c("apple", "banana", "cherry", "orange","grape", "pineapple", "pear", "melon", "fig"), nrow = 3, ncol = 3)
thismatrix
thismatrix[c(1,2),]
thismatrix[,c(1,2)]

newmatrix <- cbind(thismatrix, c("strawberry", "blueberry", "raspberry"))
newmatrix

newmatrix <- rbind(thismatrix, c("strawberry", "blueberry", "raspberry"))
newmatrix

thismatrix <- matrix(c("apple", "banana", "cherry", "orange", "mango", "pineapple"), nrow = 3, ncol =2)
thismatrix
thismatrix <- thismatrix[-c(1), -c(1)]
thismatrix

thismatrix <- matrix(c("apple", "banana", "cherry", "orange"), nrow = 2, ncol = 2)
"apple" %in% thismatrix

thismatrix <- matrix(c("apple", "banana", "cherry", "orange"), nrow = 2, ncol = 2)
dim(thismatrix)

thismatrix <- matrix(c("apple", "banana", "cherry", "orange"), nrow = 2, ncol = 2)
length(thismatrix)

thismatrix <- matrix(c("apple", "banana", "cherry", "orange"), nrow = 2, ncol = 2)
for (rows in 1:nrow(thismatrix)) {
  for (columns in 1:ncol(thismatrix)) {
    print(thismatrix[rows, columns])
  }
}

# Combine matrices
Matrix1 <- matrix(c("apple", "banana", "cherry", "grape"), nrow = 2, ncol = 2)
Matrix2 <- matrix(c("orange", "mango", "pineapple", "watermelon"), nrow = 2, ncol = 2)

# Adding it as a rows
Matrix_Combined <- rbind(Matrix1, Matrix2)
Matrix_Combined

# Adding it as a columns
Matrix_Combined <- cbind(Matrix1, Matrix2)
Matrix_Combined

# An array with one dimension with values ranging from 1 to 24
thisarray <- c(1:24)
thisarray

# An array with more than one dimension
multiarray <- array(thisarray, dim = c(4, 3, 2))
multiarray
multiarray[2, 3, 2] # row, column, dimension
multiarray[c(1),,1] # all items from first row of matrix one
multiarray[,c(1),1] # all items from first column of matrix one
2 %in% multiarray # check if something is in the array
dim(multiarray) # returns # of rows and # of columns and # of dimensions
length(multiarray) # returns # of items

for (x in multiarray) {
  print(x) # loop through array
}

data_frame <- data.frame(
  Training = c("Strength", "Stamina", "Other"),
  Pulse = c(100, 150, 120),
  Duration = c(60, 30, 45)
)
data_frame
summary(data_frame) # returns min, 1st qu., median, mean, 3rd qu., and max
data_frame[1]
data_frame[["Training"]]
data_frame$Training

newrow_df <- rbind(data_frame, c("Strength", 110, 110)) # creates new row
newrow_df

newcol_df <- cbind(data_frame, Steps = c(1000, 6000, 2000)) # creates new column
newcol_df

df_new <- data_frame[-c(1), -c(1)] # removes first row and column
df_new

dim(data_frame) # returns # of rows and columns
nrow(data_frame) # returns # of rows
ncol(data_frame) # returns # of columns
length(data_frame) # same as ncol()

Data_Frame1 <- data.frame (
  Training = c("Strength", "Stamina", "Other"),
  Pulse = c(100, 150, 120),
  Duration = c(60, 30, 45)
)

Data_Frame2 <- data.frame (
  Training = c("Stamina", "Stamina", "Strength"),
  Pulse = c(140, 150, 160),
  Duration = c(30, 30, 20)
)

new_df <- rbind(Data_Frame1, Data_Frame2) # combine the rows
new_df

Data_Frame3 <- data.frame (
  Training = c("Strength", "Stamina", "Other"),
  Pulse = c(100, 150, 120),
  Duration = c(60, 30, 45)
)

Data_Frame4 <- data.frame (
  Steps = c(3000, 6000, 2000),
  Calories = c(300, 400, 300)
)

New_Data_Frame1 <- cbind(Data_Frame3, Data_Frame4)
New_Data_Frame1

# Create a factor
music_genre <- factor(c("Jazz", "Rock", "Classic", "Classic", "Pop", "Jazz", "Rock", "Jazz"))

# Print the factor
music_genre
levels(music_genre)

music_genre <- factor(c("Jazz", "Rock", "Classic", "Classic", "Pop", "Jazz", "Rock", "Jazz"), levels = c("Classic", "Jazz", "Pop", "Rock", "Other"))
levels(music_genre) # set the levels
length(music_genre) # returns length of factor
music_genre[3]
music_genre[3] <- "Pop" # change item, cannot change it to something that isn't already in the factor of isn't previously defined
music_genre[3]

music_genre <- factor(c("Jazz", "Rock", "Classic", "Classic", "Pop", "Jazz", "Rock", "Jazz"), levels = c("Classic", "Jazz", "Pop", "Rock", "Opera"))
music_genre[3] <- "Opera"
music_genre[3]