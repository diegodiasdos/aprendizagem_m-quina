import sys
import math
from sklearn.neighbors import KNeighborsClassifier
'''
   Verificar taxa de acerto para filmes Ótimo, Bom e Ruim
'''
'''
dataset Netflix
'''

arquivo = 'dataset_netflix.txt'

#print amostras
with open(arquivo)as d:
   amostras = d.readlines()
  
#separação por classes:
otimo = amostras[:50]
bom = amostras[50:100]
ruim= amostras[100:]

#regorniza dados para ter proporcao igual de amostras 
amostras_organizadas = []
for i in range(0, 50):
#print amostras_organizadas
   amostras_organizadas.append(otimo[i])
   amostras_organizadas.append(bom[i])
   amostras_organizadas.append(ruim[i])
   
#separacao caracteristicas e classes 
caracteristicas = []
classes = []

for amostra in amostras_organizadas:
	aux = amostra.split(",")
#print caracteristicas
#print classes 	 
	
	RatingDescription = float(aux[0])
	UserRatingScore = float(aux[1])
	UserRatingSize = float(aux[2])
	classe = aux[3].strip()
	caracteristicas.append([RatingDescription,UserRatingScore,UserRatingSize])
	classes.append(classe)
	 
#separacao treinamento 
treinamento = 0.7
caracteristicas_treinamento = caracteristicas[:int(treinamento * len(amostras))]
caracteristicas_teste = caracteristicas[int(treinamento * len(amostras)):]
classes_treinamento = classes [:int(treinamento * len(amostras))]
classes_teste = classes[int(treinamento * len(amostras)) :]

#teste

knn = 3
neigh = KNeighborsClassifier(n_neighbors=knn)
neigh.fit(caracteristicas_treinamento, classes_treinamento)
classes_previstas = neigh.predict(caracteristicas_teste)

#verifica acertos 
acerto = 0 
for classe_correta, classe_prevista in zip(classes_teste, classes_previstas):
	 print(classe_correta + '-' + classe_prevista) 
	 if classe_correta == classe_prevista:
		   acerto += 1 
acerto /= float(len(classes_teste))
resultado = acerto *100;
print("Verificção de acerto %5.2f" %resultado)