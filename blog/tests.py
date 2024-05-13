from django.test import TestCase
from .models import Post
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User


class BlogTest(TestCase):
    
    def setUp(self):
        self.User = get_user_model().objects.create_user(
            username='test_user',
            email='test@email.com',
            password='secret'
        )

        self.post = Post.objects.create(
            title='Blog name',
            author=self.User,
            body='Blog writeup'
        )

    def test_string(self):
        post = Post(title='A title')
        self.assertEqual(str(post), post.title)
    
    def test_get_absolute_url(self):
        self.assertEqual(self.post.get_absolute_url(), '/post_details/1')


    def post_list(self):
        response = self.client.get(reverse('post'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Blog writeup')
        self.assertTemplateUsed(response, 'post.html')
        self.assertContains(response, '<title>', html=True)

    def home_page(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')
        self.assertContains(response, '<title>', html=True)
    
    def about_page(self):
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'about.html')
        self.assertContains(response, '<title>', html=True)

    def post_detail(self):
        response = self.client.get('post_details/1')
        no_res = self.client.get('post_details/100')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_res.status_code, 404)
        self.assertContains(response, 'Blog name')
        self.assertTemplateUsed(response, 'post_details.html')
        self.assertContains(response, '<title>', html=True)

    def test_post_create_view(self):
        url = reverse('post_new')
        response = self.client.post(url, {'title': 'A title', 'author': self.User.pk, 'body': 'Blog writeup'})
        self.assertEqual(response.status_code, 302)  # Adjust status code as per your implementation

    def test_post_update_view(self):
        post = Post.objects.create(title='A title', author=self.User, body='Blog writeup')
        new_title = 'New Title'
        url = reverse('post_edit', args=[post.pk])
        response = self.client.post(url, {'title': new_title, 'author': self.User.pk, 'body': 'new writeup'})
        self.assertEqual(response.status_code, 302)  # Adjust status code as per your implementation
        post.refresh_from_db()
        self.assertEqual(post.title, new_title)  # Adjust field to check as per your implementation

    def test_post_delete_view(self):
        post = Post.objects.create(title='A title', author=self.User, body='Blog writeup')
        url = reverse('post_delete', args=[post.pk])
        response = self.client.post(url)
        self.assertEqual(response.status_code, 302)  # Adjust status code as per your implementation

class UserTestCase(TestCase):
    def test_signup(self):
        # Ensure that the signup page loads successfully
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)
        
        # Create a new user
        response = self.client.post(reverse('signup'), {
            'username': 'testuser',
            'email': 'test@example.com',
            'password1': 'testpassword',
            'password2': 'testpassword'
        })
        self.assertEqual(response.status_code, 302)  # 302 is the HTTP status code for redirect
         # Check if the user was created successfully
        self.assertTrue(User.objects.filter(username='testuser').exists())
        

    def test_login(self):  # failed test
        # Ensure that the login page loads successfully
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        
        # Log in with the created user
        response1 = self.client.post(reverse('login'), {
            'username': 'testuser',
            'password': 'testpassword'
        })
        
        self.assertEqual(response1.status_code, 302)
        self.assertRedirects(response1, reverse('home'))# Redirect after successful login
        
        # Check if the user is authenticated
        self.assertTrue(response.wsgi_request.user.is_authenticated)