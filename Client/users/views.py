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

def loginView(request):
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
    return render(request, 'dashboard.html')

def cameraView(request ,id):
    return render(request, 'camera.html', {'id':id})

def reportView(request ,id):
    data = database.child('camera' + str(id)).get().val()
    data = [('/'.join(i[0][:10].split('_')),':'.join(i[0][11:].split('_')),i[1][i[0]]) for i in list(data.items())]
    return render(request, 'report.html', {'id':id,'data':data})

