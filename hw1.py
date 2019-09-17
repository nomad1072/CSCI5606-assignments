import numpy

# Double Precision

epsilon = 0.1

while (1 + epsilon != 1):
    result = epsilon
    epsilon = epsilon / 2

print('Results for double precision')
print('Epsilon Value: ', epsilon)
print('Power of (2^x): ', 2 ** result)

# Single Precision

epsilon1 = numpy.float32(0.1)

while(numpy.float32(1) + epsilon1 != numpy.float32(1)):
    result1 = epsilon1
    epsilon1 = epsilon1 / numpy.float32(2)

print('Results for single precision')
print('Epsilon Value: ', epsilon1)
print('Power of (2^x): ', 2 ** result1)
