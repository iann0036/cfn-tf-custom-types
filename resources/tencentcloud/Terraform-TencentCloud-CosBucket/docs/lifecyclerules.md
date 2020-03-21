# Terraform::TencentCloud::CosBucket LifecycleRules

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#filterprefix" title="FilterPrefix">FilterPrefix</a>" : <i>String</i>,
    "<a href="#expiration" title="Expiration">Expiration</a>" : <i>[ <a href="lifecyclerules-expiration.md">Expiration</a>, ... ]</i>,
    "<a href="#transition" title="Transition">Transition</a>" : <i>[ <a href="lifecyclerules-transition.md">Transition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#filterprefix" title="FilterPrefix">FilterPrefix</a>: <i>String</i>
<a href="#expiration" title="Expiration">Expiration</a>: <i>
      - <a href="lifecyclerules-expiration.md">Expiration</a></i>
<a href="#transition" title="Transition">Transition</a>: <i>
      - <a href="lifecyclerules-transition.md">Transition</a></i>
</pre>

## Properties

#### FilterPrefix

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Expiration

_Required_: No
_Type_: List of <a href="lifecyclerules-expiration.md">Expiration</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Transition

_Required_: No
_Type_: List of <a href="lifecyclerules-transition.md">Transition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

