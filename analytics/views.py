from django.shortcuts import render
from django.http import JsonResponse
off = False

def get_off(request):
    global off
    if off:
        return JsonResponse(data={}, status=200)
    else:
        return JsonResponse(data={}, status=400)

def set_off(request):
    global off
    off = (not off)
    return JsonResponse(data={"off": off}, status=200)
