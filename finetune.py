# Script de fine-tuning com LM Studio local
# Conecta no endpoint local do LM Studio e faz fine-tuning

exemplo_codigo = '''
import json
import requests
from pathlib import Path

# Configuração do LM Studio local
LM_STUDIO_URL = "http://localhost:1234/v1"

def load_dataset(filepath):
    """Carrega dataset JSON"""
    with open(filepath, 'r') as f:
        return json.load(f)

def prepare_training_data(dataset):
    """Formata dados pra treinamento"""
    training_texts = []
    for item in dataset:
        prompt = item.get("prompt", "")
        completion = item.get("completion", "")
        # Formata como: "prompt\\ncompletion\\n"
        text = f"{prompt}\\n{completion}\\n"
        training_texts.append(text)
    return training_texts

def finetune_model(training_data, output_dir="./finetuned_model"):
    """
    Faz fine-tuning do modelo
    Nota: LM Studio local não suporta fine-tuning direto
    Você precisa usar a API do modelo e salvar logs de treinamento
    """
    print(f"Preparando {len(training_data)} exemplos de treinamento...")
    
    # Salva dados de treinamento
    Path(output_dir).mkdir(exist_ok=True)
    
    with open(f"{output_dir}/training_data.txt", "w") as f:
        f.write("\\n".join(training_data))
    
    print(f"Dados salvos em {output_dir}/training_data.txt")
    print("Para fine-tuning real, use: llama.cpp, ollama com GGUF, ou plataforma cloud")

if _name_ == "_main_":
    # Carrega seu dataset
    dataset = load_dataset("dataset.json")
    
    # Prepara dados
    training_data = prepare_training_data(dataset)
    
    # Faz fine-tuning
    finetune_model(training_data)
'''

print("Script de fine-tuning pronto:")
print(exemplo_codigo)