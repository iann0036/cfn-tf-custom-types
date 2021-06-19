# TF::Alicloud::CsKubernetesPermissions PermissionsDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#cluster" title="Cluster">Cluster</a>" : <i>String</i>,
    "<a href="#iscustom" title="IsCustom">IsCustom</a>" : <i>Boolean</i>,
    "<a href="#isramrole" title="IsRamRole">IsRamRole</a>" : <i>Boolean</i>,
    "<a href="#namespace" title="Namespace">Namespace</a>" : <i>String</i>,
    "<a href="#rolename" title="RoleName">RoleName</a>" : <i>String</i>,
    "<a href="#roletype" title="RoleType">RoleType</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#cluster" title="Cluster">Cluster</a>: <i>String</i>
<a href="#iscustom" title="IsCustom">IsCustom</a>: <i>Boolean</i>
<a href="#isramrole" title="IsRamRole">IsRamRole</a>: <i>Boolean</i>
<a href="#namespace" title="Namespace">Namespace</a>: <i>String</i>
<a href="#rolename" title="RoleName">RoleName</a>: <i>String</i>
<a href="#roletype" title="RoleType">RoleType</a>: <i>String</i>
</pre>

## Properties

#### Cluster

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsCustom

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsRamRole

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Namespace

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RoleName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RoleType

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

