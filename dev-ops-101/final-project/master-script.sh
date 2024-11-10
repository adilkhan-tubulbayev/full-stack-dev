#!/bin/bash
echo "1 - update packages"
echo "2 - isntall nginx"
echo "3 - create new user + group"
echo "4 - backup files"
echo "5 - complete all steps"
echo "6 - exit"

read -p "Enter number: " num
if [ $num == "1" ]; then
	sh ./update.sh

elif [ $num == "2" ]; then
	sh ./nginx.sh

elif [ $num == "3" ]; then
	sh ./user-add.sh

elif [ $num == "4" ]; then
	sh ./backup_configs.sh
elif [ $num == "5" ]; then
	sh ./update.sh
	sh ./nginx.sh
	sh ./user-add.sh
	sh ./backup_configs.sh
elif [ $num == "6" ]; then
	exit 0
else
	echo "Invalid input!!! Try again."
fi
