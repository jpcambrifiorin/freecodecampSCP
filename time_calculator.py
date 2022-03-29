days_list = ["monday",'tuesday','wednesday','thursday','fryday','saturday','sunday']

def add_time(cTime,aTime,cDay=None):
  dayCount=0
  # mN = AM=0, PM=1
  mN=0
  hour,mornig=cTime.split()
  if mornig=='PM':
    mN=1
  hour,minute=hour.split(':')
  hour,minute=int(hour),int(minute)
  addH,addM=aTime.split(':')
  addH,addM=int(addH),int(addM)
  
  mRes=minute+addM
  hRes=hour+addH+int(mRes/60)
  mRes=int(mRes%60)
  dayCount=int(mN+int(hRes/12))/2
  mN=int(mN+int(hRes/12))%2
  hRes=int(hRes)%12

  dayPhrase=""
  if cDay is not None:
    modDay = int((days_list.index(cDay.lower())+dayCount)%7)
    dayPhrase=f", {days_list[modDay]}"
  
  if dayCount==1:
    dayPhrase=dayPhrase+" (next day)"
  elif dayCount>1:
    dayPhrase=dayPhrase+f" ({int(dayCount)} days later)"

  return f"{hRes:02}:{mRes:02} {'PM' if mN==1 else 'AM'}"+dayPhrase

x = add_time("11:43 PM", "24:20", "tueSday")
print(x)