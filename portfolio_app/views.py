
from django.shortcuts import render, redirect
from .models import ContactMessage
from django.core.mail import send_mail

def home(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        ContactMessage.objects.create(
            name=name,
            email=email,
            message=message
        )
        try:
            send_mail(
            subject="Thanks for contacting us 🚀",
            message=f"Hi {name},\n\nYour message has been received successfully.\n\nWe will contact you soon.\n\nThank you!",
            from_email='parathiban2000ktm@gmail.com',
            recipient_list=[email],
            fail_silently=False,
        )
        except Exception as e:
            print("Email error:", e)

        return redirect('/')
    


    skills = [
        {"name": "Python", "level": "95%", "icon": "fab fa-python"},
        {"name": "Django", "level": "90%", "icon": "fas fa-code"},
        {"name": "HTML5", "level": "95%", "icon": "fab fa-html5"},
        {"name": "CSS3", "level": "85%", "icon": "fab fa-css3-alt"},
        {"name": "JavaScript", "level": "80%", "icon": "fab fa-js"},
        {"name": "React", "level": "70%", "icon": "fab fa-react"},
        {"name": "Bootstrap", "level": "94%", "icon": "fab fa-bootstrap"},
        {"name": "Mysql", "level": "90%", "icon": "fab fa-database"},
        {"name": "MongoDB", "level": "80%", "icon": "fab fa-database"},
         {"name": "Github", "level": "85%", "icon": "fab fa-github"},
         
         
        
    ]
    
    projects = [
        {
            "title": "Bussiness Template", 
            "description": "We provide amazing solutions for your business growth.", 
            "tech": ["Python", "Django", "Bootstrap"],
            "link": "#"
        },
        {
            "title": " Grid E-Commerce", 
            "description": "A fully immersive shopping experience with 3D product rendering.", 
            "tech": ["Python", "Django", "Sqlite"],
            "link": "https://parthi.pythonanywhere.com/"
        },
        {
            "title": "Professional Portfolio", 
            "description": "A personal developer website featuring smooth gravity-defying physics.", 
            "tech": ["HTML/CSS", "Python", "Django"],
            "link": "#"
        }
    ]
    
    soft_skills = [
        "Team Leadership", "Self Learning", "Problem Solving", 
        "Effective Communication", "Time Management", "Adaptability"
    ]
    
    education = [
        {
            "degree": "B.E Aeonautical Engineering",
            "institution": "Thiruvalluvar College Of Enginnering",
            "year": "2020 - 2024",
            "description": "Graduated with honors, specialized in Aeronautical engineering."
        },
        {
            "degree": "Higher Secondary",
            "institution": "St.Joseph Hr.Secondary School",
            "year": "2017 - 2019",
            "description": "Focused on mathematics and computer programming."
        }
    ]
    
    certificates = [
        {"name": "Python Fullstack Developer", "issuer": "Trinite Digital", "year": "2026"},
        {"name": "Django Web Framework", "issuer": "Trinite Digital", "year": "2026"},
        {"name": "Pthon Intern", "issuer": "Trinite Digital", "year": "2026"},
    ]
    
    context = {
        'skills': skills,
        'projects': projects,
        'soft_skills': soft_skills,
        'education': education,
        'certificates': certificates
    }
    
    return render(request, 'portfolio_app/index.html', context)



 



      


    