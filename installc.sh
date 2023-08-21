#!/usr/bin/bash
pathFile="spammer" 
pkg install python
cd ~/../usr/bin 
# команда
touch HackSpam
echo "cd ~/$pathFile/ && python HackSpam.py" >  HackSpam
chmod +x HackSpam
cd ~/
#конец
