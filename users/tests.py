from django.test import TestCase 
from django.urls import reverse
from django.contrib.auth import get_user_model

class SignUpPageTest(TestCase):

    username = "testusername"
    email = "testuser@name.com"
    
    def test_sign_up_status_code(self):
        response = self.client.get('/users/signup/')
        self.assertEqual(response.status_code,200)

    def test_sign_up_status_code_by_name(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code,200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'signup.html')

    def test_sign_up_form(self):
        User = get_user_model()
        new_user = User.objects.create_user(self.username,self.email)
        self.assertEqual(User.objects.all().count(),1)
        self.assertEqual(User.objects.all()[0].username,self.username)
        self.assertEqual(User.objects.all()[0].email,self.email)

