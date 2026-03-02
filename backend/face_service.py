from deepface import DeepFace

def analyze_face(image_path):
    try:
        result = DeepFace.analyze(
            img_path=image_path,
            actions=['age', 'gender'],
            enforce_detection=False
        )
        return result
    except Exception as e:
        return str(e)