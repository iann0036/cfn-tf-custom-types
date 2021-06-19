# TF::GoogleBeta::GoogleComputeOrganizationSecurityPolicyRule ConfigDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#destipranges" title="DestIpRanges">DestIpRanges</a>" : <i>[ String, ... ]</i>,
    "<a href="#srcipranges" title="SrcIpRanges">SrcIpRanges</a>" : <i>[ String, ... ]</i>,
    "<a href="#layer4config" title="Layer4Config">Layer4Config</a>" : <i>[ <a href="layer4configdefinition.md">Layer4ConfigDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#destipranges" title="DestIpRanges">DestIpRanges</a>: <i>
      - String</i>
<a href="#srcipranges" title="SrcIpRanges">SrcIpRanges</a>: <i>
      - String</i>
<a href="#layer4config" title="Layer4Config">Layer4Config</a>: <i>
      - <a href="layer4configdefinition.md">Layer4ConfigDefinition</a></i>
</pre>

## Properties

#### DestIpRanges

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SrcIpRanges

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Layer4Config

_Required_: No

_Type_: List of <a href="layer4configdefinition.md">Layer4ConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

