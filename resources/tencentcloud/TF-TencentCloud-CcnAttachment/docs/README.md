# TF::TencentCloud::CcnAttachment

Provides a CCN attaching resource.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::TencentCloud::CcnAttachment",
    "Properties" : {
        "<a href="#ccnid" title="CcnId">CcnId</a>" : <i>String</i>,
        "<a href="#ccnuin" title="CcnUin">CcnUin</a>" : <i>String</i>,
        "<a href="#instanceid" title="InstanceId">InstanceId</a>" : <i>String</i>,
        "<a href="#instanceregion" title="InstanceRegion">InstanceRegion</a>" : <i>String</i>,
        "<a href="#instancetype" title="InstanceType">InstanceType</a>" : <i>String</i>,
    }
}
</pre>

### YAML

<pre>
Type: TF::TencentCloud::CcnAttachment
Properties:
    <a href="#ccnid" title="CcnId">CcnId</a>: <i>String</i>
    <a href="#ccnuin" title="CcnUin">CcnUin</a>: <i>String</i>
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

#### CcnUin

Uin of the ccn attached. Default is ``, which means the uin of this account. This parameter is used with case when attaching ccn of other account to the instance of this account. For now only support instance type `VPC`.

_Required_: No

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

Type of attached instance network, and available values include `VPC`, `DIRECTCONNECT`, `BMVPC` and `VPNGW`. Note: `VPNGW` type is only for whitelist customer now.

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

#### Id

Returns the <code>Id</code> value.

#### State

Returns the <code>State</code> value.

