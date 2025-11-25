import os
import google.generativeai as genai

# Set credentials
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "/Users/apple/Downloads/geminichatbotproject.json"

# Optional: suppress gRPC warnings
os.environ['GRPC_VERBOSITY'] = 'ERROR'
os.environ['GRPC_TRACE'] = ''

# List available models
models = genai.list_models()
print("Available models:")
for m in models:
    # Print just the model name
    print(m.name)

