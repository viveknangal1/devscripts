from boto import ec2
var_connect=ec2.connect_to_region('ap-southeast-1')
instancelist=var_connect.get_all_instances()


for i in instancelist:
    for j in i.instances:
        if "Name" in j.tags and j.tags["Name"]  and j.private_ip_address:
            print j.id +"||", j.tags["Name"] ,"||"+ j.launch_time ,"||"+ j.instance_type ,"||"+ j.state  ,"||" +j.private_ip_address ,"||"+j.image_id

