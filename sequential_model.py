def sigmoid(x):
    return  1/(1 + np.exp(-x)) 


class Layer():
    def __init__(self, neuron_number,activation=sigmoid, first_layer=None ,layer_location=None, parent_model=None):
        self.layer_location = layer_location
        self.first_layer = first_layer
        self.parent_model = parent_model
        self.activation = sigmoid
        self.neuron_number = neuron_number
        self.input_values_len = None
        self.weights = None
        self.bias = None
       
        
    def initialize(self):
        if self.first_layer: 
            self.input_values_len  = len(self.parent_model.input_data)
        else:
            self.input_values_len  = self.parent_model.model_layers[self.layer_location-1].neuron_number
            
            
        self.weights = np.array([np.random.rand(self.input_values_len) for x in  range(self.neuron_number)])
        self.bias = np.random.rand(self.neuron_number)
        print(f'Layer {self.layer_location} initialized')
        
    def foward(self):
        if self.first_layer:
            input_values = self.parent_model.input_data
        else:
            input_values = self.parent_model.model_layers[self.layer_location-1].foward()
            
        return self.activation (self.weights.dot(input_values.T) + self.bias)
    

class Sequential_model():
    def __init__(self, input_data):
        
        self.model_layers = []
        self.input_data = input_data

        
    def add(self, layer):
        if not self.model_layers: # if it is the first layer
            layer.layer_location =  0
            layer.first_layer = True
        else:
            layer.layer_location = len(self.model_layers) 
            layer.first_layer = False
        layer.parent_model  = self
        self.model_layers.append(layer)
            
            
    def initialize(self):
        for e in self.model_layers:
            e.initialize()
            
    
    def foward_pass(self):
        print (self.model_layers[-1].foward())

        
        
        
X = np.array([0,1,0,1])
X.shape
model = Sequential_model(X)
model.add(Layer(5))
model.add(Layer(5))
model.add(Layer(1))
model.initialize()
model.foward_pass()
