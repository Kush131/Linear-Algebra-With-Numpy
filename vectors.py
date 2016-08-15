import numpy


def vector_addition(v1, v2):
    return(v1 + v2)


def vector_subtraction(v1, v2):
    return (v1 - v2)


def vector_scalar(s, v1):
    return (s * v1)


# How far does a vector change?
def vector_magnitude(v1):
    return numpy.linalg.norm(v1)


# Normalization = finding unit vector in same direction as given vector.
def vector_normalization(v1):
    return v1 / numpy.linalg.norm(v1)


# Dot Product = Multiply across vectors, then add all results together.
def vector_dot_product(v1, v2):
    return numpy.vdot(v1, v2)


# Angle Between = ArcCos of the dot product of the unit vector of both
# given vectors. Returns radians
def vector_angle_between(v1, v2, degrees=False):
    if degrees is False:
        return(numpy.arccos(
               numpy.clip(
                   numpy.vdot(vector_normalization(v1),
                              vector_normalization(v2)), -1.0, 1)))
    else:
        return(numpy.rad2deg(
            numpy.arccos(
                numpy.clip(
                    numpy.vdot(vector_normalization(v1),
                               vector_normalization(v2)), -1.0, 1))))

# Vector addition
# print("Addition Vectors:")
# a_vector_one = numpy.array([[8.218], [-9.341]])
# a_vector_two = numpy.array([[-1.129], [2.111]])
# print(vector_addition(a_vector_one, a_vector_two))

# Vector subtraction
# print("Subtraction Vectors:")
# s_vector_one = numpy.array([[7.119], [8.215]])
# s_vector_two = numpy.array([[-8.223], [0.878]])
# print(vector_subtraction(s_vector_one, s_vector_two))

# Scalar multiplication
# print("Scalar Vectors:")
# scalar_vector = numpy.array([[1.671], [-1.012], [-0.318]])
# print(vector_scalar(7.41, scalar_vector))

# Magnitude
# 1. Take the square root of all of the coordinates in the vector.
# 2. Add all of the coordinates together
# 3. Take the square root.

# print("Magnitude Vectors:")
# m_vector_one = numpy.array([[-0.221], [7.437]])
# m_vector_two = numpy.array([[8.813], [-1.331], [-6.247]])
# print(vector_magnitude(m_vector_one))
# print(vector_magnitude(m_vector_two))

# Normalization
# print("Normalization Vectors:")
# norm_vector_one = numpy.array([[5.581], [-2.136]])
# norm_vector_two = numpy.array([[1.996], [3.108], [-4.554]])
# print(vector_normalization(norm_vector_one))
# print(vector_normalization(norm_vector_two))

# Dot Product
dot_vector_one = ([[7.887], [4.138]])
dot_vector_two = ([[-8.802], [6.776]])
print(vector_dot_product(dot_vector_one, dot_vector_two))
dot_vector_three = ([[-5.955], [-4.904], [-1.874]])
dot_vector_four = ([[-4.496], [-8.755], [7.103]])
print(vector_dot_product(dot_vector_three, dot_vector_four))

# Angle Between
angle_vector_one = ([[3.183], [-7.627]])
angle_vector_two = ([[-2.668], [5.319]])

print(vector_angle_between(angle_vector_one,
                           angle_vector_two))

angle_vector_three = ([[7.350], [0.221], [5.188]])
angle_vector_four = ([[2.751], [8.259], [3.985]])
print(vector_angle_between(
      angle_vector_three,
      angle_vector_four,
      degrees=True))
