from django.contrib.auth import get_user_model
from django.contrib.auth.models import PermissionsMixin, AbstractBaseUser, BaseUserManager
from django.core.mail import send_mail
from django.db import models
from django.apps import apps
from utils.models import upload_path
from django.core.mail import send_mail
import os

def upload_path(instance, filename):
	return os.path.join(str(instance.__class__.__name__).lower() + '/', filename)


LEARNING_TYPE = (
    ('очно', 'очно'),
    ('дистанционно', 'дистанционно'),
)

LEVELS = (
    ('juniour', 'juniour'),
    ('middle', 'middle'),
    ('senior', 'senior'),
)


VERIFICATION  = (
    ('да', 'да'),
    ('нет', 'нет'),
)

class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_admin', True)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def get_by_natural_key(self, username):
        case_insensitive_username_field = '{}__iexact'.format(self.model.USERNAME_FIELD)
        return self.get(**{case_insensitive_username_field: username})


class User(AbstractBaseUser, PermissionsMixin):
    """
    """

    class Meta:
        verbose_name = u'Пользователь'
        verbose_name_plural = u'Пользователи'

    email = models.EmailField(verbose_name='Email', unique=True)
    surname = models.CharField(verbose_name='Фамилия', max_length=64, blank=False)
    name = models.CharField(verbose_name='Имя', max_length=64, blank=False)
    patronymic = models.CharField(verbose_name='Отчество', max_length=32, blank=True, null=True)
    phone = models.CharField(verbose_name='Телефон', max_length=32, blank=True)
    # type = models.IntegerField(verbose_name='Тип', default=0, blank=False)
    is_enabled = models.BooleanField(verbose_name='Активен', default=False)
    is_admin = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to=upload_path, null=True, blank=True)
    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return "%s %s" % (self.name, self.surname)

    def get_full_name(self):
        return "%s %s" % (self.name, self.surname)

    def get_short_name(self):
        return "%s %s" % (self.name, self.surname)

    def email_user(self, subject, message, from_email=None, **kwargs):
        '''
        Sends an email to this User.
        '''
        send_mail(subject, message, from_email, [self.email], **kwargs)

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    def get_type(self):
        return self.type

    @property
    def is_staff(self):
        return self.is_admin

    def get_role(self):
        user_role = UserRole.objects.get(user=self)
        return user_role.role

    def check_access(self, action_id):
        user_role = self.get_role()
        action = RoleAction.objects.filter(role=user_role).filter(action=action_id)
        if action:
            return True
        return False

    def get_customer(self):
        try:
            user_customer = UserCustomer.objects.get(user=self)
        except Exception as e:
            return None
        return user_customer.customer




class Role(models.Model):
    class Meta:
        verbose_name = 'Роль'
        verbose_name_plural = 'Роли'

    name = models.CharField(verbose_name='Название роли', max_length=256)
    is_enabled = models.BooleanField(verbose_name='Активно', default=True)

    def __str__(self):
        return self.name


class Action(models.Model):
    class Meta:
        verbose_name = 'Действие роли'
        verbose_name_plural = 'Действия ролей'

    name = models.CharField(verbose_name='Название действия', max_length=256)
    is_enabled = models.BooleanField(verbose_name='Активно', default=True)

    def __str__(self):
        return self.name


class RoleAction(models.Model):
    class Meta:
        verbose_name = 'Действие роли'
        verbose_name_plural = 'Действия ролей'

    role = models.ForeignKey(Role, verbose_name='Роль', on_delete=models.CASCADE)
    action = models.ForeignKey(Action, verbose_name='Действие', on_delete=models.CASCADE)

    def __str__(self):
        return "%s - %s" % (self.role.name, self.action.name)


class UserRole(models.Model):
    class Meta:
        verbose_name = 'Роль пользователя'
        verbose_name_plural = 'Роли пользователя'

    user = models.OneToOneField(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    role = models.ForeignKey(Role, verbose_name='Роль', on_delete=models.CASCADE)

    def __str__(self):
        return "%s %s" % (self.user.name, self.user.surname)



