# Terraform::Alicloud::AlikafkaInstance

Provides an ALIKAFKA instance resource.

-> **NOTE:** Available in 1.59.0+

-> **NOTE:** ALIKAFKA instance resource only support create post pay instance. Creation or modification may took about 10-40 minutes.

-> **NOTE:** Only the following regions support create alikafka pre paid instance.
[`cn-hangzhou`,`cn-beijing`,`cn-shenzhen`,`cn-shanghai`,`cn-qingdao`,`cn-hongkong`,`cn-huhehaote`,`cn-zhangjiakou`,`ap-southeast-1`,`ap-south-1`,`ap-southeast-5`]

-> **NOTE:** Only the following regions support create alikafka post paid instance.
[`cn-hangzhou`,`cn-beijing`,`cn-shenzhen`,`cn-shanghai`,`cn-qingdao`,`cn-hongkong`,`cn-huhehaote`,`cn-zhangjiakou`,`ap-southeast-1`]

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Alicloud::AlikafkaInstance",
    "Properties" : {
        "<a href="#deploytype" title="DeployType">DeployType</a>" : <i>Double</i>,
        "<a href="#disksize" title="DiskSize">DiskSize</a>" : <i>Double</i>,
        "<a href="#disktype" title="DiskType">DiskType</a>" : <i>Double</i>,
        "<a href="#eipmax" title="EipMax">EipMax</a>" : <i>Double</i>,
        "<a href="#iomax" title="IoMax">IoMax</a>" : <i>Double</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#paidtype" title="PaidType">PaidType</a>" : <i>String</i>,
        "<a href="#spectype" title="SpecType">SpecType</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tags.md">Tags</a>, ... ]</i>,
        "<a href="#topicquota" title="TopicQuota">TopicQuota</a>" : <i>Double</i>,
        "<a href="#vswitchid" title="VswitchId">VswitchId</a>" : <i>String</i>,
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Alicloud::AlikafkaInstance
Properties:
    <a href="#deploytype" title="DeployType">DeployType</a>: <i>Double</i>
    <a href="#disksize" title="DiskSize">DiskSize</a>: <i>Double</i>
    <a href="#disktype" title="DiskType">DiskType</a>: <i>Double</i>
    <a href="#eipmax" title="EipMax">EipMax</a>: <i>Double</i>
    <a href="#iomax" title="IoMax">IoMax</a>: <i>Double</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#paidtype" title="PaidType">PaidType</a>: <i>String</i>
    <a href="#spectype" title="SpecType">SpecType</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tags.md">Tags</a></i>
    <a href="#topicquota" title="TopicQuota">TopicQuota</a>: <i>Double</i>
    <a href="#vswitchid" title="VswitchId">VswitchId</a>: <i>String</i>
</pre>

## Properties

#### DeployType

The deploy type of the instance. Currently only support two deploy type, 4: eip/vpc instance, 5: vpc instance.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DiskSize

The disk size of the instance. When modify this value, it only support adjust to a greater value.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DiskType

The disk type of the instance. 0: efficient cloud disk , 1: SSD.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EipMax

The max bandwidth of the instance. When modify this value, it only support adjust to a greater value.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IoMax

The max value of io of the instance. When modify this value, it only support adjust to a greater value.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Name of your Kafka instance. The length should between 3 and 64 characters. If not set, will use instance id as instance name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PaidType

The paid type of the instance. Support two type, "PrePaid": pre paid type instance, "PostPaid": post paid type instance. Default is PostPaid. When modify this value, it only support adjust from post pay to pre pay.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SpecType

The spec type of the instance. Support two type, "normal": normal version instance, "professional": professional version instance. Default is normal. When modify this value, it only support adjust from normal to professional. Note only pre paid type instance support professional specific type.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

A mapping of tags to assign to the resource.

_Required_: No

_Type_: List of <a href="tags.md">Tags</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TopicQuota

The max num of topic can be create of the instance. When modify this value, it only adjust to a greater value.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VswitchId

The ID of attaching vswitch to instance.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the Id.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Id

Returns the <code>Id</code> value.

#### VpcId

Returns the <code>VpcId</code> value.

#### ZoneId

Returns the <code>ZoneId</code> value.

