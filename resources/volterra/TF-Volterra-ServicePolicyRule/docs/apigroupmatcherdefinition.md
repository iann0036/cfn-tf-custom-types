# TF::Volterra::ServicePolicyRule ApiGroupMatcherDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#invertmatcher" title="InvertMatcher">InvertMatcher</a>" : <i>Boolean</i>,
    "<a href="#match" title="Match">Match</a>" : <i>[ String, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#invertmatcher" title="InvertMatcher">InvertMatcher</a>: <i>Boolean</i>
<a href="#match" title="Match">Match</a>: <i>
      - String</i>
</pre>

## Properties

#### InvertMatcher

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Match

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

