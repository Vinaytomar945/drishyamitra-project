import requests

def test_face_detection():

    url = "http://localhost:5000/face/detect"

    files = {
        "photo": open("uploads/cat.jpg", "rb")
    }

    response = requests.post(url, files=files)

    assert response.status_code == 200

    data = response.json()

    assert "analysis" in data

    print("Face detection API working correctly")