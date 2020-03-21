# Terraform::Panos::PanoramaBgpAggregateSuppressFilter

This resource allows you to add/update/delete a Panorama route suppression filter for a
BGP address aggregation rule.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Panos::PanoramaBgpAggregateSuppressFilter",
    "Properties" : {
        "<a href="#aspathregex" title="AsPathRegex">AsPathRegex</a>" : <i>String</i>,
        "<a href="#bgpaggregate" title="BgpAggregate">BgpAggregate</a>" : <i>String</i>,
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
        "<a href="#virtualrouter" title="VirtualRouter">VirtualRouter</a>" : <i>String</i>,
        "<a href="#addressprefix" title="AddressPrefix">AddressPrefix</a>" : <i>[ <a href="addressprefix.md">AddressPrefix</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Panos::PanoramaBgpAggregateSuppressFilter
Properties:
    <a href="#aspathregex" title="AsPathRegex">AsPathRegex</a>: <i>String</i>
    <a href="#bgpaggregate" title="BgpAggregate">BgpAggregate</a>: <i>String</i>
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
    <a href="#addressprefix" title="AddressPrefix">AddressPrefix</a>: <i>
      - <a href="addressprefix.md">AddressPrefix</a></i>
</pre>

## Properties

#### AsPathRegex

AS path to match.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BgpAggregate

The BGP address aggregation rule.

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
values are `unicast`, `multicast`, or `both`.

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

#### AddressPrefix

_Required_: No

_Type_: List of <a href="addressprefix.md">AddressPrefix</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

