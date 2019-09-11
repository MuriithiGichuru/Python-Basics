#print("Muriithi Gichuru") -

first_name = "said"
second_Name = "Hajib"
# #concatenating strings -  we use a + operater to concatenate strings
full_name = first_name + " " + second_Name
# print(full_name)
# full_name = first_name + " "                 + second_Name
# print(full_name)
# #pythone will not note the spaces outside the literal or speech marks
print (first_name)
print(first_name.title())
#the . gives methods to transform strings
print(first_name.upper())
print(first_name.lower())
print(first_name.split())
print(full_name.split())
print(full_name.count("a")) #counting the a's in full names

#where you are provided male and femal gender as below.. how do you count the M's or the F's
gender = "MFMFMFMFMFMFMFMMMMFFFFMMMMFFFFMMFM"
print(gender.count("F"))
print(gender.count("M"))
print(gender.swapcase()) # it swaps the case

