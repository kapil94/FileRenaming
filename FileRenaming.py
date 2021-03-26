import os,re,shutil,random



filename=['sample_file_']
date_list=['01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31']
month_list=['01','02','03','04','05','06','07','08','09','10','11','12']
months_with_31=['01','03','05','07','08','10','12']
months_with_30=['04','06','09','11']
path='/home/user/Desktop/Files'
os.chdir(path)
my_dict={}


# To create random sample files with dates in order DD-MM-YYYY



random_number=0

file_name=""

for i in range(0,100):
	random_number=int(random.choice(date_list))
	if random_number==31:
		file_name+=filename[0]+'31'+'-'+random.choice(months_with_31)+'-2021.txt'
		if file_name in os.listdir():
			file_name=""
			continue
		else:
			file_obj=open(os.path.join(path,file_name),'x')
			file_obj.close()
		file_name=""

	elif random_number==30:
	
		file_name+=filename[0]+'30'+'-'+random.choice(months_with_30)+'-2021.txt'
		if file_name in os.listdir():
			file_name=""
			continue
		else:
			file_obj=open(os.path.join(path,file_name),'x')
			file_obj.close()
		file_name=""
		
	elif random_number<10:
		file_name+=filename[0]+'0'+str(random_number)+'-'+random.choice(month_list)+'-2021.txt'
		
		if file_name in os.listdir():
			file_name=""
			continue
		else:
			file_obj=open(os.path.join(path,file_name),'x')
			file_obj.close()
		file_name=""
	else:
		file_name+=filename[0]+str(random_number)+'-'+random.choice(month_list)+'-2021.txt'
		
		if file_name in os.listdir():
			file_name=""
			continue
		else:
			file_obj=open(os.path.join(path,file_name),'x')
			file_obj.close()
		file_name=""


############################################# To Rename Files from Filename_DD-MM-YYYY to Filename_MM-DD-YYYY #########################

date_split=[]
month_split=[]
li=[]
changed_date=""
count=1
# To check if files of pattern File_name_DD-MM-YYYY exists
RegexPattern=re.compile(r'\w+\-+\w+\-+\w+.txt$')

for file in os.listdir():
	month_split=RegexPattern.findall(file)[0].split('-')
	for i in range(0,len(month_split)):
		date_split=month_split[0].split('_')
	month_split.insert(2,date_split[2])
	month_split.pop(0)
	date_str=""
	for i in range(0,len(date_split)-1):
		date_str+=date_split[i]
		date_str+='_'
     
	month_split.insert(0,date_str)
	
	for i in range(0,2):
		changed_date+=month_split[i]
	
	for i in range(2,len(month_split)-1):
		changed_date+='-'
		changed_date+=month_split[i]
		changed_date+='-'
		
	changed_date+=month_split[len(month_split)-1]
	changed_date+=" "

	li=changed_date.split(" ")
	while "" in li:
		li.remove("")

	for i in range(0,len(li)):
		my_dict[file]=li[i]


# Renaming the Filename_DD-MM-YYYY to Filename_MM-DD-YYYY

for key in my_dict.keys():
	shutil.move(os.path.join(path,key),os.path.join(path,my_dict[key]))


