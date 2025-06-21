from pysentimiento import create_analyzer


# eu mudei tudo agora essa é uma IA feita pra detectar emoções em textos
# vou criar o analizador de sentimentos
emotion_analyzer = create_analyzer(task="emotion", lang="pt")

def save_analysis(emotion):
    # Salva cada análise em um arquivo de log simples
    with open("analises.log", "a", encoding="utf-8") as f:
        f.write(f"{emotion}\n")
def analyze_emotions(text):
    result = emotion_analyzer.predict(text)

    # Garante que main_emotion seja string única
    main_emotion = result.output
    if isinstance(main_emotion, list):
        main_emotion = main_emotion[0]

    confidence = result.probas[main_emotion]
    all_emotions = {k: float(v) for k, v in result.probas.items()}

    return main_emotion, float(confidence), all_emotions
