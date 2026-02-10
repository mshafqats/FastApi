from ollama import chat

def generate_answer(prompt: str, search_results: list) -> str:
    context = "\n".join([f"- {r['snippet']}" for r in search_results if r.get('snippet')])
    if not context:
        context = "No context available."

    full_prompt = f"Answer the following question using the context below:\nContext: {context}\nQuestion: {prompt}"

    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": full_prompt}
    ]

    response = chat(model="gemma3:1b", messages=messages)

    return getattr(response.message, "content", "")
