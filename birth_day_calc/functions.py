day_nos = {'0' : 'Sunday','1' : 'Monday','2' : 'Tuesday','3' : 'Wednesday','4' : 'Thursday','5' : 'Friday','6' : 'Saturday'}


#handling years above 2300
#if year > 2300:

#getting the leap year code:lyc
def leap_year_code(month,year):
	if month == '1' or '2' and year % 4 == 0:
		lyc = 1

	else:
		lyc = 0

	return lyc

#getting the century code:cc
def cent_code(year):
	if  year in range(1700,1799):
		cc = 4

	elif year in range(1800,1899):
		cc = 2

	elif year in range(1900,1999):
		cc = 0

	elif year in range(2000,2099):
		cc = 6

	elif year in range(2100,2199):
		cc = 4

	elif year in range(2200,2299):
		cc = 2

	elif year == 2300:
		cc = 0

	return cc

#getting the year code:yy
def year_code(year):
	if  year in range(1700,1799):
		yy = year - 1700

	elif year in range(1800,1899):
		yy = year - 1800

	elif year in range(1900,1999):
		yy = year - 1900

	elif year in range(2000,2099):
		yy = year - 2000

	elif year in range(2100,2199):
		yy = year - 2100

	elif year in range(2200,2299):
		yy = year - 2200

	elif year == 2300:
		year = 0

	else:
		print('The year you picked is out of the program\'s range')

	#finishing up the year code
	yy_sub = yy
	yy_sub //= 4
	yy += yy_sub
	yy %= 7

	return yy

def mth_code(month):
	mthcode = {'1':0,'2':3,'3':3,'4':6,'5':1,'6':4,'7':6,'8':2,'9':5,'10':0,'11':3,'12':5}
	mm = mthcode[str(month)]
	return mm

def day_calc(yy,mm,cc,lyc,day):
	ojo = yy + mm + cc + day - lyc
	ojo %= 7
	return day_nos[str(ojo)]

def main(year,month,day):
	yy = year_code(year)
	cc = cent_code(year)
	mm = mth_code(month)
	lyc = leap_year_code(month,year)
	return day_calc(yy,mm,cc,lyc,day)