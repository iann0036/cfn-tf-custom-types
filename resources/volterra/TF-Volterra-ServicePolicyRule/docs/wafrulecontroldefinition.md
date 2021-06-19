# TF::Volterra::ServicePolicyRule WafRuleControlDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#monitoringmode" title="MonitoringMode">MonitoringMode</a>" : <i>Boolean</i>,
    "<a href="#excluderuleids" title="ExcludeRuleIds">ExcludeRuleIds</a>" : <i>[ <a href="excluderuleidsdefinition.md">ExcludeRuleIdsDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#monitoringmode" title="MonitoringMode">MonitoringMode</a>: <i>Boolean</i>
<a href="#excluderuleids" title="ExcludeRuleIds">ExcludeRuleIds</a>: <i>
      - <a href="excluderuleidsdefinition.md">ExcludeRuleIdsDefinition</a></i>
</pre>

## Properties

#### MonitoringMode

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExcludeRuleIds

_Required_: No

_Type_: List of <a href="excluderuleidsdefinition.md">ExcludeRuleIdsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

