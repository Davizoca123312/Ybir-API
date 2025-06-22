from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from sentiment import analyze_emotions
from storage import init_db, save_analysis, get_emotion_distribution

app = FastAPI()

# Inicializa o banco ao iniciar
init_db()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class AnalyzeRequest(BaseModel):
    text: str
class RankRequest(BaseModel):
    texts: list[str]

# Endpoint para análise de emoções
@app.post("/analyze")
async def analyze(request: AnalyzeRequest):
    if not request.text or not request.text.strip():
        raise HTTPException(status_code=400, detail="Campo 'text' obrigatório")
    try:
        emotion, confidence, all_emotions, explanation = analyze_emotions(request.text)
        save_analysis(request.text, emotion, confidence, explanation)  #type: ignore
        return {
            "emotion": emotion,
            "confidence": confidence,
            "all_emotions": all_emotions,
            "explanation": explanation,
            "message": "Análise concluída com sucesso"
        }
    except Exception as e:
        print("Erro no /analyze:", e)
        raise HTTPException(status_code=500, detail=str(e))

# Endpoint para ranking de emoções
@app.post("/rank")
async def rank(request: RankRequest):
    if not request.texts or not isinstance(request.texts, list):
        raise HTTPException(status_code=400, detail="Campo 'texts' obrigatório e deve ser uma lista")
    emotion_count: dict[str, int] = {}

    for text in request.texts:
        try:
            if not text or not text.strip():
                continue  # Ignora textos vazios
            emotion, confidence, all_emotions, explanation = analyze_emotions(text)
            save_analysis(text, emotion, confidence, explanation)  #type: ignore
            if emotion:
                # Incrementa a contagem da emoção
                emotion_count[emotion] = emotion_count.get(emotion, 0) + 1
                
        except Exception as e:
            print(f"Erro ao analisar o texto '{text}': {e}")
            continue
    sorted_emotions = sorted(emotion_count.items(), key=lambda x: x[1], reverse=True)    
    return {"ranked_emotions": sorted_emotions}


@app.get("/", response_class=HTMLResponse)
async def dashboard():
    distribution = get_emotion_distribution()
    html = """
    <html>
    <head>
      <title>Dashboard YbyráAPI</title>
      <style>
        body { font-family: Arial, sans-serif; padding: 20px; }
        table { border-collapse: collapse; width: 300px; }
        th, td { border: 1px solid #ddd; padding: 8px; text-align: left; }
        th { background-color: #f2f2f2; }
      </style>
    </head>
    <body>
      <h1>Dashboard de Análises de Sentimento</h1>
      <table>
        <thead><tr><th>Emoção</th><th>Percentual (%)</th></tr></thead>
        <tbody>
    """
    for emotion, percent in distribution.items():
        html += f"<tr><td>{emotion}</td><td>{percent:.2f}</td></tr>"
    html += """
        </tbody>
      </table>
    </body>
    </html>
    """
    return html

@app.get("/summary")
async def summary():
    distribution = get_emotion_distribution()
    total = sum(distribution.values())
    return {
        "total_analyses": total,
        "emotion_distribution_percent": distribution
    }
