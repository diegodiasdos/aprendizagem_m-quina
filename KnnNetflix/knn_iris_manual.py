from math import sqrt


arquivo = 'iris.txt'

with open(arquivo) as f:
    amostras = f.readlines()
# print amostras

# separacao por classes:
setosa = amostras[:50]
versicolor = amostras[50:100]
virginica = amostras[100:]

# regorniza dados para ter proporcao igual de amostras
amostras_organizadas = []
for i in range(0, 50):
    amostras_organizadas.append(setosa[i])
    amostras_organizadas.append(versicolor[i])
    amostras_organizadas.append(virginica[i])
# print amostras_organizadas

# separacao caracteristicas e classes
caracteristicas = []
classes = []
for amostra in amostras_organizadas:
    aux = amostra.split(",")
    comprimento_sepala = float(aux[0])
    largura_sepala = float(aux[1])
    comprimento_petala = float(aux[2])
    largura_petala = float(aux[3])
    classe = aux[4].strip()
    caracteristicas.append([comprimento_sepala, largura_sepala, comprimento_petala, largura_petala])
    classes.append(classe)
# print caracteristicas
# print classes

# separacao treinamento e teste
proporcao_treinamento = 0.7
caracteristicas_treinamento = caracteristicas[:int(proporcao_treinamento * len(amostras))]
caracteristicas_teste = caracteristicas[int(proporcao_treinamento * len(amostras)):]
classes_treinamento = classes[:int(proporcao_treinamento * len(amostras))]
classes_teste = classes[int(proporcao_treinamento * len(amostras)):]

# treinamento
k = 3
classes_previstas = []
for c1 in caracteristicas_teste:
    distancias_c1 = []
    for indice, c2 in enumerate(caracteristicas_treinamento):
        d = sqrt((c1[0] - c2[0]) ** 2 +
                 (c1[1] - c2[1]) ** 2 +
                 (c1[2] - c2[2]) ** 2 +
                 (c1[3] - c2[3]) ** 2)
        distancias_c1.append([indice, d, classes_treinamento[indice]])

    distancias_c1.sort(key = lambda x: x[1])
    mais_proximas = distancias_c1[0: k]
    classes_amostras_mais_proximas = []
    for amostra in mais_proximas:
        classes_amostras_mais_proximas.append(amostra[2])

    quantidade_setosa = classes_amostras_mais_proximas.count('Iris-setosa')
    quantidade_virginica = classes_amostras_mais_proximas.count('Iris-virginica')
    quantidade_versicolor = classes_amostras_mais_proximas.count('Iris-versicolor')
    lista_quantidades = [['Iris-setosa', quantidade_setosa],
                         ['Iris-virginica', quantidade_virginica],
                         ['Iris-versicolor', quantidade_versicolor]]
    lista_quantidades.sort(key = lambda x: x[1])
    classe_final = lista_quantidades[2][0]
    classes_previstas.append(classe_final)

# verifica acertos
porcentagem_acerto = 0
for classe_correta, classe_prevista in zip(classes_teste, classes_previstas):
    print(classe_correta + ' - ' + classe_prevista)
    if classe_correta == classe_prevista:
        porcentagem_acerto += 1
porcentagem_acerto /= float(len(classes_teste))
print(porcentagem_acerto * 100)
