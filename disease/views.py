from django.views import View
from .models import disease_table, pathy_table, summary_table, book_table, source_table, data_table, whatsapp_table, case_table
from django.http import JsonResponse
from django.db import models
import logging


class DiseaseView(View):
    def get(self, request, disease):
        try:
            disease_object = disease_table.objects.get(name=disease)

            # this will be sent to user
            final_data = {}

            # return 404 if data not present or not allowed
            if (disease_object is None) or (disease_object.show is False):
                return JsonResponse(data=final_data, status=404)
            
            final_data.update({'disease': disease})
            final_data.update({'text': disease_object.text})
            final_data.update({'summary': disease_object.summary})
            final_data.update({'imageLink': disease_object.image_link.url})
            
            # to store different pathies
            all_pathies = {}

            # getting data of different types of therapies
            therapiesWithDrugs = []
            for pathy in pathy_table.objects.filter(disease__name=disease, type="therapiesWithDrugs"):
                summary = summary_table.objects.get(disease__name=disease, pathy__name=pathy)
                therapiesWithDrugs.append({
                    "name": pathy.name,
                    "imageLink": pathy.image_link.url,
                    "summary": summary.summary
                })
            all_pathies.update({"therapiesWithDrugs": therapiesWithDrugs})

            therapiesWithoutDrugs = []
            for pathy in pathy_table.objects.filter(disease__name=disease, type="therapiesWithoutDrugs"):
                summary = summary_table.objects.get(disease__name=disease, pathy__name=pathy)
                therapiesWithoutDrugs.append({
                    "name": pathy.name,
                    "imageLink": pathy.image_link.url,
                    "summary": summary.summary
                })
            all_pathies.update({"therapiesWithoutDrugs": therapiesWithoutDrugs})

            lessKnownTherapies = []
            for pathy in pathy_table.objects.filter(disease__name=disease, type="lessKnownTherapies"):
                summary = summary_table.objects.get(disease__name=disease, pathy__name=pathy)
                lessKnownTherapies.append({
                    "name": pathy.name,
                    "imageLink": pathy.image_link.url,
                    "summary": summary.summary
                })
            all_pathies.update({"lessKnownTherapies": lessKnownTherapies})

            final_data.update({"pathies": all_pathies})

            return JsonResponse(data=final_data, status=200)
        except Exception as e:
            logging.error(e)
            return JsonResponse(data={"message": "error while getting data"}, status=500)


class TherapyView(View):
    def get(self, request, disease, pathy):
        try:
            # check whether show=True for disease
            disease_object = disease_table.objects.get(name=disease)
            if disease_object.show is False:
                return JsonResponse(data={"message": "No data for this disease"}, status=404)
            
            # check whether show=True for pathy
            pathy_object = pathy_table.objects.get(name=pathy)
            if pathy_object.show is False:
                return JsonResponse(data={"message": "No data for this Pathy"}, status=404)
            
            # final data to give to user
            final_data = {}
            final_data.update({'pathy': pathy})
            final_data.update({'text': summary_table.objects.get(disease__name=disease, pathy__name=pathy).summary})
            information_sources = set()
            for data in data_table.objects.filter(disease__name=disease, pathy__name=pathy):
                information_sources.add(data.source.name)
            final_data.update({'informationSources': list(information_sources)})
            
            return JsonResponse(data=final_data, status=200)
        except Exception as e:
            logging.error(e)
            return JsonResponse(data={"message": "error while getting data"}, status=500)



class BooksView(View):
    def get(self, request, disease, pathy):
        try:
            # check whether show=True for disease
            disease_object = disease_table.objects.get(disease_name=disease)
            if disease_object.show is False:
                return JsonResponse(data={"message": "No data for this disease"}, status=404)
            
            # check whether show=True for pathy
            pathy_object = pathy_table.objects.get(pathy_name=pathy)
            if pathy_object.show is False:
                return JsonResponse(data={"message": "No data for this Pathy"}, status=404)

            # final data to give to user
            final_data = {}

            # get all the relevant books data
            final_data.update({"books": book_table.objects.filter(disease__name=disease, pathy__name=pathy, show=True).values('name', 'author', 'rating', 'text', imageLink=models.F('image_link'), buyLink=models.F('buy_link'))})

            return JsonResponse(data=final_data, status=200)
        except Exception as e:
            logging.error(e)
            return JsonResponse(data={"message": "error while getting data"}, status=500)


class SourceView(View):
    def get(self, request, disease, pathy, source):
        try:
            # check whether show=True for disease
            disease_object = disease_table.objects.get(name=disease)
            if disease_object.show is False:
                return JsonResponse(data={"message": "No data for this disease"}, status=404)
            
            # check whether show=True for pathy
            pathy_object = pathy_table.objects.get(name=pathy)
            if pathy_object.show is False:
                return JsonResponse(data={"message": "No data for this Pathy"}, status=404)
            
            # check whether show=True for source
            source_object = source_table.objects.get(name=source)
            if source_object.show is False:
                return JsonResponse(data={"message": "No data for this source"}, status=404)

            # data to be sent to user
            final_data = {}
            final_data.update({'text': source_table.objects.get(name = source).text})

            if source=='directCase':
                # get all the data of direct testimonial
                case_list = []
                for case in case_table.objects.filter(disease__name = disease, pathy__name=pathy, show=True):
                    case_list.append({
                        "caseId": str(case.pk),
                        "title": case.title,
                        "summary": case.summary,
                        "rating": str(case.rating),
                        "comment": case.comment
                    })
                final_data.update({'sourceList': case_list})
            else:
                # get all the data of a source
                source_list = []
                for src in data_table.objects.filter(disease__name = disease, pathy__name=pathy, source__name=source, show=True):
                    source_list.append({
                        "id": str(src.pk),
                        "title": src.title,
                        "link": src.link,
                        "summary": src.summary,
                        "rating": str(src.rating),
                        "comment": src.comment
                    })
                final_data.update({'sourceList': source_list})

            if source=='socialMedia':
                # add whatsapp data if source is social media
                final_data.update({'whatsappData': whatsapp_table.objects.get(disease__name=disease, pathy__name=pathy, show=True).value})

            return JsonResponse(data=final_data, status=200)
        except Exception as e:
            logging.error(e)
            return JsonResponse(data={"message": "error while getting data"}, status=500)


class CaseView(View):
    def get(self, request, disease, pathy, case_id):
        try:
            case_object = case_table.objects.get(pk=case_id)

            # check whether show=True for case
            if case_object.show is False:
                return JsonResponse(data={"message": "No data for this source"}, status=404)
            
            # data to send to user
            final_data = {}
            final_data.update({"caseId": str(case_id)})
            final_data.update({"title": case_object.title})
            final_data.update({"summary": case_object.summary})
            final_data.update({"caseHistory": case_object.history_link})
            final_data.update({"allergies": case_object.allergies_link})
            final_data.update({"medicalReport": case_object.reports_link})
            final_data.update({"comment": case_object.comment})

            # personal details to add
            personal_details = {}
            personal_details.update({"age": case_object.age})
            personal_details.update({"sex": case_object.sex.sex})
            personal_details.update({"occupation": case_object.occupation})
            personal_details.update({"region": case_object.state + ", " + case_object.country})

            # add details which allowed to be added
            if case_object.show_name is True:
                personal_details.update({"name": case_object.first_name + " " + case_object.last_name})

            if case_object.show_email is True:
                personal_details.update({"emailAddress": case_object.email_address})

            if case_object.show_phone_number is True:
                personal_details.update({"phoneNumber": case_object.phone_number})

            if case_object.show_address is True:
                personal_details.update({"address": case_object.street_address + " (" + case_object.zip_code + ")"})

            # add personal details to final_data
            final_data.update({"personalDetails": personal_details})
            return JsonResponse(data=final_data, status=200)
        except Exception as e:
            logging.error(e)
            return JsonResponse(data={"message": "error while getting data"}, status=500)