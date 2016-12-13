__author__ = 'chenxinyue'
import numpy
def get_data():
    x12s = [[39.021329327548834, 6.139414357981793], [14.552571401554987, 16.899637393859702],
            [24.734102467141426, 34.25552447849699], [3.8957566261623002, 18.596865883521303],
            [7.820063914309689, 27.341672575970183], [28.1274404887128, 3.1149810424508875],
            [2.114379708272318, 3.2322764266315804], [33.807280733483616, 46.70316773596885],
            [45.52041437597939, 6.436634048846962], [19.095405802275238, 37.812796701434905]]
    x = numpy.array([[1] + [x12[0], x12[1]] for x12 in x12s])
    y = numpy.array([-1, 1, 1, 1, 1, -1, 1, -1, -1, 1])
    data = {}
    data['x'] = x
    data['y'] = y
    return data


def train(data, w):
    g = numpy.dot(data['x'], w)
    for i in range(0, len(data['y'])):
        if g[i] * data['y'][i] <= 0:
            print "i=" + str(i)
            print "x=" + str(data['x'][i])
            print "y=" + str(data['y'][i])
            print "w=" + str(w)
            delta = numpy.dot(data['y'][i], data['x'][i])
            print "delta=" + str(delta)
            new_w = w + delta
            print "new_w=" + str(new_w)
            w = new_w
            break
    return w


def pla(tran_times, data, w):
    for i in range(0, tran_times):
        print "***********" + str(i) + "*************"
        w = train(data, w)

if __name__ == '__main__':
    data = get_data()
    pla(1000, data, numpy.array([0, 1, 1]))
