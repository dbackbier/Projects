plot(1, 3) # plot a point at x = 1, and y = 3

plot(c(1,5), c(5,8))

plot(c(1, 2, 3, 4, 5), c(3, 7, 8 , 9, 12))

x <- c(1, 2, 3, 4, 5)
y <- c(3, 7, 8, 9, 12)
plot(x, y)

plot(1:10)

plot(1:10, type = "l") # makes it a line

plot(1:10, main = "My Graph", xlab = "x-axis", ylab = "y-axis") # sets names of graph, x axis, and y axis

plot(1:10, col = "red") # makes the color of the points red

plot(1:10, cex = 0.5) # halves the size of the points

plot(1:10, pch = 5, cex = 0.75) # pch changes shape of points, 1-25

plot(1:10, type = "l", lwd = 2, col = "blue") # changes width of the line

plot(1:10, type = "l", lwd = 2, lty = 6) # lty changes the type of line, 0-6

line1 <- c(1, 2, 3, 4, 5, 10)
line2 <- c(2, 5, 7, 8, 9, 10)
plot(line1, type = "l", col = "blue")
lines(line2, type = "l", col = "red")

x <- c(5,7,8,7,2,2,9,4,11,12,9,6)
y <- c(99,86,87,88,111,103,87,94,78,77,85,86)
plot(x, y, cex = 0.5)

x <- c(5,7,8,7,2,2,9,4,11,12,9,6)
y <- c(99,86,87,88,111,103,87,94,78,77,85,86)
plot(x, y, main="Observation of Cars", xlab="Car age", ylab="Car speed", cex = 0.5)

# day one, the age and speed of 12 cars:
x1 <- c(5,7,8,7,2,2,9,4,11,12,9,6)
y1 <- c(99,86,87,88,111,103,87,94,78,77,85,86)
# day two, the age and speed of 15 cars:
x2 <- c(2,2,8,1,15,8,12,9,7,3,11,4,7,14,12)
y2 <- c(100,105,84,105,90,99,90,95,94,100,79,112,91,80,85)
plot(x1, y1, main="Observation of Cars", xlab="Car age", ylab="Car speed", col="red", cex=0.5)
points(x2, y2, col="blue", cex=0.5)

# Create a vector of pies
x <- c(10,20,30,40)
# Display the pie chart
pie(x)

pie(x, init.angle = 90)

mylabel <- c("Apples", "Bananas", "Cherries", "Dates")
colors <- c("red", "yellow", "green", "blue")
pie(x, label = mylabel, main = "Fruits", col = colors)
legend("bottomright", mylabel, fill = colors, cex = 0.5)

x <- c("A", "B", "C", "D") # x axis vals
y <- c(2, 4, 6, 8) # y axis vals
barplot(y, names.arg = x, col = colors)
barplot(y, names.arg = x, density = 50, col = colors) # density changes the amount of color
barplot(y, names.arg = x, width = c(1, 2, 3, 4)) # width changes the width of the bars
barplot(y, names.arg = x, horiz = TRUE) # horiz being true makes the bars horizontal


mtcars # outputs the data for cars (built-in)
?mtcars # shows information about the data set

data_cars <- mtcars
dim(data_cars) # get dimensions of the data set: rows, columns
names(data_cars) # finds the names of the variables from the data set
rownames(data_cars) # get the name of each row in the first column

sort(data_cars$cyl)

summary(data_cars)

max(data_cars$hp)
min(data_cars$hp)

which.max(data_cars$hp)
which.min(data_cars$hp)

rownames(data_cars)[which.max(data_cars$hp)]
rownames(data_cars)[which.min(data_cars$hp)]

mean(data_cars$wt)
median(data_cars$wt)
names(sort(-table(data_cars$wt)))[1] # finds mode

quantile(data_cars$wt, 0.75)
quantile(data_cars$wt)
