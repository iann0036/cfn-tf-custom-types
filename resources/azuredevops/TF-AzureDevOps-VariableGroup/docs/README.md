# TF::AzureDevOps::VariableGroup

Manages variable groups within Azure DevOps.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AzureDevOps::VariableGroup",
    "Properties" : {
        "<a href="#allowaccess" title="AllowAccess">AllowAccess</a>" : <i>Boolean</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#projectid" title="ProjectId">ProjectId</a>" : <i>String</i>,
        "<a href="#keyvault" title="KeyVault">KeyVault</a>" : <i>[ <a href="keyvaultdefinition.md">KeyVaultDefinition</a>, ... ]</i>,
        "<a href="#variable" title="Variable">Variable</a>" : <i>[ <a href="variabledefinition.md">VariableDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AzureDevOps::VariableGroup
Properties:
    <a href="#allowaccess" title="AllowAccess">AllowAccess</a>: <i>Boolean</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#projectid" title="ProjectId">ProjectId</a>: <i>String</i>
    <a href="#keyvault" title="KeyVault">KeyVault</a>: <i>
      - <a href="keyvaultdefinition.md">KeyVaultDefinition</a></i>
    <a href="#variable" title="Variable">Variable</a>: <i>
      - <a href="variabledefinition.md">VariableDefinition</a></i>
</pre>

## Properties

#### AllowAccess

Boolean that indicate if this variable group is shared by all pipelines of this project.
- `variable` - (Optional) One or more `variable` blocks as documented below.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

The description of the Variable Group.
- `allow_access` - (Required) Boolean that indicate if this variable group is shared by all pipelines of this project.
- `variable` - (Optional) One or more `variable` blocks as documented below.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the Variable Group.
- `description` - (Optional) The description of the Variable Group.
- `allow_access` - (Required) Boolean that indicate if this variable group is shared by all pipelines of this project.
- `variable` - (Optional) One or more `variable` blocks as documented below.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProjectId

The project ID or project name.
- `name` - (Required) The name of the Variable Group.
- `description` - (Optional) The description of the Variable Group.
- `allow_access` - (Required) Boolean that indicate if this variable group is shared by all pipelines of this project.
- `variable` - (Optional) One or more `variable` blocks as documented below.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KeyVault

_Required_: No

_Type_: List of <a href="keyvaultdefinition.md">KeyVaultDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Variable

_Required_: No

_Type_: List of <a href="variabledefinition.md">VariableDefinition</a>

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

