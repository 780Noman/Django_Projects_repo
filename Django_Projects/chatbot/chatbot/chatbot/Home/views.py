from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
import openai
import os
import logging

# Set up logging
logger = logging.getLogger(__name__)

# Set the API key securely
# openai.api_key = ''

from dotenv import load_dotenv
import os
import openai

load_dotenv()  # Load the .env file
api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = api_key


def chat(request):
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")

def chatAPI(request):
    if request.method == 'POST':
        try:
            prompt = request.POST.get("prompt", "")
            if not prompt:
                return JsonResponse({"error": "Prompt is missing"}, status=400)

            # Using the new model and method
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": prompt}
                ],
                temperature=1,
                max_tokens=256,
                top_p=1,
                frequency_penalty=0,
                presence_penalty=0,
            )
            return JsonResponse({"response": response['choices'][0]['message']['content'].strip()})
        except Exception as e:
            logger.error("Error in chatAPI: %s", str(e))
            return JsonResponse({"error": str(e)}, status=500)
    return HttpResponse("Bad request!!", status=400)
# import os
# from django.shortcuts import render, HttpResponse
# from django.http import JsonResponse
# from transformers import pipeline

# # Set the Hugging Face API token
# HUGGINGFACEHUB_API_TOKEN = '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'
# os.environ["HUGGINGFACEHUB_API_TOKEN"] = HUGGINGFACEHUB_API_TOKEN

# # Load the Hugging Face conversational model (DialoGPT)
# # chat_model = pipeline("question-answering", model="microsoft/DialoGPT-small", use_auth_token=HUGGINGFACEHUB_API_TOKEN)
# chat_model = pipeline("question-answering", model="distilbert-base-uncased-distilled-squad", use_auth_token=HUGGINGFACEHUB_API_TOKEN)
# def chat(request):
#     return render(request, "index.html")

# def about(request):
#     return render(request, "about.html")

# def chatAPI(request):
#     if request.method == 'POST':
#         try:
#             prompt = request.POST.get("prompt", "")
#             if not prompt:
#                 return JsonResponse({"error": "Prompt is missing"}, status=400)

#             # Generate the response using the Hugging Face model
#             response = chat_model(prompt)
#             bot_response = response[0]['generated_text']

#             return JsonResponse({"response": bot_response})
#         except Exception as e:
#             return JsonResponse({"error": str(e)}, status=500)
#     return HttpResponse("Bad request!!", status=400)

