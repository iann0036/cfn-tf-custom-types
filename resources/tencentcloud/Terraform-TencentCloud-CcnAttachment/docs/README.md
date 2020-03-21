# Terraform::TencentCloud::CcnAttachment

Provides a CCN attaching resource.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::TencentCloud::CcnAttachment",
    "Properties" : {
        "<a href="#ccnid" title="CcnId">CcnId</a>" : <i>String</i>,
        "<a href="#instanceid" title="InstanceId">InstanceId</a>" : <i>String</i>,
        "<a href="#instanceregion" title="InstanceRegion">InstanceRegion</a>" : <i>String</i>,
        "<a href="#instancetype" title="InstanceType">InstanceType</a>" : <i>String</i>,
    }
}
</pre>

### YAML

<pre>
Type: Terraform::TencentCloud::CcnAttachment
Properties:
    <a href="#ccnid" title="CcnId">CcnId</a>: <i>String</i>
    <a href="#instanceid" title="InstanceId">InstanceId</a>: <i>String</i>
    <a href="#instanceregion" title="InstanceRegion">InstanceRegion</a>: <i>String</i>
    <a href="#instancetype" title="InstanceType">InstanceType</a>: <i>String</i>
</pre>

## Properties

#### CcnId

ID of the CCN.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InstanceId

ID of instance is attached.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InstanceRegion

The region that the instance locates at.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InstanceType

Type of attached instance network, and available values include VPC, DIRECTCONNECT and BMVPC.

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

#### AttachedTime

Returns the <code>AttachedTime</code> value.

#### CidrBlock

Returns the <code>CidrBlock</code> value.

#### State

Returns the <code>State</code> value.

