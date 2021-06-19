# TF::AVI::Vsvip

The VsVip resource allows the creation and management of Avi VsVip

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AVI::Vsvip",
    "Properties" : {
        "<a href="#bgppeerlabels" title="BgpPeerLabels">BgpPeerLabels</a>" : <i>[ String, ... ]</i>,
        "<a href="#cloudref" title="CloudRef">CloudRef</a>" : <i>String</i>,
        "<a href="#eastwestplacement" title="EastWestPlacement">EastWestPlacement</a>" : <i>Boolean</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#tenantref" title="TenantRef">TenantRef</a>" : <i>String</i>,
        "<a href="#tier1lr" title="Tier1Lr">Tier1Lr</a>" : <i>String</i>,
        "<a href="#usestandardalb" title="UseStandardAlb">UseStandardAlb</a>" : <i>Boolean</i>,
        "<a href="#uuid" title="Uuid">Uuid</a>" : <i>String</i>,
        "<a href="#vrfcontextref" title="VrfContextRef">VrfContextRef</a>" : <i>String</i>,
        "<a href="#vsvipcloudconfigcksum" title="VsvipCloudConfigCksum">VsvipCloudConfigCksum</a>" : <i>String</i>,
        "<a href="#dnsinfo" title="DnsInfo">DnsInfo</a>" : <i>[ <a href="dnsinfodefinition.md">DnsInfoDefinition</a>, ... ]</i>,
        "<a href="#ipamselector" title="IpamSelector">IpamSelector</a>" : <i>[ <a href="ipamselectordefinition.md">IpamSelectorDefinition</a>, ... ]</i>,
        "<a href="#markers" title="Markers">Markers</a>" : <i>[ <a href="markersdefinition.md">MarkersDefinition</a>, ... ]</i>,
        "<a href="#vip" title="Vip">Vip</a>" : <i>[ <a href="vipdefinition.md">VipDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AVI::Vsvip
Properties:
    <a href="#bgppeerlabels" title="BgpPeerLabels">BgpPeerLabels</a>: <i>
      - String</i>
    <a href="#cloudref" title="CloudRef">CloudRef</a>: <i>String</i>
    <a href="#eastwestplacement" title="EastWestPlacement">EastWestPlacement</a>: <i>Boolean</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#tenantref" title="TenantRef">TenantRef</a>: <i>String</i>
    <a href="#tier1lr" title="Tier1Lr">Tier1Lr</a>: <i>String</i>
    <a href="#usestandardalb" title="UseStandardAlb">UseStandardAlb</a>: <i>Boolean</i>
    <a href="#uuid" title="Uuid">Uuid</a>: <i>String</i>
    <a href="#vrfcontextref" title="VrfContextRef">VrfContextRef</a>: <i>String</i>
    <a href="#vsvipcloudconfigcksum" title="VsvipCloudConfigCksum">VsvipCloudConfigCksum</a>: <i>String</i>
    <a href="#dnsinfo" title="DnsInfo">DnsInfo</a>: <i>
      - <a href="dnsinfodefinition.md">DnsInfoDefinition</a></i>
    <a href="#ipamselector" title="IpamSelector">IpamSelector</a>: <i>
      - <a href="ipamselectordefinition.md">IpamSelectorDefinition</a></i>
    <a href="#markers" title="Markers">Markers</a>: <i>
      - <a href="markersdefinition.md">MarkersDefinition</a></i>
    <a href="#vip" title="Vip">Vip</a>: <i>
      - <a href="vipdefinition.md">VipDefinition</a></i>
</pre>

## Properties

#### BgpPeerLabels

Select bgp peers, using peer label, for vsvip advertisement. Field introduced in 20.1.5. Maximum of 128 items allowed.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CloudRef

It is a reference to an object of type cloud. Field introduced in 17.1.1.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EastWestPlacement

Force placement on all service engines in the service engine group (container clouds only). Field introduced in 17.1.1. Allowed in basic(allowed values- false) edition, essentials(allowed values- false) edition, enterprise edition.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Name for the vsvip object. Field introduced in 17.1.1.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TenantRef

It is a reference to an object of type tenant. Field introduced in 17.1.1.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tier1Lr

This sets the placement scope of virtualservice to given tier1 logical router in nsx-t. Field introduced in 20.1.1.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UseStandardAlb

This overrides the cloud level default and needs to match the se group value in which it will be used if the se group use_standard_alb value is set. This is only used when fip is used for vs on azure cloud. Field introduced in 18.2.3. Allowed in basic edition, essentials edition, enterprise edition.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Uuid

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VrfContextRef

Virtual routing context that the virtual service is bound to. This is used to provide the isolation of the set of networks the application is attached to. It is a reference to an object of type vrfcontext. Field introduced in 17.1.1.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VsvipCloudConfigCksum

Checksum of cloud configuration for vsvip. Internally set by cloud connector. Field introduced in 17.2.9, 18.1.2.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DnsInfo

_Required_: No

_Type_: List of <a href="dnsinfodefinition.md">DnsInfoDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpamSelector

_Required_: No

_Type_: List of <a href="ipamselectordefinition.md">IpamSelectorDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Markers

_Required_: No

_Type_: List of <a href="markersdefinition.md">MarkersDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vip

_Required_: No

_Type_: List of <a href="vipdefinition.md">VipDefinition</a>

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

