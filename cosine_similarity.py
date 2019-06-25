#################################################################################################
# CSE 597 - Assignment 1
# Description - This python program loads the word embeddings from the 4 GLoVE word
#               embedding files and computes the cosine similarity for the 5 lists each
#               of the randomly generated verbs and nouns and their synonyms.
# Created by - Namita Kalady Prathap
# Last Modified on - Feb 1 2019
#################################################################################################

#import files
from numpy import asarray 
from sklearn.metrics.pairwise import cosine_similarity

 
# function to load the embeddings from a file
def glove_load( fname ): 
    word_embeddings = {}
    #opening the file in which GLove embeddings are present
    fin_file = open(fname)
    for i in fin_file:
        values = i.split()
        temp = values[0]
        temp2 = asarray(values[1:], dtype='float32')
        #assigning the vector to the word
        word_embeddings[temp] = temp2
    fin_file.close()
    print(' %s vectors were loaded.' % len(word_embeddings))
    #returning the list of vectors
    return word_embeddings

# function to compute the cosine similarity for the noun/verb lists
def cosine_func( nv_list):
        cos_vec = []
        temp = []  
        for i in range (0,5):
            temp = []
            for j in range (0,5):        
                word = nv_list[i][j]
                temp.append(word_vec[word]) 
            #making the list of vectors into 2D format for cosine similarity computation
            cos_vec.append(temp)

        tmp2 = []

        for k in range (0,5):
            for i in range (0,5):
                for j  in range(i+1,5):
                    #computing the cosine similarity and printing the result.
                    tmp2 = cosine_similarity([cos_vec[k][i]],[cos_vec[k][j]])
                    print nv_list[k][i], ',' ,nv_list[k][j], '-', tmp2

noun = []
verb = []

#list of synonyms for the verbs
verb.append(['describe', 'narrate', 'recount', 'relate',  'chronicle'])
verb.append(['unlock' , 'unbolt', 'unlatch', 'unpick',  'unfasten']) 
verb.append(['flash', 'shine', 'flare', 'blaze', 'glare'])
verb.append(['screw','fasten', 'secure', 'fix', 'attach'])
verb.append(['deliver','bring', 'take', 'convey',  'transport'])

#list of synonyms for the nouns
noun.append(['expert','specialist', 'authority', 'pundit', 'oracle'])
noun.append(['trade', 'craft', 'occupation', 'job', 'profession'])
noun.append(['number','numeral', 'integer', 'figure', 'digit'])
noun.append(['request',  'appeal', 'entreaty', 'plea', 'petition'])
noun.append(['color','hue', 'shade', 'tint', 'tone'])


#files of the GLoVE embeddings
filename = ['glove.6B.50d.txt','glove.6B.100d.txt','glove.6B.200d.txt','glove.6B.300d.txt']

#Looping through each file of GLoVE embeddings to compute the cosine similarity for each list
for index in range(len(filename)):
    word_vec = []
    print 'Loading the word embeddings from ', filename[index]
    word_vec = glove_load(filename[index])
    
    print('Calculating the cosine similarities for the synonym list of verbs')
    cosine_func(verb)
    
    print('Calculating cosine similarities for the synonym list of nouns')
    cosine_func(noun)
  
    
print('Successfully calculated the cosine similarity for the synonym lists of nouns and verbs.')    



