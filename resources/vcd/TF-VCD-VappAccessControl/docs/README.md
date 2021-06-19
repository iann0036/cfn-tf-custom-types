# TF::VCD::VappAccessControl

Provides a vCloud Director Access Control structure for a vApp. This can be used to create, update, and delete access control structures for a vApp.

~> **Warning:** The access control info is tied to a vApp. Thus, there could be only one instance per vApp. Using a different
definition for the same vApp ID will result in a previous instance to be overwritten.

-> **Note:** Access control operations run in tenant context, meaning that, even if the user is a system administrator,
in every request it uses headers items that define the tenant context as restricted to the organization to which the vApp belongs.

Supported in provider *v3.0+*

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::VCD::VappAccessControl",
    "Properties" : {
        "<a href="#everyoneaccesslevel" title="EveryoneAccessLevel">EveryoneAccessLevel</a>" : <i>String</i>,
        "<a href="#org" title="Org">Org</a>" : <i>String</i>,
        "<a href="#sharedwitheveryone" title="SharedWithEveryone">SharedWithEveryone</a>" : <i>Boolean</i>,
        "<a href="#vappid" title="VappId">VappId</a>" : <i>String</i>,
        "<a href="#vdc" title="Vdc">Vdc</a>" : <i>String</i>,
        "<a href="#sharedwith" title="SharedWith">SharedWith</a>" : <i>[ <a href="sharedwithdefinition.md">SharedWithDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::VCD::VappAccessControl
Properties:
    <a href="#everyoneaccesslevel" title="EveryoneAccessLevel">EveryoneAccessLevel</a>: <i>String</i>
    <a href="#org" title="Org">Org</a>: <i>String</i>
    <a href="#sharedwitheveryone" title="SharedWithEveryone">SharedWithEveryone</a>: <i>Boolean</i>
    <a href="#vappid" title="VappId">VappId</a>: <i>String</i>
    <a href="#vdc" title="Vdc">Vdc</a>: <i>String</i>
    <a href="#sharedwith" title="SharedWith">SharedWith</a>: <i>
      - <a href="sharedwithdefinition.md">SharedWithDefinition</a></i>
</pre>

## Properties

#### EveryoneAccessLevel

Access level when the vApp is shared with everyone (one of `ReadOnly`, `Change`,
`FullControl`). Required if `shared_with_everyone` is set.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Org

The name of organization to which the vApp belongs. Optional if defined at provider level.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SharedWithEveryone

Whether the vApp is shared with everyone. If any `shared_with` blocks are included,
this property cannot be used.

_Required_: Yes

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VappId

A unique identifier for the vApp.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vdc

The name of organization to which the vApp belongs. Optional if defined at provider level.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SharedWith

_Required_: No

_Type_: List of <a href="sharedwithdefinition.md">SharedWithDefinition</a>

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

