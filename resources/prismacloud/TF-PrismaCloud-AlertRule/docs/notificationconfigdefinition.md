# TF::PrismaCloud::AlertRule NotificationConfigDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#configid" title="ConfigId">ConfigId</a>" : <i>String</i>,
    "<a href="#configtype" title="ConfigType">ConfigType</a>" : <i>String</i>,
    "<a href="#dayofmonth" title="DayOfMonth">DayOfMonth</a>" : <i>Double</i>,
    "<a href="#detailedreport" title="DetailedReport">DetailedReport</a>" : <i>Boolean</i>,
    "<a href="#enabled" title="Enabled">Enabled</a>" : <i>Boolean</i>,
    "<a href="#frequency" title="Frequency">Frequency</a>" : <i>String</i>,
    "<a href="#frequencyfromrrule" title="FrequencyFromRRule">FrequencyFromRRule</a>" : <i>String</i>,
    "<a href="#hourofday" title="HourOfDay">HourOfDay</a>" : <i>Double</i>,
    "<a href="#includeremediation" title="IncludeRemediation">IncludeRemediation</a>" : <i>Boolean</i>,
    "<a href="#rruleschedule" title="RRuleSchedule">RRuleSchedule</a>" : <i>String</i>,
    "<a href="#recipients" title="Recipients">Recipients</a>" : <i>[ String, ... ]</i>,
    "<a href="#templateid" title="TemplateId">TemplateId</a>" : <i>String</i>,
    "<a href="#timezoneid" title="TimezoneId">TimezoneId</a>" : <i>String</i>,
    "<a href="#withcompression" title="WithCompression">WithCompression</a>" : <i>Boolean</i>,
    "<a href="#daysofweek" title="DaysOfWeek">DaysOfWeek</a>" : <i>[ <a href="daysofweekdefinition.md">DaysOfWeekDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#configid" title="ConfigId">ConfigId</a>: <i>String</i>
<a href="#configtype" title="ConfigType">ConfigType</a>: <i>String</i>
<a href="#dayofmonth" title="DayOfMonth">DayOfMonth</a>: <i>Double</i>
<a href="#detailedreport" title="DetailedReport">DetailedReport</a>: <i>Boolean</i>
<a href="#enabled" title="Enabled">Enabled</a>: <i>Boolean</i>
<a href="#frequency" title="Frequency">Frequency</a>: <i>String</i>
<a href="#frequencyfromrrule" title="FrequencyFromRRule">FrequencyFromRRule</a>: <i>String</i>
<a href="#hourofday" title="HourOfDay">HourOfDay</a>: <i>Double</i>
<a href="#includeremediation" title="IncludeRemediation">IncludeRemediation</a>: <i>Boolean</i>
<a href="#rruleschedule" title="RRuleSchedule">RRuleSchedule</a>: <i>String</i>
<a href="#recipients" title="Recipients">Recipients</a>: <i>
      - String</i>
<a href="#templateid" title="TemplateId">TemplateId</a>: <i>String</i>
<a href="#timezoneid" title="TimezoneId">TimezoneId</a>: <i>String</i>
<a href="#withcompression" title="WithCompression">WithCompression</a>: <i>Boolean</i>
<a href="#daysofweek" title="DaysOfWeek">DaysOfWeek</a>: <i>
      - <a href="daysofweekdefinition.md">DaysOfWeekDefinition</a></i>
</pre>

## Properties

#### ConfigId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConfigType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DayOfMonth

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DetailedReport

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Enabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Frequency

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FrequencyFromRRule

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HourOfDay

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IncludeRemediation

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RRuleSchedule

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Recipients

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TemplateId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TimezoneId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WithCompression

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DaysOfWeek

_Required_: No

_Type_: List of <a href="daysofweekdefinition.md">DaysOfWeekDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

