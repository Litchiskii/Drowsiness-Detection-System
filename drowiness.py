import cv2
import dlib
from scipy.spatial import distance as dist
from imutils import face_utils

# Define constants
EYE_AR_THRESH = 0.25  # EAR threshold for detecting drowsiness
EYE_AR_CONSEC_FRAMES = 20  # Consecutive frames to trigger drowsiness

# Initialize counters
COUNTER = 0

# EAR calculation
def eye_aspect_ratio(eye):
    # Compute distances between the two sets of vertical eye landmarks (x, y)
    A = dist.euclidean(eye[1], eye[5])
    B = dist.euclidean(eye[2], eye[4])

    # Compute the distance between the horizontal eye landmarks (x, y)
    C = dist.euclidean(eye[0], eye[3])

    # EAR formula
    ear = (A + B) / (2.0 * C)
    return ear

# Load dlib's face detector and facial landmark predictor
print("[INFO] Loading facial landmark predictor...")
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")  # Download from dlib website

# Grab the indexes for the left and right eyes
(lStart, lEnd) = face_utils.FACIAL_LANDMARKS_IDXS["left_eye"]
(rStart, rEnd) = face_utils.FACIAL_LANDMARKS_IDXS["right_eye"]

# Start video stream
print("[INFO] Starting video stream...")
vs = cv2.VideoCapture(0)

while True:
    ret, frame = vs.read()
    if not ret:
        print("[ERROR] Could not read from webcam.")
        break

    # Convert frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the grayscale frame
    rects = detector(gray, 0)

    for rect in rects:
        shape = predictor(gray, rect)
        shape = face_utils.shape_to_np(shape)

        # Extract left and right eye coordinates
        leftEye = shape[lStart:lEnd]
        rightEye = shape[rStart:rEnd]

        # Calculate EAR for both eyes
        leftEAR = eye_aspect_ratio(leftEye)
        rightEAR = eye_aspect_ratio(rightEye)

        # Average EAR
        ear = (leftEAR + rightEAR) / 2.0

        # Visualize the eye region
        leftEyeHull = cv2.convexHull(leftEye)
        rightEyeHull = cv2.convexHull(rightEye)
        cv2.drawContours(frame, [leftEyeHull], -1, (0, 255, 0), 1)
        cv2.drawContours(frame, [rightEyeHull], -1, (0, 255, 0), 1)

        # Check if EAR is below the threshold
        if ear < EYE_AR_THRESH:
            COUNTER += 1
            if COUNTER >= EYE_AR_CONSEC_FRAMES:
                cv2.putText(frame, "DROWSINESS ALERT!", (10, 30),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
        else:
            COUNTER = 0

        # Display EAR
        cv2.putText(frame, f"EAR: {ear:.2f}", (300, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 1)

    # Show frame
    cv2.imshow("Frame", frame)

    # Break loop with 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Cleanup
vs.release()
cv2.destroyAllWindows()