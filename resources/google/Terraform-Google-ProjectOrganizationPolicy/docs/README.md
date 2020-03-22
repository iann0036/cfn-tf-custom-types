# Terraform::Google::ProjectOrganizationPolicy

Allows management of Organization policies for a Google Project. For more information see
[the official
documentation](https://cloud.google.com/resource-manager/docs/organization-policy/overview) and
[API](https://cloud.google.com/resource-manager/reference/rest/v1/projects/setOrgPolicy).

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Google::ProjectOrganizationPolicy",
    "Properties" : {
        "<a href="#constraint" title="Constraint">Constraint</a>" : <i>String</i>,
        "<a href="#project" title="Project">Project</a>" : <i>String</i>,
        "<a href="#version" title="Version">Version</a>" : <i>Double</i>,
        "<a href="#booleanpolicy" title="BooleanPolicy">BooleanPolicy</a>" : <i>[ <a href="booleanpolicy.md">BooleanPolicy</a>, ... ]</i>,
        "<a href="#listpolicy" title="ListPolicy">ListPolicy</a>" : <i>[ <a href="listpolicy.md">ListPolicy</a>, ... ]</i>,
        "<a href="#restorepolicy" title="RestorePolicy">RestorePolicy</a>" : <i>[ <a href="restorepolicy.md">RestorePolicy</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeouts.md">Timeouts</a></i>,
        "<a href="#allow" title="Allow">Allow</a>" : <i>[ <a href="allow.md">Allow</a>, ... ]</i>,
        "<a href="#deny" title="Deny">Deny</a>" : <i>[ <a href="deny.md">Deny</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Google::ProjectOrganizationPolicy
Properties:
    <a href="#constraint" title="Constraint">Constraint</a>: <i>String</i>
    <a href="#project" title="Project">Project</a>: <i>String</i>
    <a href="#version" title="Version">Version</a>: <i>Double</i>
    <a href="#booleanpolicy" title="BooleanPolicy">BooleanPolicy</a>: <i>
      - <a href="booleanpolicy.md">BooleanPolicy</a></i>
    <a href="#listpolicy" title="ListPolicy">ListPolicy</a>: <i>
      - <a href="listpolicy.md">ListPolicy</a></i>
    <a href="#restorepolicy" title="RestorePolicy">RestorePolicy</a>: <i>
      - <a href="restorepolicy.md">RestorePolicy</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeouts.md">Timeouts</a></i>
    <a href="#allow" title="Allow">Allow</a>: <i>
      - <a href="allow.md">Allow</a></i>
    <a href="#deny" title="Deny">Deny</a>: <i>
      - <a href="deny.md">Deny</a></i>
</pre>

## Properties

#### Constraint

The name of the Constraint the Policy is configuring, for example, `serviceuser.services`. Check out the [complete list of available constraints](https://cloud.google.com/resource-manager/docs/organization-policy/understanding-constraints#available_constraints).

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Project

The project id of the project to set the policy for.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Version

Version of the Policy. Default version is 0.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BooleanPolicy

_Required_: No

_Type_: List of <a href="booleanpolicy.md">BooleanPolicy</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ListPolicy

_Required_: No

_Type_: List of <a href="listpolicy.md">ListPolicy</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RestorePolicy

_Required_: No

_Type_: List of <a href="restorepolicy.md">RestorePolicy</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeouts.md">Timeouts</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Allow

_Required_: No

_Type_: List of <a href="allow.md">Allow</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Deny

_Required_: No

_Type_: List of <a href="deny.md">Deny</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Etag

Returns the <code>Etag</code> value.

#### Id

Returns the <code>Id</code> value.

#### UpdateTime

Returns the <code>UpdateTime</code> value.

