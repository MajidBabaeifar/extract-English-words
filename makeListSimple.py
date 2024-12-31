import json

# Input and output file paths
input_file = "fasttext-pos-result.json"  # Replace with your actual input file path
output_file = "fasttext-pos-result-simple.json"  # Replace with your desired output file path

# Read the JSON file
with open(input_file, "r") as file:
    data = json.load(file)

# Transform the data
transformed_data = [
    {"term": item["term"], "rawFreq": item["rawFreq"], "pos": item["pos"]}
    for item in data
]

# Write the transformed data to a new JSON file
with open(output_file, "w") as file:
    json.dump(transformed_data, file, indent=4)

print(f"Transformed JSON saved to {output_file}")
