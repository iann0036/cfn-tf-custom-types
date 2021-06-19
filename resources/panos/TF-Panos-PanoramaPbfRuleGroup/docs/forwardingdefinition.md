# TF::Panos::PanoramaPbfRuleGroup ForwardingDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#action" title="Action">Action</a>" : <i>String</i>,
    "<a href="#egressinterface" title="EgressInterface">EgressInterface</a>" : <i>String</i>,
    "<a href="#nexthoptype" title="NextHopType">NextHopType</a>" : <i>String</i>,
    "<a href="#nexthopvalue" title="NextHopValue">NextHopValue</a>" : <i>String</i>,
    "<a href="#vsys" title="Vsys">Vsys</a>" : <i>String</i>,
    "<a href="#monitor" title="Monitor">Monitor</a>" : <i>[ <a href="monitordefinition.md">MonitorDefinition</a>, ... ]</i>,
    "<a href="#symmetricreturn" title="SymmetricReturn">SymmetricReturn</a>" : <i>[ <a href="symmetricreturndefinition.md">SymmetricReturnDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#action" title="Action">Action</a>: <i>String</i>
<a href="#egressinterface" title="EgressInterface">EgressInterface</a>: <i>String</i>
<a href="#nexthoptype" title="NextHopType">NextHopType</a>: <i>String</i>
<a href="#nexthopvalue" title="NextHopValue">NextHopValue</a>: <i>String</i>
<a href="#vsys" title="Vsys">Vsys</a>: <i>String</i>
<a href="#monitor" title="Monitor">Monitor</a>: <i>
      - <a href="monitordefinition.md">MonitorDefinition</a></i>
<a href="#symmetricreturn" title="SymmetricReturn">SymmetricReturn</a>: <i>
      - <a href="symmetricreturndefinition.md">SymmetricReturnDefinition</a></i>
</pre>

## Properties

#### Action

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EgressInterface

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NextHopType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NextHopValue

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vsys

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Monitor

_Required_: No

_Type_: List of <a href="monitordefinition.md">MonitorDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SymmetricReturn

_Required_: No

_Type_: List of <a href="symmetricreturndefinition.md">SymmetricReturnDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

