# TF::Thunder::InterfaceEthernet BfdDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#demand" title="Demand">Demand</a>" : <i>Double</i>,
    "<a href="#echo" title="Echo">Echo</a>" : <i>Double</i>,
    "<a href="#uuid" title="Uuid">Uuid</a>" : <i>String</i>,
    "<a href="#authentication" title="Authentication">Authentication</a>" : <i>[ <a href="authenticationdefinition.md">AuthenticationDefinition</a>, ... ]</i>,
    "<a href="#intervalcfg" title="IntervalCfg">IntervalCfg</a>" : <i>[ <a href="intervalcfgdefinition.md">IntervalCfgDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#demand" title="Demand">Demand</a>: <i>Double</i>
<a href="#echo" title="Echo">Echo</a>: <i>Double</i>
<a href="#uuid" title="Uuid">Uuid</a>: <i>String</i>
<a href="#authentication" title="Authentication">Authentication</a>: <i>
      - <a href="authenticationdefinition.md">AuthenticationDefinition</a></i>
<a href="#intervalcfg" title="IntervalCfg">IntervalCfg</a>: <i>
      - <a href="intervalcfgdefinition.md">IntervalCfgDefinition</a></i>
</pre>

## Properties

#### Demand

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Echo

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Uuid

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Authentication

_Required_: No

_Type_: List of <a href="authenticationdefinition.md">AuthenticationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IntervalCfg

_Required_: No

_Type_: List of <a href="intervalcfgdefinition.md">IntervalCfgDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

