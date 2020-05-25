# Groupe 2 CSE 2020
# Projet Pililier
# Permet de prendre une photo avec un PI Cam et la nomme picture.jpg


from picamera import PiCamera

camera = PiCamera()
camera.resolution = (640, 480)
# camera.framerate = 30

# camera.start_preview()
camera.capture('./picture.jpg')
# camera.stop_preview()

