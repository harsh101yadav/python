letter = "Hey my name is {0} and I am from {1}"
name = "Harsh"
country = "India"

print(letter.format(name,country))

#f string

print(f"Hey my name is {name} and I am from {country}")

#0.2f means upto only 2 decimal places
txt = "For only {price:.2f} dollars!"
print(txt.format(price = 49))

print(f"This is how we use f-string. Hey my name is {{name}} and I am from {{country}}")
