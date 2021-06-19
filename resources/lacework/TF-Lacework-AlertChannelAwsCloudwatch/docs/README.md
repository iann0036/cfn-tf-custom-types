# TF::Lacework::AlertChannelAwsCloudwatch

Configure Lacework to forward alerts to an AWS CloudWatch event bus.

-> **Note:** For more information about sending and receiving events between AWS accounts, refer to the Amazon [CloudWatch Events User Guide](https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/WhatIsCloudWatchEvents.html).

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Lacework::AlertChannelAwsCloudwatch",
    "Properties" : {
        "<a href="#enabled" title="Enabled">Enabled</a>" : <i>Boolean</i>,
        "<a href="#eventbusarn" title="EventBusArn">EventBusArn</a>" : <i>String</i>,
        "<a href="#groupissuesby" title="GroupIssuesBy">GroupIssuesBy</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    }
}
</pre>

### YAML

<pre>
Type: TF::Lacework::AlertChannelAwsCloudwatch
Properties:
    <a href="#enabled" title="Enabled">Enabled</a>: <i>Boolean</i>
    <a href="#eventbusarn" title="EventBusArn">EventBusArn</a>: <i>String</i>
    <a href="#groupissuesby" title="GroupIssuesBy">GroupIssuesBy</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
</pre>

## Properties

#### Enabled

The state of the external integration. Defaults to `true`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EventBusArn

The ARN of your AWS CloudWatch event bus.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GroupIssuesBy

Defines how Lacework compliance events get grouped. Must be one of `Events` or `Resources`. Defaults to `Events`.
The available options are:
* **Events**:	Single AWS CloudWatch events will be created when compliance events of the same type but from different resources are detected by Lacework. For example, if three different S3 resources are generating the same compliance event, only one AWS event is created on the AWS CloudWatch event bus.
* **Resources**: Multiple AWS CloudWatch events will be created when multiple resources are generating the same compliance event. For example, if three different S3 resources are generating the same compliance event, three AWS events are created on the AWS CloudWatch event bus.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The Alert Channel integration name.

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

#### CreatedOrUpdatedBy

Returns the <code>CreatedOrUpdatedBy</code> value.

#### CreatedOrUpdatedTime

Returns the <code>CreatedOrUpdatedTime</code> value.

#### Id

Returns the <code>Id</code> value.

#### IntgGuid

Returns the <code>IntgGuid</code> value.

#### OrgLevel

Returns the <code>OrgLevel</code> value.

#### TypeName

Returns the <code>TypeName</code> value.

