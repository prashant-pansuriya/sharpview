from django import forms
from django.core.mail import EmailMessage

from .models import Customer


class CustomerForm(forms.ModelForm):
    class Meta:
          model = Customer
          exclude = ('status', )


    def clean(self):

        # data from the form is fetched using super function
        super(CustomerForm, self).clean()

        # extract the username and text field from the data
        if self.cleaned_data['name'] == None or len(self.cleaned_data['name']) > 200:
            self._errors['name'] = self.error_class([
                'Please Enter Valid Name !'])

        if len(self.cleaned_data['mobile_no']) != 10:
            self._errors['mobile_no'] = self.error_class([
                'Please Enter Valid Mobile No!'])

        return self.cleaned_data

    def save(self, commit=True):
        instance = super(CustomerForm, self).save(commit=False)
        if commit:
            to_email = "info.sharpview@gmail.com"
            mail_subject = "Contact Enquiry"
            email = EmailMessage(
                mail_subject, "Your name " + self.cleaned_data["name"] + "   :" + self.cleaned_data["message"],
                to=[to_email]
            )
            email.send()

            to_email = self.cleaned_data["email"]
            mail_subject = "Contact Enquiry"
            email = EmailMessage(
                mail_subject, "Name : " + self.cleaned_data["name"] + " After Some Time Call Back .",
                to=[to_email]
            )
            email.send()
            instance.save()

        return instance



