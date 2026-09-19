import os

from backend.main import get_allowed_origins


def test_vercel_cors_includes_deployed_origin():
    os.environ["VERCEL_URL"] = "demo-project.vercel.app"
    origins = get_allowed_origins()
    assert "https://demo-project.vercel.app" in origins
    assert "http://localhost:8000" in origins


def test_vercel_cors_accepts_explicit_custom_origins():
    os.environ["CORS_ORIGINS"] = "https://app.example.com,http://localhost:3000"
    origins = get_allowed_origins()
    assert "https://app.example.com" in origins
    assert "http://localhost:3000" in origins
