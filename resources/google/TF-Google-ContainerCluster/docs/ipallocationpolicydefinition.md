# TF::Google::ContainerCluster IpAllocationPolicyDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#clusteripv4cidrblock" title="ClusterIpv4CidrBlock">ClusterIpv4CidrBlock</a>" : <i>String</i>,
    "<a href="#clustersecondaryrangename" title="ClusterSecondaryRangeName">ClusterSecondaryRangeName</a>" : <i>String</i>,
    "<a href="#servicesipv4cidrblock" title="ServicesIpv4CidrBlock">ServicesIpv4CidrBlock</a>" : <i>String</i>,
    "<a href="#servicessecondaryrangename" title="ServicesSecondaryRangeName">ServicesSecondaryRangeName</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#clusteripv4cidrblock" title="ClusterIpv4CidrBlock">ClusterIpv4CidrBlock</a>: <i>String</i>
<a href="#clustersecondaryrangename" title="ClusterSecondaryRangeName">ClusterSecondaryRangeName</a>: <i>String</i>
<a href="#servicesipv4cidrblock" title="ServicesIpv4CidrBlock">ServicesIpv4CidrBlock</a>: <i>String</i>
<a href="#servicessecondaryrangename" title="ServicesSecondaryRangeName">ServicesSecondaryRangeName</a>: <i>String</i>
</pre>

## Properties

#### ClusterIpv4CidrBlock

The IP address range for the cluster pod IPs.
Set to blank to have a range chosen with the default size. Set to /netmask (e.g. /14)
to have a range chosen with a specific netmask. Set to a CIDR notation (e.g. 10.96.0.0/14)
from the RFC-1918 private networks (e.g. 10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16) to
pick a specific range to use.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClusterSecondaryRangeName

The name of the existing secondary
range in the cluster's subnetwork to use for pod IP addresses. Alternatively,
`cluster_ipv4_cidr_block` can be used to automatically create a GKE-managed one.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServicesIpv4CidrBlock

The IP address range of the services IPs in this cluster.
Set to blank to have a range chosen with the default size. Set to /netmask (e.g. /14)
to have a range chosen with a specific netmask. Set to a CIDR notation (e.g. 10.96.0.0/14)
from the RFC-1918 private networks (e.g. 10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16) to
pick a specific range to use.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServicesSecondaryRangeName

The name of the existing
secondary range in the cluster's subnetwork to use for service `ClusterIP`s.
Alternatively, `services_ipv4_cidr_block` can be used to automatically create a
GKE-managed one.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

