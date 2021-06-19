# TF::Aviatrix::FirewallInstance

The **aviatrix_firewall_instance** resource allows the creation and management of Aviatrix Firewall Instances.

This resource is used in [Aviatrix FireNet](https://docs.aviatrix.com/HowTos/firewall_network_faq.html) and [Aviatrix Transit FireNet](https://docs.aviatrix.com/HowTos/transit_firenet_faq.html) solutions, in conjunction with other resources that may include, and are not limited to: **firenet**, **firewall_instance_association**, **aws_tgw** and **transit_gateway** resources.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Aviatrix::FirewallInstance",
    "Properties" : {
        "<a href="#availabilitydomain" title="AvailabilityDomain">AvailabilityDomain</a>" : <i>String</i>,
        "<a href="#bootstrapbucketname" title="BootstrapBucketName">BootstrapBucketName</a>" : <i>String</i>,
        "<a href="#bootstrapstoragename" title="BootstrapStorageName">BootstrapStorageName</a>" : <i>String</i>,
        "<a href="#containerfolder" title="ContainerFolder">ContainerFolder</a>" : <i>String</i>,
        "<a href="#egresssubnet" title="EgressSubnet">EgressSubnet</a>" : <i>String</i>,
        "<a href="#egressvpcid" title="EgressVpcId">EgressVpcId</a>" : <i>String</i>,
        "<a href="#faultdomain" title="FaultDomain">FaultDomain</a>" : <i>String</i>,
        "<a href="#filesharefolder" title="FileShareFolder">FileShareFolder</a>" : <i>String</i>,
        "<a href="#firenetgwname" title="FirenetGwName">FirenetGwName</a>" : <i>String</i>,
        "<a href="#firewallimage" title="FirewallImage">FirewallImage</a>" : <i>String</i>,
        "<a href="#firewallimageid" title="FirewallImageId">FirewallImageId</a>" : <i>String</i>,
        "<a href="#firewallimageversion" title="FirewallImageVersion">FirewallImageVersion</a>" : <i>String</i>,
        "<a href="#firewallname" title="FirewallName">FirewallName</a>" : <i>String</i>,
        "<a href="#firewallsize" title="FirewallSize">FirewallSize</a>" : <i>String</i>,
        "<a href="#iamrole" title="IamRole">IamRole</a>" : <i>String</i>,
        "<a href="#keyname" title="KeyName">KeyName</a>" : <i>String</i>,
        "<a href="#managementsubnet" title="ManagementSubnet">ManagementSubnet</a>" : <i>String</i>,
        "<a href="#managementvpcid" title="ManagementVpcId">ManagementVpcId</a>" : <i>String</i>,
        "<a href="#password" title="Password">Password</a>" : <i>String</i>,
        "<a href="#sasurlconfig" title="SasUrlConfig">SasUrlConfig</a>" : <i>String</i>,
        "<a href="#sasurllicense" title="SasUrlLicense">SasUrlLicense</a>" : <i>String</i>,
        "<a href="#sharedirectory" title="ShareDirectory">ShareDirectory</a>" : <i>String</i>,
        "<a href="#sickey" title="SicKey">SicKey</a>" : <i>String</i>,
        "<a href="#sshpublickey" title="SshPublicKey">SshPublicKey</a>" : <i>String</i>,
        "<a href="#storageaccesskey" title="StorageAccessKey">StorageAccessKey</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tagsdefinition.md">TagsDefinition</a>, ... ]</i>,
        "<a href="#userdata" title="UserData">UserData</a>" : <i>String</i>,
        "<a href="#username" title="Username">Username</a>" : <i>String</i>,
        "<a href="#vpcid" title="VpcId">VpcId</a>" : <i>String</i>,
        "<a href="#zone" title="Zone">Zone</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Aviatrix::FirewallInstance
Properties:
    <a href="#availabilitydomain" title="AvailabilityDomain">AvailabilityDomain</a>: <i>String</i>
    <a href="#bootstrapbucketname" title="BootstrapBucketName">BootstrapBucketName</a>: <i>String</i>
    <a href="#bootstrapstoragename" title="BootstrapStorageName">BootstrapStorageName</a>: <i>String</i>
    <a href="#containerfolder" title="ContainerFolder">ContainerFolder</a>: <i>String</i>
    <a href="#egresssubnet" title="EgressSubnet">EgressSubnet</a>: <i>String</i>
    <a href="#egressvpcid" title="EgressVpcId">EgressVpcId</a>: <i>String</i>
    <a href="#faultdomain" title="FaultDomain">FaultDomain</a>: <i>String</i>
    <a href="#filesharefolder" title="FileShareFolder">FileShareFolder</a>: <i>String</i>
    <a href="#firenetgwname" title="FirenetGwName">FirenetGwName</a>: <i>String</i>
    <a href="#firewallimage" title="FirewallImage">FirewallImage</a>: <i>String</i>
    <a href="#firewallimageid" title="FirewallImageId">FirewallImageId</a>: <i>String</i>
    <a href="#firewallimageversion" title="FirewallImageVersion">FirewallImageVersion</a>: <i>String</i>
    <a href="#firewallname" title="FirewallName">FirewallName</a>: <i>String</i>
    <a href="#firewallsize" title="FirewallSize">FirewallSize</a>: <i>String</i>
    <a href="#iamrole" title="IamRole">IamRole</a>: <i>String</i>
    <a href="#keyname" title="KeyName">KeyName</a>: <i>String</i>
    <a href="#managementsubnet" title="ManagementSubnet">ManagementSubnet</a>: <i>String</i>
    <a href="#managementvpcid" title="ManagementVpcId">ManagementVpcId</a>: <i>String</i>
    <a href="#password" title="Password">Password</a>: <i>String</i>
    <a href="#sasurlconfig" title="SasUrlConfig">SasUrlConfig</a>: <i>String</i>
    <a href="#sasurllicense" title="SasUrlLicense">SasUrlLicense</a>: <i>String</i>
    <a href="#sharedirectory" title="ShareDirectory">ShareDirectory</a>: <i>String</i>
    <a href="#sickey" title="SicKey">SicKey</a>: <i>String</i>
    <a href="#sshpublickey" title="SshPublicKey">SshPublicKey</a>: <i>String</i>
    <a href="#storageaccesskey" title="StorageAccessKey">StorageAccessKey</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tagsdefinition.md">TagsDefinition</a></i>
    <a href="#userdata" title="UserData">UserData</a>: <i>String</i>
    <a href="#username" title="Username">Username</a>: <i>String</i>
    <a href="#vpcid" title="VpcId">VpcId</a>: <i>String</i>
    <a href="#zone" title="Zone">Zone</a>: <i>String</i>
</pre>

## Properties

#### AvailabilityDomain

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BootstrapBucketName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BootstrapStorageName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ContainerFolder

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EgressSubnet

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EgressVpcId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FaultDomain

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FileShareFolder

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FirenetGwName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FirewallImage

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FirewallImageId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FirewallImageVersion

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FirewallName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FirewallSize

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IamRole

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KeyName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ManagementSubnet

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ManagementVpcId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Password

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SasUrlConfig

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SasUrlLicense

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ShareDirectory

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SicKey

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SshPublicKey

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StorageAccessKey

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

_Required_: No

_Type_: List of <a href="tagsdefinition.md">TagsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserData

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Username

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VpcId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Zone

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### CloudType

Returns the <code>CloudType</code> value.

#### EgressInterface

Returns the <code>EgressInterface</code> value.

#### GcpVpcId

Returns the <code>GcpVpcId</code> value.

#### Id

Returns the <code>Id</code> value.

#### InstanceId

Returns the <code>InstanceId</code> value.

#### LanInterface

Returns the <code>LanInterface</code> value.

#### ManagementInterface

Returns the <code>ManagementInterface</code> value.

#### PublicIp

Returns the <code>PublicIp</code> value.

