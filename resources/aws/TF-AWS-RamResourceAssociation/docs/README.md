# TF::AWS::RamResourceAssociation

Manages a Resource Access Manager (RAM) Resource Association.

~> *NOTE:* Certain AWS resources (e.g. EC2 Subnets) can only be shared in an AWS account that is a member of an AWS Organizations organization with organization-wide Resource Access Manager functionality enabled. See the [Resource Access Manager User Guide](https://docs.aws.amazon.com/ram/latest/userguide/what-is.html) and AWS service specific documentation for additional information.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AWS::RamResourceAssociation",
    "Properties" : {
        "<a href="#resourcearn" title="ResourceArn">ResourceArn</a>" : <i>String</i>,
        "<a href="#resourcesharearn" title="ResourceShareArn">ResourceShareArn</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AWS::RamResourceAssociation
Properties:
    <a href="#resourcearn" title="ResourceArn">ResourceArn</a>: <i>String</i>
    <a href="#resourcesharearn" title="ResourceShareArn">ResourceShareArn</a>: <i>String</i>
</pre>

## Properties

#### ResourceArn

Amazon Resource Name (ARN) of the resource to associate with the RAM Resource Share.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourceShareArn

Amazon Resource Name (ARN) of the RAM Resource Share.

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

#### Id

Returns the <code>Id</code> value.

