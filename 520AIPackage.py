#
#  520AIPackage.py
#  520AIPackage
#
#  Created by YHQiu on 19/5/20.
#  Copyright (c) 2019年 520AIPackage. All rights reserved.
#

import random
import numpy as np
#import tensorflow as tf
#import matplotlib.pyplot as plt

love = random.randint(1,10)
a = np.array([love])
b = np.array([1000,100,10,1,0.1,0.01])

def generateYourRedPackage(a,b):
#    tensor_a = tf.convert_to_tensor(a)
#    tensor_b = tf.convert_to_tensor(b)
#    with tf.Session() as sess:
#        result = sess.run(tf.add(tensor_a,tensor_b))
#        plt.scatter(result)
#        plt.show()
    return np.sum(a*b)

def printYourRedPackageDescription(a,b,love):
    resultNum = generateYourRedPackage(a,b)
    print("Congratulations on your win an award: \nBeing single for %.0f years " % (resultNum/love))
    return resultNum

print("Your red package amount is:%.2f" % printYourRedPackageDescription(a,b,love))

