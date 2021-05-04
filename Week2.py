import tensorflow as tf
from tensorflow import keras
mnist = tf.keras.datasets.fashion_mnist
(training_images, training_labels),(test_images,test_labels) = mnist.load_data()
training_images = training_images / 255.0
test_images = test_images / 255.0 
model = tf.keras.models.Sequential([tf.keras.layers.Flatten(), 
                                    tf.keras.layers.Dense(128, activation=tf.nn.relu), 
                                    tf.keras.layers.Dense(10, activation=tf.nn.softmax)])
model.compile(optimizer = tf.optimizers.Adam(),
              loss = 'sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.fit(training_images, training_labels, epochs=5)

print(model.evaluate(test_images,test_lables))