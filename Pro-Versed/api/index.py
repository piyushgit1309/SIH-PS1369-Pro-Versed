"""
Pro-Versed — Vercel Serverless Function Entrypoint (Subdirectory)
Exports the FastAPI `app` instance for Vercel's Python runtime.
"""
import os
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
pv_dir = os.path.dirname(current_dir)
backend_dir = os.path.join(pv_dir, "backend")

for p in [backend_dir, pv_dir]:
    if os.path.exists(p) and p not in sys.path:
        sys.path.insert(0, p)

if "SEED_DEMO_DATA" not in os.environ:
    os.environ["SEED_DEMO_DATA"] = "true"

if "ENVIRONMENT" not in os.environ:
    os.environ["ENVIRONMENT"] = "production"

try:
    from backend.main import app
except ImportError:
    import main
    app = main.app
