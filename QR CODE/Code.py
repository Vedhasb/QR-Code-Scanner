import cv2
import webbrowser
from pyzbar.pyzbar import decode

# Initialize the webcam
cap = cv2.VideoCapture(0)

# Check if the camera is opened
if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

# Flag to indicate if the QR code has been detected
qr_code_detected = False

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Failed to capture image.")
        break

    # Decode the QR codes
    decoded_objects = decode(frame)

    for obj in decoded_objects:
        # Extract the data from the QR code
        qr_data = obj.data.decode('utf-8')
        print(f"QR Code Data: {qr_data}")

        if not qr_code_detected:
            # Open the URL in the web browser
            webbrowser.open(qr_data)
            qr_code_detected = True  # Ensure this only happens once
            cap.release()  # Shut off the camera
            cv2.destroyAllWindows()  # Close all OpenCV windows
            break

    # Display the resulting frame
    cv2.imshow('QR Code Scanner', frame)

    # Exit the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close the OpenCV windows
cap.release()
cv2.destroyAllWindows()
