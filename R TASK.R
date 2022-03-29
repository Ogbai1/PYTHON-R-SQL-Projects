# Importing dataset to R studio 

housing <- read.csv("C:/Users/user/Desktop/TTA General/R/housing.csv")
head(housing)

# Import library ggplot ()

library(ggplot2)

# Using qplot or no aesthetic: Display  home value on x axis and its cost on the y axis 

qplot(y = Structure.Cost, x = Home.Value, data = housing)

# Using qplot: Adding color to data points

qplot(y = Structure.Cost, x = Home.Value, data = housing, color= "blue")

# Using ggplot() to display house value on x axis and cost on the y axis

ggplot(housing, aes(x = Home.Value, y = Structure.Cost, color = "red"))+geom_point(alpha = 0.5)


# To create three vectors a, b, c with 5 integers. 

a = c(1, 2, 3,4,5)
b= c(6,7,8,9,10)
c= c(11,12,13,14,15)

# Combine the three vectors as 3x5 matrix 
A <- matrix(c(a, b, c), 3); A 

# Print content of matrix A
A

# Plot a graph and label 
library("plot.matrix")
matplot(A)

#Create a Data frames,details of 5 employees and display it

Employees = data.frame(Name=c("Ogbai Y","Andy J","Georgina S", "JAMES A","Rachel N"),
                       Age=c(23,22,25,26,32),
                       Role=c("Trainee Data Scientist","Manager","Exective","CEO","ASSISTANT"),
                      Service=c(1,2,3,5,2))
print(Employees)


# qplot graph, X =sequence of 1:20 and y =x ^  2. install.packages("ggplot2",dependencies = TRUE)

library(ggplot2)
library(dplyr)

qplot(x =seq(1:20), y = x^2)

# Using qplot: Adding color to data points

x=seq(1:20)
y=x^2

qplot(y = x^2, x = seq(1:20), color= "blue")


#Create a simple bar plot of five subjects

marks = c(70, 95, 80, 74,99)
barplot(marks,main = "Bar Plot of 5 subjects", xlab = "subjects", ylab = "marks",
        names.arg = c("English", "Chemistry", "Math", "History", "Geography"),
        col = "blue", horiz = FALSE)

#To take input from the user and display thee values provided by the user.

my.name <- readline(prompt="Enter name: ")
my.name <- readline(prompt="Minnosota: ")
my.age <- readline(prompt="Enter age: ")
my.age <- readline(prompt="21:")
# convert character into integer to display the values

my.age <- as.integer(21)
print(paste("Hi,", "Minnosota", "next year you will be", my.age +1, "years old."))

#create a sequence of numbers from 20 to 50 and find the mean and sum of the nos.

print("Sequence of numbers from 20 to 50:")
print(seq(20,50))
print("Mean of numbers from 20 to 60:")
print(mean(20:50))
print("Sum of numbers from 50 to 50:")
print(sum(20:50))

# To create a vector which contains 10 random integer values between -50 and +50

s = sample(-50:50, 10, replace=TRUE)
print("Content of the vector:")
print("Ten random integer values between -50 and +50:")
print(s)

# To get the first 10 Fibonacci numbers.

Fibonacci <- numeric(10)
Fibonacci[1] <- Fibonacci[2] <- 1
for (i in 3:10) Fibonacci[i] <- Fibonacci[i - 2] + Fibonacci[i - 1]
print("First 10 Fibonacci numbers:")
print(Fibonacci)

#To print numbers from 1 to 100 & print "Fizz" for multiples of 3, print "Buzz" for multiples of 5 & print "FizzBuzz" for multiples of both

for (n in 1:100) {
  if (n %% 3 == 0 & n %% 5 == 0) {print("FizzBuzz")}
  else if (n %% 3 == 0) {print("Fizz")}
  else if (n %% 5 == 0) {print("Buzz")}
  else print(n)
}

# Thank you very much TTA 
