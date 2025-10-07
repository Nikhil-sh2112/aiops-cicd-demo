import pytest
from aiops_web import analyze_logs, app

def test_aiops_model():
    """Quick test for AIOps model"""
    df = analyze_logs()
    assert len(df) > 0
    assert 'is_anomaly' in df.columns
    print(f"✅ Model works: {len(df)} logs processed")

def test_flask_app():
    """Quick test for Flask app"""
    with app.test_client() as client:
        response = client.get('/')
        assert response.status_code == 200
        print("✅ Flask app responds correctly")

if __name__ == "__main__":
    test_aiops_model()
    test_flask_app()
    print("🎉 All tests passed!")
