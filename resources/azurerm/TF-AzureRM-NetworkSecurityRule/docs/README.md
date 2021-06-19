# TF::AzureRM::NetworkSecurityRule

Manages a Network Security Rule.

~> **NOTE on Network Security Groups and Network Security Rules:** Terraform currently
provides both a standalone [Network Security Rule resource](network_security_rule.html), and allows for Network Security Rules to be defined in-line within the [Network Security Group resource](network_security_group.html).
At this time you cannot use a Network Security Group with in-line Network Security Rules in conjunction with any Network Security Rule resources. Doing so will cause a conflict of rule settings and will overwrite rules.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AzureRM::NetworkSecurityRule",
    "Properties" : {
        "<a href="#access" title="Access">Access</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#destinationaddressprefix" title="DestinationAddressPrefix">DestinationAddressPrefix</a>" : <i>String</i>,
        "<a href="#destinationaddressprefixes" title="DestinationAddressPrefixes">DestinationAddressPrefixes</a>" : <i>[ String, ... ]</i>,
        "<a href="#destinationapplicationsecuritygroupids" title="DestinationApplicationSecurityGroupIds">DestinationApplicationSecurityGroupIds</a>" : <i>[ String, ... ]</i>,
        "<a href="#destinationportrange" title="DestinationPortRange">DestinationPortRange</a>" : <i>String</i>,
        "<a href="#destinationportranges" title="DestinationPortRanges">DestinationPortRanges</a>" : <i>[ String, ... ]</i>,
        "<a href="#direction" title="Direction">Direction</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#networksecuritygroupname" title="NetworkSecurityGroupName">NetworkSecurityGroupName</a>" : <i>String</i>,
        "<a href="#priority" title="Priority">Priority</a>" : <i>Double</i>,
        "<a href="#protocol" title="Protocol">Protocol</a>" : <i>String</i>,
        "<a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>" : <i>String</i>,
        "<a href="#sourceaddressprefix" title="SourceAddressPrefix">SourceAddressPrefix</a>" : <i>String</i>,
        "<a href="#sourceaddressprefixes" title="SourceAddressPrefixes">SourceAddressPrefixes</a>" : <i>[ String, ... ]</i>,
        "<a href="#sourceapplicationsecuritygroupids" title="SourceApplicationSecurityGroupIds">SourceApplicationSecurityGroupIds</a>" : <i>[ String, ... ]</i>,
        "<a href="#sourceportrange" title="SourcePortRange">SourcePortRange</a>" : <i>String</i>,
        "<a href="#sourceportranges" title="SourcePortRanges">SourcePortRanges</a>" : <i>[ String, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AzureRM::NetworkSecurityRule
Properties:
    <a href="#access" title="Access">Access</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#destinationaddressprefix" title="DestinationAddressPrefix">DestinationAddressPrefix</a>: <i>String</i>
    <a href="#destinationaddressprefixes" title="DestinationAddressPrefixes">DestinationAddressPrefixes</a>: <i>
      - String</i>
    <a href="#destinationapplicationsecuritygroupids" title="DestinationApplicationSecurityGroupIds">DestinationApplicationSecurityGroupIds</a>: <i>
      - String</i>
    <a href="#destinationportrange" title="DestinationPortRange">DestinationPortRange</a>: <i>String</i>
    <a href="#destinationportranges" title="DestinationPortRanges">DestinationPortRanges</a>: <i>
      - String</i>
    <a href="#direction" title="Direction">Direction</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#networksecuritygroupname" title="NetworkSecurityGroupName">NetworkSecurityGroupName</a>: <i>String</i>
    <a href="#priority" title="Priority">Priority</a>: <i>Double</i>
    <a href="#protocol" title="Protocol">Protocol</a>: <i>String</i>
    <a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>: <i>String</i>
    <a href="#sourceaddressprefix" title="SourceAddressPrefix">SourceAddressPrefix</a>: <i>String</i>
    <a href="#sourceaddressprefixes" title="SourceAddressPrefixes">SourceAddressPrefixes</a>: <i>
      - String</i>
    <a href="#sourceapplicationsecuritygroupids" title="SourceApplicationSecurityGroupIds">SourceApplicationSecurityGroupIds</a>: <i>
      - String</i>
    <a href="#sourceportrange" title="SourcePortRange">SourcePortRange</a>: <i>String</i>
    <a href="#sourceportranges" title="SourcePortRanges">SourcePortRanges</a>: <i>
      - String</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### Access

Specifies whether network traffic is allowed or denied. Possible values are `Allow` and `Deny`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

A description for this rule. Restricted to 140 characters.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DestinationAddressPrefix

CIDR or destination IP range or * to match any IP. Tags such as ‘VirtualNetwork’, ‘AzureLoadBalancer’ and ‘Internet’ can also be used. Besides, it also supports all available Service Tags like ‘Sql.WestEurope‘, ‘Storage.EastUS‘, etc. You can list the available service tags with the cli: ```shell az network list-service-tags --location westcentralus```. For further information please see [Azure CLI - az network list-service-tags](https://docs.microsoft.com/en-us/cli/azure/network?view=azure-cli-latest#az-network-list-service-tags). This is required if `destination_address_prefixes` is not specified.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DestinationAddressPrefixes

List of destination address prefixes. Tags may not be used. This is required if `destination_address_prefix` is not specified.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DestinationApplicationSecurityGroupIds

A List of destination Application Security Group ID's.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DestinationPortRange

Destination Port or Range. Integer or range between `0` and `65535` or `*` to match any. This is required if `destination_port_ranges` is not specified.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DestinationPortRanges

List of destination ports or port ranges. This is required if `destination_port_range` is not specified.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Direction

The direction specifies if rule will be evaluated on incoming or outgoing traffic. Possible values are `Inbound` and `Outbound`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the security rule. This needs to be unique across all Rules in the Network Security Group. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetworkSecurityGroupName

The name of the Network Security Group that we want to attach the rule to. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Priority

Specifies the priority of the rule. The value can be between 100 and 4096. The priority number must be unique for each rule in the collection. The lower the priority number, the higher the priority of the rule.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Protocol

Network protocol this rule applies to. Possible values include `Tcp`, `Udp`, `Icmp`, `Esp`, `Ah` or `*` (which matches all).

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourceGroupName

The name of the resource group in which to create the Network Security Rule. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceAddressPrefix

CIDR or source IP range or * to match any IP. Tags such as ‘VirtualNetwork’, ‘AzureLoadBalancer’ and ‘Internet’ can also be used. This is required if `source_address_prefixes` is not specified.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceAddressPrefixes

List of source address prefixes. Tags may not be used. This is required if `source_address_prefix` is not specified.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceApplicationSecurityGroupIds

A List of source Application Security Group ID's.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourcePortRange

Source Port or Range. Integer or range between `0` and `65535` or `*` to match any. This is required if `source_port_ranges` is not specified.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourcePortRanges

List of source ports or port ranges. This is required if `source_port_range` is not specified.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeoutsdefinition.md">TimeoutsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Id

Returns the <code>Id</code> value.

