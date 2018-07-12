n=input()
c=ord(n)
if(c>=65 and c<=90 or c>=95 and c<=122):
	if(n=='a' or n=='e' or n=='i' or n=='o' or n=='u' or n=='A' or n=='E' or n=='I' or n=='O' or n=='U'):
		print("Vowel")
	else:
		print("Consonant")
else:
	print("invalid")
