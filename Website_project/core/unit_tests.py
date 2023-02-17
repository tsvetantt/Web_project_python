import unittest


from models import Profile, Post, LikePost, FollowersCount
from django.contrib.auth.models import User


class ProfileTestCase(unittest.TestCase):
    """Testing the profil set up"""

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.profile = Profile.objects.create(user=self.user, id_user=self.user.id, bio='Test bio', location='Test location')

    def test_profile_str_method(self):
        self.assertEqual(str(self.profile), self.user.username)

    def test_profile_fields(self):
        self.assertEqual(self.profile.user, self.user)
        self.assertEqual(self.profile.id_user, self.user.id)
        self.assertEqual(self.profile.bio, 'Test bio')
        self.assertEqual(self.profile.location, 'Test location')

    def test_profile_defaults(self):
        profile = Profile.objects.create(user=self.user, id_user=self.user.id)
        self.assertEqual(profile.bio, '')
        self.assertEqual(profile.profile_img.name, 'profile_images/blank-profile-picture-973460_1280.png')
        self.assertEqual(profile.location, '')

class PostTestCase(unittest.TestCase):
    """Testing post creation"""
    def setUp(self):
        self.post = Post.objects.create(user='testuser', image='test.jpg', caption='Test caption')

    def test_post_str_method(self):
        self.assertEqual(str(self.post), self.post.user)

    def test_post_fields(self):
        self.assertEqual(self.post.user, 'testuser')
        self.assertEqual(self.post.image.name, 'post_images/test.jpg')
        self.assertEqual(self.post.caption, 'Test caption')
        self.assertEqual(self.post.num_of_likes, 0)

class LikePostTestCase(unittest.TestCase):
    """Testing liking system"""
    def setUp(self):
        self.like_post = LikePost.objects.create(
            post_id='1', username='testuser')

    def test_likepost_str_method(self):
        self.assertEqual(str(self.like_post), self.like_post.username)

    def test_likepost_fields(self):
        self.assertEqual(self.like_post.post_id, '1')
        self.assertEqual(self.like_post.username, 'testuser')

class FollowersCountTestCase(unittest.TestCase):
    """Testing the amount of followers"""
    def setUp(self):
        self.followers_count = FollowersCount.objects.create(
            follower='testuser1', user='testuser2')

    def test_followerscount_str_method(self):
        self.assertEqual(str(self.followers_count), self.followers_count.user)

    def test_followerscount_fields(self):
        self.assertEqual(self.followers_count.follower, 'testuser1')
        self.assertEqual(self.followers_count.user, 'testuser2')