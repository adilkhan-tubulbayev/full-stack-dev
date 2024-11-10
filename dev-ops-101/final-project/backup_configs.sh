#!/bin/bash
echo "PART 4. BACKUP"
read -p "File name: " filename
cp "$filename" /home/newadilkhan/backup_configs
echo "PART 4 HAS BEEN COMPLETED >>> SUCCESS"
