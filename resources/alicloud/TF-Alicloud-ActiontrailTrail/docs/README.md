# TF::Alicloud::ActiontrailTrail

CloudFormation equivalent of alicloud_actiontrail_trail

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Alicloud::ActiontrailTrail",
    "Properties" : {
        "<a href="#eventrw" title="EventRw">EventRw</a>" : <i>String</i>,
        "<a href="#isorganizationtrail" title="IsOrganizationTrail">IsOrganizationTrail</a>" : <i>Boolean</i>,
        "<a href="#mnstopicarn" title="MnsTopicArn">MnsTopicArn</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#ossbucketname" title="OssBucketName">OssBucketName</a>" : <i>String</i>,
        "<a href="#osskeyprefix" title="OssKeyPrefix">OssKeyPrefix</a>" : <i>String</i>,
        "<a href="#osswriterolearn" title="OssWriteRoleArn">OssWriteRoleArn</a>" : <i>String</i>,
        "<a href="#rolename" title="RoleName">RoleName</a>" : <i>String</i>,
        "<a href="#slsprojectarn" title="SlsProjectArn">SlsProjectArn</a>" : <i>String</i>,
        "<a href="#slswriterolearn" title="SlsWriteRoleArn">SlsWriteRoleArn</a>" : <i>String</i>,
        "<a href="#status" title="Status">Status</a>" : <i>String</i>,
        "<a href="#trailname" title="TrailName">TrailName</a>" : <i>String</i>,
        "<a href="#trailregion" title="TrailRegion">TrailRegion</a>" : <i>String</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Alicloud::ActiontrailTrail
Properties:
    <a href="#eventrw" title="EventRw">EventRw</a>: <i>String</i>
    <a href="#isorganizationtrail" title="IsOrganizationTrail">IsOrganizationTrail</a>: <i>Boolean</i>
    <a href="#mnstopicarn" title="MnsTopicArn">MnsTopicArn</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#ossbucketname" title="OssBucketName">OssBucketName</a>: <i>String</i>
    <a href="#osskeyprefix" title="OssKeyPrefix">OssKeyPrefix</a>: <i>String</i>
    <a href="#osswriterolearn" title="OssWriteRoleArn">OssWriteRoleArn</a>: <i>String</i>
    <a href="#rolename" title="RoleName">RoleName</a>: <i>String</i>
    <a href="#slsprojectarn" title="SlsProjectArn">SlsProjectArn</a>: <i>String</i>
    <a href="#slswriterolearn" title="SlsWriteRoleArn">SlsWriteRoleArn</a>: <i>String</i>
    <a href="#status" title="Status">Status</a>: <i>String</i>
    <a href="#trailname" title="TrailName">TrailName</a>: <i>String</i>
    <a href="#trailregion" title="TrailRegion">TrailRegion</a>: <i>String</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### EventRw

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsOrganizationTrail

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MnsTopicArn

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OssBucketName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OssKeyPrefix

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OssWriteRoleArn

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RoleName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SlsProjectArn

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SlsWriteRoleArn

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Status

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TrailName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TrailRegion

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeoutsdefinition.md">TimeoutsDefinition</a>

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

