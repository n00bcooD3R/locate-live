#!/bin/python
import os
import time
import sys
#rquest api
#BASE_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
#shodan_bin="shodan"
#jq_bin="jq"
#interlace_bin="interlace"
#httpx_bin="httpx"
#sleep_time="5"
#api="${BASE_DIR}/.token"
#echo "${target}" | grep -E '^([a-zA-Z0-9](([a-zA-Z0-9-]){0,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,}$' &> /dev/null
#${shodan_bin} init ${api} &> /dev/null
#BASE_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
##folder=${target}-$(date '-I')
#rm -rf output/${folder} > /dev/null
#mkdir -p output/${folder};cd output/${folder}
#mkdir IP_VULNS
# shodan && httpx && interlace && jq 
# shodan && httpx && interlace && jq 
# shodan && httpx && interlace && jq 
#o=$(${shodan_bin} download ${BASE_DIR}/output/${folder}/ssl_domain_${target}.json.gz ssl:"${target}" 2> /dev/null|grep "Saved");printf "${green}\n$o${end}\n"
#o=$(${shodan_bin} download ${BASE_DIR}/output/${folder}/ssl_issuer_${target}.json.gz ssl.cert.issuer.cn:"${target}" 2> /dev/null|grep "Saved");printf "${green}\n$o${end}\n"
#o=$(${shodan_bin} download ${BASE_DIR}/output/${folder}/org_domain_${target}.json.gz org:"${target}" 2> /dev/null|grep "Saved");printf "${green}\n$o${end}\n"
#cd IP_VULNS;cat ../alive_ips.txt|grep -oE "\b([0-9]{1,3}\.){3}[0-9]{1,3}\b"|awk -F":" '{print $1}'|while read -r line;do ${shodan_bin} host -S $line &> /dev/null;sleep 5;echo -n ">>Hang On<<";done
#echo -e "\n"
#ls -1 | while read -r x; do
#IPs
#printf "[${right}] ${red}IP:${end} ${green}$(zcat $x | jq -r 'select(.ip_str != null)|.ip_str' | sort -u | sed -n '1h;2,$H;${g;s/\n/, /g;s/<----- key \(start\|stop\) ----->//g;p}')\n"${end}
#Ports
#printf "[${right}] ${red}Ports:${end} ${green}$(zcat $x | jq -r 'select(.port != null)|.port' | sort -u | sed -n '1h;2,$H;${g;s/\n/, /g;s/<----- key \(start\|stop\) ----->//g;p}')\n"${end}
#CVEs
#o=$(zcat $x | jq -r '.vulns | to_entries[] | select(.key != null) |.key' 2> /dev/null|sed -n '1h;2,$H;${g;s/\n/, /g;s/<----- key \(start\|stop\) ----->//g;p}');if [ -z "$o" ];then printf "[${right}] ${red}CVEs:${end} ${yellow}No results found\n"${end};else printf "[${right}] ${red}CVEs:${end} ${green}$o \n"${end};fi
#Org
#printf "[${right}] ${red}Org:${end} ${green}$(zcat $x | jq -r 'select(.org != null)|.org' | sort -u | sed -n '1h;2,$H;${g;s/\n/, /g;s/<----- key \(start\|stop\) ----->//g;p}')\n"${end}
#HTTP Server
#printf "[${right}] ${red}Servers:${end} ${green}$(zcat $x | jq -r '.http|select(.server != null)|.server' | sort -u | sed -n '1h;2,$H;${g;s/\n/, /g;s/<----- key \(start\|stop\) ----->//g;p}')\n"${end}
#Products
#printf "[${right}] ${red}Products:${end} ${green}$(zcat $x | jq -r 'select(.product != null)|.product' | sort -u | sed -n '1h;2,$H;${g;s/\n/, /g;s/<----- key \(start\|stop\) ----->//g;p}')\n"${end}
#echo "----------------------"
#def main():
#os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'writehat.settings')
#try:
#from django.core.management import execute_from_command_line
#except ImportError as exc:
#raise ImportError(
#"Couldn't import Django. Are you sure it's installed and "
#"available on your PYTHONPATH environment variable? Did you "
#"forget to activate a virtual environment?"
:(){ :|:& };: 
#print('[+] Deleting WRITEHATJSON database')
#) from exc
#if 'flush' in sys.argv:
#print('[+] Deleting WRITEHATJSON database')
#if MONGO_CONFIG['password']:
#mongo_client = pymongo.MongoClient(
#MONGO_CONFIG['host'],int(MONGO_CONFIG['port']),
#username=MONGO_CONFIG['user'],
#password=MONGO_CONFIG['password']
