# TF::GoogleBeta::GoogleMonitoringAlertPolicy ConditionsDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#displayname" title="DisplayName">DisplayName</a>" : <i>String</i>,
    "<a href="#conditionabsent" title="ConditionAbsent">ConditionAbsent</a>" : <i>[ <a href="conditionabsentdefinition.md">ConditionAbsentDefinition</a>, ... ]</i>,
    "<a href="#conditionmonitoringquerylanguage" title="ConditionMonitoringQueryLanguage">ConditionMonitoringQueryLanguage</a>" : <i>[ <a href="conditionmonitoringquerylanguagedefinition.md">ConditionMonitoringQueryLanguageDefinition</a>, ... ]</i>,
    "<a href="#conditionthreshold" title="ConditionThreshold">ConditionThreshold</a>" : <i>[ <a href="conditionthresholddefinition.md">ConditionThresholdDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#displayname" title="DisplayName">DisplayName</a>: <i>String</i>
<a href="#conditionabsent" title="ConditionAbsent">ConditionAbsent</a>: <i>
      - <a href="conditionabsentdefinition.md">ConditionAbsentDefinition</a></i>
<a href="#conditionmonitoringquerylanguage" title="ConditionMonitoringQueryLanguage">ConditionMonitoringQueryLanguage</a>: <i>
      - <a href="conditionmonitoringquerylanguagedefinition.md">ConditionMonitoringQueryLanguageDefinition</a></i>
<a href="#conditionthreshold" title="ConditionThreshold">ConditionThreshold</a>: <i>
      - <a href="conditionthresholddefinition.md">ConditionThresholdDefinition</a></i>
</pre>

## Properties

#### DisplayName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConditionAbsent

_Required_: No

_Type_: List of <a href="conditionabsentdefinition.md">ConditionAbsentDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConditionMonitoringQueryLanguage

_Required_: No

_Type_: List of <a href="conditionmonitoringquerylanguagedefinition.md">ConditionMonitoringQueryLanguageDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConditionThreshold

_Required_: No

_Type_: List of <a href="conditionthresholddefinition.md">ConditionThresholdDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

