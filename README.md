# CloudTUI-FTS

### Authors
Andrea Lombardo<br/>
Davide Monfrecola<br/>
Giorgio Gambino

### Institute
Department of Science and Innovation Technology (DiSIT) - University of Eastern Piedmont - ITALY

### Superadvisor
Massimo Canonico

### Contact info
massimo.canonico@uniupo.it

### Description
***Cloud Text User Interface - Fault Tolerant and Scalable***<br>
CloudTUI-FTS is a text user interface able to interact
with multiple cloud platforms (such as OpenStack, HPE Helion
Eucalytus and so on)

With CloudTUI-FTS, a user can:
- start/stop/clone a VM
- monitor the VM health status
- create/manage policies in order to prevent faults (i.e.,
"if the CPU utilization is higher than XX %, then clone it")

CloudTUI-FTS is an open source project written in Python,
distributed for free under GPL v.3 license.

### Step #1: Install Requirements

First you need to install the required libraries by typing the following
commands in a terminal window:

	1. boto (the following command should work on most of the linux distributions: "sudo pip install boto")
  2. python-novaclient ("sudo pip install python-novaclient")
  3. python-ceilometerclient ("sudo pip install python-ceilometerclient")
  4. antlr3 ("sudo pip install http://www.antlr3.org/download/Python/antlr_python_runtime-3.1.3.tar.gz")

### Step #2: Get the lastest CloudTUI-FTS version

Download the source code from the git repository by using one of the following
commands:

	1. git clone https://github.com/mrbuzz/CloudTUI-FTS.git (recommended)
  2. wget https://github.com/mrbuzz/CloudTUI-FTS/archive/master.zip

### Step #3: Openstack Configuration
You'll need an up and running OpenStack installation. If you do not have enough
resources to run your own installation you can use [CloudLab][1] resources
that are available for free.  In this case, we suggest to use the ***OpenStack***
profile for your experiment.

1. Open the openstack.conf file under /conf/conf_files and set those values

	1. Nova values
		+ os_auth_url = http://<HOSTNAME>:<PORT>/v2.0
		+ os_username = <USERNAME>
		+ os_password = <PASSWORD>
		+ os_api_key = <USERNAME>
		+ os_tenant_name = <USERNAME>

	2. Ceilometer values
		+ os_ceilometer_auth = = http://<HOSTNAME>:<PORT>/v2.0
		+	os_ceilometer_username = <USERNAME>
		+	os_ceilometer_password = <PASSWORD>
		+	os_ceilometer_tenant_name = <USERNAME>

 - <HOSTNAME> and <PORT> are the hostname and port of the OpenStack Nova
 	 and Openstack Ceilometer.
 - <USERNAME> and <PASSWORD> are the login credentials for your OpenStack
 	installation

	We suggest you to add a line into your /etc/hosts file (superuser permissions
	required) by adding the IP Address of the controller followed by "ctl" word. If
	you do not do this you might have connection problems.

	example: ***195.84.22.xx ctl***

	Here is a copy-paste configuration file for using the CloudLab OpenStack profile:

	>os_auth_url = http://ctl:5000/v2.0
	>os_username = admin
	>os_password = <RANDOM PASSWORD>
	>os_api_key = admin
	>os_tenant_name = admin

	>os_ceilometer_auth = http://ctl:5000/v2.0
	>os_ceilometer_username = admin
	>os_ceilometer_password = <RANDOM PASSWORD>
	>os_ceilometer_tenant_name = admin

Copy and paste in openstack.conf the above lines; change <RANDOM PASSWORD>
with the password randomly-generated by Cloudlab situated in the "Profile
Instructions" section once your experiment is started.

### Step #5: Running
The basic setup in now completed. You can run cloudtui-fts by running "python
cloudtui-fts.py" and then following the instruction provided by our tool.


For support or any comment: massimo.canonico@uniupo.it

[1]: https://cloudlab.us/
