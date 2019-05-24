#!/usr/local/bin/python
# coding: latin-1
import numpy as np
x = np.array([42,47.5,11],int)
#print x
y = np.array( [11,12,13] )
#print y
z = np.array([x,y])
#print z


# Array are zero based, array 0 is vertical, 1 is horizontal.
# (h,v)
#print 'Element at 0, 1:'
#print  y[0][1]

# Check Array size
#print y.ndim

# Shape, size, of the array.
#print y.shape

# Show up to row 2 included
#print y[:2];

# Show element 1,1, equal to y[1][1]
#print y[1,1];

#print 'Shows vertical element 2'
#print y[:,2];

#print 'Type of an array:' + str(y.dtype)

print 'Reshaping arrays....'
f = np.array(range(36))
print f
fr = f.reshape(9,4)
print fr
#2x2
print fr[:-7,:-2]



print 'Array concatenation:'
x = np.array([11,22])
y = np.array([18,7,6])
z = np.array([1,3,5])
print x
print y
print z
w = np.concatenate((x,y,z))
print w
wr = w.reshape(4,2)
print 'two x two'
print wr[:-2,:]
print 'one x two'
print wr[:-3,:]


print 'Concatenate according to axis'
z = np.concatenate((x,y),axis = 0)
print 'own try: concanate segun axis'
w = np.concatenate(f,x)
print w
quit()


print z

quit(0)

print 'Adding new dimensions'
x = np.array([2,5,18,14,4])
y = x[:, np.newaxis]
print x
print y

print np.zeros((30,30))
print np.ones((29,2))

import sys

print 'Input line parameters'
print sys.argv

print 'Byte order:'+str(sys.byteorder)
print sys.exec_prefix
print sys.executable
print sys.modules
print sys.path
print sys.version_info
print sys.platform


print sys.argv[0]

a=[1,2,3,4,5]

print a
print 'List with the last two elements truncated.'
print a[:-2]

a.append(3)
a.pop(1)
print a
print a.count(1)
a.remove(3)
print a
a.extend([3,2])
print a
a.reverse()
print a
print a.index(3)
a.sort()
a.insert(2, [3,2])
print a
