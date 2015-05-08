        echo "Menu "
        echo "1. Degister the instance from the elb"
        echo "2. Register the instance from the elb "
        echo "3. Check the status of an elb "
        echo "4. Quit"
        echo -n "Enter ur Choice = "
        read Choice
        case "$Choice" in
           1) echo -n "Enter the ELB name = "
              read f1
              echo -n "Enter the instance id which need to be degistered = "
          read f2         
              echo  "##########################################################"
		if [ "$f1" ] && [ "$f2" ];then
			aws elb deregister-instances-from-load-balancer --load-balancer-name ${f1} --instances ${f2} --output text
		else
                        echo "Input not provided"
		fi
              ;;

          2) echo -n "Enter the ELB name = "
              read r1 
              echo -n "Enter the instance id which need to be registered = "
          read r2      
              echo  "##########################################################"
		if [ "$r1" ] && [ "$r2" ];then
			aws elb register-instances-with-load-balancer --load-balancer-name ${r1} --instances ${r2} --output text
                else
                        echo "Input not provided"
                fi

             ;;
	 3)  echo -n "Enter the ELB name whose status need to be checked = "
                read a1
              echo  "##########################################################"
		if [ "$a1" ] ;then
			aws elb describe-instance-health --load-balancer-name ${a1} --output text
		else
                        echo "Input not provided"
		fi
		;;
         4) 
             echo "Exit......."
             exit;;
        esac
