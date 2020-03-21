# Terraform::AzureRM::CosmosdbAccount

CloudFormation equivalent of azurerm_cosmosdb_account

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AzureRM::CosmosdbAccount",
    "Properties" : {
        "<a href="#enableautomaticfailover" title="EnableAutomaticFailover">EnableAutomaticFailover</a>" : <i>Boolean</i>,
        "<a href="#enablemultiplewritelocations" title="EnableMultipleWriteLocations">EnableMultipleWriteLocations</a>" : <i>Boolean</i>,
        "<a href="#id" title="Id">Id</a>" : <i>String</i>,
        "<a href="#iprangefilter" title="IpRangeFilter">IpRangeFilter</a>" : <i>String</i>,
        "<a href="#isvirtualnetworkfilterenabled" title="IsVirtualNetworkFilterEnabled">IsVirtualNetworkFilterEnabled</a>" : <i>Boolean</i>,
        "<a href="#kind" title="Kind">Kind</a>" : <i>String</i>,
        "<a href="#location" title="Location">Location</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#offertype" title="OfferType">OfferType</a>" : <i>String</i>,
        "<a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tags.md">Tags</a>, ... ]</i>,
        "<a href="#capabilities" title="Capabilities">Capabilities</a>" : <i>[ <a href="capabilities.md">Capabilities</a>, ... ]</i>,
        "<a href="#consistencypolicy" title="ConsistencyPolicy">ConsistencyPolicy</a>" : <i>[ <a href="consistencypolicy.md">ConsistencyPolicy</a>, ... ]</i>,
        "<a href="#geolocation" title="GeoLocation">GeoLocation</a>" : <i>[ <a href="geolocation.md">GeoLocation</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeouts.md">Timeouts</a></i>,
        "<a href="#virtualnetworkrule" title="VirtualNetworkRule">VirtualNetworkRule</a>" : <i>[ <a href="virtualnetworkrule.md">VirtualNetworkRule</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AzureRM::CosmosdbAccount
Properties:
    <a href="#enableautomaticfailover" title="EnableAutomaticFailover">EnableAutomaticFailover</a>: <i>Boolean</i>
    <a href="#enablemultiplewritelocations" title="EnableMultipleWriteLocations">EnableMultipleWriteLocations</a>: <i>Boolean</i>
    <a href="#id" title="Id">Id</a>: <i>String</i>
    <a href="#iprangefilter" title="IpRangeFilter">IpRangeFilter</a>: <i>String</i>
    <a href="#isvirtualnetworkfilterenabled" title="IsVirtualNetworkFilterEnabled">IsVirtualNetworkFilterEnabled</a>: <i>Boolean</i>
    <a href="#kind" title="Kind">Kind</a>: <i>String</i>
    <a href="#location" title="Location">Location</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#offertype" title="OfferType">OfferType</a>: <i>String</i>
    <a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tags.md">Tags</a></i>
    <a href="#capabilities" title="Capabilities">Capabilities</a>: <i>
      - <a href="capabilities.md">Capabilities</a></i>
    <a href="#consistencypolicy" title="ConsistencyPolicy">ConsistencyPolicy</a>: <i>
      - <a href="consistencypolicy.md">ConsistencyPolicy</a></i>
    <a href="#geolocation" title="GeoLocation">GeoLocation</a>: <i>
      - <a href="geolocation.md">GeoLocation</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeouts.md">Timeouts</a></i>
    <a href="#virtualnetworkrule" title="VirtualNetworkRule">VirtualNetworkRule</a>: <i>
      - <a href="virtualnetworkrule.md">VirtualNetworkRule</a></i>
</pre>

## Properties

#### EnableAutomaticFailover

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableMultipleWriteLocations

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Id

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpRangeFilter

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsVirtualNetworkFilterEnabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Kind

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Location

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OfferType

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourceGroupName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

_Required_: No

_Type_: List of <a href="tags.md">Tags</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Capabilities

_Required_: No

_Type_: List of <a href="capabilities.md">Capabilities</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConsistencyPolicy

_Required_: No

_Type_: List of <a href="consistencypolicy.md">ConsistencyPolicy</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GeoLocation

_Required_: No

_Type_: List of <a href="geolocation.md">GeoLocation</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeouts.md">Timeouts</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VirtualNetworkRule

_Required_: No

_Type_: List of <a href="virtualnetworkrule.md">VirtualNetworkRule</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### ConnectionStrings

Returns the <code>ConnectionStrings</code> value.

#### Endpoint

Returns the <code>Endpoint</code> value.

#### PrimaryMasterKey

Returns the <code>PrimaryMasterKey</code> value.

#### PrimaryReadonlyMasterKey

Returns the <code>PrimaryReadonlyMasterKey</code> value.

#### ReadEndpoints

Returns the <code>ReadEndpoints</code> value.

#### SecondaryMasterKey

Returns the <code>SecondaryMasterKey</code> value.

#### SecondaryReadonlyMasterKey

Returns the <code>SecondaryReadonlyMasterKey</code> value.

#### WriteEndpoints

Returns the <code>WriteEndpoints</code> value.

