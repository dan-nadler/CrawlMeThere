from django.shortcuts import render

# Create your views here.

# Step 1. Get current location or start point
# Step 2. Get final destination
# Step 3. Get any filtering criteria including length of journey (time), or time of arrival.
# Step 4. Collect all applicable stops
# Step 5. Create best fit directions
# Step 6. Create multi-stop directions and display map / link to google maps.

def home(request):

    return render(request, 'home.html')