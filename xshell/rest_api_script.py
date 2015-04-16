from boto import ec2
import subprocess

name=""
hostname=""
description=""

var_connect=ec2.connect_to_region('ap-southeast-1')
instancelist=var_connect.get_all_instances()
for i in instancelist:
  for j in i.instances:
	pubip="NA"
	name="NA"
	env="NA"
	comp="NA"
	pip="NA"
	grplist=""

	if j.ip_address:
	  pubip = j.ip_address
	if "Name" in j.tags and j.tags["Name"]:
	  name=j.tags["Name"]
	if "SD_env" in j.tags and j.tags["SD_env"]:
	  env=j.tags["SD_env"]  
	if "SD_component" in j.tags and j.tags["SD_component"]: 
	  comp=j.tags["SD_component"]
        if j.private_ip_address:
	  pip=j.private_ip_address
	if j.groups:
		for z in j.groups:
		  var2 = z.name
        	  grplist = var2 +','+ grplist
	print j.id +",,", name ,",,"+ j.launch_time.rstrip('.000Z') ,",,"+ env ,",,"+ comp ,",,"+ j.instance_type ,",,"+ j.state  ,",," + pip ,",,"+pubip,",,"+grplist 
