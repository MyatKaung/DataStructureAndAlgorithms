def friend(x):
    return [y for y in x if len(y)==4]

# Example usage:
input_names = ["Ryan", "Kieran", "Jason", "Yous"]
output_names = friend(input_names)
print(output_names)  # Output: ['Ryan', 'Yous']