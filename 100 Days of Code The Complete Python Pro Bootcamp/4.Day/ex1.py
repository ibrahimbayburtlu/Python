#Remember to use the random module
#Hint: Remember to import the random module here at the top of the file. 🎲
import random
# 🚨 Don't change the code below 👇
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)
 # 🚨 Don't change the code above 👆 It's only for testing your code.
	 
#Write the rest of your code below this line 👇
random_number = random.randint(0,1)
if(random_number == 1):
    print("Heads")
else:
    print("Tails")

#Pseudo-random number generators work by performing some operations on a value. Generally, this value is the previous number generated by the generator. However, the first time you use the generator, there is no upfront value.

#Seeding the pseudo-random number generator gives it its first "previous" value. Each seed value corresponds to the set of values generated for a particular random number generator. That is, if you give the same seed twice, you will get the same number row twice.

#Generally, you want to seed your random number generator with a value that will change each run of the program. For example, the present tense is a frequently used seed. The reason this doesn't happen automatically is that if you want you can provide a specific seed to get a known sequence of numbers.