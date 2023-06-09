import cv2

# extract pre-trained face detector
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_alt.xml')

# returns "True" if face is detected in image stored at img_path
def face_detector(img_path):
    """
    Detects if there is a face in the image of the specified file path

    Inputs:
        img_path (str): file path of the image file
    Outputs:
        (bool): True if a face is detected in the image, false otherise
    """
    # load the image
    img = cv2.imread(img_path)
    # Convert the image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Detect faces using the pre-trained face detector
    faces = face_cascade.detectMultiScale(gray)
    # Return True if face is detected. False otherwise
    return len(faces) > 0
