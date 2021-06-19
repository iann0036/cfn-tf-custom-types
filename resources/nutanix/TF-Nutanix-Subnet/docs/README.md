# TF::Nutanix::Subnet

Provides a resource to create a subnet based on the input parameters. A subnet is a block of IP addresses.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Nutanix::Subnet",
    "Properties" : {
        "<a href="#availabilityzonereference" title="AvailabilityZoneReference">AvailabilityZoneReference</a>" : <i>[ <a href="availabilityzonereferencedefinition.md">AvailabilityZoneReferenceDefinition</a>, ... ]</i>,
        "<a href="#clusteruuid" title="ClusterUuid">ClusterUuid</a>" : <i>String</i>,
        "<a href="#defaultgatewayip" title="DefaultGatewayIp">DefaultGatewayIp</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#dhcpdomainnameserverlist" title="DhcpDomainNameServerList">DhcpDomainNameServerList</a>" : <i>[ String, ... ]</i>,
        "<a href="#dhcpdomainsearchlist" title="DhcpDomainSearchList">DhcpDomainSearchList</a>" : <i>[ String, ... ]</i>,
        "<a href="#dhcpoptions" title="DhcpOptions">DhcpOptions</a>" : <i>[ <a href="dhcpoptionsdefinition.md">DhcpOptionsDefinition</a>, ... ]</i>,
        "<a href="#dhcpserveraddress" title="DhcpServerAddress">DhcpServerAddress</a>" : <i>[ <a href="dhcpserveraddressdefinition.md">DhcpServerAddressDefinition</a>, ... ]</i>,
        "<a href="#dhcpserveraddressport" title="DhcpServerAddressPort">DhcpServerAddressPort</a>" : <i>Double</i>,
        "<a href="#ipconfigpoollistranges" title="IpConfigPoolListRanges">IpConfigPoolListRanges</a>" : <i>[ String, ... ]</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#networkfunctionchainreference" title="NetworkFunctionChainReference">NetworkFunctionChainReference</a>" : <i>[ <a href="networkfunctionchainreferencedefinition.md">NetworkFunctionChainReferenceDefinition</a>, ... ]</i>,
        "<a href="#ownerreference" title="OwnerReference">OwnerReference</a>" : <i>[ <a href="ownerreferencedefinition.md">OwnerReferenceDefinition</a>, ... ]</i>,
        "<a href="#prefixlength" title="PrefixLength">PrefixLength</a>" : <i>Double</i>,
        "<a href="#projectreference" title="ProjectReference">ProjectReference</a>" : <i>[ <a href="projectreferencedefinition.md">ProjectReferenceDefinition</a>, ... ]</i>,
        "<a href="#subnetip" title="SubnetIp">SubnetIp</a>" : <i>String</i>,
        "<a href="#subnettype" title="SubnetType">SubnetType</a>" : <i>String</i>,
        "<a href="#vlanid" title="VlanId">VlanId</a>" : <i>Double</i>,
        "<a href="#vswitchname" title="VswitchName">VswitchName</a>" : <i>String</i>,
        "<a href="#categories" title="Categories">Categories</a>" : <i>[ <a href="categoriesdefinition.md">CategoriesDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Nutanix::Subnet
Properties:
    <a href="#availabilityzonereference" title="AvailabilityZoneReference">AvailabilityZoneReference</a>: <i>
      - <a href="availabilityzonereferencedefinition.md">AvailabilityZoneReferenceDefinition</a></i>
    <a href="#clusteruuid" title="ClusterUuid">ClusterUuid</a>: <i>String</i>
    <a href="#defaultgatewayip" title="DefaultGatewayIp">DefaultGatewayIp</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#dhcpdomainnameserverlist" title="DhcpDomainNameServerList">DhcpDomainNameServerList</a>: <i>
      - String</i>
    <a href="#dhcpdomainsearchlist" title="DhcpDomainSearchList">DhcpDomainSearchList</a>: <i>
      - String</i>
    <a href="#dhcpoptions" title="DhcpOptions">DhcpOptions</a>: <i>
      - <a href="dhcpoptionsdefinition.md">DhcpOptionsDefinition</a></i>
    <a href="#dhcpserveraddress" title="DhcpServerAddress">DhcpServerAddress</a>: <i>
      - <a href="dhcpserveraddressdefinition.md">DhcpServerAddressDefinition</a></i>
    <a href="#dhcpserveraddressport" title="DhcpServerAddressPort">DhcpServerAddressPort</a>: <i>Double</i>
    <a href="#ipconfigpoollistranges" title="IpConfigPoolListRanges">IpConfigPoolListRanges</a>: <i>
      - String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#networkfunctionchainreference" title="NetworkFunctionChainReference">NetworkFunctionChainReference</a>: <i>
      - <a href="networkfunctionchainreferencedefinition.md">NetworkFunctionChainReferenceDefinition</a></i>
    <a href="#ownerreference" title="OwnerReference">OwnerReference</a>: <i>
      - <a href="ownerreferencedefinition.md">OwnerReferenceDefinition</a></i>
    <a href="#prefixlength" title="PrefixLength">PrefixLength</a>: <i>Double</i>
    <a href="#projectreference" title="ProjectReference">ProjectReference</a>: <i>
      - <a href="projectreferencedefinition.md">ProjectReferenceDefinition</a></i>
    <a href="#subnetip" title="SubnetIp">SubnetIp</a>: <i>String</i>
    <a href="#subnettype" title="SubnetType">SubnetType</a>: <i>String</i>
    <a href="#vlanid" title="VlanId">VlanId</a>: <i>Double</i>
    <a href="#vswitchname" title="VswitchName">VswitchName</a>: <i>String</i>
    <a href="#categories" title="Categories">Categories</a>: <i>
      - <a href="categoriesdefinition.md">CategoriesDefinition</a></i>
</pre>

## Properties

#### AvailabilityZoneReference

_Required_: No

_Type_: List of <a href="availabilityzonereferencedefinition.md">AvailabilityZoneReferenceDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClusterUuid

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefaultGatewayIp

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DhcpDomainNameServerList

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DhcpDomainSearchList

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DhcpOptions

_Required_: No

_Type_: List of <a href="dhcpoptionsdefinition.md">DhcpOptionsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DhcpServerAddress

_Required_: No

_Type_: List of <a href="dhcpserveraddressdefinition.md">DhcpServerAddressDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DhcpServerAddressPort

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpConfigPoolListRanges

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetworkFunctionChainReference

_Required_: No

_Type_: List of <a href="networkfunctionchainreferencedefinition.md">NetworkFunctionChainReferenceDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OwnerReference

_Required_: No

_Type_: List of <a href="ownerreferencedefinition.md">OwnerReferenceDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrefixLength

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProjectReference

_Required_: No

_Type_: List of <a href="projectreferencedefinition.md">ProjectReferenceDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SubnetIp

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SubnetType

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VlanId

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VswitchName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Categories

_Required_: No

_Type_: List of <a href="categoriesdefinition.md">CategoriesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### ApiVersion

Returns the <code>ApiVersion</code> value.

#### ClusterName

Returns the <code>ClusterName</code> value.

#### Id

Returns the <code>Id</code> value.

#### Metadata

Returns the <code>Metadata</code> value.

#### State

Returns the <code>State</code> value.

