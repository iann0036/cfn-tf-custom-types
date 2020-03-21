# Terraform::Datadog::Downtime

Provides a Datadog downtime resource. This can be used to create and manage Datadog downtimes.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Datadog::Downtime",
    "Properties" : {
        "<a href="#active" title="Active">Active</a>" : <i>Boolean</i>,
        "<a href="#disabled" title="Disabled">Disabled</a>" : <i>Boolean</i>,
        "<a href="#end" title="End">End</a>" : <i>Double</i>,
        "<a href="#enddate" title="EndDate">EndDate</a>" : <i>String</i>,
        "<a href="#message" title="Message">Message</a>" : <i>String</i>,
        "<a href="#monitorid" title="MonitorId">MonitorId</a>" : <i>Double</i>,
        "<a href="#monitortags" title="MonitorTags">MonitorTags</a>" : <i>[ String, ... ]</i>,
        "<a href="#scope" title="Scope">Scope</a>" : <i>[ String, ... ]</i>,
        "<a href="#start" title="Start">Start</a>" : <i>Double</i>,
        "<a href="#startdate" title="StartDate">StartDate</a>" : <i>String</i>,
        "<a href="#timezone" title="Timezone">Timezone</a>" : <i>String</i>,
        "<a href="#recurrence" title="Recurrence">Recurrence</a>" : <i>[ <a href="recurrence.md">Recurrence</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Datadog::Downtime
Properties:
    <a href="#active" title="Active">Active</a>: <i>Boolean</i>
    <a href="#disabled" title="Disabled">Disabled</a>: <i>Boolean</i>
    <a href="#end" title="End">End</a>: <i>Double</i>
    <a href="#enddate" title="EndDate">EndDate</a>: <i>String</i>
    <a href="#message" title="Message">Message</a>: <i>String</i>
    <a href="#monitorid" title="MonitorId">MonitorId</a>: <i>Double</i>
    <a href="#monitortags" title="MonitorTags">MonitorTags</a>: <i>
      - String</i>
    <a href="#scope" title="Scope">Scope</a>: <i>
      - String</i>
    <a href="#start" title="Start">Start</a>: <i>Double</i>
    <a href="#startdate" title="StartDate">StartDate</a>: <i>String</i>
    <a href="#timezone" title="Timezone">Timezone</a>: <i>String</i>
    <a href="#recurrence" title="Recurrence">Recurrence</a>: <i>
      - <a href="recurrence.md">Recurrence</a></i>
</pre>

## Properties

#### Active

A flag indicating if the downtime is active now.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Disabled

A flag indicating if the downtime was disabled.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### End

POSIX timestamp to end the downtime.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EndDate

String representing date and time to end the downtime in RFC3339 format.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Message

A message to include with notifications for this downtime.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MonitorId

Reference to which monitor this downtime is applied. When scheduling downtime for a given monitor, datadog changes `silenced` property of the monitor to match the `end` POSIX timestamp. **Note:** this will effectively change the `silenced` attribute of the referenced monitor. If that monitor is also tracked by Terraform and you don't want it to be unmuted on the next `terraform apply`, see [details](/docs/providers/datadog/r/monitor.html#silencing-by-hand-and-by-downtimes) in the monitor resource documentation. This option also conflicts with `monitor_tags` use none or one or the other.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MonitorTags

A list of monitor tags to match. The resulting downtime applies to monitors that match **all** provided monitor tags. This option conflicts with `monitor_id` as it will match all monitors that match these tags.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Scope

The scope(s) to which the downtime applies, e.g. host:app2. Provide multiple scopes as a comma-separated list, e.g. env:dev,env:prod. The resulting downtime applies to sources that matches ALL provided scopes (i.e. env:dev AND env:prod), NOT any of them.

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Start

POSIX timestamp to start the downtime.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StartDate

String representing date and time to start the downtime in RFC3339 format.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timezone

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Recurrence

_Required_: No

_Type_: List of <a href="recurrence.md">Recurrence</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

