from modeltranslation.translator import TranslationOptions, register
from .models import CustomUser, Interest, PromoCode

@register(CustomUser)
class CustomUserTranslationOptions(TranslationOptions):
    fields = ('bio',)

@register(Interest)
class InterestTranslationOptions(TranslationOptions):
    fields = ('name',)

@register(PromoCode)
class PromoCodeTranslationOptions(TranslationOptions):
    fields = ('description',)