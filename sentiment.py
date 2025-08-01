from pysentimiento import create_analyzer
from transformers.pipelines import pipeline

# Inicializa o analisador de emoções para português
emotion_analyzer = create_analyzer(task="emotion", lang="pt")

# Inicializa um gerador de texto leve, para explicações
text_generator = pipeline("text-generation", model="distilgpt2")

def generate_explanation(emotion, confidence):
    prompt = (
        f"Explique em poucas palavras por que o texto demonstra a emoção '{emotion}' "
        f"com uma confiança de {confidence:.2%}."
    )
    result = text_generator(prompt, max_length=50, do_sample=True, temperature=0.7)
    # Verifica se o resultado é válido
    if not result or not isinstance(result, list) or 'generated_text' not in result[0]:
        raise ValueError("Erro ao gerar explicação: resposta inesperada do gerador de texto.")
    explanation = str(result[0]['generated_text'])
    # Remove o prompt do texto gerado para ficar só a explicação
    explanation = explanation.replace(prompt, "").strip()
    return explanation

def save_analysis(emotion: str, confidence: float, explanation: str):
    with open("analises.log", "a", encoding="utf-8") as f:
        f.write(f"Emoção: {emotion}, Confiança: {confidence:.2f}, Explicação: {explanation}\n")

def analyze_emotions(text: str):
    result = emotion_analyzer.predict(text)

    if isinstance(result, list): 
        result = result[0]

    main_emotion = result.output

# Verifica se a emoção é uma lista ou string
    if isinstance(main_emotion, list):
        main_emotion = main_emotion[0]

    if not main_emotion or main_emotion == "NEUTRO":
        raise ValueError("Nenhuma emoção detectada no texto.")

    confidence = float(result.probas[main_emotion])
    all_emotions = {k: float(v) for k, v in result.probas.items()}

    explanation = generate_explanation(main_emotion, confidence)

    return main_emotion, confidence, all_emotions, explanation
