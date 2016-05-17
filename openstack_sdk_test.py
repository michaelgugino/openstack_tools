import os_client_config
from openstack import connection

# source an openrc file for the following to work.

cloud_config = os_client_config.OpenStackConfig().get_one_cloud('envvars')
conn = connection.from_config(cloud_config=cloud_config)

x = conn.network.agents()

l = list(x)
print l[0].id
my_id = l[0].id
print "####################"
g = conn.network.get_agent(my_id)
print g

u = conn.network.update_agent(my_id, description="testing")
print u
