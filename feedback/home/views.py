from django.shortcuts import render, redirect
from .models import Questions, CustomerFeedback, CustomerResponse, Options

def surveys(request):

    feedback = CustomerFeedback.objects.all()
    return render(request, 'surveys.html', {'feedbacks': feedback})
def survey_view(request,id):
    
    questions = Questions.objects.all()

    if request.method == 'POST':
        feedback = CustomerFeedback.objects.create()
        for question in questions:
            response_text = request.POST.get(f"response_{question.id}")
            selected_option_ids = request.POST.getlist(f"options_{question.id}")


            response = CustomerResponse.objects.create(
                feedback=feedback,
                question=question,
                response_text=response_text if question.question_type in ["Text", "BigText"] else None
            )
            
            if selected_option_ids:
                selected_options = Options.objects.filter(id__in=selected_option_ids)
                response.selected_option.set(selected_options)
        
        return redirect('thank_you')
    
    return render(request, 'survey.html', {'questions': questions})


def thank_you(request):
    return render(request, 'thank_you.html')

def survey_results(request):
    data = []
    questions = Questions.objects.all()
    for question in questions:
        responses = CustomerResponse.objects.filter(question=question)
        if question.question_type in ['Radio', 'Checkbox']:
            options = question.option.all()  # Access the related options
            option_counts = {option.option_name: responses.filter(selected_option=option).count() for option in options}
            data.append({
                'question': question.question,
                'labels': list(option_counts.keys()),
                'values': list(option_counts.values()),
            })
    print(data)
    return render(request, 'results.html', {'data': data})



