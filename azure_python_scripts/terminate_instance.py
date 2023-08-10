import sys,time
from azure.identity import ClientSecretCredential
from azure.mgmt.compute import ComputeManagementClient
from azure.mgmt.network import NetworkManagementClient


client_secret = sys.argv[1]
subscription_id = sys.argv[2]
tenant_id = sys.argv[3]
client_id = sys.argv[4]
nameVM = sys.argv[5]
RESOURCE_GROUP_NAME = sys.argv[6]


credential = ClientSecretCredential(tenant_id, client_id, client_secret)

compute_client = ComputeManagementClient(credential, subscription_id)
network_client = NetworkManagementClient(credential, subscription_id)


vm = compute_client.virtual_machines.get(RESOURCE_GROUP_NAME, nameVM)
os_disk_name = vm.storage_profile.os_disk.name

poller = compute_client.virtual_machines.begin_delete(
    RESOURCE_GROUP_NAME, nameVM
)
print('Borrando MV')
poller.wait()

poller = compute_client.disks.begin_delete(
    RESOURCE_GROUP_NAME, os_disk_name
)
print('Borrando Disco')
poller.wait()

poller = network_client.network_interfaces.begin_delete(
    RESOURCE_GROUP_NAME,nameVM+'-nic'
)
print('Borrando interfaz')
poller.wait()

poller = network_client.public_ip_addresses.begin_delete(
    RESOURCE_GROUP_NAME,nameVM+'-ip'
)
print('Borrando IP')
poller.wait()

poller = network_client.subnets.begin_delete(
    RESOURCE_GROUP_NAME,nameVM+'-vnet', nameVM+'-subnet'
)
print('Borrando Subnet')
poller.wait()

poller = network_client.virtual_networks.begin_delete(
    RESOURCE_GROUP_NAME,nameVM+'-vnet'
)
print('Borrando Vnet')
poller.wait()
