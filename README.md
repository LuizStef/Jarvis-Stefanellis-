# Demetrius

Personal Offline AI Assistant designed to learn, adapt and evolve with its user.

## Overview

Demetrius is a personal AI assistant built in Python, focused on:

- Running locally (offline-first)
- Learning from user interactions
- Adapting to user preferences and reasoning
- Maintaining privacy and full data control

## Requirements

- Python 3.10+
- [Ollama](https://ollama.com) installed and running
- Mistral model pulled: `ollama pull mistral`

## Installation

```bash
git clone https://github.com/LuizStef/Project-Jarvis.git
cd Project-Jarvis
pip install -r requirements.txt
```

## Usage

```bash
ollama serve        # terminal 1
python hearth.py    # terminal 2
```

## Commands

| Command | Action |
|---|---|
| `exit` | Shutdown Demetrius |
| `!clear` | Clear conversation history |
| `!history` | Show conversation history |
| `!mood` | Show current mood |
| `!mood excited` | Change mood |
| `!stats` | Show message statistics |

## Project Structure


Demetrius/
├── config.py           # Central configuration
├── base.py             # Base Assistant class
├── soul.py             # Personality and greetings
├── smart_memory.py     # SQLite persistent memory
├── semantic_memory.py  # FAISS semantic search
├── core.py             # AI brain (Ollama + Mistral)
├── demetrius.py        # Main Demetrius class
├── hearth.py           # Boot and main loop
├── exceptions.py       # Custom exceptions
└── requirements.txt    # Dependencies

## Tech Stack

- Python 3.10+
- SQLite
- FAISS
- Sentence Transformers
- Ollama + Mistral

## Status

In active development.

## Vision

To build a personal AI system that learns continuously, reflects the user's thinking, and remains private, lightweight, and independent.

## License

Open-source (to be defined)