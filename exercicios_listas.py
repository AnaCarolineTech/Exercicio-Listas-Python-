# exercicios_basicos.py

# ======================
# 1) Lista de livros
# ======================
livros = ["O Melhor de Mim", "Como Eu Era Antes de Você", "o verao que mudou a minha vida"]
print("Q1 - Lista de livros:", livros)

# ======================
# 2) Primeiro e último
# ======================
print("Q2 - Primeiro:", livros[0])
print("Q2 - Último:", livros[-1])

# ======================
# 3) Adicionar dois livros (append)
# ======================
livros.append("Dom Casmurro")
livros.append("A Revolução dos Bichos")
print("Q3 - Após append():", livros)

# ======================
# 4) Inserir 'Duna' na segunda posição (índice 1)
# ======================
livros.insert(1, "Duna")
print('Q4 - Após insert("Duna" na 2ª posição):', livros)

# ======================
# 5) Remover "Silêncio dos inocentes" ou avisar
# ======================
alvo = "Silêncio dos inocentes"
if alvo in livros:
    livros.remove(alvo)
    print(f'Q5 - Removido: "{alvo}"')
else:
    print("Q5 - Livro não encontrado")
print("Q5 - Lista atual:", livros)

# ======================
# 6) Contar 2 na lista números
# ======================
numeros = [1, 2, 3, 2, 4, 2, 5]
qtd = numeros.count(2)
print("Q6 - Lista:", numeros)
print("Q6 - O número 2 aparece", qtd, "vezes")

# ======================
# 7) Frase para cada livro
# ======================
print("Q7 - Frases dos livros:")
for livro in livros:
    print("O livro", livro, "é interessante")

# ======================
# 8) Idades >= 18
# ======================
idades = [12, 18, 25, 14, 30]
print("Q8 - Idades maiores ou iguais a 18:")
for idade in idades:
    if idade >= 18:
        print(idade)

# ======================
# 9) Soma manual com for
# ======================
valores = [10, 20, 30, 40]
soma = 0
for v in valores:
    soma = soma + v
print("Q9 - Valores:", valores)
print("Q9 - Soma manual:", soma)

# ======================
# 10) Notas de 2 alunos (3 notas cada) e média
# ======================
print("Q10 - Digite 3 notas para cada um dos 2 alunos.")
# aluno 1
n1a1 = float(input("Aluno 1 - Nota 1: "))
n2a1 = float(input("Aluno 1 - Nota 2: "))
n3a1 = float(input("Aluno 1 - Nota 3: "))
aluno1 = [n1a1, n2a1, n3a1]

# aluno 2
n1a2 = float(input("Aluno 2 - Nota 1: "))
n2a2 = float(input("Aluno 2 - Nota 2: "))
n3a2 = float(input("Aluno 2 - Nota 3: "))
aluno2 = [n1a2, n2a2, n3a2]

notas = [aluno1, aluno2]
print("Q10 - Notas:", notas)

media1 = (aluno1[0] + aluno1[1] + aluno1[2]) / 3
media2 = (aluno2[0] + aluno2[1] + aluno2[2]) / 3
print("Q10 - Média do aluno 1:", round(media1, 2))
print("Q10 - Média do aluno 2:", round(media2, 2))

# ======================
# 11) Tabuleiro de xadrez com list comprehension
#     [ ] = vazio, tor = torre, cav = cavalo, bis = bispo
#     rai = rainha, rei = rei, pea = peão
# ======================
# tabuleiro vazio 8x8
tabuleiro = [["[ ]" for _ in range(8)] for _ in range(8)]

# linha das peças e linha dos peões
primeira_linha = ["tor", "cav", "bis", "rai", "rei", "bis", "cav", "tor"]
peoes = ["pea", "pea", "pea", "pea", "pea", "pea", "pea", "pea"]

# pretas no topo (linhas 0 e 1), brancas em baixo (linhas 7 e 6)
tabuleiro[0] = primeira_linha[:]   # topo
tabuleiro[1] = peoes[:]
tabuleiro[6] = peoes[:]
tabuleiro[7] = primeira_linha[:]

print("Q11 - Tabuleiro:")
for linha in tabuleiro:
    print(" ".join(linha))
