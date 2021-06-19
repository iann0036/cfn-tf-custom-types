# TF::Volterra::HttpLoadbalancer IpPrefixListDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#invertmatch" title="InvertMatch">InvertMatch</a>" : <i>Boolean</i>,
    "<a href="#ipprefixes" title="IpPrefixes">IpPrefixes</a>" : <i>[ String, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#invertmatch" title="InvertMatch">InvertMatch</a>: <i>Boolean</i>
<a href="#ipprefixes" title="IpPrefixes">IpPrefixes</a>: <i>
      - String</i>
</pre>

## Properties

#### InvertMatch

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpPrefixes

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

