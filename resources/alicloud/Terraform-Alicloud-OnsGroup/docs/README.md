# Terraform::Alicloud::OnsGroup

Provides an ONS group resource.

For more information about how to use it, see [RocketMQ Group Management API](https://www.alibabacloud.com/help/doc-detail/29616.html). 

-> **NOTE:** Available in 1.53.0+

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Alicloud::OnsGroup",
    "Properties" : {
        "<a href="#groupid" title="GroupId">GroupId</a>" : <i>String</i>,
        "<a href="#instanceid" title="InstanceId">InstanceId</a>" : <i>String</i>,
        "<a href="#readenable" title="ReadEnable">ReadEnable</a>" : <i>Boolean</i>,
        "<a href="#remark" title="Remark">Remark</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Alicloud::OnsGroup
Properties:
    <a href="#groupid" title="GroupId">GroupId</a>: <i>String</i>
    <a href="#instanceid" title="InstanceId">InstanceId</a>: <i>String</i>
    <a href="#readenable" title="ReadEnable">ReadEnable</a>: <i>Boolean</i>
    <a href="#remark" title="Remark">Remark</a>: <i>String</i>
</pre>

## Properties

#### GroupId

Name of the group. Two groups on a single instance cannot have the same name. A `group_id` starts with "GID_" or "GID-", and contains letters, numbers, hyphens (-), and underscores (_).

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InstanceId

ID of the ONS Instance that owns the groups.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReadEnable

This attribute is used to set the message reading enabled or disabled. It can only be set after the group is used by the client.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Remark

This attribute is a concise description of group. The length cannot exceed 256.

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

