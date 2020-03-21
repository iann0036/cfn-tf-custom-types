# Terraform::Kubernetes::PodDisruptionBudget Spec

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#maxunavailable" title="MaxUnavailable">MaxUnavailable</a>" : <i>String</i>,
    "<a href="#minavailable" title="MinAvailable">MinAvailable</a>" : <i>String</i>,
    "<a href="#selector" title="Selector">Selector</a>" : <i>[ &lt;a href=&#34;spec-selector.md&#34;&gt;Selector&lt;/a&gt;, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#maxunavailable" title="MaxUnavailable">MaxUnavailable</a>: <i>String</i>
<a href="#minavailable" title="MinAvailable">MinAvailable</a>: <i>String</i>
<a href="#selector" title="Selector">Selector</a>: <i>
      - &lt;a href=&#34;spec-selector.md&#34;&gt;Selector&lt;/a&gt;</i>
</pre>

## Properties

#### MaxUnavailable

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MinAvailable

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Selector

_Required_: No
_Type_: List of &lt;a href=&#34;spec-selector.md&#34;&gt;Selector&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

