# tasks.py
from invoke import task

@task
def dev(c):
    """Run in development with auto-reload"""
    c.run("uvicorn src.app:app --reload --host 0.0.0.0 --port 8000")

