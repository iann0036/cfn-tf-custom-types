# TF::Google::ComputeRouterPeer

BGP information that must be configured into the routing stack to
establish BGP peering. This information must specify the peer ASN
and either the interface name, IP address, or peer IP address.
Please refer to RFC4273.


To get more information about RouterBgpPeer, see:

* [API documentation](https://cloud.google.com/compute/docs/reference/rest/v1/routers)
* How-to Guides
    * [Google Cloud Router](https://cloud.google.com/router/docs/)

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Google::ComputeRouterPeer",
    "Properties" : {
        "<a href="#advertisemode" title="AdvertiseMode">AdvertiseMode</a>" : <i>String</i>,
        "<a href="#advertisedgroups" title="AdvertisedGroups">AdvertisedGroups</a>" : <i>[ String, ... ]</i>,
        "<a href="#advertisedroutepriority" title="AdvertisedRoutePriority">AdvertisedRoutePriority</a>" : <i>Double</i>,
        "<a href="#interface" title="Interface">Interface</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#peerasn" title="PeerAsn">PeerAsn</a>" : <i>Double</i>,
        "<a href="#peeripaddress" title="PeerIpAddress">PeerIpAddress</a>" : <i>String</i>,
        "<a href="#project" title="Project">Project</a>" : <i>String</i>,
        "<a href="#region" title="Region">Region</a>" : <i>String</i>,
        "<a href="#router" title="Router">Router</a>" : <i>String</i>,
        "<a href="#advertisedipranges" title="AdvertisedIpRanges">AdvertisedIpRanges</a>" : <i>[ <a href="advertisediprangesdefinition.md">AdvertisedIpRangesDefinition</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Google::ComputeRouterPeer
Properties:
    <a href="#advertisemode" title="AdvertiseMode">AdvertiseMode</a>: <i>String</i>
    <a href="#advertisedgroups" title="AdvertisedGroups">AdvertisedGroups</a>: <i>
      - String</i>
    <a href="#advertisedroutepriority" title="AdvertisedRoutePriority">AdvertisedRoutePriority</a>: <i>Double</i>
    <a href="#interface" title="Interface">Interface</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#peerasn" title="PeerAsn">PeerAsn</a>: <i>Double</i>
    <a href="#peeripaddress" title="PeerIpAddress">PeerIpAddress</a>: <i>String</i>
    <a href="#project" title="Project">Project</a>: <i>String</i>
    <a href="#region" title="Region">Region</a>: <i>String</i>
    <a href="#router" title="Router">Router</a>: <i>String</i>
    <a href="#advertisedipranges" title="AdvertisedIpRanges">AdvertisedIpRanges</a>: <i>
      - <a href="advertisediprangesdefinition.md">AdvertisedIpRangesDefinition</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### AdvertiseMode

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AdvertisedGroups

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AdvertisedRoutePriority

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Interface

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PeerAsn

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PeerIpAddress

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Project

The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Region

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Router

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AdvertisedIpRanges

_Required_: No

_Type_: List of <a href="advertisediprangesdefinition.md">AdvertisedIpRangesDefinition</a>

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

#### IpAddress

Returns the <code>IpAddress</code> value.

#### ManagementType

Returns the <code>ManagementType</code> value.

