from boto import ec2

#from django.http import HttpResponse
#def page (request) :
 #	return HttpResponse ("Hello world!" )

############# Global variable ##############
region_name='ap-southeast-1'
ec2_connection=ec2.connect_to_region(region_name)
vpc_connection=vpc.connect_to_region(region_name)

subnet_list=[]
def fetchSubnet():
	for i in vpc_connect.get_all_subnets():
	    print i.cidr_block ,"----",i.available_ip_address_count
	    subnet_list.append(i.cidr_block ,"----",i.available_ip_address_count)
	return subnet_list
	

from django.shortcuts import render
# View for index page. 
#def page(request):
  #return render(request, 'index.html')

def page(request):
  my_variable = "Hello World !"
  years_old = 5
  array_city_capitale = [ "Paris", "London", "Washington" ]
  return render(request, 'index.html', { "my_var":my_variable, "years":years_old, "array_city":array_city_capitale })

def home(request):
	return render(request, 'home.html')
def createinstance(request):
	subnet_list=fetchSubnet()
	return render(request, 'createinstance.html',{"subnet_list":subnet_list})
def confirmation(request):
	instid = request.GET.get('instid')
	print instid
	var_connect=ec2.connect_to_region('ap-southeast-1')
	ss=var_connect.get_all_regions()
	list=['Please Select']
	for i in ss:
		print i.name
		list.append(i.name)
	#return render(request, 'confirmation.html', { "instid":instid})
	print list
	return render(request, 'confirmation.html', { "instid":instid,"list":list})
