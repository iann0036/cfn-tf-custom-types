# TF::AVI::Serviceengine VnicNetworksDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#ctlralloc" title="CtlrAlloc">CtlrAlloc</a>" : <i>Boolean</i>,
    "<a href="#mode" title="Mode">Mode</a>" : <i>String</i>,
    "<a href="#ip" title="Ip">Ip</a>" : <i>[ <a href="ipdefinition.md">IpDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#ctlralloc" title="CtlrAlloc">CtlrAlloc</a>: <i>Boolean</i>
<a href="#mode" title="Mode">Mode</a>: <i>String</i>
<a href="#ip" title="Ip">Ip</a>: <i>
      - <a href="ipdefinition.md">IpDefinition</a></i>
</pre>

## Properties

#### CtlrAlloc

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Mode

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ip

_Required_: No

_Type_: List of <a href="ipdefinition.md">IpDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

