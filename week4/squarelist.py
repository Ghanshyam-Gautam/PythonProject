numbers=[1,3,5,7,9]

'''
squarelist=[]
for item in numbers:
    squarelist.append(item**2)
print(squarelist)
'''

squarelist=[item**2 for item in numbers]
print(squarelist)

