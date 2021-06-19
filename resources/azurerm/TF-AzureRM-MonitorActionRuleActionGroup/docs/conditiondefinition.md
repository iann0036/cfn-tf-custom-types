# TF::AzureRM::MonitorActionRuleActionGroup ConditionDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#alertcontext" title="AlertContext">AlertContext</a>" : <i>[ <a href="alertcontextdefinition.md">AlertContextDefinition</a>, ... ]</i>,
    "<a href="#alertruleid" title="AlertRuleId">AlertRuleId</a>" : <i>[ <a href="alertruleiddefinition.md">AlertRuleIdDefinition</a>, ... ]</i>,
    "<a href="#description" title="Description">Description</a>" : <i>[ <a href="descriptiondefinition.md">DescriptionDefinition</a>, ... ]</i>,
    "<a href="#monitor" title="Monitor">Monitor</a>" : <i>[ <a href="monitordefinition.md">MonitorDefinition</a>, ... ]</i>,
    "<a href="#monitorservice" title="MonitorService">MonitorService</a>" : <i>[ <a href="monitorservicedefinition.md">MonitorServiceDefinition</a>, ... ]</i>,
    "<a href="#severity" title="Severity">Severity</a>" : <i>[ <a href="severitydefinition.md">SeverityDefinition</a>, ... ]</i>,
    "<a href="#targetresourcetype" title="TargetResourceType">TargetResourceType</a>" : <i>[ <a href="targetresourcetypedefinition.md">TargetResourceTypeDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#alertcontext" title="AlertContext">AlertContext</a>: <i>
      - <a href="alertcontextdefinition.md">AlertContextDefinition</a></i>
<a href="#alertruleid" title="AlertRuleId">AlertRuleId</a>: <i>
      - <a href="alertruleiddefinition.md">AlertRuleIdDefinition</a></i>
<a href="#description" title="Description">Description</a>: <i>
      - <a href="descriptiondefinition.md">DescriptionDefinition</a></i>
<a href="#monitor" title="Monitor">Monitor</a>: <i>
      - <a href="monitordefinition.md">MonitorDefinition</a></i>
<a href="#monitorservice" title="MonitorService">MonitorService</a>: <i>
      - <a href="monitorservicedefinition.md">MonitorServiceDefinition</a></i>
<a href="#severity" title="Severity">Severity</a>: <i>
      - <a href="severitydefinition.md">SeverityDefinition</a></i>
<a href="#targetresourcetype" title="TargetResourceType">TargetResourceType</a>: <i>
      - <a href="targetresourcetypedefinition.md">TargetResourceTypeDefinition</a></i>
</pre>

## Properties

#### AlertContext

_Required_: No

_Type_: List of <a href="alertcontextdefinition.md">AlertContextDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AlertRuleId

_Required_: No

_Type_: List of <a href="alertruleiddefinition.md">AlertRuleIdDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

_Required_: No

_Type_: List of <a href="descriptiondefinition.md">DescriptionDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Monitor

_Required_: No

_Type_: List of <a href="monitordefinition.md">MonitorDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MonitorService

_Required_: No

_Type_: List of <a href="monitorservicedefinition.md">MonitorServiceDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Severity

_Required_: No

_Type_: List of <a href="severitydefinition.md">SeverityDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TargetResourceType

_Required_: No

_Type_: List of <a href="targetresourcetypedefinition.md">TargetResourceTypeDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

