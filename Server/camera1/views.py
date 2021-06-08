from django.http.response import StreamingHttpResponse
from camera1.camera import VideoCamera


# Create your views here.

def indexView(request):
    return StreamingHttpResponse(gen(VideoCamera()), content_type='multipart/x-mixed-replace; boundary=frame')


def gen(camera):
    while True:
        frame = camera.get_frame()
        yield b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n'