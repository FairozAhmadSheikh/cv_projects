import cv2
import dlib

def main():
    # Initialize dlib's face detector (HOG-based)
    detector = dlib.get_frontal_face_detector()
    
    # Start video capture
    cap = cv2.VideoCapture(0)  # 0 for default webcam
    
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        # Convert frame to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        # Detect faces in the frame
        faces = detector(gray)
        
        # Draw rectangles around detected faces
        for face in faces:
            x, y, w, h = face.left(), face.top(), face.width(), face.height()
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        
        # Display the frame
        cv2.imshow('Face Tracking with dlib', frame)
        
        # Press 'q' to exit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    # Release resources
#     cap.release()
#     cv2.destroyAllWindows()

# if __name__ == "__main__":
    main()
