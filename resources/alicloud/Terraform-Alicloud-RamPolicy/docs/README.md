# Terraform::Alicloud::RamPolicy

Provides a RAM Policy resource. 

-> **NOTE:** When you want to destroy this resource forcefully(means remove all the relationships associated with it automatically and then destroy it) without set `force`  with `true` at beginning, you need add `force = true` to configuration file and run `terraform plan`, then you can delete resource forcefully.
-> **NOTE:** Each policy can own at most 5 versions and the oldest version will be removed after its version achieves 5.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Alicloud::RamPolicy",
    "Properties" : {
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#document" title="Document">Document</a>" : <i>String</i>,
        "<a href="#force" title="Force">Force</a>" : <i>Boolean</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#version" title="Version">Version</a>" : <i>String</i>,
        "<a href="#statement" title="Statement">Statement</a>" : <i>[ <a href="statement.md">Statement</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Alicloud::RamPolicy
Properties:
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#document" title="Document">Document</a>: <i>String</i>
    <a href="#force" title="Force">Force</a>: <i>Boolean</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#version" title="Version">Version</a>: <i>String</i>
    <a href="#statement" title="Statement">Statement</a>: <i>
      - <a href="statement.md">Statement</a></i>
</pre>

## Properties

#### Description

Description of the RAM policy. This name can have a string of 1 to 1024 characters.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Document

Document of the RAM policy. It is required when the `statement` is not specified.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Force

This parameter is used for resource destroy. Default value is `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Name of the RAM policy. This name can have a string of 1 to 128 characters, must contain only alphanumeric characters or hyphen "-", and must not begin with a hyphen.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Version

(It has been deprecated from version 1.49.0, and use field 'document' to replace.) Version of the RAM policy document. Valid value is `1`. Default value is `1`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Statement

_Required_: No

_Type_: List of <a href="statement.md">Statement</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the Id.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### AttachmentCount

Returns the <code>AttachmentCount</code> value.

#### Id

Returns the <code>Id</code> value.

#### Type

Returns the <code>Type</code> value.

