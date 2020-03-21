# Terraform::Alicloud::OnsInstance

Provides an ONS instance resource.

For more information about how to use it, see [RocketMQ Instance Management API](https://www.alibabacloud.com/help/doc-detail/106354.html). 

-> **NOTE:** The number of instances in the same region cannot exceed 8. At present, the resource does not support region "mq-internet-access" and "ap-southeast-5". 

-> **NOTE:** Available in 1.51.0+

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Alicloud::OnsInstance",
    "Properties" : {
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#remark" title="Remark">Remark</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Alicloud::OnsInstance
Properties:
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#remark" title="Remark">Remark</a>: <i>String</i>
</pre>

## Properties

#### Name

Two instances on a single account in the same region cannot have the same name. The length must be 3 to 64 characters. Chinese characters, English letters digits and hyphen are allowed.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Remark

This attribute is a concise description of instance. The length cannot exceed 128.

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

#### InstanceStatus

Returns the <code>InstanceStatus</code> value.

#### InstanceType

Returns the <code>InstanceType</code> value.

#### ReleaseTime

Returns the <code>ReleaseTime</code> value.

