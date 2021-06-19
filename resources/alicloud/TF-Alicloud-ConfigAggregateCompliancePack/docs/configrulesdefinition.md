# TF::Alicloud::ConfigAggregateCompliancePack ConfigRulesDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#managedruleidentifier" title="ManagedRuleIdentifier">ManagedRuleIdentifier</a>" : <i>String</i>,
    "<a href="#configruleparameters" title="ConfigRuleParameters">ConfigRuleParameters</a>" : <i>[ <a href="configruleparametersdefinition.md">ConfigRuleParametersDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#managedruleidentifier" title="ManagedRuleIdentifier">ManagedRuleIdentifier</a>: <i>String</i>
<a href="#configruleparameters" title="ConfigRuleParameters">ConfigRuleParameters</a>: <i>
      - <a href="configruleparametersdefinition.md">ConfigRuleParametersDefinition</a></i>
</pre>

## Properties

#### ManagedRuleIdentifier

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConfigRuleParameters

_Required_: No

_Type_: List of <a href="configruleparametersdefinition.md">ConfigRuleParametersDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

