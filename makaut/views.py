import json
import csv
import io
from PIL import ImageFont, ImageDraw, Image
from django.shortcuts import render, redirect
from django.http import *
from django.contrib.auth.models import User
from django.contrib import auth
from django.core.exceptions import *
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy

from .models import *
from accounts.views import message
from students.addons import get_idcard_details
from students.models import Student
from teachers.models import Teacher
from teachers.addons import (get_teach_details)

@login_required(login_url=reverse_lazy('login'))
def student_report(request):
    if Student.objects.filter(id=request.user.username):
        title = "404"
        error = ['Students cannot view this page!']
        return message(title, error, request)

    if request.method == "POST":
        student_id = request.POST.get('student_id',  '')
        mentor_id = request.user.username

        sems_all_object = semester_1.objects.filter(student_id=student_id)
        length = len(sems_all_object)
        std = Student.objects.filter(id=student_id)

        sem1 = semester_1.objects.filter(student_id=student_id)
        sem2 = semester_2.objects.filter(student_id=student_id)
        sem3 = semester_3.objects.filter(student_id=student_id)
        sem4 = semester_4.objects.filter(student_id=student_id)
        sem5 = semester_5.objects.filter(student_id=student_id)
        sem6 = semester_6.objects.filter(student_id=student_id)
        sem7 = semester_7.objects.filter(student_id=student_id)
        sem8 = semester_8.objects.filter(student_id=student_id)
        total_table = total.objects.filter(student_id=student_id)

        # sem1_list=sem1.values()
        # to check wether the student in new or not
        total_marks = 0
        for i in total_table:
            total_marks = i.total

        for cert in std:
            certificate = cert.has_certificate    
        new_entry = 0
        if len(sem1) == 0:
            p1 = semester_1.objects.create(student_id=student_id)
        if len(sem2) == 0:
            p2 = semester_2.objects.create(student_id=student_id)
        if len(sem3) == 0:
            p3 = semester_3.objects.create(student_id=student_id)
        if len(sem4) == 0:
            p4 = semester_4.objects.create(student_id=student_id)
        if len(sem5) == 0:
            p5 = semester_5.objects.create(student_id=student_id)
        if len(sem6) == 0:
            p6 = semester_6.objects.create(student_id=student_id)
        if len(sem7) == 0:
            p7 = semester_7.objects.create(student_id=student_id)
        if len(sem8) == 0:
            p8 = semester_8.objects.create(student_id=student_id)
        if len(total_table) == 0:
            p_total = total.objects.create(student_id=student_id)
            new_entry = 1
        details = get_idcard_details(student_id)
        d =  get_teach_details(request)
        print(certificate)
        a = {
            'certificate' : certificate,
            'total_marks' : int(total_marks),
            'info_student': std,
            'mentor': mentor_id,
            'check': "0",
            'sem1': sem1,
            'sem2': sem2,
            'sem3': sem3,
            'sem4': sem4,
            'sem5': sem5,
            'sem6': sem6,
            'sem7': sem7,
            'sem8': sem8,
            'total': total_table,
            'new_entry': new_entry,
        }
        a.update(details)
        a.update(d)
        return render(request, 'makaut/student_view.html', a)
    else: # GET request redirects
        return mentees(request)


@login_required(login_url=reverse_lazy('login'))
def mentees(request):
    if Student.objects.filter(id=request.user.username):
        title = "404"
        error = ['Students cannot view this page!']
        return message(title, error, request)
    mentor_id = request.user.username
    ment = Teacher.objects.get(id=mentor_id)
    student_obj = Student.objects.filter(mentor=mentor_id)
    d =  get_teach_details(request)
    d['mentor'] = mentor_id
    d['info'] = student_obj[:]
    d['check'] = "0"
    return render(request, 'makaut/mentees.html', d)

@login_required(login_url=reverse_lazy('login'))
def update(request):
    if Student.objects.filter(id=request.user.username):
        title = "404"
        error = ['Students cannot view this page!']
        return message(title, error, request)
    
    if request.method == 'POST' and request.is_ajax():
        (sem1_total,sem2_total, sem3_total,sem4_total,sem5_total,sem6_total,sem7_total,sem8_total) = (0,0,0,0,0,0,0,0)
        student_id = request.POST['student_id'].strip()
        sem1 = [int(i) for i in json.loads(request.POST['sem1'])]
        sem2 = [int(i) for i in json.loads(request.POST['sem2'])]
        sem3 = [int(i) for i in json.loads(request.POST['sem3'])]
        sem4 = [int(i) for i in json.loads(request.POST['sem4'])]
        sem5 = [int(i) for i in json.loads(request.POST['sem5'])]
        sem6 = [int(i) for i in json.loads(request.POST['sem6'])]
        sem7 = [int(i) for i in json.loads(request.POST['sem7'])]
        sem8 = [int(i) for i in json.loads(request.POST['sem8'])]
        total_rq = [int(i) for i in json.loads(request.POST['total'])]
        SEM1 = semester_1.objects.get(student_id=student_id)
        SEM2 = semester_2.objects.get(student_id=student_id)
        SEM3 = semester_3.objects.get(student_id=student_id)
        SEM4 = semester_4.objects.get(student_id=student_id)
        SEM5 = semester_5.objects.get(student_id=student_id)
        SEM6 = semester_6.objects.get(student_id=student_id)
        SEM7 = semester_7.objects.get(student_id=student_id)
        SEM8 = semester_8.objects.get(student_id=student_id)
        total_obj = total.objects.get(student_id=student_id)

        for i in sem1:
            sem1_total = sem1_total + i
        for i in sem2:
            sem2_total = sem2_total + i
        for i in sem3:
            sem3_total = sem3_total + i
        for i in sem4:
            sem4_total = sem4_total + i
        for i in sem5:
            sem5_total = sem5_total + i
        for i in sem6:
            sem6_total = sem6_total + i
        for i in sem7:
            sem7_total = sem7_total + i
        for i in sem8:
            sem8_total = sem8_total + i                            
        if(sem1_total+sem2_total <= 30 and sem3_total+sem4_total <= 30 and sem5_total+sem6_total <= 30 and sem7_total+sem8_total <= 30):
        # total
            total_obj.moocs = total_rq[0]
            total_obj.tech_fest = total_rq[1]
            total_obj.rural_reporting = total_rq[2]
            total_obj.tree_planting = total_rq[3]
            total_obj.part_relief_camps = total_rq[4]
            total_obj.part_tech_quiz = total_rq[5]
            total_obj.public_writing_editing = total_rq[6]
            total_obj.publication = total_rq[7]
            total_obj.research_publications = total_rq[8]
            total_obj.innovative_projects = total_rq[9]
            total_obj.blodd = total_rq[10]
            total_obj.sports = total_rq[11]
            total_obj.cultural_programme = total_rq[12]
            total_obj.member_prof_society = total_rq[13]
            total_obj.student_chapter = total_rq[14]
            total_obj.industry_visit = total_rq[15]
            total_obj.photography = total_rq[16]
            total_obj.yoga_camp = total_rq[17]
            total_obj.entrepreneur = total_rq[18]
            total_obj.adventure_sports = total_rq[19]
            total_obj.training_privileged = total_rq[20]
            total_obj.com_service = total_rq[21]
            # total_rq[22] contains the all over total marks in every fields
            total_obj.total = total_rq[22]

            # SEM1
            SEM1.moocs_for_12 = sem1[0]
            SEM1.moocs_for_8 = sem1[1]
            SEM1.tech_fest_organizer = sem1[2]
            SEM1.tech_fest_participant = sem1[3]
            SEM1.rural_reporting = sem1[4]
            SEM1.tree_planting = sem1[5]
            SEM1.part_relief_camps = sem1[6]
            SEM1.part_tech_quiz = sem1[7]
            SEM1.public_editing = sem1[8]
            SEM1.public_writting = sem1[9]
            SEM1.publication = sem1[10]
            SEM1.research_publications = sem1[11]
            SEM1.innovative_projects = sem1[12]
            SEM1.blodd_donation = sem1[13]
            SEM1.blood_organization = sem1[14]
            SEM1.sports_college = sem1[15]
            SEM1.sports_university = sem1[16]
            SEM1.sports_district = sem1[17]
            SEM1.sports_state = sem1[18]
            SEM1.sports_national = sem1[19]
            SEM1.cultural_programme = sem1[20]
            SEM1.member_prof_society = sem1[2]
            SEM1.student_chapter = sem1[22]
            SEM1.industry_visit = sem1[23]
            SEM1.photography = sem1[24]
            SEM1.yoga_camp = sem1[25]
            SEM1.entrepreneur = sem1[26]
            SEM1.adventure_sports = sem1[27]
            SEM1.training_privileged = sem1[28]
            SEM1.com_service = sem1[29]
            
            # SEM2
            SEM2.moocs_for_12 = sem2[0]
            SEM2.moocs_for_8 = sem2[1]
            SEM2.tech_fest_organizer = sem2[2]
            SEM2.tech_fest_participant = sem2[3]
            SEM2.rural_reporting = sem2[4]
            SEM2.tree_planting = sem2[5]
            SEM2.part_relief_camps = sem2[6]
            SEM2.part_tech_quiz = sem2[7]
            SEM2.public_editing = sem2[8]
            SEM2.public_writting = sem2[9]
            SEM2.publication = sem2[10]
            SEM2.research_publications = sem2[11]
            SEM2.innovative_projects = sem2[12]
            SEM2.blodd_donation = sem2[13]
            SEM2.blood_organization = sem2[14]
            SEM2.sports_college = sem2[15]
            SEM2.sports_university = sem2[16]
            SEM2.sports_district = sem2[17]
            SEM2.sports_state = sem2[18]
            SEM2.sports_national = sem2[19]
            SEM2.cultural_programme = sem2[20]
            SEM2.member_prof_society = sem2[2]
            SEM2.student_chapter = sem2[22]
            SEM2.industry_visit = sem2[23]
            SEM2.photography = sem2[24]
            SEM2.yoga_camp = sem2[25]
            SEM2.entrepreneur = sem2[26]
            SEM2.adventure_sports = sem2[27]
            SEM2.training_privileged = sem2[28]
            SEM2.com_service = sem2[29]

            # SEM3
            SEM3.moocs_for_12 = sem3[0]
            SEM3.moocs_for_8 = sem3[1]
            SEM3.tech_fest_organizer = sem3[2]
            SEM3.tech_fest_participant = sem3[3]
            SEM3.rural_reporting = sem3[4]
            SEM3.tree_planting = sem3[5]
            SEM3.part_relief_camps = sem3[6]
            SEM3.part_tech_quiz = sem3[7]
            SEM3.public_editing = sem3[8]
            SEM3.public_writting = sem3[9]
            SEM3.publication = sem3[10]
            SEM3.research_publications = sem3[11]
            SEM3.innovative_projects = sem3[12]
            SEM3.blodd_donation = sem3[13]
            SEM3.blood_organization = sem3[14]
            SEM3.sports_college = sem3[15]
            SEM3.sports_university = sem3[16]
            SEM3.sports_district = sem3[17]
            SEM3.sports_state = sem3[18]
            SEM3.sports_national = sem3[19]
            SEM3.cultural_programme = sem3[20]
            SEM3.member_prof_society = sem3[2]
            SEM3.student_chapter = sem3[22]
            SEM3.industry_visit = sem3[23]
            SEM3.photography = sem3[24]
            SEM3.yoga_camp = sem3[25]
            SEM3.entrepreneur = sem3[26]
            SEM3.adventure_sports = sem3[27]
            SEM3.training_privileged = sem3[28]
            SEM3.com_service = sem3[29]

            # SEM4
            SEM4.moocs_for_12 = sem4[0]
            SEM4.moocs_for_8 = sem4[1]
            SEM4.tech_fest_organizer = sem4[2]
            SEM4.tech_fest_participant = sem4[3]
            SEM4.rural_reporting = sem4[4]
            SEM4.tree_planting = sem4[5]
            SEM4.part_relief_camps = sem4[6]
            SEM4.part_tech_quiz = sem4[7]
            SEM4.public_editing = sem4[8]
            SEM4.public_writting = sem4[9]
            SEM4.publication = sem4[10]
            SEM4.research_publications = sem4[11]
            SEM4.innovative_projects = sem4[12]
            SEM4.blodd_donation = sem4[13]
            SEM4.blood_organization = sem4[14]
            SEM4.sports_college = sem4[15]
            SEM4.sports_university = sem4[16]
            SEM4.sports_district = sem4[17]
            SEM4.sports_state = sem4[18]
            SEM4.sports_national = sem4[19]
            SEM4.cultural_programme = sem4[20]
            SEM4.member_prof_society = sem4[2]
            SEM4.student_chapter = sem4[22]
            SEM4.industry_visit = sem4[23]
            SEM4.photography = sem4[24]
            SEM4.yoga_camp = sem4[25]
            SEM4.entrepreneur = sem4[26]
            SEM4.adventure_sports = sem4[27]
            SEM4.training_privileged = sem4[28]
            SEM4.com_service = sem4[29]

            # SEM5
            SEM5.moocs_for_12 = sem5[0]
            SEM5.moocs_for_8 = sem5[1]
            SEM5.tech_fest_organizer = sem5[2]
            SEM5.tech_fest_participant = sem5[3]
            SEM5.rural_reporting = sem5[4]
            SEM5.tree_planting = sem5[5]
            SEM5.part_relief_camps = sem5[6]
            SEM5.part_tech_quiz = sem5[7]
            SEM5.public_editing = sem5[8]
            SEM5.public_writting = sem5[9]
            SEM5.publication = sem5[10]
            SEM5.research_publications = sem5[11]
            SEM5.innovative_projects = sem5[12]
            SEM5.blodd_donation = sem5[13]
            SEM5.blood_organization = sem5[14]
            SEM5.sports_college = sem5[15]
            SEM5.sports_university = sem5[16]
            SEM5.sports_district = sem5[17]
            SEM5.sports_state = sem5[18]
            SEM5.sports_national = sem5[19]
            SEM5.cultural_programme = sem5[20]
            SEM5.member_prof_society = sem5[2]
            SEM5.student_chapter = sem5[22]
            SEM5.industry_visit = sem5[23]
            SEM5.photography = sem5[24]
            SEM5.yoga_camp = sem5[25]
            SEM5.entrepreneur = sem5[26]
            SEM5.adventure_sports = sem5[27]
            SEM5.training_privileged = sem5[28]
            SEM5.com_service = sem5[29]

            # SEM6
            SEM6.moocs_for_12 = sem6[0]
            SEM6.moocs_for_8 = sem6[1]
            SEM6.tech_fest_organizer = sem6[2]
            SEM6.tech_fest_participant = sem6[3]
            SEM6.rural_reporting = sem6[4]
            SEM6.tree_planting = sem6[5]
            SEM6.part_relief_camps = sem6[6]
            SEM6.part_tech_quiz = sem6[7]
            SEM6.public_editing = sem6[8]
            SEM6.public_writting = sem6[9]
            SEM6.publication = sem6[10]
            SEM6.research_publications = sem6[11]
            SEM6.innovative_projects = sem6[12]
            SEM6.blodd_donation = sem6[13]
            SEM6.blood_organization = sem6[14]
            SEM6.sports_college = sem6[15]
            SEM6.sports_university = sem6[16]
            SEM6.sports_district = sem6[17]
            SEM6.sports_state = sem6[18]
            SEM6.sports_national = sem6[19]
            SEM6.cultural_programme = sem6[20]
            SEM6.member_prof_society = sem6[2]
            SEM6.student_chapter = sem6[22]
            SEM6.industry_visit = sem6[23]
            SEM6.photography = sem6[24]
            SEM6.yoga_camp = sem6[25]
            SEM6.entrepreneur = sem6[26]
            SEM6.adventure_sports = sem6[27]
            SEM6.training_privileged = sem6[28]
            SEM6.com_service = sem6[29]

            # SEM7
            SEM7.moocs_for_12 = sem7[0]
            SEM7.moocs_for_8 = sem7[1]
            SEM7.tech_fest_organizer = sem7[2]
            SEM7.tech_fest_participant = sem7[3]
            SEM7.rural_reporting = sem7[4]
            SEM7.tree_planting = sem7[5]
            SEM7.part_relief_camps = sem7[6]
            SEM7.part_tech_quiz = sem7[7]
            SEM7.public_editing = sem7[8]
            SEM7.public_writting = sem7[9]
            SEM7.publication = sem7[10]
            SEM7.research_publications = sem7[11]
            SEM7.innovative_projects = sem7[12]
            SEM7.blodd_donation = sem7[13]
            SEM7.blood_organization = sem7[14]
            SEM7.sports_college = sem7[15]
            SEM7.sports_university = sem7[16]
            SEM7.sports_district = sem7[17]
            SEM7.sports_state = sem7[18]
            SEM7.sports_national = sem7[19]
            SEM7.cultural_programme = sem7[20]
            SEM7.member_prof_society = sem7[2]
            SEM7.student_chapter = sem7[22]
            SEM7.industry_visit = sem7[23]
            SEM7.photography = sem7[24]
            SEM7.yoga_camp = sem7[25]
            SEM7.entrepreneur = sem7[26]
            SEM7.adventure_sports = sem7[27]
            SEM7.training_privileged = sem7[28]
            SEM7.com_service = sem7[29]

            # SEM8
            SEM8.moocs_for_12 = sem8[0]
            SEM8.moocs_for_8 = sem8[1]
            SEM8.tech_fest_organizer = sem8[2]
            SEM8.tech_fest_participant = sem8[3]
            SEM8.rural_reporting = sem8[4]
            SEM8.tree_planting = sem8[5]
            SEM8.part_relief_camps = sem8[6]
            SEM8.part_tech_quiz = sem8[7]
            SEM8.public_editing = sem8[8]
            SEM8.public_writting = sem8[9]
            SEM8.publication = sem8[10]
            SEM8.research_publications = sem8[11]
            SEM8.innovative_projects = sem8[12]
            SEM8.blodd_donation = sem8[13]
            SEM8.blood_organization = sem8[14]
            SEM8.sports_college = sem8[15]
            SEM8.sports_university = sem8[16]
            SEM8.sports_district = sem8[17]
            SEM8.sports_state = sem8[18]
            SEM8.sports_national = sem8[19]
            SEM8.cultural_programme = sem8[20]
            SEM8.member_prof_society = sem8[2]
            SEM8.student_chapter = sem8[22]
            SEM8.industry_visit = sem8[23]
            SEM8.photography = sem8[24]
            SEM8.yoga_camp = sem8[25]
            SEM8.entrepreneur = sem8[26]
            SEM8.adventure_sports = sem8[27]
            SEM8.training_privileged = sem8[28]
            SEM8.com_service = sem8[29]

            SEM1.save()
            SEM2.save()
            SEM3.save()
            SEM4.save()
            SEM5.save()
            SEM6.save()
            SEM7.save()
            SEM8.save()
            total_obj.save()
            if(total_rq[22] >= 100):
                cert = 1;
            else:
                cert = 0;    
            return JsonResponse({'success':'1','cert':cert })
        else:
            return HttpResponse("A student cannot get more than 30 marks in a year.")
    # d =  get_teach_details(request)
    # d['title'] = "M.A.R. Update"
    # d['student_id'] = student_id
    # return render(request, 'makaut/mentees.html', d)
    return HttpResponse("Change is done successfully!!!")

@login_required(login_url=reverse_lazy('login'))
def certificate(request, x, y, z):
    student_id = x
    cert_name = ''
    info ={}
    teach = Teacher.objects.get(id=request.user.username)
    #print(student_id)
    #print(mentor_id)
    img=Image.open(r'C:\Users\SWARNAVA\Desktop\project_nstc\media\certificates\original.png')
    std = Student.objects.filter(id=student_id)
    if(True):
        total_table = total.objects.filter(student_id=student_id)
        for i in std:
            if i.middle_name != 'NULL':
                std_name = i.name +" "+i.middle_name +" "+ i.surname
            else:
                std_name = i.name +" "+ i.surname
            univ_roll_no = i.univ_roll_no
            batch = i.batch[3:7]+"-"+i.batch[7:11]
            for k in total_table:
                total_mar = k.total
            teach_name = teach.name
            dept = teach.dept
            if dept == "CSE":
                stream = "Computer Science Engineering"
        font = ImageFont.truetype('arial.ttf', 20)
        font1 = ImageFont.truetype('arial.ttf', 16)
        draw = ImageDraw.Draw(img)
        draw.text(xy=(400,250),text=std_name,fill=(0,0,0),font=font)
        draw.text(xy=(330,295),text=univ_roll_no,fill=(0,0,0),font=font)
        draw.text(xy=(750,295),text=batch,fill=(0,0,0),font=font)
        draw.text(xy=(320,335),text=stream,fill=(0,0,0),font=font)
        draw.text(xy=(860,425),text=str(total_mar),fill=(0,0,0),font=font)
        draw.text(xy=(140,558),text=teach_name,fill=(89,89,89),font=font1)
        draw.text(xy=(200,579),text=dept,fill=(89,89,89),font=font1)
        draw.text(xy=(430,560),text="U-ID: "+student_id ,fill=(89,89,89),font=font)
        for i in student_id:
            if i != '/':
                cert_name = cert_name + i
            else:
                cert_name = cert_name + '_'
        img.save(r'C:\Users\SWARNAVA\Desktop\project_nstc\media\certificates\student_certificate\{}.png'.format(cert_name))
        info['cert_name'] = cert_name + '.png'
        # std.certificate = cert_name + '.png'
        # std.has_certificate = True
        # std.save()
    else:
        # info['cert_name'] = std.certificate  
        pass
    return render(request, "makaut/certificate.html/", info)

    # return render(request, 'teachers/int_marks_landing.html', {'fixed_footer': True})
    # return render(request, 'teachers/table.html')
    # return render(request, 'message.html', {'title': '404', 'error': True, 'fof': True})
    # data = Template('''{% load static %} <center>hello world<img src="{% static 'img/cert.png' %}" alt="Certificate Unavailable!" /></center>''')
    # return HttpResponse(data.render(Context(request)))    

@login_required(login_url=reverse_lazy('login'))
def gen_certificate(request):
    if request.method == "POST":
        student_id = request.POST.get('student_id',  '').strip()
        std = Student.objects.filter(id=student_id)
        info ={}
        for i in std:
            if(i.has_certificate == False):
                cert_name = ''
                teach = Teacher.objects.get(id=request.user.username)
                img=Image.open(r'C:\Users\SWARNAVA\Desktop\project_nstc\media\certificates\original.png')
                total_table = total.objects.filter(student_id=student_id)
               
                if i.middle_name != 'NULL':
                    std_name = i.name +" "+i.middle_name +" "+ i.surname
                else:
                    std_name = i.name +" "+ i.surname
                univ_roll_no = i.univ_roll_no
                batch = i.batch[3:7]+"-"+i.batch[7:11]
                for k in total_table:
                    total_mar = k.total
                teach_name = teach.name
                dept = teach.dept
                if dept == "CSE":
                    stream = "Computer Science Engineering"
                font = ImageFont.truetype('arial.ttf', 20)
                font1 = ImageFont.truetype('arial.ttf', 16)
                draw = ImageDraw.Draw(img)
                draw.text(xy=(400,250),text=std_name,fill=(0,0,0),font=font)
                draw.text(xy=(330,295),text=univ_roll_no,fill=(0,0,0),font=font)
                draw.text(xy=(750,295),text=batch,fill=(0,0,0),font=font)
                draw.text(xy=(320,335),text=stream,fill=(0,0,0),font=font)
                draw.text(xy=(860,425),text=str(total_mar),fill=(0,0,0),font=font)
                draw.text(xy=(140,558),text=teach_name,fill=(89,89,89),font=font1)
                draw.text(xy=(200,579),text=dept,fill=(89,89,89),font=font1)
                draw.text(xy=(430,560),text="U-ID: "+student_id ,fill=(89,89,89),font=font)
                for j in student_id:
                    print(j)
                    if j != '/':
                        cert_name = cert_name + j
                    else:
                        cert_name = cert_name + '_'
                print(cert_name)        
                img.save(r'C:\Users\SWARNAVA\Desktop\project_nstc\media\certificates\student_certificate\{}.png'.format(cert_name))
                info['cert_name'] = cert_name + '.png'
                info['status'] = "done"
                i.certificate = cert_name + '.png'
                i.has_certificate = True
                i.save()
            else:
                info['cert_name'] = i.certificate  
                info['status'] = "student has certificate"
        return JsonResponse(info)


