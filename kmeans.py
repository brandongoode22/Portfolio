#!/usr/bin/env python3

import sys, math, random
import numpy as np

random.seed(int(sys.argv[1]))
K = int(sys.argv[2])
training = open(sys.argv[3])
testing = open(sys.argv[4])


training = np.loadtxt(training)
testing = np.loadtxt(testing)


N = K-1

eligible_vectors = np.copy(training)
centroids = []

attributes = training[0].__len__()-1
training_size = training.__len__()
testing_size = testing.__len__()

for i in range(K):
    index_to_delete = random.randint(0, N)
    centroids.append(list(eligible_vectors[index_to_delete]))
    eligible_vectors = np.delete(eligible_vectors, index_to_delete , 0)
    N -=1


centroids = np.array(centroids)
centroids_size = centroids.__len__()



nearest_centroids = []
convergence = False
total = 0
convergence_control = 0


for i in range(training_size):
    min_index = None
    distance = None
    
    for j in range(centroids_size):
        d_sum = 0
        for k in range(attributes):
            d_sum += (centroids[j][k]-training[i][k])**2
        if distance == None or math.sqrt(d_sum) < distance:
            min_index = j
            distance = math.sqrt(d_sum) 
    nearest_centroids.append(min_index)      
            
        

for i in range(centroids_size):
    for j in range(training_size):
        if nearest_centroids[j] == i:
            total += 1
            for k in range(attributes):
                if total == 1:
                    centroids[i][k] = training[j][k]
                else:
                    centroids[i][k] += training[j][k]
    if(total > 0):
        for l in range(attributes):
            centroids[i][l] = (centroids[i][l])/total
    total = 0
  
   
    
    
     
while(not convergence):
    convergence_control = 0
    for i in range(training_size):
        min_index = None
        distance = None

        for j in range(centroids_size):
            d_sum = 0
            for k in range(attributes):
                d_sum += (centroids[j][k]-training[i][k])**2
            if distance == None or math.sqrt(d_sum) < distance:
                min_index = j
                distance = math.sqrt(d_sum) 
        nearest_centroids[i] = min_index    




    for i in range(centroids_size):
        temp = np.copy(centroids[i])
        for j in range(training_size):
            if nearest_centroids[j] == i:
                total += 1
                for k in range(attributes):
                    if total == 1:
                        centroids[i][k] = training[j][k]
                    else:
                        centroids[i][k] += training[j][k]
        if(total > 0):
            for l in range(attributes):
                centroids[i][l] = (centroids[i][l])/total
        total = 0
        for m in range(attributes):
            if centroids[i][m] != temp[m]:
                convergence_control += 1
        
    if convergence_control == 0:
        convergence = True

indices = np.argsort(training, axis=0)

n_classes = 1

for i in range(training_size):
    if i == 0:
        cur = training[indices[i][attributes]][attributes]
    else:
        if cur != training[indices[i][attributes]][attributes]:
            n_classes +=1
            cur = training[indices[i][attributes]][attributes]
    


centroid_classes = [[0 for _ in range(n_classes)] for _ in range(centroids_size)]

        
for i in range(centroids_size):
    for j in range(training_size):
        if nearest_centroids[j] == i:
            centroid_classes[i][int(training[j][attributes])] +=1
                
classification_list = []

for i in range(centroids_size):
    most = 0
    for j in range(n_classes):
        if centroid_classes[i][j] > most:
            most = j
    classification_list.append(most)
    
correct = 0
    
for i in range(testing_size):
    min_index = None
    distance = None
    
    for j in range(centroids_size):
        d_sum = 0
        for k in range(attributes):
            d_sum += (centroids[j][k]-testing[i][k])**2
        if distance == None or math.sqrt(d_sum) < distance:
            min_index = j
            distance = math.sqrt(d_sum)
  
    if classification_list[min_index] == int(testing[i][attributes]):
        correct +=1

print(correct)

        
    

            
