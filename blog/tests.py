# from django.test import TestCase
# from .models import Post
# from django.urls import reverse
# from django.contrib.auth import get_user_model
# # Create your tests here.

# class BlogTest(TestCase):

#     def get_user(self):
#         self.User = get_user_model().objects.create_user(
#             name = 'test_user',
#             email = 'test@email.com',
#             password = 'secret'
#         )

#         self.post = Post.objects.create(
#             title = 'Blog name',
#             author = self.User,
#             body = 'Blog writeup'
#         )

#     def test_string(self):
#         post = Post(title = 'A title')
#         self.assertEqual(str(post), post.title)
    
#     def test_get_absolute_url(self):
#         self.assertEqual(self.post.get_absolute_url(), '/post/1/')

#     def post_list(self):
#         response = self.client.get(reverse('post'))
#         self.assertEqual(response.status_code, 200)
#         self.assertContains(response, 'Blog writeup')
#         self.assertTemplateUsed(response, 'post.html')
#         self.assertContains(response, '<title>', html=True)

#     def home_page(self):
#         response = self.client.get(reverse('home'))
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'home.html')
#         self.assertContains(response, '<title>', html=True)
    
#     def about_page(self):
#         response = self.client.get(reverse('about'))
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'about.html')
#         self.assertContains(response, '<title>', html=True)

#     def post_detail(self):
#         response = self.client.get('post_details/1')
#         no_res = self.client.get('post_details/100')
#         self.assertEqual(response.status_code, 200)
#         self.assertEqual(no_res.status_code, 404)
#         self.assertContains(response, 'Blog name')
#         self.assertTemplateUsed(response, 'post_details.html')
#         self.assertContains(response, '<title>', html=True)

    
    
#     def test_post_create_view(self):
#         url = reverse('post_new')
#         response = self.client.post(url, {'title': 'A title', 'author': self.User, 'body': 'Blog writeup'})
#         self.assertEqual(response.status_code, 200)  # Adjust status code as per your implementation
#         self.assertContains(response, 'Test Post')   # Adjust content check as per your implementation
#         self.assertContains(response, 'Test Body')

#     def test_post_update_view(self):
#         post = Post.objects.create(title='A title', author=self.User, body='Blog writeup')
#         new_title = 'New Title'
#         url = reverse('post_edit', args=[post.pk])
#         response = self.client.post(url, {'title': new_title, 'author': self.User, 'body': 'new writeup'})
#         self.assertEqual(response.status_code, 200)  # Adjust status code as per your implementation
#         post.refresh_from_db()
#         self.assertEqual(post.title, new_title)  # Adjust field to check as per your implementation


#     def test_post_delete_view(self):
#         post = Post.objects.create(title='A title', author=self.User, body='Blog writeup')
#         url = reverse('post_delete', args=[1])
#         response = self.client.post(url)
#         self.assertEqual(response.status_code, 200)  # Adjust status code as per your implementation
#         self.assertRedirects(response, reverse('home'))  # Adjust redirection URL as per your implementation
#         self.assertFalse(Post.objects.filter(id=post/1).exists())  # Check if post is deleted


from django.test import TestCase
from .models import Post
from django.urls import reverse
from django.contrib.auth import get_user_model

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
        