# TF::AWS::CloudwatchEventArchive

Provides an EventBridge event archive resource.

~> **Note:** EventBridge was formerly known as CloudWatch Events. The functionality is identical.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AWS::CloudwatchEventArchive",
    "Properties" : {
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#eventpattern" title="EventPattern">EventPattern</a>" : <i>String</i>,
        "<a href="#eventsourcearn" title="EventSourceArn">EventSourceArn</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#retentiondays" title="RetentionDays">RetentionDays</a>" : <i>Double</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AWS::CloudwatchEventArchive
Properties:
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#eventpattern" title="EventPattern">EventPattern</a>: <i>String</i>
    <a href="#eventsourcearn" title="EventSourceArn">EventSourceArn</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#retentiondays" title="RetentionDays">RetentionDays</a>: <i>Double</i>
</pre>

## Properties

#### Description

The description of the new event archive.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EventPattern

Instructs the new event archive to only capture events matched by this pattern. By default, it attempts to archive every event received in the `event_source_arn`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EventSourceArn

Event bus source ARN from where these events should be archived.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the new event archive. The archive name cannot exceed 48 characters.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RetentionDays

The maximum number of days to retain events in the new event archive. By default, it archives indefinitely.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Arn

Returns the <code>Arn</code> value.

#### Id

Returns the <code>Id</code> value.

