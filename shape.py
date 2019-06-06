import tensorflow as tf
import numpy as np
a_array=np.array([[1,2,3],[4,5,6]])
b_list=[[1,2,3],[3,4,5]]
c_tensor=tf.constant([[1,2,3],[4,5,6]])
(2,3)
print(c_tensor.get_shape())

[2,3]
print(c_tensor.get_shape().as_list())
with tf.Session() as sess:
    #[2,3]
    print(sess.run(tf.shape(a_array)))
    #[2,3]
    print(sess.run(tf.shape(b_list)))
    #[2,3]
    print(sess.run(tf.shape(c_tensor)))
