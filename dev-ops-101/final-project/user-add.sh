#!/bin/bash

echo "PART 3. USER AND GROUP"
read -p "Enter username: " username

if id "$username"; then
	echo "$username user already exists!!!"
else	
	sudo useradd "$username"
	sudo passwd "$username"
fi

	echo ""

        echo "1 - create and enter to a new group"
        echo "2 - enter to the existing one"

        read -p "Input number: " num
        read -p "Group name: " grpname

        case $num in
                1)
                        sudo groupadd $grpname
                        sudo usermod -aG $grpname $username
                        getent group $grpname
                        id $username
                ;;
                2)
                        sudo usermod -aG $grpname $username
                        getent group $grpname
                        id $username
                ;;
                *)
                        echo "Invalid data. Try again."

        esac

echo "PART 3  HAS BEEN COMPLETED >>> SUCCESS"
echo ""
