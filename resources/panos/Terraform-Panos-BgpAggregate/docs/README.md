# Terraform::Panos::BgpAggregate

This resource allows you to add/update/delete BGP address aggregation
rules.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Panos::BgpAggregate",
    "Properties" : {
        "<a href="#aspathlimit" title="AsPathLimit">AsPathLimit</a>" : <i>Double</i>,
        "<a href="#aspathtype" title="AsPathType">AsPathType</a>" : <i>String</i>,
        "<a href="#aspathvalue" title="AsPathValue">AsPathValue</a>" : <i>String</i>,
        "<a href="#asset" title="AsSet">AsSet</a>" : <i>Boolean</i>,
        "<a href="#communitytype" title="CommunityType">CommunityType</a>" : <i>String</i>,
        "<a href="#communityvalue" title="CommunityValue">CommunityValue</a>" : <i>String</i>,
        "<a href="#enable" title="Enable">Enable</a>" : <i>Boolean</i>,
        "<a href="#extendedcommunitytype" title="ExtendedCommunityType">ExtendedCommunityType</a>" : <i>String</i>,
        "<a href="#extendedcommunityvalue" title="ExtendedCommunityValue">ExtendedCommunityValue</a>" : <i>String</i>,
        "<a href="#localpreference" title="LocalPreference">LocalPreference</a>" : <i>String</i>,
        "<a href="#med" title="Med">Med</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#nexthop" title="NextHop">NextHop</a>" : <i>String</i>,
        "<a href="#origin" title="Origin">Origin</a>" : <i>String</i>,
        "<a href="#prefix" title="Prefix">Prefix</a>" : <i>String</i>,
        "<a href="#summary" title="Summary">Summary</a>" : <i>Boolean</i>,
        "<a href="#virtualrouter" title="VirtualRouter">VirtualRouter</a>" : <i>String</i>,
        "<a href="#weight" title="Weight">Weight</a>" : <i>Double</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Panos::BgpAggregate
Properties:
    <a href="#aspathlimit" title="AsPathLimit">AsPathLimit</a>: <i>Double</i>
    <a href="#aspathtype" title="AsPathType">AsPathType</a>: <i>String</i>
    <a href="#aspathvalue" title="AsPathValue">AsPathValue</a>: <i>String</i>
    <a href="#asset" title="AsSet">AsSet</a>: <i>Boolean</i>
    <a href="#communitytype" title="CommunityType">CommunityType</a>: <i>String</i>
    <a href="#communityvalue" title="CommunityValue">CommunityValue</a>: <i>String</i>
    <a href="#enable" title="Enable">Enable</a>: <i>Boolean</i>
    <a href="#extendedcommunitytype" title="ExtendedCommunityType">ExtendedCommunityType</a>: <i>String</i>
    <a href="#extendedcommunityvalue" title="ExtendedCommunityValue">ExtendedCommunityValue</a>: <i>String</i>
    <a href="#localpreference" title="LocalPreference">LocalPreference</a>: <i>String</i>
    <a href="#med" title="Med">Med</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#nexthop" title="NextHop">NextHop</a>: <i>String</i>
    <a href="#origin" title="Origin">Origin</a>: <i>String</i>
    <a href="#prefix" title="Prefix">Prefix</a>: <i>String</i>
    <a href="#summary" title="Summary">Summary</a>: <i>Boolean</i>
    <a href="#virtualrouter" title="VirtualRouter">VirtualRouter</a>: <i>String</i>
    <a href="#weight" title="Weight">Weight</a>: <i>Double</i>
</pre>

## Properties

#### AsPathLimit

Add AS path limit attribute if it does
not exist.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AsPathType

AS path update options.  Valid values are
`none` (default) or `prepend`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AsPathValue

For `as_path_type` of `prepend`, the value to
prepend.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AsSet

Generate AS-set attribute.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CommunityType

Community update options.  Valid values are
`none` (default), `remove-all`, `remove-regex`, `append`, or `overwrite`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CommunityValue

If `community_type` is `remove-regex`,
`append`, or `overwrite`, the value associated with that setting.  For the
`append` and `overwrite` types specifically, valid values are
`no-export`, `no-advertise`, `local-as`, or `nopeer`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Enable

Enable this rule (default: `true`).

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExtendedCommunityType

Extended community update options.  Valid
values are `none` (default), `remove-all`, `remove-regex`, `append`, or `overwrite`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExtendedCommunityValue

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LocalPreference

New local preference value.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Med

New MED value.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The rule name.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NextHop

Next hop address.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Origin

New route origin.  Valid values are `incomplete`
(default), `igp`, or `egp`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Prefix

Aggregating address prefix.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Summary

Summarize route.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VirtualRouter

The virtual router to put the rule into.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Weight

New weight value.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

