# TF::FortiOS::SystemAutomationtrigger

Trigger for automation stitches.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::FortiOS::SystemAutomationtrigger",
    "Properties" : {
        "<a href="#dynamicsortsubtable" title="DynamicSortSubtable">DynamicSortSubtable</a>" : <i>String</i>,
        "<a href="#eventtype" title="EventType">EventType</a>" : <i>String</i>,
        "<a href="#fazeventname" title="FazEventName">FazEventName</a>" : <i>String</i>,
        "<a href="#fazeventseverity" title="FazEventSeverity">FazEventSeverity</a>" : <i>String</i>,
        "<a href="#fazeventtags" title="FazEventTags">FazEventTags</a>" : <i>String</i>,
        "<a href="#ioclevel" title="IocLevel">IocLevel</a>" : <i>String</i>,
        "<a href="#licensetype" title="LicenseType">LicenseType</a>" : <i>String</i>,
        "<a href="#logid" title="Logid">Logid</a>" : <i>Double</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#reporttype" title="ReportType">ReportType</a>" : <i>String</i>,
        "<a href="#triggerday" title="TriggerDay">TriggerDay</a>" : <i>Double</i>,
        "<a href="#triggerfrequency" title="TriggerFrequency">TriggerFrequency</a>" : <i>String</i>,
        "<a href="#triggerhour" title="TriggerHour">TriggerHour</a>" : <i>Double</i>,
        "<a href="#triggerminute" title="TriggerMinute">TriggerMinute</a>" : <i>Double</i>,
        "<a href="#triggertype" title="TriggerType">TriggerType</a>" : <i>String</i>,
        "<a href="#triggerweekday" title="TriggerWeekday">TriggerWeekday</a>" : <i>String</i>,
        "<a href="#vdomparam" title="Vdomparam">Vdomparam</a>" : <i>String</i>,
        "<a href="#fields" title="Fields">Fields</a>" : <i>[ <a href="fieldsdefinition.md">FieldsDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::FortiOS::SystemAutomationtrigger
Properties:
    <a href="#dynamicsortsubtable" title="DynamicSortSubtable">DynamicSortSubtable</a>: <i>String</i>
    <a href="#eventtype" title="EventType">EventType</a>: <i>String</i>
    <a href="#fazeventname" title="FazEventName">FazEventName</a>: <i>String</i>
    <a href="#fazeventseverity" title="FazEventSeverity">FazEventSeverity</a>: <i>String</i>
    <a href="#fazeventtags" title="FazEventTags">FazEventTags</a>: <i>String</i>
    <a href="#ioclevel" title="IocLevel">IocLevel</a>: <i>String</i>
    <a href="#licensetype" title="LicenseType">LicenseType</a>: <i>String</i>
    <a href="#logid" title="Logid">Logid</a>: <i>Double</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#reporttype" title="ReportType">ReportType</a>: <i>String</i>
    <a href="#triggerday" title="TriggerDay">TriggerDay</a>: <i>Double</i>
    <a href="#triggerfrequency" title="TriggerFrequency">TriggerFrequency</a>: <i>String</i>
    <a href="#triggerhour" title="TriggerHour">TriggerHour</a>: <i>Double</i>
    <a href="#triggerminute" title="TriggerMinute">TriggerMinute</a>: <i>Double</i>
    <a href="#triggertype" title="TriggerType">TriggerType</a>: <i>String</i>
    <a href="#triggerweekday" title="TriggerWeekday">TriggerWeekday</a>: <i>String</i>
    <a href="#vdomparam" title="Vdomparam">Vdomparam</a>: <i>String</i>
    <a href="#fields" title="Fields">Fields</a>: <i>
      - <a href="fieldsdefinition.md">FieldsDefinition</a></i>
</pre>

## Properties

#### DynamicSortSubtable

true or false, set this parameter to true when using dynamic for_each + toset to configure and sort sub-tables, please do not set this parameter when configuring static sub-tables.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EventType

Event type.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FazEventName

FortiAnalyzer event handler name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FazEventSeverity

FortiAnalyzer event severity.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FazEventTags

FortiAnalyzer event tags.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IocLevel

IOC threat level. Valid values: `medium`, `high`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LicenseType

License type.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Logid

Log ID to trigger event.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReportType

Security Rating report. Valid values: `PostureReport`, `CoverageReport`, `OptimizationReport`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TriggerDay

Day within a month to trigger.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TriggerFrequency

Scheduled trigger frequency (default = daily). Valid values: `hourly`, `daily`, `weekly`, `monthly`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TriggerHour

Hour of the day on which to trigger (0 - 23, default = 1).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TriggerMinute

Minute of the hour on which to trigger (0 - 59, 60 to randomize).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TriggerType

Trigger type. Valid values: `event-based`, `scheduled`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TriggerWeekday

Day of week for trigger. Valid values: `sunday`, `monday`, `tuesday`, `wednesday`, `thursday`, `friday`, `saturday`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vdomparam

Specifies the vdom to which the resource will be applied when the FortiGate unit is running in VDOM mode. Only one vdom can be specified. If you want to inherit the vdom configuration of the provider, please do not set this parameter.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Fields

_Required_: No

_Type_: List of <a href="fieldsdefinition.md">FieldsDefinition</a>

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

