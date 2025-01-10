import pytest

@pytest.mark.asyncio
async def test_post_article(client):
    """Test endpoint for an article"""
    headers={"telegram-user-id": "test"}
    response = client.post("/api/v1/somearticle", headers=headers)
    assert response.status_code == 200
    # response = client.get("/api/v1")
    # assert response.status_code == 400

