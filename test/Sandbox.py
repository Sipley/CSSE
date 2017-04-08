import datetime
import math
import calendar

stars = ['Alpheratz', 'Ankaa', 'Schedar', 'Diphda', 'Achernar', 'Hamal', 'Polaris', 'Akamar', 'Menkar', 'Mirfak', 'Aldebaran', 'Rigel', 'Capella', 'Bellatrix', 'Elnath','Alnilam','Betelgeuse','Canopus','Sirius','Adara','Procyon','Pollux','Avior','Suhail','Miaplacidus','Alphard','Regulus','Dubhe','Denebola','Gienah','Acrux','Gacrux','Alioth','Spica','Alcaid','Hadar','Menkent','Arcturus','Rigil Kent.','Zubenelg.','Kochab','Alphecca','Antares','Atria','Sabik','Shaula','Rasalhague','Etamin','Kaus Aust.','Vega','Nunki','Altair','Peacock','Deneb','Enif','Alnair','Fomalhaut','Scheat','Markab']
declination= ['29d10.9','-42d13.4','56d37.7','-17d54.1','-57d09.7','23d32.3','89d20.1','-40d14.8','4d09.0','49d55.1','16d32.3','-8d11.3','46d00.7','6d21.6','28d37.1','-1d11.8','7d24.3','-52d42.5','-16d44.3','-28d59.9','5d10.9','27d59.0','-59d33.7','-43d29.8','-69d46.9','-8d43.8','11d53.2','61d39.5','14d28.9','-17d37.7','-63d10.9','-57d11.9','55d52.1','-11d14.5','49d13.8','-60d26.6','-36d26.6','19d06.2','-60d53.6','-16d06.3','74d05.2','26d39.7','-26d27.8','-69d03.0','-15d44.4','-37d06.6','12d33.1','51d29.3','-34d22.4','38d48.1','-26d16.4','8d54.8','-56d41.0','45d20.5','9d57.0','-46d53.1','-29d32.3','28d10.3','15d17.6']

print stars
print stars.index('Ankaa')

def convertAngleFromDeg(angle):
    degree = angle.split('d')[0]
    arcminute = float(angle.split('d')[1])/60
    convertedAngle = float(degree) + arcminute
    if '-' in degree:
        convertedAngle = -convertedAngle
    return convertedAngle

def convertAngleToDeg(angle):
    angle = str(angle)
    degree = angle.split('.')[0]
    arcminute = round((abs(float(angle)) - abs(int(degree)))*60,1)
    convertedAngle = str(degree)+'d'+str(arcminute)
    return convertedAngle

values = {'date':'2016-01-17', 'time':'03:15:42'}
if 'date' in values:
    date = values['date']
    GHAaries = '100d42.6'
    GHAariesAnnualDecrease = '-0d14.31667'
    refYear = 2001
    obsYear = datetime.datetime.strptime(date,'%Y-%m-%d').year
    diffYear = obsYear - refYear
    cumProgression = diffYear * convertAngleFromDeg(GHAariesAnnualDecrease)
    print cumProgression

numLeapYear = 0
for year in range(refYear,obsYear):
    if calendar.isleap(year):
        numLeapYear += 1
print numLeapYear
rotPeriod = 86164.1
clockPeriod = 86400
dailyDeg = convertAngleFromDeg('360d0.00')
dailyRot = abs(dailyDeg-(rotPeriod/clockPeriod*dailyDeg))
totalLeapProg = numLeapYear * dailyRot
GHAariesObs = convertAngleFromDeg(GHAaries) + cumProgression + totalLeapProg

time = values['time']
refDate = str(obsYear) + '-01-01' + ' ' + '00:00:00'
obsDate = date + ' ' + time
refDateDate = datetime.datetime.strptime(refDate, '%Y-%m-%d %H:%M:%S')
obsDateDate = datetime.datetime.strptime(obsDate, '%Y-%m-%d %H:%M:%S')
deltaSeconds = (obsDateDate-refDateDate).total_seconds()

amtRot = deltaSeconds/rotPeriod * 360
while amtRot > 360:
    amtRot = amtRot - 360

GHAariesTotal = convertAngleToDeg(GHAariesObs + amtRot)
print GHAariesTotal

GHAstar = GHAariesTotal + SHA

