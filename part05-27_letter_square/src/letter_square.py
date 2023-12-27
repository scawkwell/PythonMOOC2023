# Write your solution here
layer_count = int(input("Layers: "))
box_size = layer_count*2-1

alphabet = ["A", "B", "C", "D", "E", "F", "G", "H",
 "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", 
 "S", "T", "U", "V", "W", "X", "Y", "Z"]

layers = list(range(layer_count))  # [0, 1, 2, ..., layer_count-1]

# Create the first layer
layers[0] = alphabet[layer_count-1]*box_size

for index, layer in enumerate(layers):
    if index == 0:
        continue # Skip the first layer
    layers[index] = layers[index-1] # Copy the layer above
     # replace the middle of the text with the new letter the appropriate number of times:
    layers[index] = layers[index][:index] + alphabet[layer_count-index-1]*(box_size - 2 * index) + layers[index][-index:]
    
for layer in layers:
    print(layer)

for index, layer in enumerate(layers[::-1]):
    if index == 0:
        continue # skip the middle layer as it has already been printed
    print(layer)

