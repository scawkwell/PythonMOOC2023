# Write your solution here

def spruce(height):
    print("a spruce!")
    layer = 1
    
    while layer <= height:
        
        leaves = 2 * layer -1
        spaces = height - layer
        tree = spaces * " " + leaves * "*"

        print(tree)

        layer += 1
    
    print((height-1) * " " + "*")

# You can test your function by calling it within the following block
if __name__ == "__main__":
    spruce(5)