n=int(input())
if(n>=0 and n<=9):
	print("invalid")
if(n=='a' or n=='e' or n=='i' or n=='o' or n=='u'):
	print("Vowel")
else:
	print("Consonant")
