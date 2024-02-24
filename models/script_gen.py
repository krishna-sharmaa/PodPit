import ollama

def contentGenerator(kyaHuaa):
    stream = ollama.generate(
    model="llama2",
    prompt=kyaHuaa,
    stream=True
    )
    ans=""
    for chunk in stream:
        ans=ans+(chunk.get('response'))
    return ans 
