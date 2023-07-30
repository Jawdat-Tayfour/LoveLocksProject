from datetime import datetime

from django.http  import HttpResponseRedirect
from django.test import SimpleTestCase , TestCase ,Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import PadLock


class HomePageTest(SimpleTestCase):
    
    def test_homepage_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code,200)

    def test_view_url_by_name(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code,200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'home.html')


class CreatePadlockTest(TestCase):

    date = datetime.date(datetime.today())
    motto = "motto field"
    def test_create_padlock(self):
        response = self.client.get("/padlocks/create_padlock/")
        self.assertEqual(response.status_code,200)


    def test_create_padlock_by_name(self):
        response = self.client.get(reverse('create_padlock'))
        self.assertEqual(response.status_code,200)


    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('create_padlock'))
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,"create_padlock.html")


    def test_create_padlock_form(self):
        new_Padlock = PadLock.objects.create(
            start_date = self.date,
            motto_field = self.motto
        )
        self.assertEqual(PadLock.objects.all().count(),1)
        self.assertEqual(PadLock.objects.all()[0].start_date, self.date)
        self.assertEqual(PadLock.objects.all()[0].motto_field, self.motto)


class EditPadlockTest(TestCase):

    def test_update_padlock(self):      
        User = get_user_model()
        user2 = User.objects.create_user(username="nvay",email="Jay@Yay.com",password="adminadminadmin")
        user = User.objects.create_user(username="nEay",email="Jay@Yay.com",password="adminadminadmin",user_locked_with=user2.username)
        new_padlock= PadLock.objects.create(start_date=datetime.date(datetime.today()),
                                            motto_field="Jodo is my motto",story_field='',modifier=user)
        c = Client()
        c.login(username="nEay",email="Jay@Yay.com",password="adminadminadmin")   
        response = c.post(
            reverse('edit_padlock',kwargs={'pk':new_padlock.id}),
        {'start_date':datetime.date(datetime.today()),
            'motto_field':"Jodo is not my motto",'story_field':''})
        
        self.assertEqual(response.status_code,302)

        new_padlock.refresh_from_db()
        self.assertEqual(new_padlock.motto_field,"Jodo is not my motto")

    def test_edit_padlock_status_code(self):
        c = Client()
        c.login(username="nEay",email="Jay@Yay.com",password="adminadminadmin")   
        new_padlock= PadLock.objects.create(start_date=datetime.date(datetime.today()),
                                            motto_field="Jodo is my motto",story_field='')
        response = self.client.get(reverse('edit_padlock',kwargs={'pk':new_padlock.id}))
        self.assertEqual(response.status_code,302)

class SearchPadlockTest(TestCase):
    
    def test_search_padlock_status_code(self):
        response = self.client.get('/padlocks/search_padlocks/')
        self.assertEqual(response.status_code,200)


    def test_search_padlock_url_by_view_name(self):
        response = self.client.get(reverse('search_padlocks'))
        self.assertEqual(response.status_code,200)
    
    
    def test_search_padlock_used_correct_template(self):
        response = self.client.get(reverse('search_padlocks'))
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'search_padlocks.html')

    
    


class PadlockDetailTest(TestCase):
    def test_padlock_detail_status_code(self):
        new_padlock= PadLock.objects.create(start_date=datetime.date(datetime.today()),motto_field="Jodo is my motto",story_field='')
        response = self.client.get('/padlocks/%i/' %(new_padlock.id))
        self.assertEqual(response.status_code,200)
    
    def test_padlock_detail_correct_view(self):
        new_padlock= PadLock.objects.create(start_date=datetime.date(datetime.today()),motto_field="Jodo is my motto",story_field='')
        response = self.client.get(reverse('padlock_detail',kwargs={'pk':new_padlock.id}))
        self.assertEqual(response.status_code,200)
    
    def test_padlock_detail_correct_template(self):
        new_padlock= PadLock.objects.create(start_date=datetime.date(datetime.today()),motto_field="Jodo is my motto",story_field='')
        response = self.client.get(reverse('padlock_detail',kwargs={'pk':new_padlock.id}))
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'padlock_detail.html')
