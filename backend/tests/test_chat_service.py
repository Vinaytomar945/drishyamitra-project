import requests

def test_chat_service():

    url = "http://localhost:5000/chat/chat"

    payload = {
        "message": "Hello"
    }

    response = requests.post(url, json=payload)

    assert response.status_code == 200

    data = response.json()

    assert "ai_response" in data

    print("Chat service working correctly")