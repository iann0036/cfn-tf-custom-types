# Terraform::AzureRM::CosmosdbAccount

CloudFormation equivalent of azurerm_cosmosdb_account

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AzureRM::CosmosdbAccount",
    "Properties" : {
        "<a href="#tfcfnid" title="tfcfnid">tfcfnid</a>" : <i>String</i>,
        "<a href="#connectionstrings" title="ConnectionStrings">ConnectionStrings</a>" : <i>[ String, ... ]</i>,
        "<a href="#enableautomaticfailover" title="EnableAutomaticFailover">EnableAutomaticFailover</a>" : <i>Boolean</i>,
        "<a href="#enablemultiplewritelocations" title="EnableMultipleWriteLocations">EnableMultipleWriteLocations</a>" : <i>Boolean</i>,
        "<a href="#endpoint" title="Endpoint">Endpoint</a>" : <i>String</i>,
        "<a href="#iprangefilter" title="IpRangeFilter">IpRangeFilter</a>" : <i>String</i>,
        "<a href="#isvirtualnetworkfilterenabled" title="IsVirtualNetworkFilterEnabled">IsVirtualNetworkFilterEnabled</a>" : <i>Boolean</i>,
        "<a href="#kind" title="Kind">Kind</a>" : <i>String</i>,
        "<a href="#location" title="Location">Location</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#offertype" title="OfferType">OfferType</a>" : <i>String</i>,
        "<a href="#primarymasterkey" title="PrimaryMasterKey">PrimaryMasterKey</a>" : <i>String</i>,
        "<a href="#primaryreadonlymasterkey" title="PrimaryReadonlyMasterKey">PrimaryReadonlyMasterKey</a>" : <i>String</i>,
        "<a href="#readendpoints" title="ReadEndpoints">ReadEndpoints</a>" : <i>[ String, ... ]</i>,
        "<a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>" : <i>String</i>,
        "<a href="#secondarymasterkey" title="SecondaryMasterKey">SecondaryMasterKey</a>" : <i>String</i>,
        "<a href="#secondaryreadonlymasterkey" title="SecondaryReadonlyMasterKey">SecondaryReadonlyMasterKey</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ &lt;a href=&#34;tags.md&#34;&gt;Tags&lt;/a&gt;, ... ]</i>,
        "<a href="#writeendpoints" title="WriteEndpoints">WriteEndpoints</a>" : <i>[ String, ... ]</i>,
        "<a href="#capabilities" title="Capabilities">Capabilities</a>" : <i>[ &lt;a href=&#34;capabilities.md&#34;&gt;Capabilities&lt;/a&gt;, ... ]</i>,
        "<a href="#consistencypolicy" title="ConsistencyPolicy">ConsistencyPolicy</a>" : <i>[ &lt;a href=&#34;consistencypolicy.md&#34;&gt;ConsistencyPolicy&lt;/a&gt;, ... ]</i>,
        "<a href="#geolocation" title="GeoLocation">GeoLocation</a>" : <i>[ &lt;a href=&#34;geolocation.md&#34;&gt;GeoLocation&lt;/a&gt;, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i>&lt;a href=&#34;timeouts.md&#34;&gt;Timeouts&lt;/a&gt;</i>,
        "<a href="#virtualnetworkrule" title="VirtualNetworkRule">VirtualNetworkRule</a>" : <i>[ &lt;a href=&#34;virtualnetworkrule.md&#34;&gt;VirtualNetworkRule&lt;/a&gt;, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AzureRM::CosmosdbAccount
Properties:
    <a href="#tfcfnid" title="tfcfnid">tfcfnid</a>: <i>String</i>
    <a href="#connectionstrings" title="ConnectionStrings">ConnectionStrings</a>: <i>
      - String</i>
    <a href="#enableautomaticfailover" title="EnableAutomaticFailover">EnableAutomaticFailover</a>: <i>Boolean</i>
    <a href="#enablemultiplewritelocations" title="EnableMultipleWriteLocations">EnableMultipleWriteLocations</a>: <i>Boolean</i>
    <a href="#endpoint" title="Endpoint">Endpoint</a>: <i>String</i>
    <a href="#iprangefilter" title="IpRangeFilter">IpRangeFilter</a>: <i>String</i>
    <a href="#isvirtualnetworkfilterenabled" title="IsVirtualNetworkFilterEnabled">IsVirtualNetworkFilterEnabled</a>: <i>Boolean</i>
    <a href="#kind" title="Kind">Kind</a>: <i>String</i>
    <a href="#location" title="Location">Location</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#offertype" title="OfferType">OfferType</a>: <i>String</i>
    <a href="#primarymasterkey" title="PrimaryMasterKey">PrimaryMasterKey</a>: <i>String</i>
    <a href="#primaryreadonlymasterkey" title="PrimaryReadonlyMasterKey">PrimaryReadonlyMasterKey</a>: <i>String</i>
    <a href="#readendpoints" title="ReadEndpoints">ReadEndpoints</a>: <i>
      - String</i>
    <a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>: <i>String</i>
    <a href="#secondarymasterkey" title="SecondaryMasterKey">SecondaryMasterKey</a>: <i>String</i>
    <a href="#secondaryreadonlymasterkey" title="SecondaryReadonlyMasterKey">SecondaryReadonlyMasterKey</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - &lt;a href=&#34;tags.md&#34;&gt;Tags&lt;/a&gt;</i>
    <a href="#writeendpoints" title="WriteEndpoints">WriteEndpoints</a>: <i>
      - String</i>
    <a href="#capabilities" title="Capabilities">Capabilities</a>: <i>
      - &lt;a href=&#34;capabilities.md&#34;&gt;Capabilities&lt;/a&gt;</i>
    <a href="#consistencypolicy" title="ConsistencyPolicy">ConsistencyPolicy</a>: <i>
      - &lt;a href=&#34;consistencypolicy.md&#34;&gt;ConsistencyPolicy&lt;/a&gt;</i>
    <a href="#geolocation" title="GeoLocation">GeoLocation</a>: <i>
      - &lt;a href=&#34;geolocation.md&#34;&gt;GeoLocation&lt;/a&gt;</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i>&lt;a href=&#34;timeouts.md&#34;&gt;Timeouts&lt;/a&gt;</i>
    <a href="#virtualnetworkrule" title="VirtualNetworkRule">VirtualNetworkRule</a>: <i>
      - &lt;a href=&#34;virtualnetworkrule.md&#34;&gt;VirtualNetworkRule&lt;/a&gt;</i>
</pre>

## Properties

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConnectionStrings

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableAutomaticFailover

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableMultipleWriteLocations

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Endpoint

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

#### PrimaryMasterKey

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrimaryReadonlyMasterKey

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReadEndpoints

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourceGroupName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecondaryMasterKey

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecondaryReadonlyMasterKey

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

_Required_: No

_Type_: List of &lt;a href=&#34;tags.md&#34;&gt;Tags&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WriteEndpoints

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Capabilities

_Required_: No

_Type_: List of &lt;a href=&#34;capabilities.md&#34;&gt;Capabilities&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConsistencyPolicy

_Required_: No

_Type_: List of &lt;a href=&#34;consistencypolicy.md&#34;&gt;ConsistencyPolicy&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GeoLocation

_Required_: No

_Type_: List of &lt;a href=&#34;geolocation.md&#34;&gt;GeoLocation&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: &lt;a href=&#34;timeouts.md&#34;&gt;Timeouts&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VirtualNetworkRule

_Required_: No

_Type_: List of &lt;a href=&#34;virtualnetworkrule.md&#34;&gt;VirtualNetworkRule&lt;/a&gt;

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

Returns the &lt;code&gt;ConnectionStrings&lt;/code&gt; value.

#### Endpoint

Returns the &lt;code&gt;Endpoint&lt;/code&gt; value.

#### PrimaryMasterKey

Returns the &lt;code&gt;PrimaryMasterKey&lt;/code&gt; value.

#### PrimaryReadonlyMasterKey

Returns the &lt;code&gt;PrimaryReadonlyMasterKey&lt;/code&gt; value.

#### ReadEndpoints

Returns the &lt;code&gt;ReadEndpoints&lt;/code&gt; value.

#### SecondaryMasterKey

Returns the &lt;code&gt;SecondaryMasterKey&lt;/code&gt; value.

#### SecondaryReadonlyMasterKey

Returns the &lt;code&gt;SecondaryReadonlyMasterKey&lt;/code&gt; value.

#### WriteEndpoints

Returns the &lt;code&gt;WriteEndpoints&lt;/code&gt; value.

