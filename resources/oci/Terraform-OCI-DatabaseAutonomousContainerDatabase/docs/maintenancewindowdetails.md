# Terraform::OCI::DatabaseAutonomousContainerDatabase MaintenanceWindowDetails

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#hoursofday" title="HoursOfDay">HoursOfDay</a>" : <i>[ Double, ... ]</i>,
    "<a href="#preference" title="Preference">Preference</a>" : <i>String</i>,
    "<a href="#weeksofmonth" title="WeeksOfMonth">WeeksOfMonth</a>" : <i>[ Double, ... ]</i>,
    "<a href="#daysofweek" title="DaysOfWeek">DaysOfWeek</a>" : <i>[ &lt;a href=&#34;maintenancewindowdetails-daysofweek.md&#34;&gt;DaysOfWeek&lt;/a&gt;, ... ]</i>,
    "<a href="#months" title="Months">Months</a>" : <i>[ &lt;a href=&#34;maintenancewindowdetails-months.md&#34;&gt;Months&lt;/a&gt;, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#hoursofday" title="HoursOfDay">HoursOfDay</a>: <i>
      - Double</i>
<a href="#preference" title="Preference">Preference</a>: <i>String</i>
<a href="#weeksofmonth" title="WeeksOfMonth">WeeksOfMonth</a>: <i>
      - Double</i>
<a href="#daysofweek" title="DaysOfWeek">DaysOfWeek</a>: <i>
      - &lt;a href=&#34;maintenancewindowdetails-daysofweek.md&#34;&gt;DaysOfWeek&lt;/a&gt;</i>
<a href="#months" title="Months">Months</a>: <i>
      - &lt;a href=&#34;maintenancewindowdetails-months.md&#34;&gt;Months&lt;/a&gt;</i>
</pre>

## Properties

#### HoursOfDay

_Required_: No
_Type_: List of Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Preference

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WeeksOfMonth

_Required_: No
_Type_: List of Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DaysOfWeek

_Required_: No
_Type_: List of &lt;a href=&#34;maintenancewindowdetails-daysofweek.md&#34;&gt;DaysOfWeek&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Months

_Required_: No
_Type_: List of &lt;a href=&#34;maintenancewindowdetails-months.md&#34;&gt;Months&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

