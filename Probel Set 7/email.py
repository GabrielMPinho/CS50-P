'''
regex: regular expression. Validar se um dado é realmente verdadeiro. (EX: email, cpf, cnpj, etc)
re: biblioteca. padrões para encontrar e manipular textos
    re.search: procura por um padrão em uma string. re.search(padrão, string). P printar o resultado, usar o método .group()
    re.findall():encontrar todas as ocorrências de um padrão em um texto. Ela retorna uma lista contendo todos os matches.
    re.sub(): Subistituir. re.sub(padrão, substituição, string)
    re.split(): Dividir. re.split(padrão, string)
    PADROES:
        .: usado para representar qualquer  caractere. Ex: '1.3' pode ser 123, 1a3, 1#3, 1 3. 
        \d: qualquer dígito numérico de 0 a 9. É como dizer: "Procure números no texto".
        \D: qualquer caractere que não seja um dígito numérico. É como dizer: "Procure tudo que não for número no texto".
        \w: qualquer caractere alfanumérico. É como dizer: "Procure letras e números no texto" menos caracters especias.
        \W: qualquer caractere que não seja alfanumérico. É como dizer: "Procure tudo que não for letra ou número no texto".
        \s: qualquer caractere de espaço em branco. É como dizer: "Procure espaços no texto".
        \S: qualquer caractere que não seja um espaço em branco. É como dizer: "Procure tudo que não for espaço no texto".
        \b: usado para representar a fronteira de uma palavra. Ex: '\bfoo\b' procura pela palavra "foo" no texto.
        ^: usado para representar o início de uma string. Ex: '^a' procura por strings que começam com a letra "a".
        $: usado para representar o final de uma string. Ex: 'a$' procura por strings que terminam com a letra "a".
        []: usado para especificar um conjunto de caracteres. Ex: '[abc]' procura por ocorrências de "a", "b" ou "c" no texto.
        [^]: usado para especificar um conjunto de caracteres que não queremos. Ex: '[^abc]' procura por ocorrências de qualquer caractere que não seja "a", "b" ou "c" no texto.
    QUANTIFICADORES:
        *: zero ou mais ocorrências" do elemento que vem antes dele. Ex:  re.findall(r"a*", texto) busca por todas as ocorrências de "a" ou "aaaaa" ou "aaaa" ou "a" ou "" no texto.
        +: uma ou mais ocorrências" do elemento que vem antes dele. Ex: re.findall(r"a+", texto) busca por todas as ocorrências de "a" ou "aaaaa" ou "aaaa" no texto.
        ?: zero ou uma ocorrência" do elemento que vem antes dele. Ex: re.findall(r"a?", texto) busca por todas as ocorrências de "a" ou "" no texto.
        {n}: exatamente n ocorrências" do elemento que vem antes dele. Ex: re.findall(r"a{3}", texto) busca por todas as ocorrências de "aaa" no texto.  
        {n, m}: entre n e m ocorrências" do elemento que vem antes dele. Ex: re.findall(r"a{2, 3}", texto) busca por todas as ocorrências de "aa" ou "aaa" no texto.
        A|B: Ou A ou B
    OPICIONAIS:
        re.IGNORECASE: ignora se a letra é maiúscula ou minúscula
        re.MULTILINE: considera cada linha como uma string diferente e vai olhar todas
        re.DOTALL: o ponto(.) vai considerar o fim da string
'''
import re 

email = input('Digite o email: ').strip()

if re.search(r"^\w+@(\w+\.)?\w+\.com$", email, re.IGNORECASE):#Preciso de algo que começe(^) com uma sequência de pelo menos um caracteres alfanumericos(\w+),uma sequência OPCIONAL de pelo menos um caracteres alfanumericos(\w) e '.'((\w+\.)?), uma  sequência de pelo menos um caracteres alfanumericos(\w+), dps .com(\.com) e termine($)
    print('Email válido')
else:
    print('Email inválido')














































