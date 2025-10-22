# GitBuddy CLI

**GitBuddy CLI** is a command-line assistant for Git that helps you manage your repository, make commits, and even explain Git errors in simple terms using **Google Gemini AI**. Think of it as your personal Git tutor, available right in your terminal.

---

## Features

* ✅ Show Git status (`gitbuddy status`)
* ✅ Stage and commit all changes with a message (`gitbuddy commit "message"`)
* 🤖 AI-powered Git error explanations (`gitbuddy explain "error message"`)
* 💡 Uses Google Gemini 2.0 Flash for natural language explanations
* 🎨 Clean and user-friendly CLI output

---

## Prerequisites

* Python 3.10+
* Virtual environment recommended (`venv`)
* Git installed
* Google Gemini API Key

---

## Installation

1. Clone the repository:

```bash
git clone <your-repo-url>
cd gitbuddy-cli
```

2. Create a virtual environment and activate it:

```bash
python -m venv venv
source venv/bin/activate   # Mac/Linux
# venv\Scripts\activate     # Windows
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Setup

1. Obtain a **Google Gemini API Key** and set it in your environment:

```bash
export GEMINI_API_KEY="your_gemini_key_here"  # Mac/Linux
# set GEMINI_API_KEY="your_gemini_key_here"    # Windows
```

2. Initialize your Git repository if you haven’t already:

```bash
git init
```

---

## Usage

### 1. Show Git status

```bash
python gitbuddy.py status
```

### 2. Commit changes

```bash
python gitbuddy.py commit "your commit message"
```

### 3. Explain a Git error using AI

```bash
python gitbuddy.py explain "fatal: refusing to merge unrelated histories"
```

The AI will provide a plain-language explanation and suggested fix.

---

## Notes

* Make sure your API key has active access and credits for Gemini API usage.
* Avoid hardcoding the API key in the script — use environment variables for security.
* You can extend GitBuddy to generate AI-powered commit messages, visualize repo stats, and more!


