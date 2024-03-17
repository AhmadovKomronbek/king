alphabet = ['a', 'b', 'c', 'd', 'e']
text = "Hello, world. Let's play minecraft"
if len(text) >= len(alphabet):
    num = len(text) % len(alphabet)
    print(num)
    alphabet=alphabet*num
    print(alphabet)