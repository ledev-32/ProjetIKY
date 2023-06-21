import cv2
import pickle

# Charger le fichier cascade pour la détection des visages
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Initialiser la capture vidéo à partir de la webcam
cap = cv2.VideoCapture(0)

# Initialiser l'algorithme de reconnaissance faciale
face_recognizer = cv2.face.LBPHFaceRecognizer_create()
recognition=cv2.face.LBPHFaceRecognizer_create()

# Enregistrer le visage
def register_face(face_id, name):
    face_samples = []
    count = 0
    while True:
        # Lire une image depuis la vidéo
        ret, frame = cap.read()

        # Convertir l'image en niveaux de gris
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Détecter les visages dans l'image
        faces = face_cascade.detectMultiScale(gray, minNeighbors=5, minSize=(30, 30))

        # Dessiner des rectangles autour des visages détectés
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 3)

            # Enregistrer les échantillons du visage
            face_roi = gray[y:y+h, x:x+w]
            face_samples.append(face_roi)
            count += 1

        # Afficher l'image avec les rectangles des visages
        cv2.imshow('Enregistrement du visage', frame)

        # Quitter la boucle si le nombre d'échantillons atteint 100
        if count >= 100:
            break

        # Quitter la boucle si la touche 'q' est pressée
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Entraîner l'algorithme de reconnaissance faciale avec les échantillons enregistrés
    face_recognizer.train(face_samples, face_id)

    # Stocker les informations dans un fichier
    data = {"face_id": face_id, "name": name}
    with open("data.pickle", "wb") as file:
        pickle.dump(data, file)
    print("Visage enregistré avec succès.")

# Reconnaître le visage
def recognize_face():
    # Charger les informations à partir du fichier
    try:
        with open("data.pickle", "rb") as file:
            data = pickle.load(file)
    except FileNotFoundError:
        print("Aucune donnée d'enregistrement trouvée.")
        return

    while True:
        # Lire une image depuis la vidéo
        ret, frame = cap.read()

        # Convertir l'image en niveaux de gris
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Détecter les visages dans l'image
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

        # Dessiner des rectangles autour des visages détectés
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 3)

            # Reconnaître le visage
            face_roi = gray[y:y+h, x:x+w]
            label, confidence = face_recognizer.predict(face_roi)
            if confidence < 50:  # Ajuster le seuil de confiance selon vos besoins
                if label == data["face_id"]:
                    print("Visage reconnu :", data["name"])
                else:
                    print("Visage inconnu")
            else:
                print("Visage inconnu")

        # Afficher l'image avec les rectangles des visages
        cv2.imshow('Reconnaissance faciale', frame)

        # Quitter la boucle si la touche 'q' est pressée
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

# Enregistrer votre visage avec l'ID 1 et votre nom
register_face(1, "Votre Nom")

# Lancer la reconnaissance faciale
recognize_face()

# Libérer les ressources
cap.release()
cv2.destroyAllWindows()
