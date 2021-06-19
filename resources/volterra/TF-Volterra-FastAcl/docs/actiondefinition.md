# TF::Volterra::FastAcl ActionDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#simpleaction" title="SimpleAction">SimpleAction</a>" : <i>String</i>,
    "<a href="#policeraction" title="PolicerAction">PolicerAction</a>" : <i>[ <a href="policeractiondefinition.md">PolicerActionDefinition</a>, ... ]</i>,
    "<a href="#protocolpoliceraction" title="ProtocolPolicerAction">ProtocolPolicerAction</a>" : <i>[ <a href="protocolpoliceractiondefinition.md">ProtocolPolicerActionDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#simpleaction" title="SimpleAction">SimpleAction</a>: <i>String</i>
<a href="#policeraction" title="PolicerAction">PolicerAction</a>: <i>
      - <a href="policeractiondefinition.md">PolicerActionDefinition</a></i>
<a href="#protocolpoliceraction" title="ProtocolPolicerAction">ProtocolPolicerAction</a>: <i>
      - <a href="protocolpoliceractiondefinition.md">ProtocolPolicerActionDefinition</a></i>
</pre>

## Properties

#### SimpleAction

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PolicerAction

_Required_: No

_Type_: List of <a href="policeractiondefinition.md">PolicerActionDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProtocolPolicerAction

_Required_: No

_Type_: List of <a href="protocolpoliceractiondefinition.md">ProtocolPolicerActionDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

