from rest_framework.views import APIView
from rest_framework.response import Response
from .models import FAQ

class FAQList(APIView):
    def get(self, request):
        lang = request.query_params.get('lang', 'en')
        faqs = FAQ.objects.all()
        data = [{"question": faq.get_translated_question(lang), "answer": faq.get_translated_answer(lang)} for faq in faqs]
        return Response(data)
