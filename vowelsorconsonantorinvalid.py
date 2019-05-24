def vowel_or_consonant(c):
  if not c.isalpha():
    return"invalid"
  vowels='aeiou'
  if c.lower() in vowels:
    return"Vowel"
  else:
    return"Consonant"
c=input()
r=vowel_or_consonant(c)
print(r)
    


