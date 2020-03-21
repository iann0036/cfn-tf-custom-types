# Terraform::Google::ComputeResourcePolicy Schedule

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#dailyschedule" title="DailySchedule">DailySchedule</a>" : <i>[ &lt;a href=&#34;schedule-dailyschedule.md&#34;&gt;DailySchedule&lt;/a&gt;, ... ]</i>,
    "<a href="#hourlyschedule" title="HourlySchedule">HourlySchedule</a>" : <i>[ &lt;a href=&#34;schedule-hourlyschedule.md&#34;&gt;HourlySchedule&lt;/a&gt;, ... ]</i>,
    "<a href="#weeklyschedule" title="WeeklySchedule">WeeklySchedule</a>" : <i>[ &lt;a href=&#34;schedule-weeklyschedule.md&#34;&gt;WeeklySchedule&lt;/a&gt;, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#dailyschedule" title="DailySchedule">DailySchedule</a>: <i>
      - &lt;a href=&#34;schedule-dailyschedule.md&#34;&gt;DailySchedule&lt;/a&gt;</i>
<a href="#hourlyschedule" title="HourlySchedule">HourlySchedule</a>: <i>
      - &lt;a href=&#34;schedule-hourlyschedule.md&#34;&gt;HourlySchedule&lt;/a&gt;</i>
<a href="#weeklyschedule" title="WeeklySchedule">WeeklySchedule</a>: <i>
      - &lt;a href=&#34;schedule-weeklyschedule.md&#34;&gt;WeeklySchedule&lt;/a&gt;</i>
</pre>

## Properties

#### DailySchedule

_Required_: No
_Type_: List of &lt;a href=&#34;schedule-dailyschedule.md&#34;&gt;DailySchedule&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HourlySchedule

_Required_: No
_Type_: List of &lt;a href=&#34;schedule-hourlyschedule.md&#34;&gt;HourlySchedule&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WeeklySchedule

_Required_: No
_Type_: List of &lt;a href=&#34;schedule-weeklyschedule.md&#34;&gt;WeeklySchedule&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

