import requests

def test_photo_upload():

    url = "http://localhost:5000/photo/upload"

    files = {
        "photo": open("uploads/cat.jpg", "rb")
    }

    response = requests.post(url, files=files)

    assert response.status_code == 200

    data = response.json()

    assert "analysis" in data

    print("Photo upload and labeling working correctly")