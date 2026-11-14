from modeltranslation.translator import TranslationOptions, register
from .models import Category, Course, Module, Video

@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name',)


@register(Course)
class CourseTranslationOptions(TranslationOptions):
    fields = ('description',)

@register(Module)
class ModuleTranslationOptions(TranslationOptions):
    fields = ('name', 'description',)
    

@register(Video)
class VideoTranslationOptions(TranslationOptions):
    fields = ('title', 'description',)
    
