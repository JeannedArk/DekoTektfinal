from django.shortcuts import render
from .models import Project, ProjectGallery
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

def home(request):       
    return render(request, 'home.html')

def work(request):
    #Creating the Query
    projects = Project.objects.all().filter(is_available=True).order_by('id')
    # Creating this the context dictionary to display the query's value on work.html
    
    #Pagination
    paginator= Paginator(projects, 6)
    page = request.GET.get('page')
    paged_projects = paginator.get_page(page)
    
    context = {
        'projects' : paged_projects,        
    }
            
    return render(request, 'work.html', context)

def work_details(request, project_slug): 
    single_project = Project.objects.get(slug=project_slug)

    project_gallery = ProjectGallery.objects.filter(project_id=single_project.id)
    context = {
        'single_project': single_project,  
        'project_gallery': project_gallery,
             
    } 
    return render(request, 'work_details.html', context)

def about(request):    
    return render(request, 'about.html')

def services(request):    
    return render(request, 'services.html')

def contact(request): 
    if request.method == "POST":  
              
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')         
        email_check = email
        send_mail(subject,message,[name, email],['a.shalapi@dekotekt.com'], fail_silently=False)
        if email_check:
            messages.success(request, 'Contact request submitted successfully.')           

    return render(request, 'contact.html')

