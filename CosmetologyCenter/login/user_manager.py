from django.contrib.auth.models import BaseUserManager

class CustomUserManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, date_of_birth, phone_number, password=None, **extra_fields):
        """
        Создает и сохраняет обычного пользователя с указанными данными.
        """
        if not email:
            raise ValueError('The Email field must be set')

        email = self.normalize_email(email)
        user = self.model(email=email, first_name=first_name, last_name=last_name,
                          date_of_birth=date_of_birth, phone_number=phone_number, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email='', first_name='', last_name='', date_of_birth='1900-12-12', phone_number='123', password=None, **extra_fields):
        """
        Создает и сохраняет суперпользователя с указанными данными.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self.create_user(email, first_name, last_name, date_of_birth, phone_number, password, **extra_fields)