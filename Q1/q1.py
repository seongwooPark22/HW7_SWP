import numpy as np

def determinant2by2(a) :
    return a[0, 0]*a[1, 1]-a[0, 1]*a[1, 0]

def main() :
    vec1 = np.array([1,2,3])
    vec2 = np.array([4,5,6])

    arr = np.array([[1,2], [3,4]])
    eigen_vals, eigen_vectors = np.linalg.eig(arr)
    determinant = determinant2by2(arr)
    
    #determinant = np.linalg.det(arr)
    #it returns -2.0000000000000004, which is incorect.
    #to test bigger n*n matrix, please use this
    
    print("Eigenvalues:", eigen_vals)
    print("Eigenvectors:")
    print(eigen_vectors)

    print("Determinant:", determinant)
    
    cross_product = np.cross(vec1, vec2)
    print("Cross product:")
    print(cross_product)

    A = np.array([[1,2,-2],[2,1,-5],[1,-4,1]])
    solution = np.matmul(np.linalg.inv(A), np.array([-15,-21,18]))
    print("Solution:")
    print(solution)

if __name__ == "__main__" :
    main()

