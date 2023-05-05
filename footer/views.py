from django.shortcuts import render
from django.views import View
from .models import footer_table
from django.http import JsonResponse

class FooterView(View):
    def get(self, request):
        try:
            # final data to be sent as response
            final_data = {
                "contactInformation": {
                    "contactEmail": footer_table.objects.get(key="contact_email_address").value,
                    "contactPhoneNumber": footer_table.objects.get(key="contact_phone_no").value,
                    "contactAddress": footer_table.objects.get(key="contact_address").value
                },
                "socialMediaInformation": {
                    "instagramLink": footer_table.objects.get(key="instagram_link").value,
                    "facebookLink": footer_table.objects.get(key="facebook_link").value,
                    "youtubeLink": footer_table.objects.get(key="youtube_link").value,
                    "twitterLink": footer_table.objects.get(key="twitter_link").value
                }
            }
            return JsonResponse(data={"footer": final_data}, status=200)
        except:
            return JsonResponse(data={"message": "error while getting data"}, status=200)

