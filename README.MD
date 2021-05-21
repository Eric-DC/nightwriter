README.MD
# Nightwriter
Nightwriter is a project with the goal of being able to rapidly deploy a wordpress site. 

For Fun && || Profit  

# Disclaimer
This procedure is a work in progress, if something can be made easier, let's make it easier; There has been little testing at this phase in development and the mainteiners of this repo provide this software "AS IS"

SETUP/PREREQUISITES:

- *nix makes it easier
- python3 & ansible installed #Refer to ansible_venv_setup.sh
- aws cli configued with credentials
- a existing key/pair within aws
- A domain name registered with the ability to modify it's records. 
- An install of terraform https://www.terraform.io/


# Deployment procedure. 
you@computer:cd tf/
# Apply terraform
#It will prompt you for a deployment, update the config with the name of your aws key file that you should have the loaded on your machine in awscli
you@computer:terraform apply
#Now retrieve the publicip from the terraform statefile 
#todo oneliner this
you@computer: grep terraforterraform.tfstate

# Ansible Steps
you@computer: cd .. & cd ansible/
you@computer: ansible-playbook  playbook.yaml -i hosts --key-file ~/.ssh/<yourkey>.pem
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







