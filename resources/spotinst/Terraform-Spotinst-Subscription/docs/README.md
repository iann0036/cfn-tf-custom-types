# Terraform::Spotinst::Subscription

Provides a Spotinst subscription resource.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Spotinst::Subscription",
    "Properties" : {
        "<a href="#endpoint" title="Endpoint">Endpoint</a>" : <i>String</i>,
        "<a href="#eventtype" title="EventType">EventType</a>" : <i>String</i>,
        "<a href="#format" title="Format">Format</a>" : <i>[ <a href="format.md">Format</a>, ... ]</i>,
        "<a href="#protocol" title="Protocol">Protocol</a>" : <i>String</i>,
        "<a href="#resourceid" title="ResourceId">ResourceId</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Spotinst::Subscription
Properties:
    <a href="#endpoint" title="Endpoint">Endpoint</a>: <i>String</i>
    <a href="#eventtype" title="EventType">EventType</a>: <i>String</i>
    <a href="#format" title="Format">Format</a>: <i>
      - <a href="format.md">Format</a></i>
    <a href="#protocol" title="Protocol">Protocol</a>: <i>String</i>
    <a href="#resourceid" title="ResourceId">ResourceId</a>: <i>String</i>
</pre>

## Properties

#### Endpoint

The endpoint the notification will be sent to: url in case of `"http"`/`"https"`, email address in case of `"email"`/`"email-json"`, sns-topic-arn in case of `"aws-sns"`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EventType

The event to send the notification when triggered. Valid values: `"AWS_EC2_INSTANCE_TERMINATE"`, `"AWS_EC2_INSTANCE_TERMINATED"`, `"AWS_EC2_INSTANCE_LAUNCH"`, `"AWS_EC2_INSTANCE_UNHEALTHY_IN_ELB"`, `"GROUP_ROLL_FAILED"`, `"GROUP_ROLL_FINISHED"`, `"CANT_SCALE_UP_GROUP_MAX_CAPACITY"`, `"GROUP_UPDATED"`, `"AWS_EC2_CANT_SPIN_OD"`, `"AWS_EMR_PROVISION_TIMEOUT"`, `"AWS_EC2_INSTANCE_READY_SIGNAL_TIMEOUT"`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Format

The format of the notification content (JSON Format - Key+Value). Valid values: `"%instance-id%"`, `"%event%"`, `"%resource-id%"`, `"%resource-name%"`.

_Required_: No

_Type_: List of <a href="format.md">Format</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Protocol

The protocol to send the notification. Valid values: `"http"`, `"https"`, `"email"`, `"email-json"`, `"aws-sns"`, `"web"`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourceId

Spotinst Resource ID (Elastigroup ID).

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

