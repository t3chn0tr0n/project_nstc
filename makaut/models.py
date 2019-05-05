from django.db import models
from students.models import Student


class semester_1(models.Model):
    student_id = models.CharField(default=" ", max_length=15, primary_key=True)
    moocs_for_12 = models.IntegerField(null=False, blank=False, default='0')
    moocs_for_8 = models.IntegerField(null=False, blank=False, default='0')
    tech_fest_organizer = models.IntegerField(
        null=False, blank=False, default='0')
    tech_fest_participant = models.IntegerField(
        null=False, blank=False, default='0')
    rural_reporting = models.IntegerField(null=False, blank=False, default='0')
    tree_planting = models.IntegerField(null=False, blank=False, default='0')
    part_relief_camps = models.IntegerField(
        null=False, blank=False, default='0')
    part_tech_quiz = models.IntegerField(null=False, blank=False, default='0')
    public_editing = models.IntegerField(null=False, blank=False, default='0')
    public_writting = models.IntegerField(null=False, blank=False, default='0')
    publication = models.IntegerField(null=False, blank=False, default='0')
    research_publications = models.IntegerField(
        null=False, blank=False, default='0')
    innovative_projects = models.IntegerField(
        null=False, blank=False, default='0')
    blodd_donation = models.IntegerField(null=False, blank=False, default='0')
    blood_organization = models.IntegerField(
        null=False, blank=False, default='0')
    sports_college = models.IntegerField(null=False, blank=False, default='0')
    sports_university = models.IntegerField(
        null=False, blank=False, default='0')
    sports_district = models.IntegerField(null=False, blank=False, default='0')
    sports_state = models.IntegerField(null=False, blank=False, default='0')
    sports_national = models.IntegerField(null=False, blank=False, default='0')
    cultural_programme = models.IntegerField(
        null=False, blank=False, default='0')
    member_prof_society = models.IntegerField(
        null=False, blank=False, default='0')
    student_chapter = models.IntegerField(null=False, blank=False, default='0')
    industry_visit = models.IntegerField(null=False, blank=False, default='0')
    photography = models.IntegerField(null=False, blank=False, default='0')
    yoga_camp = models.IntegerField(null=False, blank=False, default='0')
    entrepreneur = models.IntegerField(null=False, blank=False, default='0')
    adventure_sports = models.IntegerField(
        null=False, blank=False, default='0')
    training_privileged = models.IntegerField(
        null=False, blank=False, default='0')
    com_service = models.IntegerField(null=False, blank=False, default='0')
    total = models.IntegerField(null=False, blank=False, default='0')


class semester_2(models.Model):
    student_id = models.CharField(default=" ", max_length=15, primary_key=True)
    moocs_for_12 = models.IntegerField(null=False, blank=False, default='0')
    moocs_for_8 = models.IntegerField(null=False, blank=False, default='0')
    tech_fest_organizer = models.IntegerField(
        null=False, blank=False, default='0')
    tech_fest_participant = models.IntegerField(
        null=False, blank=False, default='0')
    rural_reporting = models.IntegerField(null=False, blank=False, default='0')
    tree_planting = models.IntegerField(null=False, blank=False, default='0')
    part_relief_camps = models.IntegerField(
        null=False, blank=False, default='0')
    part_tech_quiz = models.IntegerField(null=False, blank=False, default='0')
    public_editing = models.IntegerField(null=False, blank=False, default='0')
    public_writting = models.IntegerField(null=False, blank=False, default='0')
    publication = models.IntegerField(null=False, blank=False, default='0')
    research_publications = models.IntegerField(
        null=False, blank=False, default='0')
    innovative_projects = models.IntegerField(
        null=False, blank=False, default='0')
    blodd_donation = models.IntegerField(null=False, blank=False, default='0')
    blood_organization = models.IntegerField(
        null=False, blank=False, default='0')
    sports_college = models.IntegerField(null=False, blank=False, default='0')
    sports_university = models.IntegerField(
        null=False, blank=False, default='0')
    sports_district = models.IntegerField(null=False, blank=False, default='0')
    sports_state = models.IntegerField(null=False, blank=False, default='0')
    sports_national = models.IntegerField(null=False, blank=False, default='0')
    cultural_programme = models.IntegerField(
        null=False, blank=False, default='0')
    member_prof_society = models.IntegerField(
        null=False, blank=False, default='0')
    student_chapter = models.IntegerField(null=False, blank=False, default='0')
    industry_visit = models.IntegerField(null=False, blank=False, default='0')
    photography = models.IntegerField(null=False, blank=False, default='0')
    yoga_camp = models.IntegerField(null=False, blank=False, default='0')
    entrepreneur = models.IntegerField(null=False, blank=False, default='0')
    adventure_sports = models.IntegerField(
        null=False, blank=False, default='0')
    training_privileged = models.IntegerField(
        null=False, blank=False, default='0')
    com_service = models.IntegerField(null=False, blank=False, default='0')
    total = models.IntegerField(null=False, blank=False, default='0')


class semester_3(models.Model):
    student_id = models.CharField(default=" ", max_length=15, primary_key=True)
    moocs_for_12 = models.IntegerField(null=False, blank=False, default='0')
    moocs_for_8 = models.IntegerField(null=False, blank=False, default='0')
    tech_fest_organizer = models.IntegerField(
        null=False, blank=False, default='0')
    tech_fest_participant = models.IntegerField(
        null=False, blank=False, default='0')
    rural_reporting = models.IntegerField(null=False, blank=False, default='0')
    tree_planting = models.IntegerField(null=False, blank=False, default='0')
    part_relief_camps = models.IntegerField(
        null=False, blank=False, default='0')
    part_tech_quiz = models.IntegerField(null=False, blank=False, default='0')
    public_editing = models.IntegerField(null=False, blank=False, default='0')
    public_writting = models.IntegerField(null=False, blank=False, default='0')
    publication = models.IntegerField(null=False, blank=False, default='0')
    research_publications = models.IntegerField(
        null=False, blank=False, default='0')
    innovative_projects = models.IntegerField(
        null=False, blank=False, default='0')
    blodd_donation = models.IntegerField(null=False, blank=False, default='0')
    blood_organization = models.IntegerField(
        null=False, blank=False, default='0')
    sports_college = models.IntegerField(null=False, blank=False, default='0')
    sports_university = models.IntegerField(
        null=False, blank=False, default='0')
    sports_district = models.IntegerField(null=False, blank=False, default='0')
    sports_state = models.IntegerField(null=False, blank=False, default='0')
    sports_national = models.IntegerField(null=False, blank=False, default='0')
    cultural_programme = models.IntegerField(
        null=False, blank=False, default='0')
    member_prof_society = models.IntegerField(
        null=False, blank=False, default='0')
    student_chapter = models.IntegerField(null=False, blank=False, default='0')
    industry_visit = models.IntegerField(null=False, blank=False, default='0')
    photography = models.IntegerField(null=False, blank=False, default='0')
    yoga_camp = models.IntegerField(null=False, blank=False, default='0')
    entrepreneur = models.IntegerField(null=False, blank=False, default='0')
    adventure_sports = models.IntegerField(
        null=False, blank=False, default='0')
    training_privileged = models.IntegerField(
        null=False, blank=False, default='0')
    com_service = models.IntegerField(null=False, blank=False, default='0')
    total = models.IntegerField(null=False, blank=False, default='0')


class semester_4(models.Model):
    student_id = models.CharField(default=" ", max_length=15, primary_key=True)
    moocs_for_12 = models.IntegerField(null=False, blank=False, default='0')
    moocs_for_8 = models.IntegerField(null=False, blank=False, default='0')
    tech_fest_organizer = models.IntegerField(
        null=False, blank=False, default='0')
    tech_fest_participant = models.IntegerField(
        null=False, blank=False, default='0')
    rural_reporting = models.IntegerField(null=False, blank=False, default='0')
    tree_planting = models.IntegerField(null=False, blank=False, default='0')
    part_relief_camps = models.IntegerField(
        null=False, blank=False, default='0')
    part_tech_quiz = models.IntegerField(null=False, blank=False, default='0')
    public_editing = models.IntegerField(null=False, blank=False, default='0')
    public_writting = models.IntegerField(null=False, blank=False, default='0')
    publication = models.IntegerField(null=False, blank=False, default='0')
    research_publications = models.IntegerField(
        null=False, blank=False, default='0')
    innovative_projects = models.IntegerField(
        null=False, blank=False, default='0')
    blodd_donation = models.IntegerField(null=False, blank=False, default='0')
    blood_organization = models.IntegerField(
        null=False, blank=False, default='0')
    sports_college = models.IntegerField(null=False, blank=False, default='0')
    sports_university = models.IntegerField(
        null=False, blank=False, default='0')
    sports_district = models.IntegerField(null=False, blank=False, default='0')
    sports_state = models.IntegerField(null=False, blank=False, default='0')
    sports_national = models.IntegerField(null=False, blank=False, default='0')
    cultural_programme = models.IntegerField(
        null=False, blank=False, default='0')
    member_prof_society = models.IntegerField(
        null=False, blank=False, default='0')
    student_chapter = models.IntegerField(null=False, blank=False, default='0')
    industry_visit = models.IntegerField(null=False, blank=False, default='0')
    photography = models.IntegerField(null=False, blank=False, default='0')
    yoga_camp = models.IntegerField(null=False, blank=False, default='0')
    entrepreneur = models.IntegerField(null=False, blank=False, default='0')
    adventure_sports = models.IntegerField(
        null=False, blank=False, default='0')
    training_privileged = models.IntegerField(
        null=False, blank=False, default='0')
    com_service = models.IntegerField(null=False, blank=False, default='0')
    total = models.IntegerField(null=False, blank=False, default='0')


class semester_5(models.Model):
    student_id = models.CharField(default=" ", max_length=15, primary_key=True)
    moocs_for_12 = models.IntegerField(null=False, blank=False, default='0')
    moocs_for_8 = models.IntegerField(null=False, blank=False, default='0')
    tech_fest_organizer = models.IntegerField(
        null=False, blank=False, default='0')
    tech_fest_participant = models.IntegerField(
        null=False, blank=False, default='0')
    rural_reporting = models.IntegerField(null=False, blank=False, default='0')
    tree_planting = models.IntegerField(null=False, blank=False, default='0')
    part_relief_camps = models.IntegerField(
        null=False, blank=False, default='0')
    part_tech_quiz = models.IntegerField(null=False, blank=False, default='0')
    public_editing = models.IntegerField(null=False, blank=False, default='0')
    public_writting = models.IntegerField(null=False, blank=False, default='0')
    publication = models.IntegerField(null=False, blank=False, default='0')
    research_publications = models.IntegerField(
        null=False, blank=False, default='0')
    innovative_projects = models.IntegerField(
        null=False, blank=False, default='0')
    blodd_donation = models.IntegerField(null=False, blank=False, default='0')
    blood_organization = models.IntegerField(
        null=False, blank=False, default='0')
    sports_college = models.IntegerField(null=False, blank=False, default='0')
    sports_university = models.IntegerField(
        null=False, blank=False, default='0')
    sports_district = models.IntegerField(null=False, blank=False, default='0')
    sports_state = models.IntegerField(null=False, blank=False, default='0')
    sports_national = models.IntegerField(null=False, blank=False, default='0')
    cultural_programme = models.IntegerField(
        null=False, blank=False, default='0')
    member_prof_society = models.IntegerField(
        null=False, blank=False, default='0')
    student_chapter = models.IntegerField(null=False, blank=False, default='0')
    industry_visit = models.IntegerField(null=False, blank=False, default='0')
    photography = models.IntegerField(null=False, blank=False, default='0')
    yoga_camp = models.IntegerField(null=False, blank=False, default='0')
    entrepreneur = models.IntegerField(null=False, blank=False, default='0')
    adventure_sports = models.IntegerField(
        null=False, blank=False, default='0')
    training_privileged = models.IntegerField(
        null=False, blank=False, default='0')
    com_service = models.IntegerField(null=False, blank=False, default='0')
    total = models.IntegerField(null=False, blank=False, default='0')


class semester_6(models.Model):
    student_id = models.CharField(default=" ", max_length=15, primary_key=True)
    moocs_for_12 = models.IntegerField(null=False, blank=False, default='0')
    moocs_for_8 = models.IntegerField(null=False, blank=False, default='0')
    tech_fest_organizer = models.IntegerField(
        null=False, blank=False, default='0')
    tech_fest_participant = models.IntegerField(
        null=False, blank=False, default='0')
    rural_reporting = models.IntegerField(null=False, blank=False, default='0')
    tree_planting = models.IntegerField(null=False, blank=False, default='0')
    part_relief_camps = models.IntegerField(
        null=False, blank=False, default='0')
    part_tech_quiz = models.IntegerField(null=False, blank=False, default='0')
    public_editing = models.IntegerField(null=False, blank=False, default='0')
    public_writting = models.IntegerField(null=False, blank=False, default='0')
    publication = models.IntegerField(null=False, blank=False, default='0')
    research_publications = models.IntegerField(
        null=False, blank=False, default='0')
    innovative_projects = models.IntegerField(
        null=False, blank=False, default='0')
    blodd_donation = models.IntegerField(null=False, blank=False, default='0')
    blood_organization = models.IntegerField(
        null=False, blank=False, default='0')
    sports_college = models.IntegerField(null=False, blank=False, default='0')
    sports_university = models.IntegerField(
        null=False, blank=False, default='0')
    sports_district = models.IntegerField(null=False, blank=False, default='0')
    sports_state = models.IntegerField(null=False, blank=False, default='0')
    sports_national = models.IntegerField(null=False, blank=False, default='0')
    cultural_programme = models.IntegerField(
        null=False, blank=False, default='0')
    member_prof_society = models.IntegerField(
        null=False, blank=False, default='0')
    student_chapter = models.IntegerField(null=False, blank=False, default='0')
    industry_visit = models.IntegerField(null=False, blank=False, default='0')
    photography = models.IntegerField(null=False, blank=False, default='0')
    yoga_camp = models.IntegerField(null=False, blank=False, default='0')
    entrepreneur = models.IntegerField(null=False, blank=False, default='0')
    adventure_sports = models.IntegerField(
        null=False, blank=False, default='0')
    training_privileged = models.IntegerField(
        null=False, blank=False, default='0')
    com_service = models.IntegerField(null=False, blank=False, default='0')
    total = models.IntegerField(null=False, blank=False, default='0')


class semester_7(models.Model):
    student_id = models.CharField(default=" ", max_length=15, primary_key=True)
    moocs_for_12 = models.IntegerField(null=False, blank=False, default='0')
    moocs_for_8 = models.IntegerField(null=False, blank=False, default='0')
    tech_fest_organizer = models.IntegerField(
        null=False, blank=False, default='0')
    tech_fest_participant = models.IntegerField(
        null=False, blank=False, default='0')
    rural_reporting = models.IntegerField(null=False, blank=False, default='0')
    tree_planting = models.IntegerField(null=False, blank=False, default='0')
    part_relief_camps = models.IntegerField(
        null=False, blank=False, default='0')
    part_tech_quiz = models.IntegerField(null=False, blank=False, default='0')
    public_editing = models.IntegerField(null=False, blank=False, default='0')
    public_writting = models.IntegerField(null=False, blank=False, default='0')
    publication = models.IntegerField(null=False, blank=False, default='0')
    research_publications = models.IntegerField(
        null=False, blank=False, default='0')
    innovative_projects = models.IntegerField(
        null=False, blank=False, default='0')
    blodd_donation = models.IntegerField(null=False, blank=False, default='0')
    blood_organization = models.IntegerField(
        null=False, blank=False, default='0')
    sports_college = models.IntegerField(null=False, blank=False, default='0')
    sports_university = models.IntegerField(
        null=False, blank=False, default='0')
    sports_district = models.IntegerField(null=False, blank=False, default='0')
    sports_state = models.IntegerField(null=False, blank=False, default='0')
    sports_national = models.IntegerField(null=False, blank=False, default='0')
    cultural_programme = models.IntegerField(
        null=False, blank=False, default='0')
    member_prof_society = models.IntegerField(
        null=False, blank=False, default='0')
    student_chapter = models.IntegerField(null=False, blank=False, default='0')
    industry_visit = models.IntegerField(null=False, blank=False, default='0')
    photography = models.IntegerField(null=False, blank=False, default='0')
    yoga_camp = models.IntegerField(null=False, blank=False, default='0')
    entrepreneur = models.IntegerField(null=False, blank=False, default='0')
    adventure_sports = models.IntegerField(
        null=False, blank=False, default='0')
    training_privileged = models.IntegerField(
        null=False, blank=False, default='0')
    com_service = models.IntegerField(null=False, blank=False, default='0')
    total = models.IntegerField(null=False, blank=False, default='0')


class semester_8(models.Model):
    student_id = models.CharField(default=" ", max_length=15, primary_key=True)
    moocs_for_12 = models.IntegerField(null=False, blank=False, default='0')
    moocs_for_8 = models.IntegerField(null=False, blank=False, default='0')
    tech_fest_organizer = models.IntegerField(
        null=False, blank=False, default='0')
    tech_fest_participant = models.IntegerField(
        null=False, blank=False, default='0')
    rural_reporting = models.IntegerField(null=False, blank=False, default='0')
    tree_planting = models.IntegerField(null=False, blank=False, default='0')
    part_relief_camps = models.IntegerField(
        null=False, blank=False, default='0')
    part_tech_quiz = models.IntegerField(null=False, blank=False, default='0')
    public_editing = models.IntegerField(null=False, blank=False, default='0')
    public_writting = models.IntegerField(null=False, blank=False, default='0')
    publication = models.IntegerField(null=False, blank=False, default='0')
    research_publications = models.IntegerField(
        null=False, blank=False, default='0')
    innovative_projects = models.IntegerField(
        null=False, blank=False, default='0')
    blodd_donation = models.IntegerField(null=False, blank=False, default='0')
    blood_organization = models.IntegerField(
        null=False, blank=False, default='0')
    sports_college = models.IntegerField(null=False, blank=False, default='0')
    sports_university = models.IntegerField(
        null=False, blank=False, default='0')
    sports_district = models.IntegerField(null=False, blank=False, default='0')
    sports_state = models.IntegerField(null=False, blank=False, default='0')
    sports_national = models.IntegerField(null=False, blank=False, default='0')
    cultural_programme = models.IntegerField(
        null=False, blank=False, default='0')
    member_prof_society = models.IntegerField(
        null=False, blank=False, default='0')
    student_chapter = models.IntegerField(null=False, blank=False, default='0')
    industry_visit = models.IntegerField(null=False, blank=False, default='0')
    photography = models.IntegerField(null=False, blank=False, default='0')
    yoga_camp = models.IntegerField(null=False, blank=False, default='0')
    entrepreneur = models.IntegerField(null=False, blank=False, default='0')
    adventure_sports = models.IntegerField(
        null=False, blank=False, default='0')
    training_privileged = models.IntegerField(
        null=False, blank=False, default='0')
    com_service = models.IntegerField(null=False, blank=False, default='0')
    total = models.IntegerField(null=False, blank=False, default='0')


class total(models.Model):
    student_id = models.CharField(default=" ", max_length=15, primary_key=True)
    moocs = models.IntegerField(null=False, blank=False, default='0')
    tech_fest = models.IntegerField(null=False, blank=False, default='0')
    rural_reporting = models.IntegerField(null=False, blank=False, default='0')
    tree_planting = models.IntegerField(null=False, blank=False, default='0')
    part_relief_camps = models.IntegerField(
        null=False, blank=False, default='0')
    part_tech_quiz = models.IntegerField(null=False, blank=False, default='0')
    public_writing_editing = models.IntegerField(
        null=False, blank=False, default='0')
    publication = models.IntegerField(null=False, blank=False, default='0')
    research_publications = models.IntegerField(
        null=False, blank=False, default='0')
    innovative_projects = models.IntegerField(
        null=False, blank=False, default='0')
    blodd = models.IntegerField(null=False, blank=False, default='0')
    sports = models.IntegerField(null=False, blank=False, default='0')
    cultural_programme = models.IntegerField(
        null=False, blank=False, default='0')
    member_prof_society = models.IntegerField(
        null=False, blank=False, default='0')
    student_chapter = models.IntegerField(null=False, blank=False, default='0')
    industry_visit = models.IntegerField(null=False, blank=False, default='0')
    photography = models.IntegerField(null=False, blank=False, default='0')
    yoga_camp = models.IntegerField(null=False, blank=False, default='0')
    entrepreneur = models.IntegerField(null=False, blank=False, default='0')
    adventure_sports = models.IntegerField(
        null=False, blank=False, default='0')
    training_privileged = models.IntegerField(
        null=False, blank=False, default='0')
    com_service = models.IntegerField(null=False, blank=False, default='0')
    total = models.IntegerField(null=False, blank=False, default='0')
