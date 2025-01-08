import pytest

@pytest.mark.asyncio
async def test_get_all_articles(client):
    """Test endpoint for read all articles"""
    headers={"telegram-user-id": "test"}
    response = client.get("/api/v1", headers=headers)
    assert response.status_code == 200
    response = client.get("/api/v1")
    assert response.status_code == 400

