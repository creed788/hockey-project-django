from django.db import models

# Create your models here.

STATE_CHOICES = (
    ('Andaman and Nicobar Islands', 'Andaman and Nicobar Islands'),
    ('Andhra Pradesh', 'Andhra Pradesh'),
    ('Arunachal Pradesh', 'Arunachal Pradesh'),
    ('Assam', 'Assam'),
    ('Bihar', 'Bihar'),
    ('Chandigarh', 'Chandigarh'),
    ('Chhattisgarh', 'Chhattisgarh'),
    ('Dadra and Nagar Haveli and Daman and Diu', 'Dadra and Nagar Haveli and Daman and Diu'),
    ('Delhi', 'Delhi'),
    ('Goa', 'Goa'),
    ('Gujarat', 'Gujarat'),
    ('Haryana', 'Haryana'),
    ('Himachal Pradesh', 'Himachal Pradesh'),
    ('Jammu and Kashmir', 'Jammu and Kashmir'),
    ('Jharkhand', 'Jharkhand'),
    ('Karnataka', 'Karnataka'),
    ('Kerala', 'Kerala'),
    ('Ladakh', 'Ladakh'),
    ('Lakshadweep', 'Lakshadweep'),
    ('Madhya Pradesh', 'Madhya Pradesh'),
    ('Maharashtra', 'Maharashtra'),
    ('Manipur', 'Manipur'),
    ('Meghalaya', 'Meghalaya'),
    ('Mizoram', 'Mizoram'),
    ('Nagaland', 'Nagaland'),
    ('Odisha', 'Odisha'),
    ('Puducherry', 'Puducherry'),
    ('Punjab', 'Punjab'),
    ('Rajasthan', 'Rajasthan'),
    ('Sikkim', 'Sikkim'),
    ('Tamil Nadu', 'Tamil Nadu'),
    ('Telangana', 'Telangana'),
    ('Tripura', 'Tripura'),
    ('Uttar Pradesh', 'Uttar Pradesh'),
    ('Uttarakhand', 'Uttarakhand'),
    ('West Bengal', 'West Bengal')

)

GENDER_CHOICES = [
  ('M', 'Male'),
  ('F', 'Female'),
  ('O', 'Other'),
    ]

LEVELS = [('I', 'interantional'), ('N', 'national')]

class Team(models.Model):
    team_name = models.CharField(max_length=100)
    coach_name = models.CharField(max_length=100)
    team_captain = models.ForeignKey('Player', on_delete=models.SET_NULL, null=True, related_name='captain_of')
    team_contact_info = models.CharField(max_length=200)

    def __str__(self):
        return self.team_name

class Player(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    contact_info = models.CharField(max_length=200)
    address = models.TextField()
    playing_position = models.CharField(max_length=50)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='players')
    player_image = models.ImageField(upload_to='player_images/', blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Match(models.Model):
    date_time = models.DateTimeField()
    location = models.CharField(max_length=100)
    home_team = models.ForeignKey(Team, related_name='home_matches', on_delete=models.CASCADE)
    away_team = models.ForeignKey(Team, related_name='away_matches', on_delete=models.CASCADE)
    home_team_goals = models.PositiveIntegerField()
    away_team_goals = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.home_team} vs {self.away_team} - {self.date_time}"

class Tournament(models.Model):
    tournament_name = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    venue = models.CharField(max_length = 100, null=True)
    host_country = models.CharField(max_length=100)
    level = models.CharField(max_length= 1, choices=LEVELS, null=True)

    def __str__(self):
        return self.tournament_name

class AdministrativeStaff(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    position = models.CharField(max_length=100)
    contact_info = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    

class GalleryPhoto(models.Model):
    photo_title = models.CharField(max_length=100, null = True)
    phot_desc = models.TextField(null=True)
    g_image = models.ImageField(null = True, upload_to='gallery_images/')
    date_added = models.DateTimeField(null=True)
    insta = models.CharField(max_length=100, null=True)
    tweet = models.CharField(max_length=100, null = True)
    fb = models.CharField(max_length=100, null=True)
    profile = models.CharField(max_length=100, null=True)

    def __str__(self):
        return f"{self.photo_title}"
    
class GalleryVideo(models.Model):
    video_title = models.CharField(null=True, max_length=100)
    video_desc = models.TextField( null=True)
    g_video = models.FileField(null = True, upload_to='videos/')
    date_added = models.DateTimeField(null=True)

def __str__(self):
        return f"{self.video_title}"


class News(models.Model):
    news_title = models.CharField(max_length=100, null = True)
    news_desc = models.TextField(null=True)
    news_img = models.ImageField(null = True, upload_to='news/', blank=True)
    news_date = models.DateTimeField(null=True)
    
    def __str__(self):
        return f"{self.news_title}"


class Contact(models.Model):
    name = models.CharField(null=True, max_length=100)
    email = models.EmailField(null=True, max_length=100)
    subject = models.CharField(null=True, max_length=100)
    message = models.TextField(null=True)
    date_added = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f"{self.name}"
    

    