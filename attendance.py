import face_recognition as fr
import cv2
import sqlite3
conn = sqlite3.connect('attendance.db')
cursor = conn.cursor()
def attend():
    video_capture = cv2.VideoCapture(0)
    global names
    names = []
    a = fr.load_image_file("rimon.jpg")
    a_enc = fr.face_encodings(a)[0]

    b = fr.load_image_file("vinay.jpg")
    b_enc = fr.face_encodings(b)[0]

    c = fr.load_image_file("shailesh.jpg")
    c_enc = fr.face_encodings(c)[0]
    
    d = fr.load_image_file("rick.jpg")
    d_enc = fr.face_encodings(d)[0]

    
    known_face_encodings = [
        a_enc,
        b_enc,
        c_enc,
        d_enc,
    ]
    known_face_names = [
        "Rimon Sarmah",
        "Vinay Sharma",
        "Shailesh Gahlawat",
        "Rick Dhillon",
    ]
    face_locations = []
    face_encodings = []
    face_names = []
    process_this_frame = True

    while True:
        ret, frame = video_capture.read()
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
        rgb_small_frame = small_frame[:, :, ::-1]
        if process_this_frame:
            face_locations = fr.face_locations(rgb_small_frame)
            face_encodings = fr.face_encodings(rgb_small_frame, face_locations)
            face_names = []
            for face_encoding in face_encodings:
                matches = fr.compare_faces(known_face_encodings, face_encoding)
                name = "Unknown"
                if True in matches:
                    first_match_index = matches.index(True)
                    name = known_face_names[first_match_index]
                face_names.append(name)
                x=face_names[-1]
                d=x.encode('ASCII')
                d = str(d)
                d = d[2:]
                d = d[:-1]
                print(d)
                names.append(d)
        process_this_frame = not process_this_frame
        for (top, right, bottom, left), name in zip(face_locations, face_names):
            top *= 4
            right *= 4
            bottom *= 4
            left *= 4
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
            cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)
        cv2.imshow('Video', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    video_capture.release()
    cv2.destroyAllWindows()
    names = list(dict.fromkeys(names))

