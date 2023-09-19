from .models import clinics_table
from django.http import JsonResponse
import logging
from datetime import datetime
import time
logger = logging.getLogger('file_log')

def get_clinics(request):
    start_time = time.time()
    logger.info("\nrequest to get clinics")
    logger.info(f"Time: {datetime.now()}")
    try:
        # final data to be sent
        final_data = {}

        # filtering clinics data
        clinics_list = []
        for clinic in clinics_table.objects.filter(show=True):
            clinics_list.append({
                "name": clinic.name,
                "imageLink": clinic.image.url,
                "location": clinic.location,
                "summary": clinic.summary,
                "contact": clinic.contact,
                "tagList": clinic.tags.split(',')
            })
        logger.info("fetched all clinics data")
        final_data.update({"clinicsList": clinics_list})

        logger.info(f"Time taken: {time.time()-start_time}")
        return JsonResponse(data=final_data, status=200)
    except Exception as e:
        logger.error(e)
        return JsonResponse(data={"message": "error while getting data"}, status=500)

