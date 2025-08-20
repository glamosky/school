from jar import Jar

j = Jar(5)
print(str(j))          # ""
j.deposit(3)
print(str(j))          # "🍪🍪🍪"
j.withdraw(1)
print(str(j))          # "🍪🍪"