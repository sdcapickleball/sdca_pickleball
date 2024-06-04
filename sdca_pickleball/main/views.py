import openpyxl
from django.shortcuts import render, redirect
from django.http import HttpResponse

def home(request):
    return render(request, 'home.html')

def events(request):
    return render(request, 'events.html')

def register(request):
    if request.method == 'POST':
        event = request.POST['event']
        division = request.POST['division']
        age_bracket = request.POST['age_bracket']
        player1_first_name = request.POST['player1_first_name']
        player1_last_name = request.POST['player1_last_name']
        player1_dupr_id = request.POST['player1_dupr_id']
        player2_first_name = request.POST['player2_first_name']
        player2_last_name = request.POST['player2_last_name']
        player2_dupr_id = request.POST['player2_dupr_id']
        
        # Open or create an Excel file
        try:
            wb = openpyxl.load_workbook('registrations.xlsx')
            ws = wb.active
        except FileNotFoundError:
            wb = openpyxl.Workbook()
            ws = wb.active
            # Add header row
            ws.append([
                'Event', 'Division', 'Age Bracket',
                'Player 1 First Name', 'Player 1 Last Name', 'Player 1 DUPR ID',
                'Player 2 First Name', 'Player 2 Last Name', 'Player 2 DUPR ID'
            ])
        
        # Append the form data to the Excel file
        ws.append([
            event, division, age_bracket,
            player1_first_name, player1_last_name, player1_dupr_id,
            player2_first_name, player2_last_name, player2_dupr_id
        ])
        
        # Save the Excel file
        wb.save('registrations.xlsx')
        
        # Redirect to PayPal payment (assuming you have a PayPal button integration here)
        return redirect('https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=YOUR_BUTTON_ID')
        
    return render(request, 'register.html')

def local_open_plays(request):
    return render(request, 'local_open_plays.html')

def about_us(request):
    return render(request, 'about_us.html')

def contact_us(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        # Handle the contact form submission (e.g., send email)
        return HttpResponse("Thank you for contacting us!")
    return render(request, 'contact_us.html')
