import cohere

# Initialize Cohere client with your API key
co = cohere.Client('2CyeJ8YI9GjTFae45ilb1fuTMQu5ET0L10tuSaed')  # Replace with your actual key

# Define your message
# message = "Give me a recipe using chicken, garlic, and tomatoes."
message = input("Enter the incrediants: ")

# Use chat endpoint instead of generate
response = co.chat(
    model='command-r-plus',  # You can use 'command-r' or 'command-r-plus' if available
    message=message
)

# Print the response
print("Recipe:\n")
print(response.text.strip())