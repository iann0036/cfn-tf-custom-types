# Terraform::Alicloud::Actiontrail

Provides a new resource to manage [Action Trail](https://www.alibabacloud.com/help/doc-detail/28804.htm).

-> **NOTE:** Available in 1.35.0+

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Alicloud::Actiontrail",
    "Properties" : {
        "<a href="#eventrw" title="EventRw">EventRw</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#ossbucketname" title="OssBucketName">OssBucketName</a>" : <i>String</i>,
        "<a href="#osskeyprefix" title="OssKeyPrefix">OssKeyPrefix</a>" : <i>String</i>,
        "<a href="#rolename" title="RoleName">RoleName</a>" : <i>String</i>,
        "<a href="#slsprojectarn" title="SlsProjectArn">SlsProjectArn</a>" : <i>String</i>,
        "<a href="#slswriterolearn" title="SlsWriteRoleArn">SlsWriteRoleArn</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Alicloud::Actiontrail
Properties:
    <a href="#eventrw" title="EventRw">EventRw</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#ossbucketname" title="OssBucketName">OssBucketName</a>: <i>String</i>
    <a href="#osskeyprefix" title="OssKeyPrefix">OssKeyPrefix</a>: <i>String</i>
    <a href="#rolename" title="RoleName">RoleName</a>: <i>String</i>
    <a href="#slsprojectarn" title="SlsProjectArn">SlsProjectArn</a>: <i>String</i>
    <a href="#slswriterolearn" title="SlsWriteRoleArn">SlsWriteRoleArn</a>: <i>String</i>
</pre>

## Properties

#### EventRw

Indicates whether the event is a read or a write event. Valid values: Read, Write, and All. Default value: Write.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the trail to be created, which must be unique for an account.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OssBucketName

The OSS bucket to which the trail delivers logs. Ensure that this is an existing OSS bucket.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OssKeyPrefix

The prefix of the specified OSS bucket name. This parameter can be left empty.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RoleName

The RAM role in ActionTrail permitted by the user.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SlsProjectArn

The unique ARN of the Log Service project.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SlsWriteRoleArn

The unique ARN of the Log Service role.

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

#### Id

Returns the <code>Id</code> value.

