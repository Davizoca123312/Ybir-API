
# 🌿 YbyráAPI – Análise Emocional de Conteúdo Brasileiro em Tempo Real

A **YbyráAPI** é uma API inteligente para análise de sentimentos e emoções em textos escritos em **português brasileiro**, com foco especial em conteúdos oriundos de **redes sociais**. Ideal para sistemas que precisam entender o comportamento emocional de usuários, ela fornece informações úteis para empresas, ferramentas de moderação, bots inteligentes e produtos baseados em interação humana.

## 🚀 Funcionalidades principais

- 🧠 **Identificação automática de sentimentos predominantes** (ex: alegria, tristeza, raiva, medo, etc.)
- 📈 **Índice de confiança** para cada sentimento detectado
- 🗣️ **Sugestões interpretativas** com base nas emoções identificadas
- 🔁 **Análise em tempo real** com resposta rápida para aplicações integradas

---

## 🛠️ Em desenvolvimento / Funcionalidades futuras

- 📋 **Listagem dos principais sentimentos** encontrados ao analisar listas de textos (ex: de posts ou comentários)
- 📊 **Contagem total de sentimentos** identificados em um texto
- 🧩 **Análise combinada** de emoções sutis (ex: misturas como alegria + nostalgia)
- 🕵️ **Detecção de ironia/sarcasmo** (experimental)
- 🧪 **Interpretação contextual com base em gírias ou expressões populares brasileiras**

---

## 📊 Aplicações ideais

- **Plataformas de monitoramento e análise de redes sociais**
- **Ferramentas SaaS de marketing digital e publicidade**
- **Mecanismos de moderação automática de conteúdo**
- **Assistentes virtuais e chatbots com respostas emocionalmente adaptadas**
- **Pesquisas acadêmicas e estudos de comportamento social**

---

## 💡 Por que usar a YbyráAPI?

- 📊 Gerem **insights úteis para empresas** baseados em como as pessoas se sentem
- 🧠 Representem **estados emocionais reais e sutis** de usuários em redes sociais
- 🧪 Sejam **viáveis de detectar via linguagem natural** com IA moderna e suporte multilíngue

---

## 🔌 Exemplo de uso

### Requisição:

```bash
POST /analyze
Content-Type: application/json

{
  "text": "Estou muito feliz com o seu serviço!"
}
```

### Resposta:

```json
{
  "sentiment": ["Joy", 0.85, {
    "Joy": 0.85,
    "Sadness": 0.05,
    "Anger": 0.03,
    "Fear": 0.02
  }],
  "message": "Analysis completed successfully"
}
```

---

## 🧠 Tecnologias utilizadas

- [Python 3.10+](https://www.python.org/)
- [Flask](https://flask.palletsprojects.com/)
- [Transformers (Hugging Face)](https://huggingface.co/)
- Modelo BERT multilíngue para análise de sentimentos

---

## 📦 Instalação (modo local)

```bash
# Clone o repositório
git clone https://github.com/seu-usuario/ybyraapi.git
cd ybyraapi

# Instale dependências
pip install -r requirements.txt

# Inicie a API
python app.py
```

---

## 📬 Contato

Desenvolvido por Isaac Estevan Geuster  
📧 Email: isaacegeuster@gmail.com

---

> “Ybyrá”, do tupi-guarani: **árvore**, símbolo de vida e conexão — como os sentimentos que conectam as pessoas.
