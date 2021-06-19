# TF::TencentCloud::CosBucket LifecycleRulesDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#filterprefix" title="FilterPrefix">FilterPrefix</a>" : <i>String</i>,
    "<a href="#expiration" title="Expiration">Expiration</a>" : <i>[ <a href="expirationdefinition.md">ExpirationDefinition</a>, ... ]</i>,
    "<a href="#transition" title="Transition">Transition</a>" : <i>[ <a href="transitiondefinition.md">TransitionDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#filterprefix" title="FilterPrefix">FilterPrefix</a>: <i>String</i>
<a href="#expiration" title="Expiration">Expiration</a>: <i>
      - <a href="expirationdefinition.md">ExpirationDefinition</a></i>
<a href="#transition" title="Transition">Transition</a>: <i>
      - <a href="transitiondefinition.md">TransitionDefinition</a></i>
</pre>

## Properties

#### FilterPrefix

Object key prefix identifying one or more objects to which the rule applies.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Expiration

_Required_: No

_Type_: List of <a href="expirationdefinition.md">ExpirationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Transition

_Required_: No

_Type_: List of <a href="transitiondefinition.md">TransitionDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

