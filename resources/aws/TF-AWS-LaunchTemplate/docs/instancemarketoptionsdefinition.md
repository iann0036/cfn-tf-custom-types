# TF::AWS::LaunchTemplate InstanceMarketOptionsDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#markettype" title="MarketType">MarketType</a>" : <i>String</i>,
    "<a href="#spotoptions" title="SpotOptions">SpotOptions</a>" : <i>[ <a href="spotoptionsdefinition.md">SpotOptionsDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#markettype" title="MarketType">MarketType</a>: <i>String</i>
<a href="#spotoptions" title="SpotOptions">SpotOptions</a>: <i>
      - <a href="spotoptionsdefinition.md">SpotOptionsDefinition</a></i>
</pre>

## Properties

#### MarketType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SpotOptions

_Required_: No

_Type_: List of <a href="spotoptionsdefinition.md">SpotOptionsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

