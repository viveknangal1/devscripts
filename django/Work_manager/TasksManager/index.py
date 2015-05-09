from boto import ec2
from boto import vpc
from django.shortcuts import render

############# Global variable ##############
region_name='ap-southeast-1'
ec2_connection=ec2.connect_to_region(region_name)
vpc_connection=vpc.connect_to_region(region_name)
subnet_list=[]
subnet_dict={}

def fetchSubnet():
	for i in vpc_connection.get_all_subnets():
	    print i.cidr_block ,"----",i.available_ip_address_count
	    value='%s ==> %s ips available ' %(i.cidr_block,i.available_ip_address_count)
	    key=i.id
	    print 'key'+key
	    print 'value'+value
	    subnet_dict[key]=value
	print "-----------"
	return subnet_dict

def home(request):
	return render(request, 'home.html')
def createinstance(request):
	subnet_dict=fetchSubnet()
	return render(request, 'createinstance.html',{"subnet_dict":subnet_dict})
def confirmation(request):
	amiid = request.GET.get('amiid')
	instancetype = request.GET.get('instancetype')
	subnet = request.GET.get('subnet')
	intsname = request.GET.get('intsname')
	component = request.GET.get('component')
	instancecount = request.GET.get('instancecount')

	print  request.GET.get('amiid')
	print request.GET.get('instancetype')
	print request.GET.get('subnet')
	print request.GET.get('intsname')
	print request.GET.get('component')
	print request.GET.get('instancecount')
	counter=0
	for counter in range(0,int(instancecount)):
		reservation_id=ec2_connection.run_instances(amiid,min_count=1,instance_type=instancetype,subnet_id=subnet,dry_run=False)
		print type(reservation_id)
		print reservation_id
		instance = reservation_id.instances[0]
		print instance
		ec2_connection.create_tags([instance.id], {"Name": intsname,"SD_component":component})
	
	return render(request, 'confirmation.html', { "instid":amiid})
