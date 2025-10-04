# Ex.05 Design a Website for Server Side Processing
## Date:04.10.2025

## AIM:
 To design a website to calculate the power of a lamp filament in an incandescent bulb in the server side. 


## FORMULA:
P = I<sup>2</sup>R
<br> P --> Power (in watts)
<br> I --> Intensity
<br> R --> Resistance

## DESIGN STEPS:

### Step 1:
Clone the repository from GitHub.

### Step 2:
Create Django Admin project.

### Step 3:
Create a New App under the Django Admin project.

### Step 4:
Create python programs for views and urls to perform server side processing.

### Step 5:
Create a HTML file to implement form based input and output.

### Step 6:
Publish the website in the given URL.

## PROGRAM :

```
math.html

<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <title>Lamp Filament Power Calculator</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      text-align: center;
      margin-top: 50px;
    }
    h1 {
      font-size: 28px;
    }
    .input-box {
      margin: 15px 0;
    }
    label {
      display: inline-block;
      width: 200px;
      text-align: right;
      margin-right: 10px;
    }
    input {
      padding: 6px;
      font-size: 16px;
      width: 120px;
    }
    button {
      padding: 8px 20px;
      font-size: 16px;
      margin-top: 15px;
      cursor: pointer;
    }
    #result {
      margin-top: 30px;
      font-size: 24px;
      font-weight: bold;
      border: 2px solid black;
      padding: 15px;
      display: inline-block;
      min-width: 200px;
    }
  </style>
</head>
<body>
  <h1>Lamp Filament Power Calculator</h1>
  <p>Use the formula: P = I²R</p>

  <div class="input-box">
    <label for="current">Current (I) in Amperes:</label>
    <input type="number" id="current" placeholder="Enter current">
  </div>

  <div class="input-box">
    <label for="resistance">Resistance (R) in Ohms:</label>
    <input type="number" id="resistance" placeholder="Enter resistance">
  </div>

  <button onclick="calculatePower()">Calculate Power</button>

  <div id="result">Power = ? W</div>

  <script>
    function calculatePower() {
      let I = parseFloat(document.getElementById("current").value);
      let R = parseFloat(document.getElementById("resistance").value);

      if (isNaN(I) || isNaN(R)) {
        document.getElementById("result").innerText = "Please enter valid numbers!";
        return;
      }

      let P = I * I * R;  // P = I²R
      document.getElementById("result").innerText = "Power = " + P + " W";
    }
  </script>
</body>
</html>

views.py

from django.shortcuts import render
def rectarea(request):
    context = {}
    context['area'] = ""
    context['l'] = ""
    context['b'] = ""
    if request.method == 'POST':
        print("POST method is used")
        l = request.POST.get('length', '0')
        b = request.POST.get('breadth', '0')
        print('request', request)
        print("Length=", l)
        print("Breadth=", b)
        area = int(l) * int(b)
        context['area'] = area
        context['l'] = l
        context['b'] = b
        print('Area', area)
    return render(request, 'mathapp/math.html', context)

    urls.py

    from django.contrib import admin
from django.urls import path
from mathapp import views

urlpatterns = [
    path("admin", admin.site.urls),
    path('areaofrectangle/',views.rectarea, name="areaofrectangle"),
    path("",views.rectarea,name="areaofrectangleroot")
]

```


## SERVER SIDE PROCESSING:
![alt text](<Screenshot 2025-10-04 204740-1.png>)

## HOMEPAGE:
![alt text](<Screenshot 2025-10-04 205907-1.png>)


## RESULT:
The program for performing server side processing is completed successfully.
