for i in instancelist:
    for j in i.instances:
        if "Name" in j.tags and j.tags["Name"]  and j.private_ip_address:
            var1=""
            for z in j.groups:
                var2 = z.name
                var1 = var2 +','+ var1
            print j.id +"||", j.tags["Name"] ,"||"+ j.launch_time ,"||"+ j.instance_type ,"||"+ j.state  ,"||" +j.private_ip_address ,"||"+var1

