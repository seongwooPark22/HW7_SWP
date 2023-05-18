import numpy as np

def main() : 
    docs = np.array([
        [1,1,0,1,0,1],
        [1,1,1,0,1,0],
        [1,1,0,1,0,0]
    ])
    
    query = [1,1,0,0,1,0]
    query_norm = np.dot(query, query)

    cosine_similarity = []
    for i in docs : 
        cos_sim_norm = np.dot(i, i)
        cosine_similarity.append(
            np.dot(i, query)/(query_norm * cos_sim_norm)
        )
    for i in range(len(docs)) : 
        print("doc{0}={1:.2f}".format(i+1, cosine_similarity[i]))

if __name__ == "__main__" :
    main()
