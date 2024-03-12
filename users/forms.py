from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

User = get_user_model()


class RegistrationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')

    def clean(self):
        data = self.data
        for key in data.keys():
            if 'username' in key:
                if User.objects.filter(username=data[key]).exists():
                    self.add_error(
                        'username',
                        'К сожалению, это имя пользователя уже используется.'
                    )
