# Consultant Matcher

AI-powered tool that matches freelance consultants to project briefs using Claude.

## What it does
Paste a client mission brief. The tool reads a consultant database and returns 
the top 3 matches, ranked by fit, with detailed explanations in French.

## Why I built it
I work in consulting staffing. Matching consultants to missions manually 
takes hours. This tool does it in 30 seconds.

## Tech stack
Python · Anthropic Claude API · pandas

## How to use
1. Clone the repo
2. pip3 install anthropic pandas python-dotenv
3. Create a .env file with your ANTHROPIC_API_KEY
4. python3 matcher.py
