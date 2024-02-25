import ollama
# kyaHuaa="farmer protest"
def contentGenerator(kyaHuaa):
    stream = ollama.generate(
    model="llama2",
    prompt=kyaHuaa,
    stream=True
    )
    ans=""
    for chunk in stream:
        ans=ans+(chunk.get('response'))
        # print(ans)
    return ans 

# print(contentGenerator(kyaHuaa))