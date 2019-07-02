#K-NN(K-Nearest Neighbors)

Implementação do algoritmo K-NN(K-Nearest Neighbors),
usando a scikit-learn.
(http://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html)

O K-NN é um algoritmo de classificação supervisionado.
Dado um conjunto de amostras,as quais já se conhece a classe, 
uma nova  anostra pode ser classificada selecionando as K amostras mais 
proximas a ela,utilizando alguma métrica de distância(como a distância euclidiana) e 
então classificando a nova amostra de acordo com a classe mais 
recorrente entre as K amostras selecionadas.