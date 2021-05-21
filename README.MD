README.MD

Nightwriter is a project with the goal of being able to rapidly deploy a wordpress site. 

For Fun && || Profit  

######################################
#This is an activce WIP. Things work, but the process could be more user friendly.
#Complain about things not working.
#I will try to make them work more better!
######################################

SETUP/PREREQUISITES:

-*nix make it easier
-python3 & ansible installed #Refer to ansible_venv_setup.sh
-aws cli configued with credentials
-a existing key within aws
-A domain name registered with the ability to modify it's records. 
-An install of terraform https://www.terraform.io/


#Deployment procedure. 
you@computer:cd tf/
#Apply terraform, it will prompt you for a deployment, update the config with the name of your aws key file that you should have the loaded on your machine in awscli
you@computer:terraform apply
# Now retrieve the publicip from the terraform statefile #todo oneliner this
you@computer: grep terraforterraform.tfstate
you@computer: cd .. & cd ansible/
you@computer: ansible-playbook  playbook.yaml -i hosts --key-file ~/.ssh/azkey.pem
#edit the ansible config src/default.yml updating the defaultdomain with your youdomainnamee.com ensuring you have a host file

#This should deploy evreything navigate to youdomainnamee.com 
#Do the setup 

#todo, posting script

#todo, ssl 
#todo, better credential managmenet between accounts
#todo, break playbook into roles

#BUGS Troubleshooting.

#Issue#Ansible playbook crashing 
#Solution# ensure you have sourced the python virtual env and are not running as root.







