# TF::AzureDevOps::GroupMembership

Manages group membership within Azure DevOps.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AzureDevOps::GroupMembership",
    "Properties" : {
        "<a href="#group" title="Group">Group</a>" : <i>String</i>,
        "<a href="#members" title="Members">Members</a>" : <i>[ String, ... ]</i>,
        "<a href="#mode" title="Mode">Mode</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AzureDevOps::GroupMembership
Properties:
    <a href="#group" title="Group">Group</a>: <i>String</i>
    <a href="#members" title="Members">Members</a>: <i>
      - String</i>
    <a href="#mode" title="Mode">Mode</a>: <i>String</i>
</pre>

## Properties

#### Group

The descriptor of the group being managed.
- `members` - (Required) A list of user or group descriptors that will become members of the group.
> NOTE: It's possible to define group members both within the `azuredevops_group_membership resource` via the members block and by using the `azuredevops_group` resource. However it's not possible to use both methods to manage group members, since there'll be conflicts.
- `mode` - (Optional) The mode how the resource manages group members.
- `mode == add`: the resource will ensure that all specified members will be part of the referenced group
- `mode == overwrite`: the resource will replace all existing members with the members specified within the `members` block
> NOTE: To clear all members from a group, specify an empty list of descriptors in the `members` attribute and set the `mode` member to `overwrite`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Members

A list of user or group descriptors that will become members of the group.
> NOTE: It's possible to define group members both within the `azuredevops_group_membership resource` via the members block and by using the `azuredevops_group` resource. However it's not possible to use both methods to manage group members, since there'll be conflicts.
- `mode` - (Optional) The mode how the resource manages group members.
- `mode == add`: the resource will ensure that all specified members will be part of the referenced group
- `mode == overwrite`: the resource will replace all existing members with the members specified within the `members` block
> NOTE: To clear all members from a group, specify an empty list of descriptors in the `members` attribute and set the `mode` member to `overwrite`.

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Mode

The mode how the resource manages group members.
- `mode == add`: the resource will ensure that all specified members will be part of the referenced group
- `mode == overwrite`: the resource will replace all existing members with the members specified within the `members` block
> NOTE: To clear all members from a group, specify an empty list of descriptors in the `members` attribute and set the `mode` member to `overwrite`.

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

