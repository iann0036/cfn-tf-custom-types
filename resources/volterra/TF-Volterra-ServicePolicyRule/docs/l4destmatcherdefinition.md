# TF::Volterra::ServicePolicyRule L4DestMatcherDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#invertmatcher" title="InvertMatcher">InvertMatcher</a>" : <i>Boolean</i>,
    "<a href="#l4dests" title="L4Dests">L4Dests</a>" : <i>[ <a href="l4destsdefinition.md">L4DestsDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#invertmatcher" title="InvertMatcher">InvertMatcher</a>: <i>Boolean</i>
<a href="#l4dests" title="L4Dests">L4Dests</a>: <i>
      - <a href="l4destsdefinition.md">L4DestsDefinition</a></i>
</pre>

## Properties

#### InvertMatcher

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### L4Dests

_Required_: No

_Type_: List of <a href="l4destsdefinition.md">L4DestsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

