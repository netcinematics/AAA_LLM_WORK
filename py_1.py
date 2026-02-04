# ~GEM~ Verification
data = {'apple': 10, 'orange': 5, 'banana': 20, 'thing':1}
# data = {'apple': 10, 'orange': 5, 'banana': 20}

# Paste AI Code Below:
sorted_data = dict(sorted(data.items(), key=lambda item: item[1]))

# Add a print statement to SEE the result immediately
print(f"Original: {data}")
print(f"Result:   {sorted_data}") 
# Look for: {'orange': 5, 'apple': 10, 'banana': 20} in output
