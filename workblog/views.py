from django.shortcuts import render,HttpResponse,get_object_or_404,HttpResponseRedirect,redirect,Http404
from workblog.models import *
from django.contrib import messages
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.db.models import Q
import string
import xlsxwriter
import os
from datetime import date
# Create your views here.
abc = string.ascii_lowercase

def workblog_index(request):

    workcharts_list = Workchart.objects.all()
    query = request.GET.get("q")
    if query:
        workcharts_list = workcharts_list.filter(
            Q(project__icontains=query) |
            Q(user__first_name__icontains=query) |
            Q(user__last_name__icontains=query) |
            Q(content__icontains=query)

        ).distinct()

    paginator = Paginator(workcharts_list, 15) # Show 15 contacts per page
    page = request.GET.get('page')
    try:
        workcharts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        workcharts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        workcharts = paginator.page(paginator.num_pages)

    return render(request, "workblog/index.html", {"workcharts": workcharts})

def workblog_detail(request,id):

    workcharts = get_object_or_404(Workchart,id=id)
    context = {"workcharts" : workcharts}
    return render(request, "workblog/detail.html", context )

def workblog_create(request):
    workcharts = Workchart
    if not request.user.is_authenticated:
        return Http404

    return render(request,"workblog/create.html", {"workcharts": workcharts})

def workblog_update(request,id):
    if not request.user.is_authenticated:
        return Http404

    workcharts = get_object_or_404(Workchart, id=id)

    return render(request,"workblog/update.html",{"workcharts": workcharts})

def workblog_delete(request,id):
    if not request.user.is_authenticated:
        return Http404
    workcharts = get_object_or_404(Workchart, id=id)
    workcharts.delete()
    messages.warning(request, "Workchart Silindi!", extra_tags='alert alert-warning alert-dismissible')
    return HttpResponseRedirect("/workblog/index")

def workblog_addtodb(request):
    if request.user.is_authenticated:
        userid = request.user
    if request.method == "GET":
        redirect("index")
    else:
        datetime = request.POST.get("datetime")
        content = str(request.POST.getlist("content"))
        section = request.POST.get("section")
        projectpart = str(request.POST.getlist("projectpart"))
        projectpart = projectpart.replace("[", "")
        projectpart = projectpart.replace("]", "")
        projectpart = projectpart.replace("'", "")
        content = content.replace("[", "")
        content = content.replace("]", "")
        content = content.replace("'", "")

        project = request.POST.get("project")
        newworkchart = Workchart(datetime=datetime,content=content,section=section, projectpart=projectpart, project=project, user=userid)
        newworkchart.save()


        messages.success(request,"Başarılı Giriş!", extra_tags='alert alert-success alert-dismissible')

        return HttpResponseRedirect("/workblog/create")

def workblog_updated(request,id):
    if not request.user.is_authenticated:
        return Http404

    workcharts = get_object_or_404(Workchart, id=id)
    content = str(request.POST.getlist("content"))
    projectpart = str(request.POST.getlist("projectpart"))
    projectpart = projectpart.replace("[", "")
    projectpart = projectpart.replace("]", "")
    projectpart = projectpart.replace("'", "")
    content = content.replace("[", "")
    content = content.replace("]", "")
    content = content.replace("'", "")
    workcharts.content = content
    workcharts.projectpart = projectpart
    workcharts.project = request.POST.get("project")

    workcharts.save()
    messages.success(request, "Değişiklik Başarıyla Gerçekleşti!", extra_tags='alert alert-success alert-dismissible')
    return HttpResponseRedirect("/workblog/index")

def workblog_export(request):
    if not request.user.is_superuser:
        return Http404
    desktop = os.path.join(os.path.join(os.environ["USERPROFILE"]),'Desktop')
    today = date.today()
    d1 = "/Bold-Workblog-"+str(today.strftime("%Y%m%d"))+".xlsx"
    workbook = xlsxwriter.Workbook(desktop+d1)
    worksheet = workbook.add_worksheet("Workblog")
    workcharts = Workchart.objects.all()
    items = []
    control = []
    for i in workcharts:
        k=[]
        r=""
        k.append(i.datetime)
        r = str(i.datetime) + r
        if i.section == "Öğleden Önce":
            r = "Öğleden Önce" + r
            k.append(3)
        else:
            r = "Öğleden Sonra" + r
            k.append(4)
        k.append(i.project)
        k.append(i.projectpart)
        k.append(i.content)
        k.append(i.user.get_full_name())
        r = i.user.get_full_name() + r
        control.append(r)
        items.append(k)
    for v,i in enumerate(control):
        c = control.count(i)
        items[v][1] = items[v][1]/c


    row = 1
    col = 0
    worksheet.write(0, 0, "Date Time")
    worksheet.write(0, 1, "Date Section")
    worksheet.write(0, 2, "Project")
    worksheet.write(0, 3, "Project Part")
    worksheet.write(0, 4, "Content")
    worksheet.write(0, 5, "Author")



    for datetime,section,project,projectpart,content,user in (items):
        worksheet.write(row, col,str(datetime))
        worksheet.write(row, col+1, section)
        worksheet.write(row, col+2, project)
        worksheet.write(row, col+3, projectpart)
        worksheet.write(row, col+4, content)
        worksheet.write(row, col+5, user)
        row += 1
    workbook.close()
    return HttpResponseRedirect("/workblog/index")