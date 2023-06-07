from django.shortcuts import render
from .models import Device, Issue
from .forms import DeviceForm, IssueForm
from django.views.generic import ListView
from django.core.exceptions import PermissionDenied
from django.http import HttpResponseRedirect
from django.http import HttpResponseNotFound
from cart.forms import CartIssueAddForm
# def index(request):
#     return render(request, 'services/mainPage.html')


def services(request):
    devices = Device.objects.all()

    return render(request, 'services/ourServices.html', {'devices': devices})


class all_devices_view(ListView):
    model = Device
    template_name = 'services/mainPage.html'
    context_object_name = 'devices'

def create(request):

    if request.method == 'POST':
        form = DeviceForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            error = 'MISTAKE'

    form = DeviceForm()

    data = {
        'form': form,

    }
    return render(request, 'services/create.html',data)


def create_issue(request):
    if not request.user.is_staff:
        raise PermissionDenied("Net dostupa")

    if request.method == 'POST':
        form = IssueForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            error = 'MISTAKE'

    form = IssueForm()

    data = {
        'form': form,

    }
    return render(request, 'services/create_issue.html', data)

def issue_edit(request,id):
    if not request.user.is_staff:
        raise PermissionDenied("Net dostupa")
    try:
        issue = Issue.objects.get(id=id) # problem because id - device-id

        form = IssueForm(initial={'issue_type': issue.issue_type, 'price': issue.price,
                                 'device_type': issue.device_type})

        if request.method == "POST":
            issue.title = request.POST.get('issue_type')
            print(request.POST.get('title'))
            issue.price = request.POST.get('price')
            issue.device_type = Device.objects.get(id=request.POST.get('device_type'))

            issue.save()
            return HttpResponseRedirect("/")
        else:
            return render(request, "services/edit.html", {"issue": issue, 'form': form})
    except issue.DoesNotExist:
        return HttpResponseNotFound("<h2>book not found</h2>")


def detail(request, id):
    device = Device.objects.get(id=id)
    issues = Issue.objects.filter(device_type__name=device.name)
    cart_form = CartIssueAddForm()

    sort_t = request.GET.get('sort')

    if (str(sort_t) == 'ascending'):
        issues = issues.order_by('price')
    elif (str(sort_t) == 'descending'):
        issues = issues.order_by('-price')


    data = {
        'device': device,
        'issues': issues,
        'cart_form':cart_form
    }
    return render(request, 'services/details.html', data)