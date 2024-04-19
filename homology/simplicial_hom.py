import numpy as np

class Simplicial_Complex:
	'''
	Return the dimension of a simplex, which is just the # of vertices - 1
	'''
	@staticmethod
	def dim(simplex) -> int:
		return len(simplex) - 1

	'''
 	For a simplex, check if the class has all subsets of this simplex one dimension lower 
  	'''
	def contains_subsets_of(self, simplex):
		# Vertices have no proper subset but the empty set
		if Simplicial_Complex.dim(simplex) == 0:
			return True
  
		lower_simplices = self.simplices[Simplicial_Complex.dim(simplex) - 1]
  
		# Generate all the faces for the simplex
		face = simplex
		for i in range(Simplicial_Complex.dim(simplex) + 1):
			vert = face.pop(i)
			is_face_in = False
			for lower_simplex in lower_simplices:
				if set(lower_simplex) == set(face):
					is_face_in = True
			face.insert(i, vert)
   
			if not is_face_in:
				return False

		# All possible faces are already in the complex
		return True

	'''
	Check if the simplicial complex given is valid
	'''
	def is_valid(self):
		# For every simplex, check if all subsets of it is contained within the class
		for cur_dim in range(0, self.dim + 1):
			for simplex in self.simplices[cur_dim]:
				if not self.contains_subsets_of(simplex):
					return False
		return True


	'''
	Initiate a simplicial complex
	'''
	def __init__(self, complex_as_list):
		# Store the list
		self.complex_as_list = complex_as_list
    
  		# Get the dimension of the simplicial complex (the maximum of the dimensions of all the simplices)
		self.dim = 0
		for simplex in complex_as_list:
			if Simplicial_Complex.dim(simplex) > self.dim:
				self.dim = Simplicial_Complex.dim(simplex)

		# Seperate the list into different dimension

		# Create an array that holds simplices of 0th dimension to the highest dimension 
		self.simplices = []
		for cur_dim in range(self.dim + 1):
			self.simplices.append([])
			for simplex in complex_as_list:
				if Simplicial_Complex.dim(simplex) == cur_dim:
					self.simplices[cur_dim].append(simplex)
		# Then confirm that the list given is indeed a simplicial complex
		assert(self.is_valid())
  
		# Once it is confirmed that the simplicial complex is valid
	
	'''
	Compute the boundary operators 
 	'''
	def compute_homology():
		...
	
  	

if __name__ == '__main__':
    # valid simplicial complex
	K_list = [['A'], ['B'], ['C'], ['A', 'B', 'C'], ['A', 'B'], ['B', 'C'], ['C', 'A']]
	K = Simplicial_Complex(K_list)
	K.boundary([['A', 'B']])
	
	# not valid simplicial complex, throws assertion error
	# K_prime_list = [['A'], ['B'], ['C'], ['A', 'B', 'C'], ['A', 'B'], ['B', 'C']]
	# K_prime = Simplicial_Complex(K_prime_list)
 
	