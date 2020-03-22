# Terraform::Panos::PanoramaBgpConditionalAdvAdvertiseFilter

This resource allows you to add/update/delete a Panorama advertise filter for a
BGP conditional advertisement.

~> **Note:** A BGP conditional advertisement is valid only if there is at least
one non-exist filter and one advertise filter attached.  This filter must be paired
with the other in order for the configuration to be valid.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Panos::PanoramaBgpConditionalAdvAdvertiseFilter",
    "Properties" : {
        "<a href="#addressprefixes" title="AddressPrefixes">AddressPrefixes</a>" : <i>[ String, ... ]</i>,
        "<a href="#aspathregex" title="AsPathRegex">AsPathRegex</a>" : <i>String</i>,
        "<a href="#bgpconditionaladv" title="BgpConditionalAdv">BgpConditionalAdv</a>" : <i>String</i>,
        "<a href="#communityregex" title="CommunityRegex">CommunityRegex</a>" : <i>String</i>,
        "<a href="#enable" title="Enable">Enable</a>" : <i>Boolean</i>,
        "<a href="#extendedcommunityregex" title="ExtendedCommunityRegex">ExtendedCommunityRegex</a>" : <i>String</i>,
        "<a href="#frompeers" title="FromPeers">FromPeers</a>" : <i>[ String, ... ]</i>,
        "<a href="#med" title="Med">Med</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#nexthops" title="NextHops">NextHops</a>" : <i>[ String, ... ]</i>,
        "<a href="#routetable" title="RouteTable">RouteTable</a>" : <i>String</i>,
        "<a href="#template" title="Template">Template</a>" : <i>String</i>,
        "<a href="#templatestack" title="TemplateStack">TemplateStack</a>" : <i>String</i>,
        "<a href="#virtualrouter" title="VirtualRouter">VirtualRouter</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Panos::PanoramaBgpConditionalAdvAdvertiseFilter
Properties:
    <a href="#addressprefixes" title="AddressPrefixes">AddressPrefixes</a>: <i>
      - String</i>
    <a href="#aspathregex" title="AsPathRegex">AsPathRegex</a>: <i>String</i>
    <a href="#bgpconditionaladv" title="BgpConditionalAdv">BgpConditionalAdv</a>: <i>String</i>
    <a href="#communityregex" title="CommunityRegex">CommunityRegex</a>: <i>String</i>
    <a href="#enable" title="Enable">Enable</a>: <i>Boolean</i>
    <a href="#extendedcommunityregex" title="ExtendedCommunityRegex">ExtendedCommunityRegex</a>: <i>String</i>
    <a href="#frompeers" title="FromPeers">FromPeers</a>: <i>
      - String</i>
    <a href="#med" title="Med">Med</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#nexthops" title="NextHops">NextHops</a>: <i>
      - String</i>
    <a href="#routetable" title="RouteTable">RouteTable</a>: <i>String</i>
    <a href="#template" title="Template">Template</a>: <i>String</i>
    <a href="#templatestack" title="TemplateStack">TemplateStack</a>: <i>String</i>
    <a href="#virtualrouter" title="VirtualRouter">VirtualRouter</a>: <i>String</i>
</pre>

## Properties

#### AddressPrefixes

List of matching address prefixes.

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AsPathRegex

AS path to match.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BgpConditionalAdv

The BGP conditional advertisement to add
this filter to.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CommunityRegex

Community to match.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Enable

Enable or not (default: `true`).

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExtendedCommunityRegex

Extended community to match.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FromPeers

List of peers that advertised the route entry.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Med

Match MED.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NextHops

List of next hop attributes.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RouteTable

Route table to match rule.  Valid
values are `unicast`, `multicast`, or `both`.  As of PAN-OS 8.1, there doesn't
seem to be a way to configure this in the GUI, it is always set to `unicast`.
Thus, if you're running this resource against PAN-OS 8.0+, the appropriate
thing to do is set this value to `unicast` as well to match the GUI functionality.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Template

The template name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TemplateStack

The template stack name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VirtualRouter

The virtual router to add this filter to.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the Id.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Id

Returns the <code>Id</code> value.

