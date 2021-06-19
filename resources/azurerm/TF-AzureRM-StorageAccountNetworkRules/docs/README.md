# TF::AzureRM::StorageAccountNetworkRules

Manages network rules inside of a Azure Storage Account.

~> **NOTE:** Network Rules can be defined either directly on the `azurerm_storage_account` resource, or using the `azurerm_storage_account_network_rules` resource - but the two cannot be used together. Spurious changes will occur if both are used against the same Storage Account.

~> **NOTE:** Only one `azurerm_storage_account_network_rules` can be tied to an `azurerm_storage_account`. Spurious changes will occur if more than `azurerm_storage_account_network_rules` is tied to the same `azurerm_storage_account`.

~> **NOTE:** Deleting this resource updates the storage account back to the default values it had when the storage account was created.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AzureRM::StorageAccountNetworkRules",
    "Properties" : {
        "<a href="#bypass" title="Bypass">Bypass</a>" : <i>[ String, ... ]</i>,
        "<a href="#defaultaction" title="DefaultAction">DefaultAction</a>" : <i>String</i>,
        "<a href="#iprules" title="IpRules">IpRules</a>" : <i>[ String, ... ]</i>,
        "<a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>" : <i>String</i>,
        "<a href="#storageaccountname" title="StorageAccountName">StorageAccountName</a>" : <i>String</i>,
        "<a href="#virtualnetworksubnetids" title="VirtualNetworkSubnetIds">VirtualNetworkSubnetIds</a>" : <i>[ String, ... ]</i>,
        "<a href="#privatelinkaccess" title="PrivateLinkAccess">PrivateLinkAccess</a>" : <i>[ <a href="privatelinkaccessdefinition.md">PrivateLinkAccessDefinition</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AzureRM::StorageAccountNetworkRules
Properties:
    <a href="#bypass" title="Bypass">Bypass</a>: <i>
      - String</i>
    <a href="#defaultaction" title="DefaultAction">DefaultAction</a>: <i>String</i>
    <a href="#iprules" title="IpRules">IpRules</a>: <i>
      - String</i>
    <a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>: <i>String</i>
    <a href="#storageaccountname" title="StorageAccountName">StorageAccountName</a>: <i>String</i>
    <a href="#virtualnetworksubnetids" title="VirtualNetworkSubnetIds">VirtualNetworkSubnetIds</a>: <i>
      - String</i>
    <a href="#privatelinkaccess" title="PrivateLinkAccess">PrivateLinkAccess</a>: <i>
      - <a href="privatelinkaccessdefinition.md">PrivateLinkAccessDefinition</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### Bypass

Specifies whether traffic is bypassed for Logging/Metrics/AzureServices. Valid options are any combination of `Logging`, `Metrics`, `AzureServices`, or `None`.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefaultAction

Specifies the default action of allow or deny when no other rules match. Valid options are `Deny` or `Allow`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpRules

List of public IP or IP ranges in CIDR Format. Only IPV4 addresses are allowed. Private IP address ranges (as defined in [RFC 1918](https://tools.ietf.org/html/rfc1918#section-3)) are not allowed.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourceGroupName

The name of the resource group in which to create the storage account. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StorageAccountName

Specifies the name of the storage account. Changing this forces a new resource to be created. This must be unique across the entire Azure service, not just within the resource group.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VirtualNetworkSubnetIds

A list of virtual network subnet ids to to secure the storage account.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrivateLinkAccess

_Required_: No

_Type_: List of <a href="privatelinkaccessdefinition.md">PrivateLinkAccessDefinition</a>

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

