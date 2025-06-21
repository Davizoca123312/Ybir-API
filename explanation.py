from transformers import pipeline

# Use um modelo leve para geração de texto
generator = pipeline("text2text-generation", model="google/flan-t5-small")

def generate_explanation(text: str, emotion: str) -> str:
    prompt = (
        f"Explique de forma simples por que o texto a seguir expressa a emoção '{emotion}'. "
        f"Texto: {text}"
    )
    try:
        output = generator(prompt, max_length=60, do_sample=False)
        explanation = output[0]['generated_text']
        return explanation
    except Exception as e:
        print("Erro ao gerar explicação:", e)
        return "Não foi possível gerar uma explicação automática."
