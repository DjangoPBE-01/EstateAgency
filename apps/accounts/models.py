from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import UserManager
from apps.base.models import media_upload_to, BaseModel
from .choices import DeletedReason

# Create your models here.


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True, null=True, blank=True, verbose_name=_('email address'))
    phone_number = models.CharField(max_length=20, blank=True, null=True, verbose_name=_('phone number'))
    bio = models.TextField(blank=True, null=True, verbose_name=_('bio'))
    photo = models.ImageField(upload_to=media_upload_to, blank=True, null=True, verbose_name=_('photo'))
    deleted_reason = models.CharField(max_length=255, choices=DeletedReason.choices, blank=True, null=True, default=DeletedReason.I_THOUGH_ABOUT_IT, verbose_name=_('deleted reason'))
    
    
    objects = UserManager()
    
    
    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')
        
    

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.username
    
    
    
class Interest(BaseModel):
    user = models.ManyToManyField(CustomUser, related_name='interests', verbose_name=_('user'), through='UserInterest')
    name = models.CharField(max_length=255, verbose_name=_('name'))
    
    class Meta:
        verbose_name = _('Interest')
        verbose_name_plural = _('Interests')
    
    def __str__(self):
        return self.name



class UserInterest(BaseModel):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name=_('user'))
    interest = models.ForeignKey(Interest, on_delete=models.CASCADE, verbose_name=_('interest'))
    
    class Meta:
        verbose_name = _('User Interest')
        verbose_name_plural = _('User Interests')
        ordering = ['-created_at']
        
    
    def __str__(self):
        return f"{self.user.username} - {self.interest.name}"
    
    
    
    

class PromoCode(BaseModel):
    code = models.CharField(max_length=50, unique=True, verbose_name=_('code'))
    description = models.TextField(blank=True, null=True, verbose_name=_('description'))
    discount_percentage = models.DecimalField(max_digits=5, decimal_places=2, verbose_name=_('discount percentage'))
    valid_from = models.DateTimeField(verbose_name=_('valid from'))
    valid_to = models.DateTimeField(verbose_name=_('valid to'))
    is_active = models.BooleanField(default=True, verbose_name=_('is active'))
    is_used = models.BooleanField(default=False, verbose_name=_('is used'))
    user = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, blank=True, null=True, verbose_name=_('user'))
    
    
    
    class Meta:
        verbose_name = _('Promo Code')
        verbose_name_plural = _('Promo Codes')
        ordering = ['-created_at']
        
        
        
    @property
    def period_time(self):
        return f"{self.valid_from.strftime('%Y-%m-%d %H:%M:%S')} - {self.valid_to.strftime('%Y-%m-%d %H:%M:%S')}"
    
    def __str__(self):
        return self.code