from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
def get_feature_matrix(N = 55):
    
    #initialize the feature vector with zeros. 
    x_vec = np.zeros((N,3))

    x = []
    for i in range (N):
        im = Image.open("images/image_{number}.jpg".format(number=i+1))

        width, height = im.size

        rgb_im = im.convert('RGB')

        red = []
        green = []
        blue = []

        for y in range (height):
            for x in range (width):
                pixel = rgb_im.getpixel((x,y))
                red.append(pixel[0])
                green.append(pixel[1])
                blue.append(pixel[2])
        x_vec[i] = np.mean(red), np.mean(green), np.mean(blue)
    
    return x_vec;

def get_labels(N=55):
    y = np.zeros((N,1));
  
    y = np.zeros((N,1))
    #raise NotImplementedError()
    for i in range (0,20):
        y[i] = 1
    for i in range (21, N):
        y[i] = 0
    return y

def sigmoid_func(z):
    sigmoid = 1/(1+np.exp(-z))
    return sigmoid

def gradient(X,y,w):
    grad = []
    grad = np.transpose(np.dot(np.transpose(X), -(y-sigmoid_func(np.dot(X, np.transpose(w))))))/len(X)
    #raise NotImplementedError()
    return grad

def logisticRegression_func(X,y,step_size, K):
    N = X.shape[0]
    d = X.shape[1]
    # Initialize w as 1xd array.
    w = np.zeros((1,d))
    loss = float('inf')
    loss_list = []
    for i in range(K):
       # loss_list.append(gradient(X,y,w))
      
        cost = (1/N*np.dot(np.transpose(-y),np.log(sigmoid_func(np.dot(X,np.transpose(w)))))-np.dot(np.transpose((1-y)),np.log(1-sigmoid_func(np.dot(X,np.transpose(w))))))
        w = np.subtract(w, step_size*loss_list[i])
        loss_list.append(cost[0])
        #raise NotImplementedError()
    return loss_list, w

""" Predict Output """
def predict_output(X,w):
    y = []

    value = sigmoid_func(np.dot(X, np.transpose(w)))
    for i in range (len(value)):
        if value[i] >= 0.5:
            y.append(1)
        else:
            y.append(0)
    return y

y = get_labels()
X = get_feature_matrix()


# Full Vector
# Let s label : Grass = 1 , Soil = 0, Tiles = 0
assert X.shape == (55,3)
#axes = Visualize_data(X,y)
step_size = 1e-5
num_iter = 3000
e_list, w_opt = logisticRegression_func(X,y,step_size,num_iter)
print ('The optimal weight vector is:', w_opt)
y_hat = predict_output(X,w_opt)

def visualize_error(X, y, step_sizes, best = None, num_iter = 2000):
    plt.figure(figsize=(12, 4))
    fig, axes = plt.subplots(1, 2,figsize=(12, 4))
    for step in step_sizes:
        loss_list, w_opt = logisticRegression_func(X, y, step, num_iter)
        #raise NotImplementedError()
        n = len(loss_list) # Size of list remains the same.
        x_axes = np.linspace(0,n,n,endpoint=False)
        axes[0].plot(x_axes, loss_list, label=step)
    axes[0].set_xlabel('Number of Iterations')
    axes[0].set_ylabel('Loss Function')
    axes[0].legend()
    axes[0].set_title(r'$\bf{Figure\ 4.}$Converge of GD')
    
    for step in step_sizes:
        ### STUDENT TASK ###
        # Plot Error against Step Size.
        # Now mark the best converge in red. Use value from best as a correct step size.
        loss_list, w_opt = logisticRegression_func(X, y, step, num_iter)
        # YOUR CODE HERE
        #raise NotImplementedError()
        n = len(loss_list) # Size of list remains the same.
        x_axes = np.linspace(0,n,n,endpoint=False)
        if step == best:
            axes[1].plot(x_axes, loss_list, label=step, color="red")
        else:
            axes[1].plot(x_axes, loss_list, label=step, color="blue")
    
    axes[1].set_xlabel('Number of Iterations')
    axes[1].set_ylabel('Loss Function')
    axes[1].legend()
    axes[1].set_title(r'$\bf{Figure\ 5.}$Converge of GD')
    plt.tight_layout()
    return best, axes

### STUDENT TASK ###
# Change best=None into step size from the list that provides the fastest converge. e.g best=1
res0_1, axes = visualize_error(X/255, y, best=None, step_sizes=[0.1,0.5,1,5,10,16])
# YOUR CODE HERE
#raise NotImplementedError()