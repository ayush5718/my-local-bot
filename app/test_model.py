from llama_cpp import Llama

model_path = r"E:\React projects\local-ai-assistant\model\phi-2.Q4_K_M.gguf"

llm = Llama(
    model_path=model_path,
    n_ctx=2048,
    n_threads=6
)

response = llm(
    "Q: What is 2 + 2?\nA:",
    max_tokens=50
)

print(response["choices"][0]["text"])
