# Terraform::Google::MonitoringAlertPolicy Conditions

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#displayname" title="DisplayName">DisplayName</a>" : <i>String</i>,
    "<a href="#conditionabsent" title="ConditionAbsent">ConditionAbsent</a>" : <i>[ &lt;a href=&#34;conditions-conditionabsent.md&#34;&gt;ConditionAbsent&lt;/a&gt;, ... ]</i>,
    "<a href="#conditionthreshold" title="ConditionThreshold">ConditionThreshold</a>" : <i>[ &lt;a href=&#34;conditions-conditionthreshold.md&#34;&gt;ConditionThreshold&lt;/a&gt;, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#displayname" title="DisplayName">DisplayName</a>: <i>String</i>
<a href="#conditionabsent" title="ConditionAbsent">ConditionAbsent</a>: <i>
      - &lt;a href=&#34;conditions-conditionabsent.md&#34;&gt;ConditionAbsent&lt;/a&gt;</i>
<a href="#conditionthreshold" title="ConditionThreshold">ConditionThreshold</a>: <i>
      - &lt;a href=&#34;conditions-conditionthreshold.md&#34;&gt;ConditionThreshold&lt;/a&gt;</i>
</pre>

## Properties

#### DisplayName

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConditionAbsent

_Required_: No
_Type_: List of &lt;a href=&#34;conditions-conditionabsent.md&#34;&gt;ConditionAbsent&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConditionThreshold

_Required_: No
_Type_: List of &lt;a href=&#34;conditions-conditionthreshold.md&#34;&gt;ConditionThreshold&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

