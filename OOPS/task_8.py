# 5)Write a program which contains one class named as Numbers.
# Arithmetic class contains one instance variables as Value.
# Inside init method initialize that instance variables to the value which is accepted from user.
# There are four instance methods inside class as ChkPrime(), ChkPerfect() , SumFactors(), Factors().
# ChkPrime() method will returns true if number is prime otherwise return false
# ChkPerfect () method will returns true if number is perfect otherwise return false.
# Factors () method will display all factors of instance variable.
# SumFactors() method will return addition of all factors. Use this method in any another method
# As a helper method if required.
# After Designing the above class call all instance methods by creating multiple objects.



class Numbers:
    

    def __init__(self):
        self.value=0

    def chkPrime(self):
        count=0
        self.value=int(input("enter the value: "))
        for i in range(2,self.value):
            if(self.value%2!=0):
                count=0
            else:
                count=1
        if(count==0):
            print("it is prime number")
        else:
            print("it is not a prime number")
