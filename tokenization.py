import tiktoken

encoder = tiktoken.encoding_for_model("gpt-4")

print("Vocab size", encoder.n_vocab)

text = "The cat sat on the mat"
tokens = encoder.encode(text)

print("Tokens:", tokens)

my_tokens = [791, 8415, 7731, 389, 279, 5634]
decoded_text = encoder.decode(my_tokens)
print("Decoded text:", decoded_text)