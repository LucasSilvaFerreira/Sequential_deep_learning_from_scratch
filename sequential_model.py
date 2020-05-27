def sigmoid(x):
    return  1/(1 + np.exp(-x)) 


class layer():
    def __init__(neuron_number, input_values, activation=sigmoid, first_layer=None ,layer_location=None, parent_model=None):
        self.layer_location = layer_location
        self.first_layer = first_layer
        self.activation = sigmoid
        self.neuron_number = neuron_number

            
        self.weights = np.array([np.random.rand(len(self.input_values)) for x in  range(self.neuron_number)])
        self.bias = np.random.rand(self.neuron_number)
        
    def initialize(self):
        if self.first_layer: 
            self.input_values = parent_model.input_values
        else:
        
        
    def foward(self,input_values):
        return self.activation (self.weights.dot(input_values) + self.bias)
    
    
    
class sequential_model():
    def __init__(self, input_data):
        
        self.model_layers = []
        self.input_data = input_data
        
    def add(self, layer):
        if not self.model_layers: # if it is the first layer
            layer.layer_location =  0
            layer.first_Layer = True
        else:
            layer.layer_location = len(self.model_layers) 
            layer.first_Layer = False
        self.layer.parent_model  = self
        self.model_layers.append(self.layer)
            
