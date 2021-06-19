# TF::AVI::Nsxtsegmentruntime

The NsxtSegmentRuntime resource allows the creation and management of Avi NsxtSegmentRuntime

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AVI::Nsxtsegmentruntime",
    "Properties" : {
        "<a href="#cloudref" title="CloudRef">CloudRef</a>" : <i>String</i>,
        "<a href="#dhcp6ranges" title="Dhcp6Ranges">Dhcp6Ranges</a>" : <i>[ String, ... ]</i>,
        "<a href="#dhcpenabled" title="DhcpEnabled">DhcpEnabled</a>" : <i>Boolean</i>,
        "<a href="#dhcpranges" title="DhcpRanges">DhcpRanges</a>" : <i>[ String, ... ]</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#nwname" title="NwName">NwName</a>" : <i>String</i>,
        "<a href="#nwref" title="NwRef">NwRef</a>" : <i>String</i>,
        "<a href="#opaquenetworkid" title="OpaqueNetworkId">OpaqueNetworkId</a>" : <i>String</i>,
        "<a href="#segmentgw" title="SegmentGw">SegmentGw</a>" : <i>String</i>,
        "<a href="#segmentgw6" title="SegmentGw6">SegmentGw6</a>" : <i>String</i>,
        "<a href="#segmentid" title="SegmentId">SegmentId</a>" : <i>String</i>,
        "<a href="#segname" title="Segname">Segname</a>" : <i>String</i>,
        "<a href="#subnet" title="Subnet">Subnet</a>" : <i>String</i>,
        "<a href="#subnet6" title="Subnet6">Subnet6</a>" : <i>String</i>,
        "<a href="#tenantref" title="TenantRef">TenantRef</a>" : <i>String</i>,
        "<a href="#tier1id" title="Tier1Id">Tier1Id</a>" : <i>String</i>,
        "<a href="#uuid" title="Uuid">Uuid</a>" : <i>String</i>,
        "<a href="#vlanids" title="VlanIds">VlanIds</a>" : <i>[ String, ... ]</i>,
        "<a href="#vrfcontextref" title="VrfContextRef">VrfContextRef</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AVI::Nsxtsegmentruntime
Properties:
    <a href="#cloudref" title="CloudRef">CloudRef</a>: <i>String</i>
    <a href="#dhcp6ranges" title="Dhcp6Ranges">Dhcp6Ranges</a>: <i>
      - String</i>
    <a href="#dhcpenabled" title="DhcpEnabled">DhcpEnabled</a>: <i>Boolean</i>
    <a href="#dhcpranges" title="DhcpRanges">DhcpRanges</a>: <i>
      - String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#nwname" title="NwName">NwName</a>: <i>String</i>
    <a href="#nwref" title="NwRef">NwRef</a>: <i>String</i>
    <a href="#opaquenetworkid" title="OpaqueNetworkId">OpaqueNetworkId</a>: <i>String</i>
    <a href="#segmentgw" title="SegmentGw">SegmentGw</a>: <i>String</i>
    <a href="#segmentgw6" title="SegmentGw6">SegmentGw6</a>: <i>String</i>
    <a href="#segmentid" title="SegmentId">SegmentId</a>: <i>String</i>
    <a href="#segname" title="Segname">Segname</a>: <i>String</i>
    <a href="#subnet" title="Subnet">Subnet</a>: <i>String</i>
    <a href="#subnet6" title="Subnet6">Subnet6</a>: <i>String</i>
    <a href="#tenantref" title="TenantRef">TenantRef</a>: <i>String</i>
    <a href="#tier1id" title="Tier1Id">Tier1Id</a>: <i>String</i>
    <a href="#uuid" title="Uuid">Uuid</a>: <i>String</i>
    <a href="#vlanids" title="VlanIds">VlanIds</a>: <i>
      - String</i>
    <a href="#vrfcontextref" title="VrfContextRef">VrfContextRef</a>: <i>String</i>
</pre>

## Properties

#### CloudRef

Nsxt segment belongs to cloud. It is a reference to an object of type cloud. Field introduced in 20.1.1.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Dhcp6Ranges

V6 dhcp ranges configured in nsxt. Field introduced in 20.1.1.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DhcpEnabled

Ip address management scheme for this segment associated network. Field introduced in 20.1.1.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DhcpRanges

Dhcp ranges configured in nsxt. Field introduced in 20.1.1.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Segment object name. Field introduced in 20.1.1.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NwName

Network name. Field introduced in 20.1.1.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NwRef

Corresponding network object in avi. It is a reference to an object of type network. Field introduced in 20.1.1.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OpaqueNetworkId

Opaque network id. Field introduced in 20.1.1.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SegmentGw

Segment gateway. Field introduced in 20.1.1.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SegmentGw6

V6 segment gateway. Field introduced in 20.1.1.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SegmentId

Segment id. Field introduced in 20.1.1.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Segname

Segment name. Field introduced in 20.1.1.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Subnet

Segment cidr. Field introduced in 20.1.1.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Subnet6

V6 segment cidr. Field introduced in 20.1.1.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TenantRef

Nsxt segment belongs to tenant. It is a reference to an object of type tenant. Field introduced in 20.1.1.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tier1Id

Tier1 router id. Field introduced in 20.1.1.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Uuid

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VlanIds

Segment vlan ids. Field introduced in 20.1.5.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VrfContextRef

Corresponding vrf context object in avi. It is a reference to an object of type vrfcontext. Field introduced in 20.1.1.

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

#### Id

Returns the <code>Id</code> value.

