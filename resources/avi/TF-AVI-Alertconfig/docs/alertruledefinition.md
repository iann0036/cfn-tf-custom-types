# TF::AVI::Alertconfig AlertRuleDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#eventmatchfilter" title="EventMatchFilter">EventMatchFilter</a>" : <i>String</i>,
    "<a href="#operator" title="Operator">Operator</a>" : <i>String</i>,
    "<a href="#connapplogrule" title="ConnAppLogRule">ConnAppLogRule</a>" : <i>[ <a href="connapplogruledefinition.md">ConnAppLogRuleDefinition</a>, ... ]</i>,
    "<a href="#metricsrule" title="MetricsRule">MetricsRule</a>" : <i>[ <a href="metricsruledefinition.md">MetricsRuleDefinition</a>, ... ]</i>,
    "<a href="#syseventrule" title="SysEventRule">SysEventRule</a>" : <i>[ <a href="syseventruledefinition.md">SysEventRuleDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#eventmatchfilter" title="EventMatchFilter">EventMatchFilter</a>: <i>String</i>
<a href="#operator" title="Operator">Operator</a>: <i>String</i>
<a href="#connapplogrule" title="ConnAppLogRule">ConnAppLogRule</a>: <i>
      - <a href="connapplogruledefinition.md">ConnAppLogRuleDefinition</a></i>
<a href="#metricsrule" title="MetricsRule">MetricsRule</a>: <i>
      - <a href="metricsruledefinition.md">MetricsRuleDefinition</a></i>
<a href="#syseventrule" title="SysEventRule">SysEventRule</a>: <i>
      - <a href="syseventruledefinition.md">SysEventRuleDefinition</a></i>
</pre>

## Properties

#### EventMatchFilter

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Operator

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConnAppLogRule

_Required_: No

_Type_: List of <a href="connapplogruledefinition.md">ConnAppLogRuleDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MetricsRule

_Required_: No

_Type_: List of <a href="metricsruledefinition.md">MetricsRuleDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SysEventRule

_Required_: No

_Type_: List of <a href="syseventruledefinition.md">SysEventRuleDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

