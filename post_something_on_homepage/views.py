from django.http import JsonResponse
from django.shortcuts import render
from .models import Post_a_Jobs

def homepage(request):
    jobs = Post_a_Jobs.objects.all().order_by('-pub_date')

    if request.method == 'POST':
        content = request.POST.get('content')
        job_details = Post_a_Jobs.objects.create(content=content)
        response_data = {
            'content': job_details.content,
            'pub_date': job_details.pub_date.strftime('%Y-%m-%d')
        }
        return JsonResponse(response_data)
    else:
        return render(request, 'post_something_on_homepage/index.html', {'jobs': jobs})
