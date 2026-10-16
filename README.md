# Fine-tuning de modelos para Three.js e shaders

Projeto experimental de fine-tuning para adaptar um modelo de linguagem a perguntas e tarefas de programação gráfica com **Three.js**, **GLSL** e shaders. A ideia foi explorar como um modelo local pode gerar exemplos de código mais direcionados a cenas 3D, materiais, iluminação, animação e efeitos visuais.

O fine-tuning foi executado com **LLaMA Factory**, usando o modelo base **Qwen3.5-9B-Base** e a técnica **LoRA**. O **LM Studio** foi usado como ambiente local para carregar e interagir com modelos. São ferramentas com papéis diferentes neste fluxo: o treinamento foi feito no LLaMA Factory; o LM Studio é voltado à execução e interação local com modelos compatíveis.

## Objetivos

- Experimentar fine-tuning supervisionado de um modelo para programação gráfica.
- Preparar exemplos de instruções e respostas com código Three.js e GLSL.
- Explorar LoRA como alternativa para adaptar um modelo sem salvar uma cópia completa dos pesos ajustados.
- Investigar um fluxo local de uso de modelos com o LM Studio.

## Tecnologias

- **LLaMA Factory** — configuração e execução do fine-tuning supervisionado (SFT).
- **LoRA / PEFT** — ajuste eficiente do modelo por meio de um adapter.
- **Qwen3.5-9B-Base** — modelo base utilizado no treinamento.
- **LM Studio** — ambiente local para carregar e interagir com modelos.
- **Three.js, JavaScript e GLSL** — tecnologias e temas abordados pelos exemplos do dataset.
- **JSON** — formato dos dados de treinamento.

## Dataset

O conjunto de dados está em [`data/threejs_shaders.json`](data/threejs_shaders.json) e contém **10 exemplos** no formato de instrução e resposta:

```json
{
  "prompt": "Crie um ShaderMaterial com um gradiente vertical no fragment shader.",
  "completion": "..."
}
```

Os exemplos cobrem tópicos como criação de cenas e geometrias, materiais e iluminação, animação com `uTime`, `ShaderMaterial`, efeitos Fresnel, sombras, `InstancedMesh`, carregamento de modelos GLTF/GLB e pós-processamento.

O mapeamento do dataset usado pelo LLaMA Factory está descrito em [`data/dataset_info.json`](data/dataset_info.json).

## Configuração do fine-tuning

O treinamento registrado nos arquivos do projeto utilizou:

| Parâmetro | Valor |
| --- | --- |
| Modelo base | `Qwen/Qwen3.5-9B-Base` |
| Etapa | SFT (fine-tuning supervisionado) |
| Método | LoRA |
| Épocas | 3 |
| Learning rate | `5e-5` |
| Rank LoRA | 8 |
| Alpha LoRA | 16 |
| Batch por dispositivo | 2 |
| Acumulação de gradiente | 8 |
| Comprimento máximo da sequência | 2048 tokens |
| Precisão | BF16 |
| Template | `qwen3_5` |

As configurações e os resultados gerados pelo treinamento ficam em `saves/`. Essa pasta é ignorada pelo Git, pois pode conter pesos grandes e arquivos intermediários. Portanto, os artefatos locais do treinamento não são incluídos neste repositório.

## Resultados registrados

Na execução registrada, o treinamento chegou a **3 de 3 passos**, percorreu **3 épocas** e processou **9.392 tokens**. A perda de treinamento registrada foi **0,3637**, com duração aproximada de **67 minutos**.

Esses números descrevem apenas o treinamento: não há métricas de avaliação em um conjunto de validação nem comparação documentada com o modelo base. Como o dataset atual tem somente 10 exemplos, este trabalho deve ser entendido como uma **prova de conceito**, não como evidência de desempenho ou generalização para uso em produção. Uma próxima etapa importante é ampliar e revisar os dados e medir a qualidade das respostas em prompts que não aparecem no treinamento.

## Estrutura do projeto

```text
.
├── data/
│   ├── dataset_info.json
│   └── threejs_shaders.json
├── finetune.py
└── README.md
```

Os diretórios `saves/`, `output/` e `models/`, além de pesos e checkpoints, são ignorados pelo Git. O arquivo `finetune.py` é um exemplo introdutório de preparação de dados; o treinamento documentado neste README foi executado pelo LLaMA Factory.

## Possíveis melhorias

- Expandir o dataset com exemplos variados, revisados e consistentes.
- Separar dados de treino e validação e registrar métricas de avaliação.
- Testar as respostas do modelo ajustado em tarefas Three.js/GLSL não presentes no dataset.
- Documentar o fluxo de exportação ou carregamento do adapter no ambiente local, verificando a compatibilidade do formato com o LM Studio.

## Observação

Este repositório documenta um experimento de aprendizado e fine-tuning. O modelo e as ferramentas citados pertencem aos seus respectivos autores e seguem suas próprias licenças e condições de uso.
