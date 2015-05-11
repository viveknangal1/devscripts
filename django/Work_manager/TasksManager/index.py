from boto import ec2
from boto import vpc
from django.shortcuts import render

############# Global variable ##############
region_name='ap-southeast-1'
ec2_connection=ec2.connect_to_region(region_name)
vpc_connection=vpc.connect_to_region(region_name)
subnet_list=[]
security_group_list=[]
security_group_dict={}
instance_type_list=[]
subnet_dict={}

def fetchInstanceType():
        instance_handler= open('/root/django/Work_manager/TasksManager/instance_types','r')
        for i in instance_handler:
                instance_type_list.append(i)
        return instance_type_list

def fetchSecurityGroup():
	security_group_dict={}
	filecon= open('/root/django/Work_manager/TasksManager/security_group','r')
	for s in filecon:
		list=s.split(",")
		value=list[0]
		key=list[1]
		security_group_dict[key]=value
		print 'key'+key
                print 'value'+value
	print "*********return security grp****"
	return security_group_dict
	
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
	security_group_dict=fetchSecurityGroup()
	print "*********before sort****"
	print security_group_dict
	#sorted(security_group_dict.items())
	print "*********after sort****"
	print security_group_dict
	print "*************"
	instance_type_list=fetchInstanceType()
	
	return render(request, 'createinstance.html',{"subnet_dict":subnet_dict,"security_group_dict":security_group_dict,"instance_type_list":instance_type_list})
def confirmation(request):
	amiid = request.GET.get('amiid')
	instancetype = request.GET.get('instancetype')
	subnet = request.GET.get('subnet')
	intsname = request.GET.get('intsname')
	component = request.GET.get('component')
	instancecount = request.GET.get('instancecount')
	securitygrp = request.GET.get('hiddengrp')
	securitygrp=securitygrp[1:]
	ssh = request.GET.get('ssh')
	securitygrp_list=[]

	print  request.GET.get('amiid')
	print request.GET.get('instancetype')
	print request.GET.get('subnet')
	print request.GET.get('intsname')
	print request.GET.get('component')
	print request.GET.get('instancecount')
	print request.GET.get('hiddengrp')
	print request.GET.get('ssh')
	for z in securitygrp.split(','):
		print 'z----'+z
		securitygrp_list.append(z)
		
	counter=0
	instancelist=[]
	for counter in range(0,int(instancecount)):
		print securitygrp_list
		reservation_id=ec2_connection.run_instances(amiid,key_name=ssh,security_group_ids=securitygrp_list,min_count=1,instance_type=instancetype,subnet_id=subnet,dry_run=False)
		print type(reservation_id)
		print reservation_id
		instance = reservation_id.instances[0]
		print instance
		instancelist.append(instance)
		ec2_connection.create_tags([instance.id], {"Name": intsname,"SD_component":component})
	
	return render(request, 'confirmation.html', { "instancelist":instancelist})
