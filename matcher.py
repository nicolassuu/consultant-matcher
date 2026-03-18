import anthropic
import pandas as pd
from dotenv import load_dotenv
import os

load_dotenv()
client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

def load_consultants():
    df = pd.read_csv("consultants.csv")
    consultants_text = ""
    for _, row in df.iterrows():
        consultants_text += f"""
Name: {row['name']}
Skills: {row['skills']}
Experience: {row['experience_years']} years
Industries: {row['industries']}
Availability: {row['availability']}
TJM: {row['tjm']}€/day
---"""
    return consultants_text

def match_consultants(project_brief):
    consultants = load_consultants()
    
    prompt = f"""Tu es un expert en staffing de consultants freelance pour des cabinets de conseil français.

Voici une mission d'un client :
{project_brief}

Voici les consultants disponibles dans notre base :
{consultants}

Ta mission :
1. Identifier le top 3 des meilleurs profils pour cette mission
2. Donner un score de matching sur 100 pour chacun
3. Expliquer en 2-3 phrases pourquoi ce profil est adapté
4. Signaler les points de vigilance (disponibilité, TJM, écarts de compétences)
5. Ne recommander que les consultants marqués comme 'available'

Réponds en français. Sois précis et professionnel."""

    message = client.messages.create(
        model="claude-opus-4-5",
        max_tokens=1024,
        messages=[{"role": "user", "content": prompt}]
    )
    
    return message.content[0].text

def main():
    print("=== Consultant Matcher — MPG Partners ===\n")
    print("Colle le brief de la mission ci-dessous (appuie sur Entrée deux fois quand tu as fini) :\n")
    
    lines = []
    while True:
        line = input()
        if line == "":
            if lines:
                break
        else:
            lines.append(line)
    
    brief = "\n".join(lines)
    print("\nAnalyse en cours...\n")
    result = match_consultants(brief)
    print(result)

if __name__ == "__main__":
    main()