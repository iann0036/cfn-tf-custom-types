# TF::AVI::Network

The Network resource allows the creation and management of Avi Network

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AVI::Network",
    "Properties" : {
        "<a href="#cloudref" title="CloudRef">CloudRef</a>" : <i>String</i>,
        "<a href="#dhcpenabled" title="DhcpEnabled">DhcpEnabled</a>" : <i>Boolean</i>,
        "<a href="#excludediscoveredsubnets" title="ExcludeDiscoveredSubnets">ExcludeDiscoveredSubnets</a>" : <i>Boolean</i>,
        "<a href="#ip6autocfgenabled" title="Ip6AutocfgEnabled">Ip6AutocfgEnabled</a>" : <i>Boolean</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#syncedfromse" title="SyncedFromSe">SyncedFromSe</a>" : <i>Boolean</i>,
        "<a href="#tenantref" title="TenantRef">TenantRef</a>" : <i>String</i>,
        "<a href="#uuid" title="Uuid">Uuid</a>" : <i>String</i>,
        "<a href="#vcenterdvs" title="VcenterDvs">VcenterDvs</a>" : <i>Boolean</i>,
        "<a href="#vrfcontextref" title="VrfContextRef">VrfContextRef</a>" : <i>String</i>,
        "<a href="#attrs" title="Attrs">Attrs</a>" : <i>[ <a href="attrsdefinition.md">AttrsDefinition</a>, ... ]</i>,
        "<a href="#configuredsubnets" title="ConfiguredSubnets">ConfiguredSubnets</a>" : <i>[ <a href="configuredsubnetsdefinition.md">ConfiguredSubnetsDefinition</a>, ... ]</i>,
        "<a href="#markers" title="Markers">Markers</a>" : <i>[ <a href="markersdefinition.md">MarkersDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AVI::Network
Properties:
    <a href="#cloudref" title="CloudRef">CloudRef</a>: <i>String</i>
    <a href="#dhcpenabled" title="DhcpEnabled">DhcpEnabled</a>: <i>Boolean</i>
    <a href="#excludediscoveredsubnets" title="ExcludeDiscoveredSubnets">ExcludeDiscoveredSubnets</a>: <i>Boolean</i>
    <a href="#ip6autocfgenabled" title="Ip6AutocfgEnabled">Ip6AutocfgEnabled</a>: <i>Boolean</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#syncedfromse" title="SyncedFromSe">SyncedFromSe</a>: <i>Boolean</i>
    <a href="#tenantref" title="TenantRef">TenantRef</a>: <i>String</i>
    <a href="#uuid" title="Uuid">Uuid</a>: <i>String</i>
    <a href="#vcenterdvs" title="VcenterDvs">VcenterDvs</a>: <i>Boolean</i>
    <a href="#vrfcontextref" title="VrfContextRef">VrfContextRef</a>: <i>String</i>
    <a href="#attrs" title="Attrs">Attrs</a>: <i>
      - <a href="attrsdefinition.md">AttrsDefinition</a></i>
    <a href="#configuredsubnets" title="ConfiguredSubnets">ConfiguredSubnets</a>: <i>
      - <a href="configuredsubnetsdefinition.md">ConfiguredSubnetsDefinition</a></i>
    <a href="#markers" title="Markers">Markers</a>: <i>
      - <a href="markersdefinition.md">MarkersDefinition</a></i>
</pre>

## Properties

#### CloudRef

It is a reference to an object of type cloud.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DhcpEnabled

Select the ip address management scheme for this network.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExcludeDiscoveredSubnets

When selected, excludes all discovered subnets in this network from consideration for virtual service placement.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ip6AutocfgEnabled

Enable ipv6 auto configuration. Field introduced in 18.1.1.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Name of the object.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SyncedFromSe

Boolean flag to set synced_from_se.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TenantRef

It is a reference to an object of type tenant.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Uuid

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VcenterDvs

Boolean flag to set vcenter_dvs.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VrfContextRef

It is a reference to an object of type vrfcontext.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Attrs

_Required_: No

_Type_: List of <a href="attrsdefinition.md">AttrsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConfiguredSubnets

_Required_: No

_Type_: List of <a href="configuredsubnetsdefinition.md">ConfiguredSubnetsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Markers

_Required_: No

_Type_: List of <a href="markersdefinition.md">MarkersDefinition</a>

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

