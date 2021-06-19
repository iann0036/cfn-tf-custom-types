# TF::GoogleBeta::GoogleComputeResourcePolicy InstanceSchedulePolicyDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#expirationtime" title="ExpirationTime">ExpirationTime</a>" : <i>String</i>,
    "<a href="#starttime" title="StartTime">StartTime</a>" : <i>String</i>,
    "<a href="#timezone" title="TimeZone">TimeZone</a>" : <i>String</i>,
    "<a href="#vmstartschedule" title="VmStartSchedule">VmStartSchedule</a>" : <i>[ <a href="vmstartscheduledefinition.md">VmStartScheduleDefinition</a>, ... ]</i>,
    "<a href="#vmstopschedule" title="VmStopSchedule">VmStopSchedule</a>" : <i>[ <a href="vmstopscheduledefinition.md">VmStopScheduleDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#expirationtime" title="ExpirationTime">ExpirationTime</a>: <i>String</i>
<a href="#starttime" title="StartTime">StartTime</a>: <i>String</i>
<a href="#timezone" title="TimeZone">TimeZone</a>: <i>String</i>
<a href="#vmstartschedule" title="VmStartSchedule">VmStartSchedule</a>: <i>
      - <a href="vmstartscheduledefinition.md">VmStartScheduleDefinition</a></i>
<a href="#vmstopschedule" title="VmStopSchedule">VmStopSchedule</a>: <i>
      - <a href="vmstopscheduledefinition.md">VmStopScheduleDefinition</a></i>
</pre>

## Properties

#### ExpirationTime

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StartTime

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TimeZone

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VmStartSchedule

_Required_: No

_Type_: List of <a href="vmstartscheduledefinition.md">VmStartScheduleDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VmStopSchedule

_Required_: No

_Type_: List of <a href="vmstopscheduledefinition.md">VmStopScheduleDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

