# TF::Volterra::ServicePolicyRule WafActionDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#none" title="None">None</a>" : <i>Boolean</i>,
    "<a href="#wafinmonitoringmode" title="WafInMonitoringMode">WafInMonitoringMode</a>" : <i>Boolean</i>,
    "<a href="#wafskipprocessing" title="WafSkipProcessing">WafSkipProcessing</a>" : <i>Boolean</i>,
    "<a href="#wafinlinerulecontrol" title="WafInlineRuleControl">WafInlineRuleControl</a>" : <i>[ <a href="wafinlinerulecontroldefinition.md">WafInlineRuleControlDefinition</a>, ... ]</i>,
    "<a href="#wafrulecontrol" title="WafRuleControl">WafRuleControl</a>" : <i>[ <a href="wafrulecontroldefinition.md">WafRuleControlDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#none" title="None">None</a>: <i>Boolean</i>
<a href="#wafinmonitoringmode" title="WafInMonitoringMode">WafInMonitoringMode</a>: <i>Boolean</i>
<a href="#wafskipprocessing" title="WafSkipProcessing">WafSkipProcessing</a>: <i>Boolean</i>
<a href="#wafinlinerulecontrol" title="WafInlineRuleControl">WafInlineRuleControl</a>: <i>
      - <a href="wafinlinerulecontroldefinition.md">WafInlineRuleControlDefinition</a></i>
<a href="#wafrulecontrol" title="WafRuleControl">WafRuleControl</a>: <i>
      - <a href="wafrulecontroldefinition.md">WafRuleControlDefinition</a></i>
</pre>

## Properties

#### None

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WafInMonitoringMode

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WafSkipProcessing

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WafInlineRuleControl

_Required_: No

_Type_: List of <a href="wafinlinerulecontroldefinition.md">WafInlineRuleControlDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WafRuleControl

_Required_: No

_Type_: List of <a href="wafrulecontroldefinition.md">WafRuleControlDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

