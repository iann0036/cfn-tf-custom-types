# TF::RKE::Cluster IngressDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#dnspolicy" title="DnsPolicy">DnsPolicy</a>" : <i>String</i>,
    "<a href="#extraargs" title="ExtraArgs">ExtraArgs</a>" : <i>[ <a href="extraargsdefinition.md">ExtraArgsDefinition</a>, ... ]</i>,
    "<a href="#nodeselector" title="NodeSelector">NodeSelector</a>" : <i>[ <a href="nodeselectordefinition.md">NodeSelectorDefinition</a>, ... ]</i>,
    "<a href="#options" title="Options">Options</a>" : <i>[ <a href="optionsdefinition.md">OptionsDefinition</a>, ... ]</i>,
    "<a href="#provider" title="Provider">Provider</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#dnspolicy" title="DnsPolicy">DnsPolicy</a>: <i>String</i>
<a href="#extraargs" title="ExtraArgs">ExtraArgs</a>: <i>
      - <a href="extraargsdefinition.md">ExtraArgsDefinition</a></i>
<a href="#nodeselector" title="NodeSelector">NodeSelector</a>: <i>
      - <a href="nodeselectordefinition.md">NodeSelectorDefinition</a></i>
<a href="#options" title="Options">Options</a>: <i>
      - <a href="optionsdefinition.md">OptionsDefinition</a></i>
<a href="#provider" title="Provider">Provider</a>: <i>String</i>
</pre>

## Properties

#### DnsPolicy

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExtraArgs

_Required_: No

_Type_: List of <a href="extraargsdefinition.md">ExtraArgsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NodeSelector

_Required_: No

_Type_: List of <a href="nodeselectordefinition.md">NodeSelectorDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Options

_Required_: No

_Type_: List of <a href="optionsdefinition.md">OptionsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Provider

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

