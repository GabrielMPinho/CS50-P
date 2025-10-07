import re

url = input('Digite a url: ').strip()
#Original: https://twitter.com/Manata
username = re.sub(r"^(https?://)?(www\.)?twitter\.com/", "", url) #Substitui a parte inicial da URL por nada, deixando apenas o username. N precisa do 's' no final do 'http', nem do https://, nem do www.
print(username)
















































