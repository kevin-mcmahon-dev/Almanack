from django.contrib.auth.forms import UserCreationForm

# class ProfileForm(models.model):
#     fields = 
    
class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ("email", "first_name", "last_name")
    # class Meta:
    #     model = User
    #     fields = ('username', 'first_name', 'last_name', 'email',)

    # def save(self, commit=True):
    #     user = super(UserCreationForm, self).save(commit=False)
    #     user.save()
    #     return user
