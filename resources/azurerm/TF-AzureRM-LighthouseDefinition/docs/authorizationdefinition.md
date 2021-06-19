# TF::AzureRM::LighthouseDefinition AuthorizationDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#delegatedroledefinitionids" title="DelegatedRoleDefinitionIds">DelegatedRoleDefinitionIds</a>" : <i>[ String, ... ]</i>,
    "<a href="#principaldisplayname" title="PrincipalDisplayName">PrincipalDisplayName</a>" : <i>String</i>,
    "<a href="#principalid" title="PrincipalId">PrincipalId</a>" : <i>String</i>,
    "<a href="#roledefinitionid" title="RoleDefinitionId">RoleDefinitionId</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#delegatedroledefinitionids" title="DelegatedRoleDefinitionIds">DelegatedRoleDefinitionIds</a>: <i>
      - String</i>
<a href="#principaldisplayname" title="PrincipalDisplayName">PrincipalDisplayName</a>: <i>String</i>
<a href="#principalid" title="PrincipalId">PrincipalId</a>: <i>String</i>
<a href="#roledefinitionid" title="RoleDefinitionId">RoleDefinitionId</a>: <i>String</i>
</pre>

## Properties

#### DelegatedRoleDefinitionIds

The set of role definition ids which define all the permissions that the principal id can assign.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrincipalDisplayName

The display name of the security group/service principal/user that would be assigned permissions to the projected subscription.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrincipalId

Principal ID of the security group/service principal/user that would be assigned permissions to the projected subscription.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RoleDefinitionId

The role definition identifier. This role will define the permissions that are granted to the principal. This cannot be an `Owner` role.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

