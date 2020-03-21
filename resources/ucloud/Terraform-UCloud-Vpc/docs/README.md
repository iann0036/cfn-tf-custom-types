# Terraform::UCloud::Vpc

Provides a VPC resource.

~> **Note**  The network segment can only be created or deleted, can not perform both of them at the same time.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::UCloud::Vpc",
    "Properties" : {
        "<a href="#cidrblocks" title="CidrBlocks">CidrBlocks</a>" : <i>[ String, ... ]</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#remark" title="Remark">Remark</a>" : <i>String</i>,
        "<a href="#tag" title="Tag">Tag</a>" : <i>String</i>,
    }
}
</pre>

### YAML

<pre>
Type: Terraform::UCloud::Vpc
Properties:
    <a href="#cidrblocks" title="CidrBlocks">CidrBlocks</a>: <i>
      - String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#remark" title="Remark">Remark</a>: <i>String</i>
    <a href="#tag" title="Tag">Tag</a>: <i>String</i>
</pre>

## Properties

#### CidrBlocks

The CIDR blocks of VPC.

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of VPC. If not specified, terraform will auto-generate a name beginning with `tf-vpc`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Remark

The remarks of the VPC. (Default: `""`).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tag

A tag assigned to VPC, which contains at most 63 characters and only support Chinese, English, numbers, '-', '_', and '.'. If it is not filled in or a empty string is filled in, then default tag will be assigned. (Default: `Default`).

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

#### CreateTime

Returns the <code>CreateTime</code> value.

#### NetworkInfo

Returns the <code>NetworkInfo</code> value.

#### UpdateTime

Returns the <code>UpdateTime</code> value.

