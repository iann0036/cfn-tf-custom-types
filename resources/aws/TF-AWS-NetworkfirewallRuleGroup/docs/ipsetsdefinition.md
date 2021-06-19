# TF::AWS::NetworkfirewallRuleGroup IpSetsDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#key" title="Key">Key</a>" : <i>String</i>,
    "<a href="#ipset" title="IpSet">IpSet</a>" : <i>[ <a href="ipsetdefinition.md">IpSetDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#key" title="Key">Key</a>: <i>String</i>
<a href="#ipset" title="IpSet">IpSet</a>: <i>
      - <a href="ipsetdefinition.md">IpSetDefinition</a></i>
</pre>

## Properties

#### Key

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpSet

_Required_: No

_Type_: List of <a href="ipsetdefinition.md">IpSetDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

