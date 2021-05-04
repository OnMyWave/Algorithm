import tensorflow as tw
import matplotlib.pyplot as plt
X = [1,2,3]
Y = [1,2,3]

W = tw.placeholder(tw.float32)
# Our hypothesis for linear model X*W

hypothesis  = X * W

# Cost / Loss function
cost = tw.reduce_mean(tw.square(hypothesis - Y))

# Launch the graph in a session
sess = tw.Session()

# initializes global variables  in the graph.
sess.run(tw.global_variables_initializer())

W_val = []
cost_val = []
for i in range(-30,50):
    feed_W = i* 0.1
    curr_cost, curr_W = sess.run([cost,W],feed_dict = {W: feed_W})
    cost_val.append(curr_cost)

#show the cost function
plt.plot(W_val,cost_val)
plt.show()
