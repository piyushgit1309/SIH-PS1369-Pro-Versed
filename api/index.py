"""
Pro-Versed — Vercel Serverless Function Entrypoint
Exports the FastAPI `app` instance for Vercel's Python runtime.
"""
import os
import sys

# Configure system path to locate backend and Pro-Versed packages
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.dirname(current_dir)
pv_dir = os.path.join(root_dir, "Pro-Versed")
pv_backend = os.path.join(pv_dir, "backend")
backend_dir = os.path.join(root_dir, "backend")

for p in [pv_backend, pv_dir, backend_dir, root_dir]:
    if os.path.exists(p) and p not in sys.path:
        sys.path.insert(0, p)

# Auto-enable demo data seeding on Vercel serverless environment
if "SEED_DEMO_DATA" not in os.environ:
    os.environ["SEED_DEMO_DATA"] = "true"

if "ENVIRONMENT" not in os.environ:
    os.environ["ENVIRONMENT"] = "production"

try:
    from backend.main import app
except ImportError:
    import main
    app = main.app
