from django.db import models
from ckeditor.fields import RichTextField

class FAQ(models.Model):
    question = models.TextField()
    answer = RichTextField()
    question_hi = models.TextField(null=True, blank=True)
    question_bn = models.TextField(null=True, blank=True)
    answer_hi = RichTextField(null=True, blank=True)
    answer_bn = RichTextField(null=True, blank=True)

    def get_translated_question(self, language_code='en'):
        return getattr(self, f"question_{language_code}", self.question)

    def get_translated_answer(self, language_code='en'):
        return getattr(self, f"answer_{language_code}", self.answer)
