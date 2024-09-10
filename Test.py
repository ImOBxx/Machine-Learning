import uproot

# Open a ROOT file
file = uproot.open("your_file.root")

# Access a histogram or tree
hist = file["hist_name"]

# Convert the histogram to a NumPy array
values = hist.values()
edges = hist.edges()

print(values)
print(edges)
