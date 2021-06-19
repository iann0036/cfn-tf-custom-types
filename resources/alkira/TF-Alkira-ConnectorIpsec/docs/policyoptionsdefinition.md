# TF::Alkira::ConnectorIpsec PolicyOptionsDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#cxpprefixlistids" title="CxpPrefixListIds">CxpPrefixListIds</a>" : <i>[ Double, ... ]</i>,
    "<a href="#onpremprefixlistids" title="OnPremPrefixListIds">OnPremPrefixListIds</a>" : <i>[ Double, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#cxpprefixlistids" title="CxpPrefixListIds">CxpPrefixListIds</a>: <i>
      - Double</i>
<a href="#onpremprefixlistids" title="OnPremPrefixListIds">OnPremPrefixListIds</a>: <i>
      - Double</i>
</pre>

## Properties

#### CxpPrefixListIds

_Required_: Yes

_Type_: List of Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OnPremPrefixListIds

_Required_: Yes

_Type_: List of Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

