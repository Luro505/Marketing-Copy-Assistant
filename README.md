# Marketing-Copy-Assistant
A Python-based marketing asset generator utilizing Mistral LLMs. Demonstrates programmatic control over text generation styles by dynamically tuning hyperparameters (temperature, top_p, penalties) to generate structured, production-ready JSON marketing kits.



# LLM Marketing Copy Assistant: Hyperparameter-Tuned Asset Generation

A production-ready Python tool designed to automate the generation of diverse marketing collateral using Large Language Models (LLMs). This project demonstrates how to programmatically control LLM behavior—such as creativity, repetition, and length—by dynamically tuning API hyperparameters rather than relying solely on prompt engineering.

Utilizing the `mistralai/mistral-small-3.2-24b-instruct` model, the system generates highly distinct styles of marketing copy (taglines, ad campaigns, email newsletters, and product descriptions) and compiles them into a single, structured JSON marketing kit.

## Key Features

* **Dynamic Hyperparameter Tuning**: Programmatic control over LLM "dials" (Temperature, Top-P, Frequency/Presence Penalties) to match specific brand voices.
* **Multi-Format Asset Generation**: Generates four distinct marketing assets per product (emotional taglines, persuasive ad copy, structured emails, and detailed product descriptions).
* **Structured JSON Output**: Automatically aggregates, validates, and exports all generated assets into a structured JSON file ready for CMS or database ingestion.
* **Batch Processing**: Designed to process a multi-product catalog in a single pipeline execution.

## Technical Deep Dive: The Parameters

To achieve distinct writing styles for different marketing assets, the assistant fine-tunes the following API parameters under the hood:

| Asset Type | Primary Goal | Temperature | Top-P | Frequency Penalty | Presence Penalty |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Tagline** | High creativity, punchy, brief | 0.85 | 0.95 | 0.2 | 0.1 |
| **Ad Copy** | Persuasive, balanced, direct | 0.70 | 0.90 | 0.3 | 0.2 |
| **Email Campaign** | Informative, structured, natural | 0.60 | 0.85 | 0.1 | 0.1 |
| **Product Description** | Factual, detailed, professional | 0.40 | 0.80 | 0.0 | 0.0 |

### Parameter Definitions:
* **Temperature**: Controls randomness. Higher values (0.8+) yield creative, unexpected copy; lower values (below 0.5) ensure deterministic, factual descriptions.
* **Top-P (Nucleus Sampling)**: Limits the model's vocabulary pool to the top $P$ cumulative probability. Working alongside temperature, it prevents highly improbable word choices.
* **Frequency Penalty**: Discourages the model from repeating the exact same words or phrases, forcing more diverse vocabulary in longer assets like emails.
* **Presence Penalty**: Encourages the model to introduce new topics and ideas, ideal for brainstorming creative taglines and ad copy.

## Project Structure

```text
├── data/
│   └── products.json          # Fictional product catalog input
├── output/
│   └── marketing_kit.json     # Generated and structured marketing assets
├── config.py                  # Model and parameter configurations per asset type
├── generator.py               # Main pipeline logic and API integration 
└── main.py                    # CLI entry point to run the pipeline
