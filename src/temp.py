__author__ = 'chenxinyue'
import random
import numpy

def init_param():
    x = []
    y = []
    for i in range(0, 10):
        x.append([random.uniform(0, 50), random.uniform(0, 50)])
        if 3 * x[i][0] - 40 < x[i][1]:
            y.append(1)
        else:
            y.append(-1)
    print x
    print y
    y = numpy.array(y)
    print numpy.dot(-1, y)


if __name__ == '__main__':
    # init_param()
    print numpy.dot(numpy.array([102, -26.52354866, 16.82703243]), numpy.array([  1, 14.552571401554987, 16.899637393859702]))

