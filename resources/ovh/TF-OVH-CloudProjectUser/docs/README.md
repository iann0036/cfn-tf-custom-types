# TF::OVH::CloudProjectUser

Creates a user in a public cloud project.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::OVH::CloudProjectUser",
    "Properties" : {
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#openstackrc" title="OpenstackRc">OpenstackRc</a>" : <i>[ <a href="openstackrcdefinition.md">OpenstackRcDefinition</a>, ... ]</i>,
        "<a href="#rolename" title="RoleName">RoleName</a>" : <i>String</i>,
        "<a href="#rolenames" title="RoleNames">RoleNames</a>" : <i>[ String, ... ]</i>,
        "<a href="#servicename" title="ServiceName">ServiceName</a>" : <i>String</i>,
    }
}
</pre>

### YAML

<pre>
Type: TF::OVH::CloudProjectUser
Properties:
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#openstackrc" title="OpenstackRc">OpenstackRc</a>: <i>
      - <a href="openstackrcdefinition.md">OpenstackRcDefinition</a></i>
    <a href="#rolename" title="RoleName">RoleName</a>: <i>String</i>
    <a href="#rolenames" title="RoleNames">RoleNames</a>: <i>
      - String</i>
    <a href="#servicename" title="ServiceName">ServiceName</a>: <i>String</i>
</pre>

## Properties

#### Description

A description associated with the user.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OpenstackRc

_Required_: No

_Type_: List of <a href="openstackrcdefinition.md">OpenstackRcDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RoleName

The name of a role. See `role_names`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RoleNames

A list of role names. Values can be:
- administrator,
- ai_training_operator
- authentication
- backup_operator
- compute_operator
- image_operator
- infrastructure_supervisor
- network_operator
- network_security_operator
- objectstore_operator
- volume_operator.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceName

The id of the public cloud project. If omitted,
the `OVH_CLOUD_PROJECT_SERVICE` environment variable is used.

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

#### CreationDate

Returns the <code>CreationDate</code> value.

#### Id

Returns the <code>Id</code> value.

#### Password

Returns the <code>Password</code> value.

#### Roles

Returns the <code>Roles</code> value.

#### Status

Returns the <code>Status</code> value.

#### Username

Returns the <code>Username</code> value.

