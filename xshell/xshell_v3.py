from boto import ec2
import sys
import subprocess

name=""
hostname=""
description=""

var_connect=ec2.connect_to_region('ap-southeast-1')
instancelist=var_connect.get_all_instances()
for i in instancelist:
  for j in i.instances:
	pubip="Not Defined"
	name="Not Defined"
	env="Not Defined"
	comp="Not Defined"

	if j.ip_address:
	  pubip = j.ip_address
	if "Name" in j.tags and j.tags["Name"]:
	  name=j.tags["Name"]
	if "SD_env" in j.tags and j.tags["SD_env"]:
	  env=j.tags["SD_env"]  
	if "SD_component" in j.tags and j.tags["SD_component"]: 
	  comp=j.tags["SD_component"]
        print(j.private_ip_address),"<<<"
        if j.private_ip_address:
	  hostname=j.ip_address
	  description="LaunchTime:"+j.launch_time +"|| SD_component:"+comp+"|| SD_env:"+env+"|| Public_IP:"+pubip+"||"+j.instance_type
	  print "name",name
	  print description
	  try:
		with open("/data/sessions/"+name+".xsh", 'w') as target_file:
    			with open("template_xshell.xsh", 'r') as source_file:
		        	for line in source_file:
			            if "[HOSTNAME]" in line:
        	        		target_file.write(line.replace("[HOSTNAME]",hostname))
			            elif "[DESCRIPTION]" in line:
                			target_file.write(line.replace("[DESCRIPTION]",description))
			            else:    
        	        		target_file.write(line)
	  except Exception, err:
		sys.stderr.write('ERROR: %s\n' % str(err))
		print "exception:"
		pass
