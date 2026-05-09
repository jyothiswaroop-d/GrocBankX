import face_recognition
import numpy as np

def verify_face(live_image_path, owner_image_path):
    try:
        print("🔍 Loading images...")
        live_img = face_recognition.load_image_file(live_image_path)
        owner_img = face_recognition.load_image_file(owner_image_path)

        print("🧠 Encoding faces...")
        live_enc = face_recognition.face_encodings(live_img)
        owner_enc = face_recognition.face_encodings(owner_img)

        if len(live_enc) == 0:
            print("❌ No face detected in LIVE image")
            return False

        if len(owner_enc) == 0:
            print("❌ No face detected in OWNER image")
            return False

        if len(live_enc) > 1:
            print("⚠️ Multiple faces detected in LIVE image")
            return False

        distance = np.linalg.norm(live_enc[0] - owner_enc[0])
        print(f"📏 Face distance: {distance}")

        # 🔥 Relaxed threshold for webcam
        return distance < 0.7

    except Exception as e:
        print("🔥 Face verification error:", e)
        return False
