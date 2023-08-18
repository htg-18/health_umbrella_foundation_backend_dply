from django.shortcuts import render
from .models import feedback_table
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import logging
import json
logger = logging.getLogger('file_log')

@csrf_exempt
def add_feeback(request):
    if request.method!='POST':
        return JsonResponse(data={"message": "only POST method allowed"}, status=405)
    try:
        data = json.loads(request.body.decode('utf-8'))
        feedback_obj = feedback_table(
            rating = int(data.get('rating')),
            feedback = str(data.get('feedback'))
        )
        if feedback_obj.rating>5 or feedback_obj.rating<1:
            return JsonResponse(data={"message": "invalid rating"}, status=400)
        
        feedback_obj.save()
        return JsonResponse(data={"message":"feedback submitted successfully"}, status=200)
    except Exception as e:
        logger.info(e)
        return JsonResponse(data={"message": "error while submitting request"}, status=500)
