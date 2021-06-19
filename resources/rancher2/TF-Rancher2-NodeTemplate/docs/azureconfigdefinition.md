# TF::Rancher2::NodeTemplate AzureConfigDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#availabilityset" title="AvailabilitySet">AvailabilitySet</a>" : <i>String</i>,
    "<a href="#clientid" title="ClientId">ClientId</a>" : <i>String</i>,
    "<a href="#clientsecret" title="ClientSecret">ClientSecret</a>" : <i>String</i>,
    "<a href="#customdata" title="CustomData">CustomData</a>" : <i>String</i>,
    "<a href="#disksize" title="DiskSize">DiskSize</a>" : <i>String</i>,
    "<a href="#dns" title="Dns">Dns</a>" : <i>String</i>,
    "<a href="#dockerport" title="DockerPort">DockerPort</a>" : <i>String</i>,
    "<a href="#environment" title="Environment">Environment</a>" : <i>String</i>,
    "<a href="#faultdomaincount" title="FaultDomainCount">FaultDomainCount</a>" : <i>String</i>,
    "<a href="#image" title="Image">Image</a>" : <i>String</i>,
    "<a href="#location" title="Location">Location</a>" : <i>String</i>,
    "<a href="#manageddisks" title="ManagedDisks">ManagedDisks</a>" : <i>Boolean</i>,
    "<a href="#nopublicip" title="NoPublicIp">NoPublicIp</a>" : <i>Boolean</i>,
    "<a href="#nsg" title="Nsg">Nsg</a>" : <i>String</i>,
    "<a href="#openport" title="OpenPort">OpenPort</a>" : <i>[ String, ... ]</i>,
    "<a href="#privateipaddress" title="PrivateIpAddress">PrivateIpAddress</a>" : <i>String</i>,
    "<a href="#resourcegroup" title="ResourceGroup">ResourceGroup</a>" : <i>String</i>,
    "<a href="#size" title="Size">Size</a>" : <i>String</i>,
    "<a href="#sshuser" title="SshUser">SshUser</a>" : <i>String</i>,
    "<a href="#staticpublicip" title="StaticPublicIp">StaticPublicIp</a>" : <i>Boolean</i>,
    "<a href="#storagetype" title="StorageType">StorageType</a>" : <i>String</i>,
    "<a href="#subnet" title="Subnet">Subnet</a>" : <i>String</i>,
    "<a href="#subnetprefix" title="SubnetPrefix">SubnetPrefix</a>" : <i>String</i>,
    "<a href="#subscriptionid" title="SubscriptionId">SubscriptionId</a>" : <i>String</i>,
    "<a href="#updatedomaincount" title="UpdateDomainCount">UpdateDomainCount</a>" : <i>String</i>,
    "<a href="#useprivateip" title="UsePrivateIp">UsePrivateIp</a>" : <i>Boolean</i>,
    "<a href="#vnet" title="Vnet">Vnet</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#availabilityset" title="AvailabilitySet">AvailabilitySet</a>: <i>String</i>
<a href="#clientid" title="ClientId">ClientId</a>: <i>String</i>
<a href="#clientsecret" title="ClientSecret">ClientSecret</a>: <i>String</i>
<a href="#customdata" title="CustomData">CustomData</a>: <i>String</i>
<a href="#disksize" title="DiskSize">DiskSize</a>: <i>String</i>
<a href="#dns" title="Dns">Dns</a>: <i>String</i>
<a href="#dockerport" title="DockerPort">DockerPort</a>: <i>String</i>
<a href="#environment" title="Environment">Environment</a>: <i>String</i>
<a href="#faultdomaincount" title="FaultDomainCount">FaultDomainCount</a>: <i>String</i>
<a href="#image" title="Image">Image</a>: <i>String</i>
<a href="#location" title="Location">Location</a>: <i>String</i>
<a href="#manageddisks" title="ManagedDisks">ManagedDisks</a>: <i>Boolean</i>
<a href="#nopublicip" title="NoPublicIp">NoPublicIp</a>: <i>Boolean</i>
<a href="#nsg" title="Nsg">Nsg</a>: <i>String</i>
<a href="#openport" title="OpenPort">OpenPort</a>: <i>
      - String</i>
<a href="#privateipaddress" title="PrivateIpAddress">PrivateIpAddress</a>: <i>String</i>
<a href="#resourcegroup" title="ResourceGroup">ResourceGroup</a>: <i>String</i>
<a href="#size" title="Size">Size</a>: <i>String</i>
<a href="#sshuser" title="SshUser">SshUser</a>: <i>String</i>
<a href="#staticpublicip" title="StaticPublicIp">StaticPublicIp</a>: <i>Boolean</i>
<a href="#storagetype" title="StorageType">StorageType</a>: <i>String</i>
<a href="#subnet" title="Subnet">Subnet</a>: <i>String</i>
<a href="#subnetprefix" title="SubnetPrefix">SubnetPrefix</a>: <i>String</i>
<a href="#subscriptionid" title="SubscriptionId">SubscriptionId</a>: <i>String</i>
<a href="#updatedomaincount" title="UpdateDomainCount">UpdateDomainCount</a>: <i>String</i>
<a href="#useprivateip" title="UsePrivateIp">UsePrivateIp</a>: <i>Boolean</i>
<a href="#vnet" title="Vnet">Vnet</a>: <i>String</i>
</pre>

## Properties

#### AvailabilitySet

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClientId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClientSecret

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CustomData

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DiskSize

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Dns

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DockerPort

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Environment

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FaultDomainCount

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Image

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Location

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ManagedDisks

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NoPublicIp

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Nsg

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OpenPort

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrivateIpAddress

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourceGroup

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Size

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SshUser

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StaticPublicIp

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StorageType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Subnet

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SubnetPrefix

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SubscriptionId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UpdateDomainCount

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UsePrivateIp

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vnet

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

