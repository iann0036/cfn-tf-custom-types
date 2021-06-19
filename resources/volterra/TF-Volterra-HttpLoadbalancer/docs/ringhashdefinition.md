# TF::Volterra::HttpLoadbalancer RingHashDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#hashpolicy" title="HashPolicy">HashPolicy</a>" : <i>[ <a href="hashpolicydefinition.md">HashPolicyDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#hashpolicy" title="HashPolicy">HashPolicy</a>: <i>
      - <a href="hashpolicydefinition.md">HashPolicyDefinition</a></i>
</pre>

## Properties

#### HashPolicy

_Required_: No

_Type_: List of <a href="hashpolicydefinition.md">HashPolicyDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

