# Terraform::Alicloud::DatahubProject

The project is the basic unit of resource management in Datahub Service and is used to isolate and control resources. It contains a set of Topics. You can manage the datahub sources of an application by using projects. [Refer to details](https://help.aliyun.com/document_detail/47440.html).

-> **NOTE:** Currently Datahub service only can be supported in the regions: cn-beijing, cn-hangzhou, cn-shanghai, cn-shenzhen,  ap-southeast-1.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Alicloud::DatahubProject",
    "Properties" : {
        "<a href="#comment" title="Comment">Comment</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Alicloud::DatahubProject
Properties:
    <a href="#comment" title="Comment">Comment</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
</pre>

## Properties

#### Comment

Comment of the datahub project. It cannot be longer than 255 characters.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the datahub project. Its length is limited to 3-32 and only characters such as letters, digits and '_' are allowed. It is case-insensitive.

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

#### CreateTime

Returns the <code>CreateTime</code> value.

#### LastModifyTime

Returns the <code>LastModifyTime</code> value.

