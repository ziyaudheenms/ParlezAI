from django.db import models
from django.contrib.auth.models import User


class CandidateProfile(models.Model):
    user = models.ForeignKey(User , on_delete= models.CASCADE)
    detailed_description = models.TextField()
    designation = models.CharField(max_length=255)
    profile_pic = models.ImageField(upload_to='images/Candidate')

class RecruiterProfile(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    company_name = models.CharField(max_length=255)
    company_info = models.TextField()
    profile_pic = models.ImageField(upload_to='images/Reruiter')

    def __str__(self) :

        return self.user.username


class InterviewCard(models.Model):  
    position_name = models.CharField(max_length=255)
    interview_type= models.CharField(max_length=200)
    job_description = models.TextField()
    primeSkills = models.TextField()
    Recruiter = models.ForeignKey(User , on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=100,default='active')
    total_appearence = models.IntegerField(default=0)

class ResumeFeedBack(models.Model):
    candidate = models.ForeignKey(User , on_delete=models.CASCADE)
    resume = models.FileField(upload_to="resume/")
    resume_feedback = models.TextField()
    interview_card = models.ForeignKey(InterviewCard , on_delete=models.CASCADE,related_name="Interview") 

class Interview(models.Model):
    candidate = models.ForeignKey(User , on_delete=models.CASCADE)
    interview_card = models.ForeignKey(InterviewCard , on_delete=models.CASCADE,related_name="Interview_Card")
    transcript = models.TextField()
    feedback = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    performance = models.TextField()
