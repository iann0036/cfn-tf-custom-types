# TF::AzureDevOps::Group

Manages a group within Azure DevOps.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AzureDevOps::Group",
    "Properties" : {
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#displayname" title="DisplayName">DisplayName</a>" : <i>String</i>,
        "<a href="#mail" title="Mail">Mail</a>" : <i>String</i>,
        "<a href="#members" title="Members">Members</a>" : <i>[ String, ... ]</i>,
        "<a href="#originid" title="OriginId">OriginId</a>" : <i>String</i>,
        "<a href="#scope" title="Scope">Scope</a>" : <i>String</i>,
    }
}
</pre>

### YAML

<pre>
Type: TF::AzureDevOps::Group
Properties:
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#displayname" title="DisplayName">DisplayName</a>: <i>String</i>
    <a href="#mail" title="Mail">Mail</a>: <i>String</i>
    <a href="#members" title="Members">Members</a>: <i>
      - String</i>
    <a href="#originid" title="OriginId">OriginId</a>: <i>String</i>
    <a href="#scope" title="Scope">Scope</a>: <i>String</i>
</pre>

## Properties

#### Description

The Description of the Project.
- `members` - (Optional)
> NOTE: It's possible to define group members both within the `azuredevops_group` resource via the members block and by using the `azuredevops_group_membership` resource. However it's not possible to use both methods to manage group members, since there'll be conflicts.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisplayName

The name of a new Azure DevOps group that is not backed by an external provider. The `origin_id` and `mail` arguments cannot be used simultaneously with `display_name`.
- `description` - (Optional) The Description of the Project.
- `members` - (Optional)
> NOTE: It's possible to define group members both within the `azuredevops_group` resource via the members block and by using the `azuredevops_group_membership` resource. However it's not possible to use both methods to manage group members, since there'll be conflicts.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Mail

The mail address as a reference to an existing group from an external AD or AAD backed provider. The `scope`, `origin_id` and `display_name` arguments cannot be used simultaneously with `mail`.
- `display_name` - (Optional) The name of a new Azure DevOps group that is not backed by an external provider. The `origin_id` and `mail` arguments cannot be used simultaneously with `display_name`.
- `description` - (Optional) The Description of the Project.
- `members` - (Optional)
> NOTE: It's possible to define group members both within the `azuredevops_group` resource via the members block and by using the `azuredevops_group_membership` resource. However it's not possible to use both methods to manage group members, since there'll be conflicts.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Members

> NOTE: It's possible to define group members both within the `azuredevops_group` resource via the members block and by using the `azuredevops_group_membership` resource. However it's not possible to use both methods to manage group members, since there'll be conflicts.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OriginId

The OriginID as a reference to a group from an external AD or AAD backed provider. The `scope`, `mail` and `display_name` arguments cannot be used simultaneously with `origin_id`.
- `mail` - (Optional) The mail address as a reference to an existing group from an external AD or AAD backed provider. The `scope`, `origin_id` and `display_name` arguments cannot be used simultaneously with `mail`.
- `display_name` - (Optional) The name of a new Azure DevOps group that is not backed by an external provider. The `origin_id` and `mail` arguments cannot be used simultaneously with `display_name`.
- `description` - (Optional) The Description of the Project.
- `members` - (Optional)
> NOTE: It's possible to define group members both within the `azuredevops_group` resource via the members block and by using the `azuredevops_group_membership` resource. However it's not possible to use both methods to manage group members, since there'll be conflicts.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Scope

The scope of the group. A descriptor referencing the scope (collection, project) in which the group should be created. If omitted, will be created in the scope of the enclosing account or organization.x
- `origin_id` - (Optional) The OriginID as a reference to a group from an external AD or AAD backed provider. The `scope`, `mail` and `display_name` arguments cannot be used simultaneously with `origin_id`.
- `mail` - (Optional) The mail address as a reference to an existing group from an external AD or AAD backed provider. The `scope`, `origin_id` and `display_name` arguments cannot be used simultaneously with `mail`.
- `display_name` - (Optional) The name of a new Azure DevOps group that is not backed by an external provider. The `origin_id` and `mail` arguments cannot be used simultaneously with `display_name`.
- `description` - (Optional) The Description of the Project.
- `members` - (Optional)
> NOTE: It's possible to define group members both within the `azuredevops_group` resource via the members block and by using the `azuredevops_group_membership` resource. However it's not possible to use both methods to manage group members, since there'll be conflicts.

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

#### Descriptor

Returns the <code>Descriptor</code> value.

#### Domain

Returns the <code>Domain</code> value.

#### Id

Returns the <code>Id</code> value.

#### Origin

Returns the <code>Origin</code> value.

#### PrincipalName

Returns the <code>PrincipalName</code> value.

#### SubjectKind

Returns the <code>SubjectKind</code> value.

#### Url

Returns the <code>Url</code> value.

