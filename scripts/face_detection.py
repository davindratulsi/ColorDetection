import cv2

def main():
    # # Load the cascade
    face_cascade = cv2.CascadeClassifier('./tests/haarcascade_frontalcatface.xml')
    # # Read the input image
    image = cv2.imread('./tests/cats/smiling_cat.jpg')
    # image = cv2.resize(image, (600, 600))
    # # Convert into grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # # Detect faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    # # Draw rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)
    # # Display the output
    cv2.imshow('image', image)
    cv2.waitKey(0)
    cv2.imwrite('./tests/image_cat_detection.jpg', image)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()