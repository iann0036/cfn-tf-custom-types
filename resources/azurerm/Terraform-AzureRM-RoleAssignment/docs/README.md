# Terraform::AzureRM::RoleAssignment

Assigns a given Principal (User or Application) to a given Role.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AzureRM::RoleAssignment",
    "Properties" : {
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#principalid" title="PrincipalId">PrincipalId</a>" : <i>String</i>,
        "<a href="#roledefinitionid" title="RoleDefinitionId">RoleDefinitionId</a>" : <i>String</i>,
        "<a href="#roledefinitionname" title="RoleDefinitionName">RoleDefinitionName</a>" : <i>String</i>,
        "<a href="#scope" title="Scope">Scope</a>" : <i>String</i>,
        "<a href="#skipserviceprincipalaadcheck" title="SkipServicePrincipalAadCheck">SkipServicePrincipalAadCheck</a>" : <i>Boolean</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeouts.md">Timeouts</a></i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AzureRM::RoleAssignment
Properties:
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#principalid" title="PrincipalId">PrincipalId</a>: <i>String</i>
    <a href="#roledefinitionid" title="RoleDefinitionId">RoleDefinitionId</a>: <i>String</i>
    <a href="#roledefinitionname" title="RoleDefinitionName">RoleDefinitionName</a>: <i>String</i>
    <a href="#scope" title="Scope">Scope</a>: <i>String</i>
    <a href="#skipserviceprincipalaadcheck" title="SkipServicePrincipalAadCheck">SkipServicePrincipalAadCheck</a>: <i>Boolean</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeouts.md">Timeouts</a></i>
</pre>

## Properties

#### Name

A unique UUID/GUID for this Role Assignment - one will be generated if not specified. Changing this forces a new resource to be created.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrincipalId

The ID of the Principal (User, Group, Service Principal, or Application) to assign the Role Definition to. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RoleDefinitionId

The Scoped-ID of the Role Definition. Changing this forces a new resource to be created. Conflicts with `role_definition_name`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RoleDefinitionName

The name of a built-in Role. Changing this forces a new resource to be created. Conflicts with `role_definition_id`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Scope

The scope at which the Role Assignment applies to, such as `/subscriptions/0b1f6471-1bf0-4dda-aec3-111122223333`, `/subscriptions/0b1f6471-1bf0-4dda-aec3-111122223333/resourceGroups/myGroup`, or `/subscriptions/0b1f6471-1bf0-4dda-aec3-111122223333/resourceGroups/myGroup/providers/Microsoft.Compute/virtualMachines/myVM`, or `/providers/Microsoft.Management/managementGroups/myMG`. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SkipServicePrincipalAadCheck

If the `principal_id` is a newly provisioned `Service Principal` set this value to `true` to skip the `Azure Active Directory` check which may fail due to replication lag. This argument is only valid if the `principal_id` is a `Service Principal` identity. If it is not a `Service Principal` identity it will cause the role assignment to fail. Defaults to `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeouts.md">Timeouts</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### PrincipalType

Returns the <code>PrincipalType</code> value.

