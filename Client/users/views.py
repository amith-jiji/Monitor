from django.shortcuts import render, redirect
from django.contrib import messages
import pyrebase

# Create your views here.

config = {
    "apiKey": "AIzaSyB9rHPXZpzCltsCYBmRUTJuAJX4gGUeI5w",
    "authDomain": "social-distance-monitoring.firebaseapp.com",
    "databaseURL": "https://social-distance-monitoring-default-rtdb.asia-southeast1.firebasedatabase.app",
    "projectId": "social-distance-monitoring",
    "storageBucket": "social-distance-monitoring.appspot.com",
    "messagingSenderId": "601954862762",
    "appId": "1:601954862762:web:bc6f6988daa1378615b2d3",
}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
database = firebase.database()

metadata = dict(database.child("data").get().val())


def loginView(request):
    if 'uid' in request.session:
        return redirect('dashboard')

    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['pass']

        try:
            user = auth.sign_in_with_email_and_password(email, password)
            session_id = user['idToken']
            request.session['uid'] = str(session_id)
            return redirect('dashboard')

        except:
            messages.error(request, "Invalid Credentials!!Please Check your Data")
            return redirect('login')

    return render(request, 'index.html')


def logout(request):
    try:
        del request.session['uid']
    except:
        pass
    return redirect('login')


def dashboardView(request):
    return render(request, 'dashboard.html', metadata)


def cameraView(request, id):
    return render(request, 'camera.html', {'id': id, 'data': metadata['camera' + str(id)]})


def reportView(request, id):
    data = database.child('camera' + str(id)).get().val()
    data = list(data.items())[::-1]
    if data is None:
        data = {}
    else:
        data = [('/'.join(i[0][:10].split('_')), ':'.join(i[0][11:].split('_')), i[1][i[0]]) for i in data][
               :min(30, len(data))]
    return render(request, 'report.html', {'id': id, 'data': data})
