# TF::Volterra::ServicePolicyRule L4DestsDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#portranges" title="PortRanges">PortRanges</a>" : <i>String</i>,
    "<a href="#prefixes" title="Prefixes">Prefixes</a>" : <i>[ String, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#portranges" title="PortRanges">PortRanges</a>: <i>String</i>
<a href="#prefixes" title="Prefixes">Prefixes</a>: <i>
      - String</i>
</pre>

## Properties

#### PortRanges

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Prefixes

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

