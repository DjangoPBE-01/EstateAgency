from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from apps.base.models import BaseModel, media_upload_to
from django.core.validators import MinValueValidator, MaxValueValidator
from apps.accounts.models import PromoCode



User = get_user_model()


class Category(BaseModel):
    name = models.CharField(max_length=255, verbose_name=_('Category Name'))

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')
        ordering = ['-created_at']
        

    def __str__(self):
        return self.name




class Course(BaseModel):
    title = models.CharField(max_length=255, verbose_name=_('title'))
    description = models.TextField(verbose_name=_('description'))
    image = models.ImageField(upload_to=media_upload_to, blank=True, null=True, verbose_name=_('image'))
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_('price'))
    is_active = models.BooleanField(default=True, verbose_name=_('is active'))
    author = models.CharField(max_length=255, verbose_name=_('author'))
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, related_name='courses', verbose_name=_('category'))
    promo_code = models.ForeignKey(PromoCode, on_delete=models.SET_NULL, null=True, blank=True, related_name='courses', verbose_name=_('promo code'))

    class Meta:
        verbose_name = _('Course')
        verbose_name_plural = _('Courses')
        ordering = ['-created_at']
        

    def __str__(self):
        return self.title
    
    


class Module(BaseModel):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='modules', verbose_name=_('course'))
    name = models.CharField(max_length=255, verbose_name=_('name'))
    description = models.TextField(blank=True, null=True, verbose_name=_('description'))
    order = models.PositiveIntegerField(default=0, verbose_name=_('order'))

    class Meta:
        verbose_name = _('Module')
        verbose_name_plural = _('Modules')
        ordering = ['-created_at']
        

    def __str__(self):
        return self.name


class Video(BaseModel):
    module = models.ForeignKey(Module, on_delete=models.CASCADE, related_name='videos', verbose_name=_('module'))
    title = models.CharField(max_length=255, verbose_name=_('title'))
    description = models.TextField(blank=True, null=True, verbose_name=_('description'))
    video_file = models.FileField(upload_to=media_upload_to, blank=True, null=True, verbose_name=_('video file'))
    order = models.PositiveIntegerField(default=0, verbose_name=_('order'))
    status = models.BooleanField(default=True, verbose_name=_('status'), help_text=_('If the video is locked, we can see the field is False, and if the video is unlocked, we can see the field is True.'))
    period_time = models.DurationField(blank=True, null=True, verbose_name=_('period time'))

    class Meta:
        verbose_name = _('Video')
        verbose_name_plural = _('Videos')
        ordering = ['-created_at']

    def __str__(self):
        return self.title
    
    

class Comment(BaseModel):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='comments', verbose_name=_('user'))
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='comments', verbose_name=_('course'))
    content = models.TextField(verbose_name=_('content'), null=True, blank=True, help_text=_('The content field is used to write a comment about the course.'))
    review = models.PositiveIntegerField(default=0, verbose_name=_('review'), validators=[MinValueValidator(1), MaxValueValidator(5)], help_text=_('The review field is used to rate the course from 1 to 5.'))

    class Meta:
        verbose_name = _('Comment')
        verbose_name_plural = _('Comments')
        ordering = ['-created_at']
        

    def __str__(self):
        return f"{self.user.username} - {self.course.title}"
    
    
    

class CourseCertificate(BaseModel):
    name = models.CharField(max_length=255, verbose_name=_('name'), null=True, blank=True)
    description = models.TextField(blank=True, null=True, verbose_name=_('description'), help_text=_('The description field is used to write a description about the course certificate.'))
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='certificates', verbose_name=_('user'))
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='certificates', verbose_name=_('course'))
    certificate_file = models.FileField(upload_to=media_upload_to, blank=True, null=True, verbose_name=_('certificate file'))

    class Meta:
        verbose_name = _('Course Certificate')
        verbose_name_plural = _('Course Certificates')
        ordering = ['-created_at']
        

    def __str__(self):
        return f"{self.user.username} - {self.course.title}"
    
    
    
    
