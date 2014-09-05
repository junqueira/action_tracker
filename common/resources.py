from tastypie.resources import ModelResource
from tastypie.authorization import Authorization
from apps.centre.models import Centre
from apps.imageresource.models import ImageResource
from apps.pdfresource.models import PDFResource
from apps.employee.models import Employee
from apps.request.models import Request
from apps.shift.models import Shift
from apps.breaks.models import Break
from apps.checklistresource.models import Checklist, ChecklistQuestion
from django.contrib.auth.models import User
from apps.reports.models import Report
from tastypie  import fields


class CentreResource (ModelResource):
    """ Centre webservice
    """
    class Meta:
        queryset = Centre.objects.all()
        resource_name = 'centreresource'
        authorization = Authorization()

class ImageResourceResource (ModelResource):
    """ Image resource webservice
    """
    class Meta:
        queryset = ImageResource.objects.all()
        resource_name = 'imageresource'
        authorization = Authorization()

class PDFResourceResource (ModelResource):
    """ Image resource webservice
    """
    class Meta:
        queryset = PDFResource.objects.all()
        resource_name = 'pdfresource'
        authorization = Authorization()

class UserResource (ModelResource):
    """ User webservice
    """
    class Meta:
        queryset = User.objects.all()
        resource_name = 'userresource'
        authorization = Authorization()


class EmployeeResource (ModelResource):
    """ Employee webservice
    """
    user = fields.ForeignKey(UserResource,'user',full=True,null=False,blank=False)

    class Meta:
        queryset = Employee.objects.all()
        resource_name = 'employeeresource'
        authorization = Authorization()

class RequestResource (ModelResource):
    """ Request webservice
    """
    class Meta:
        queryset = Request.objects.all()
        resource_name = 'requestresource'
        authorization = Authorization()

class ShiftResource (ModelResource):
    """ Shift webservice
    """
    class Meta:
        queryset = Shift.objects.all()
        resource_name = 'shiftresource'
        authorization = Authorization()

class BreakResource (ModelResource):
    """ Break webservice
    """
    class Meta:
        queryset = Break.objects.all()
        resource_name = 'breakresource'
        authorization = Authorization()



class ChecklistResource (ModelResource):
    """ Checklist webservice
    """
    class Meta:
        queryset = Checklist.objects.all()
        resource_name = 'checklistresource'
        authorization = Authorization()


class ChecklistQuestionResource (ModelResource):
    """ Checklist webservice
    """
    class Meta:
        queryset = ChecklistQuestion.objects.all()
        resource_name = 'checklistquestionresource'
        authorization = Authorization()

class ReportResource (ModelResource):
    """ Report webservice
    """
    class Meta:
        queryset = Report.objects.all()
        resource_name = 'reportresource'
        authorization = Authorization()

