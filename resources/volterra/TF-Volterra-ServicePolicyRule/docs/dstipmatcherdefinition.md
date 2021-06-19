# TF::Volterra::ServicePolicyRule DstIpMatcherDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#invertmatcher" title="InvertMatcher">InvertMatcher</a>" : <i>Boolean</i>,
    "<a href="#prefixsets" title="PrefixSets">PrefixSets</a>" : <i>[ <a href="prefixsetsdefinition.md">PrefixSetsDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#invertmatcher" title="InvertMatcher">InvertMatcher</a>: <i>Boolean</i>
<a href="#prefixsets" title="PrefixSets">PrefixSets</a>: <i>
      - <a href="prefixsetsdefinition.md">PrefixSetsDefinition</a></i>
</pre>

## Properties

#### InvertMatcher

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrefixSets

_Required_: No

_Type_: List of <a href="prefixsetsdefinition.md">PrefixSetsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

