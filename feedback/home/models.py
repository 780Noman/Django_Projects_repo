from django.db import models

# Create your models here.
class Questions(models.Model):
    QUESTION_CHOICE = (
        ("Text","Text"),
        ("BigText",'BigText'),
        ("Radio","Radio"),
        ("Checkbox","Checkbox"),
    )
    question = models.CharField(max_length=200)
    question_type = models.CharField(choices=QUESTION_CHOICE, max_length=100, default="Text")
    
    def __str__(self):
        return f"{self.question} {self.question_type}"

class Options(models.Model):
    question = models.ForeignKey(Questions, related_name="option", on_delete=models.CASCADE)
    option_name = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.option_name} {self.question.question}"

class CustomerFeedback(models.Model):
    question = models.ManyToManyField(Questions)

class CustomerResponse(models.Model):
    feedback = models.ForeignKey(CustomerFeedback, on_delete=models.CASCADE)
    question = models.ForeignKey(Questions, on_delete=models.CASCADE)
    response_text = models.TextField(null=True, blank=True)
    selected_option = models.ManyToManyField(Options, blank=True)
