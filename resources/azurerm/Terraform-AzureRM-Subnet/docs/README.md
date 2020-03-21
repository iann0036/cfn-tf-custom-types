# Terraform::AzureRM::Subnet

Manages a subnet. Subnets represent network segments within the IP space defined by the virtual network.

~> **NOTE on Virtual Networks and Subnet's:** Terraform currently
provides both a standalone [Subnet resource](subnet.html), and allows for Subnets to be defined in-line within the [Virtual Network resource](virtual_network.html).
At this time you cannot use a Virtual Network with in-line Subnets in conjunction with any Subnet resources. Doing so will cause a conflict of Subnet configurations and will overwrite Subnet's.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AzureRM::Subnet",
    "Properties" : {
        "<a href="#addressprefix" title="AddressPrefix">AddressPrefix</a>" : <i>String</i>,
        "<a href="#enforceprivatelinkendpointnetworkpolicies" title="EnforcePrivateLinkEndpointNetworkPolicies">EnforcePrivateLinkEndpointNetworkPolicies</a>" : <i>Boolean</i>,
        "<a href="#enforceprivatelinkservicenetworkpolicies" title="EnforcePrivateLinkServiceNetworkPolicies">EnforcePrivateLinkServiceNetworkPolicies</a>" : <i>Boolean</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>" : <i>String</i>,
        "<a href="#serviceendpoints" title="ServiceEndpoints">ServiceEndpoints</a>" : <i>[ String, ... ]</i>,
        "<a href="#virtualnetworkname" title="VirtualNetworkName">VirtualNetworkName</a>" : <i>String</i>,
        "<a href="#delegation" title="Delegation">Delegation</a>" : <i>[ <a href="delegation.md">Delegation</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeouts.md">Timeouts</a></i>,
        "<a href="#servicedelegation" title="ServiceDelegation">ServiceDelegation</a>" : <i>[ <a href="servicedelegation.md">ServiceDelegation</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AzureRM::Subnet
Properties:
    <a href="#addressprefix" title="AddressPrefix">AddressPrefix</a>: <i>String</i>
    <a href="#enforceprivatelinkendpointnetworkpolicies" title="EnforcePrivateLinkEndpointNetworkPolicies">EnforcePrivateLinkEndpointNetworkPolicies</a>: <i>Boolean</i>
    <a href="#enforceprivatelinkservicenetworkpolicies" title="EnforcePrivateLinkServiceNetworkPolicies">EnforcePrivateLinkServiceNetworkPolicies</a>: <i>Boolean</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>: <i>String</i>
    <a href="#serviceendpoints" title="ServiceEndpoints">ServiceEndpoints</a>: <i>
      - String</i>
    <a href="#virtualnetworkname" title="VirtualNetworkName">VirtualNetworkName</a>: <i>String</i>
    <a href="#delegation" title="Delegation">Delegation</a>: <i>
      - <a href="delegation.md">Delegation</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeouts.md">Timeouts</a></i>
    <a href="#servicedelegation" title="ServiceDelegation">ServiceDelegation</a>: <i>
      - <a href="servicedelegation.md">ServiceDelegation</a></i>
</pre>

## Properties

#### AddressPrefix

The address prefix to use for the subnet.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnforcePrivateLinkEndpointNetworkPolicies

Enable or Disable network policies for the private link endpoint on the subnet. Default value is `false`. Conflicts with enforce_private_link_service_network_policies.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnforcePrivateLinkServiceNetworkPolicies

Enable or Disable network policies for the private link service on the subnet. Default valule is `false`. Conflicts with `enforce_private_link_endpoint_network_policies`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the subnet. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourceGroupName

The name of the resource group in which to create the subnet. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceEndpoints

The list of Service endpoints to associate with the subnet. Possible values include: `Microsoft.AzureActiveDirectory`, `Microsoft.AzureCosmosDB`, `Microsoft.ContainerRegistry`, `Microsoft.EventHub`, `Microsoft.KeyVault`, `Microsoft.ServiceBus`, `Microsoft.Sql`, `Microsoft.Storage` and `Microsoft.Web`.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VirtualNetworkName

The name of the virtual network to which to attach the subnet. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Delegation

_Required_: No

_Type_: List of <a href="delegation.md">Delegation</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeouts.md">Timeouts</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceDelegation

_Required_: No

_Type_: List of <a href="servicedelegation.md">ServiceDelegation</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

