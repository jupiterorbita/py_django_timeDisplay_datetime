from django.shortcuts import render
import datetime
from django.utils import timezone
from time import gmtime, strftime

def index(request):
  print('\n ENTERED ROUTE -------> / \n')
  nowDatetime = datetime.datetime.now()
  nowTimezone = timezone.now()
  
  context = {
    "time1" : strftime("%Y-%b.-%d %H:%M %p", gmtime()),
    "date" : strftime("%b. %d, %Y", gmtime()),
    "time" : strftime("%I:%M %p", gmtime()),
    "datetimeNow" : nowDatetime,
    "timezoneNow" : nowTimezone
  }
  
  return render(request, 'index.html', context)
