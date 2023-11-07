from django.shortcuts import render
from django.http import JsonResponse
off = False
offg = False

async def get_off(request):
    global off
    if off:
        return JsonResponse(data={}, status=200)
    else:
        return JsonResponse(data={}, status=400)

async def set_off(request):
    global off
    off = (not off)
    return JsonResponse(data={"off": off}, status=200)

async def get_offg(request):
    global offg
    if offg:
        return JsonResponse(data={}, status=200)
    else:
        return JsonResponse(data={}, status=400)

async def set_offg(request):
    global offg
    offg = (not offg)
    return JsonResponse(data={"offg": offg}, status=200)
