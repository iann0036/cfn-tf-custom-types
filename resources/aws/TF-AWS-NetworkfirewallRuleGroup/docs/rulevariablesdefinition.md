# TF::AWS::NetworkfirewallRuleGroup RuleVariablesDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#ipsets" title="IpSets">IpSets</a>" : <i>[ <a href="ipsetsdefinition.md">IpSetsDefinition</a>, ... ]</i>,
    "<a href="#portsets" title="PortSets">PortSets</a>" : <i>[ <a href="portsetsdefinition.md">PortSetsDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#ipsets" title="IpSets">IpSets</a>: <i>
      - <a href="ipsetsdefinition.md">IpSetsDefinition</a></i>
<a href="#portsets" title="PortSets">PortSets</a>: <i>
      - <a href="portsetsdefinition.md">PortSetsDefinition</a></i>
</pre>

## Properties

#### IpSets

_Required_: No

_Type_: List of <a href="ipsetsdefinition.md">IpSetsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PortSets

_Required_: No

_Type_: List of <a href="portsetsdefinition.md">PortSetsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

