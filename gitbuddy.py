import typer
import git
import os
import google.generativeai as genai

app = typer.Typer(help="🤖 GitBuddy – now powered by Google Gemini!")


api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    typer.echo("⚠️ Please set GEMINI_API_KEY in your environment.")
else:
    genai.configure(api_key=api_key)


@app.command()
def status():
    """Show current git status."""
    try:
        repo = git.Repo('.')
        typer.echo(repo.git.status())
    except Exception as e:
        typer.echo(f"❌ Error: {e}")


@app.command()
def commit(msg: str):
    """Stage all files and commit with message."""
    try:
        repo = git.Repo('.')
        repo.git.add(all=True)
        repo.index.commit(msg)
        typer.echo(f"✅ Commit successful: {msg}")
    except Exception as e:
        typer.echo(f"❌ Commit failed: {e}")


@app.command()
def explain(error: str):
    """Ask Gemini AI to explain a git error."""
    if not api_key:
        typer.echo("⚠️ Please set GEMINI_API_KEY in your environment.")
        return

    try:
        typer.echo("💬 Asking GitBuddy...")
        model = genai.GenerativeModel("gemini-2.0-flash")
        prompt = f"Explain this git error in simple terms and suggest fixes: {error}"
        response = model.generate_content(prompt)
        typer.echo(response.text.strip())
    except Exception as e:
        typer.echo(f"❌ Could not explain: {e}")


if __name__ == "__main__":
    app()
