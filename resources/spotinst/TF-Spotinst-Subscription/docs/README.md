# TF::Spotinst::Subscription

Provides a Spotinst subscription resource.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Spotinst::Subscription",
    "Properties" : {
        "<a href="#endpoint" title="Endpoint">Endpoint</a>" : <i>String</i>,
        "<a href="#eventtype" title="EventType">EventType</a>" : <i>String</i>,
        "<a href="#format" title="Format">Format</a>" : <i>[ <a href="formatdefinition.md">FormatDefinition</a>, ... ]</i>,
        "<a href="#protocol" title="Protocol">Protocol</a>" : <i>String</i>,
        "<a href="#resourceid" title="ResourceId">ResourceId</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Spotinst::Subscription
Properties:
    <a href="#endpoint" title="Endpoint">Endpoint</a>: <i>String</i>
    <a href="#eventtype" title="EventType">EventType</a>: <i>String</i>
    <a href="#format" title="Format">Format</a>: <i>
      - <a href="formatdefinition.md">FormatDefinition</a></i>
    <a href="#protocol" title="Protocol">Protocol</a>: <i>String</i>
    <a href="#resourceid" title="ResourceId">ResourceId</a>: <i>String</i>
</pre>

## Properties

#### Endpoint

The endpoint the notification will be sent to. url in case of `"http"`/`"https"`/`"web"`, email address in case of `"email"`/`"email-json"` and sns-topic-arn in case of `"aws-sns"`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EventType

The event to send the notification when triggered. Valid values: `"AWS_EC2_INSTANCE_TERMINATE"`, `"AWS_EC2_INSTANCE_TERMINATED"`, `"AWS_EC2_INSTANCE_LAUNCH"`, `"AWS_EC2_INSTANCE_READY_SIGNAL_TIMEOUT"`, `"AWS_EC2_CANT_SPIN_OD"`, `"AWS_EC2_INSTANCE_UNHEALTHY_IN_ELB"`, `"GROUP_ROLL_FAILED"`, `"GROUP_ROLL_FINISHED"`,
`"CANT_SCALE_UP_GROUP_MAX_CAPACITY"`,
`"GROUP_UPDATED"`,
`"AWS_EMR_PROVISION_TIMEOUT"`,
`"GROUP_BEANSTALK_INIT_READY"`,
`"AZURE_VM_TERMINATED"`,
`"AZURE_VM_TERMINATE"`,
`"AWS_EC2_MANAGED_INSTANCE_PAUSING"`,
`"AWS_EC2_MANAGED_INSTANCE_RESUMING"`,
`"AWS_EC2_MANAGED_INSTANCE_RECYCLING"`,`"AWS_EC2_MANAGED_INSTANCE_DELETING"`.
Ocean Events:`"CLUSTER_ROLL_FINISHED"`,`"GROUP_ROLL_FAILED"`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Format

The format of the notification content (JSON Format - Key+Value). Valid Values : `"instance-id"`, `"event"`, `"resource-id"`, `"resource-name"`, `"subnet-id"`, `"availability-zone"`, `"reason"`, `"private-ip"`, `"launchspec-id"`
Example: {"event": `"event"`, `"resourceId"`: `"resource-id"`, `"resourceName"`: `"resource-name"`", `"myCustomKey"`: `"My content is set here"` }
Default: {`"event"`: `"<event>"`, `"instanceId"`: `"<instance-id>"`, `"resourceId"`: `"<resource-id>"`, `"resourceName"`: `"<resource-name>"` }.

_Required_: No

_Type_: List of <a href="formatdefinition.md">FormatDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Protocol

The protocol to send the notification. Valid values: `"email"`, `"email-json"`, `"aws-sns"`, `"web"`.
The following values are deprecated: `"http"` , `"https"`
You can use the generic `"web"` protocol instead.
`"aws-sns"` is only supported with AWS provider.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourceId

Spotinst Resource id (Elastigroup or Ocean ID).

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

#### Id

Returns the <code>Id</code> value.

