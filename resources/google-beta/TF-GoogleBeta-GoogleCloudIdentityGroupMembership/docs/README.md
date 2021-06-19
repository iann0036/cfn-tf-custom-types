# TF::GoogleBeta::GoogleCloudIdentityGroupMembership

CloudFormation equivalent of google_cloud_identity_group_membership

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::GoogleBeta::GoogleCloudIdentityGroupMembership",
    "Properties" : {
        "<a href="#group" title="Group">Group</a>" : <i>String</i>,
        "<a href="#memberkey" title="MemberKey">MemberKey</a>" : <i>[ <a href="memberkeydefinition.md">MemberKeyDefinition</a>, ... ]</i>,
        "<a href="#preferredmemberkey" title="PreferredMemberKey">PreferredMemberKey</a>" : <i>[ <a href="preferredmemberkeydefinition.md">PreferredMemberKeyDefinition</a>, ... ]</i>,
        "<a href="#roles" title="Roles">Roles</a>" : <i>[ <a href="rolesdefinition.md">RolesDefinition</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::GoogleBeta::GoogleCloudIdentityGroupMembership
Properties:
    <a href="#group" title="Group">Group</a>: <i>String</i>
    <a href="#memberkey" title="MemberKey">MemberKey</a>: <i>
      - <a href="memberkeydefinition.md">MemberKeyDefinition</a></i>
    <a href="#preferredmemberkey" title="PreferredMemberKey">PreferredMemberKey</a>: <i>
      - <a href="preferredmemberkeydefinition.md">PreferredMemberKeyDefinition</a></i>
    <a href="#roles" title="Roles">Roles</a>: <i>
      - <a href="rolesdefinition.md">RolesDefinition</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### Group

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MemberKey

_Required_: No

_Type_: List of <a href="memberkeydefinition.md">MemberKeyDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PreferredMemberKey

_Required_: No

_Type_: List of <a href="preferredmemberkeydefinition.md">PreferredMemberKeyDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Roles

_Required_: No

_Type_: List of <a href="rolesdefinition.md">RolesDefinition</a>

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

#### CreateTime

Returns the <code>CreateTime</code> value.

#### Id

Returns the <code>Id</code> value.

#### Name

Returns the <code>Name</code> value.

#### Type

Returns the <code>Type</code> value.

#### UpdateTime

Returns the <code>UpdateTime</code> value.

