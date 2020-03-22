# Terraform::Panos::PanoramaBgpRedistRule

This resource allows you to add/update/delete a Panorama BGP redistribution rule.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Panos::PanoramaBgpRedistRule",
    "Properties" : {
        "<a href="#addressfamily" title="AddressFamily">AddressFamily</a>" : <i>String</i>,
        "<a href="#enable" title="Enable">Enable</a>" : <i>Boolean</i>,
        "<a href="#metric" title="Metric">Metric</a>" : <i>Double</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#routetable" title="RouteTable">RouteTable</a>" : <i>String</i>,
        "<a href="#setaspathlimit" title="SetAsPathLimit">SetAsPathLimit</a>" : <i>Double</i>,
        "<a href="#setcommunities" title="SetCommunities">SetCommunities</a>" : <i>[ String, ... ]</i>,
        "<a href="#setextendedcommunities" title="SetExtendedCommunities">SetExtendedCommunities</a>" : <i>[ String, ... ]</i>,
        "<a href="#setlocalpreference" title="SetLocalPreference">SetLocalPreference</a>" : <i>String</i>,
        "<a href="#setmed" title="SetMed">SetMed</a>" : <i>String</i>,
        "<a href="#setorigin" title="SetOrigin">SetOrigin</a>" : <i>String</i>,
        "<a href="#template" title="Template">Template</a>" : <i>String</i>,
        "<a href="#templatestack" title="TemplateStack">TemplateStack</a>" : <i>String</i>,
        "<a href="#virtualrouter" title="VirtualRouter">VirtualRouter</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Panos::PanoramaBgpRedistRule
Properties:
    <a href="#addressfamily" title="AddressFamily">AddressFamily</a>: <i>String</i>
    <a href="#enable" title="Enable">Enable</a>: <i>Boolean</i>
    <a href="#metric" title="Metric">Metric</a>: <i>Double</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#routetable" title="RouteTable">RouteTable</a>: <i>String</i>
    <a href="#setaspathlimit" title="SetAsPathLimit">SetAsPathLimit</a>: <i>Double</i>
    <a href="#setcommunities" title="SetCommunities">SetCommunities</a>: <i>
      - String</i>
    <a href="#setextendedcommunities" title="SetExtendedCommunities">SetExtendedCommunities</a>: <i>
      - String</i>
    <a href="#setlocalpreference" title="SetLocalPreference">SetLocalPreference</a>: <i>String</i>
    <a href="#setmed" title="SetMed">SetMed</a>: <i>String</i>
    <a href="#setorigin" title="SetOrigin">SetOrigin</a>: <i>String</i>
    <a href="#template" title="Template">Template</a>: <i>String</i>
    <a href="#templatestack" title="TemplateStack">TemplateStack</a>: <i>String</i>
    <a href="#virtualrouter" title="VirtualRouter">VirtualRouter</a>: <i>String</i>
</pre>

## Properties

#### AddressFamily

The address family.  Valid values are
`ipv4` (default) or `ipv6`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Enable

Enable this rule or not (default: `true`).

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Metric

Metric value.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

A subnet or a redistribution profile.

_Required_: Yes

_Type_: String

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

#### SetAsPathLimit

Add the AS_PATHLIMIT path attribute.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SetCommunities

List of COMMUNITY path attributes to add.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SetExtendedCommunities

List of EXTENDED COMMUNITY path attributes to add.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SetLocalPreference

Add the LOCAL_PREF path attribute.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SetMed

Add the MULTI_EXIT_DISC path attribute.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SetOrigin

Add the origin path attribute.  Valid values are
`incomplete` (default), `igp`, or `egp`.

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

The virtual router to add this BGP
redist rule to.

_Required_: Yes

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

