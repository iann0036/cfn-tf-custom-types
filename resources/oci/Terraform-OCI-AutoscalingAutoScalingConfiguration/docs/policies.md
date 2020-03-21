# Terraform::OCI::AutoscalingAutoScalingConfiguration Policies

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#displayname" title="DisplayName">DisplayName</a>" : <i>String</i>,
    "<a href="#policytype" title="PolicyType">PolicyType</a>" : <i>String</i>,
    "<a href="#capacity" title="Capacity">Capacity</a>" : <i>[ &lt;a href=&#34;policies-capacity.md&#34;&gt;Capacity&lt;/a&gt;, ... ]</i>,
    "<a href="#rules" title="Rules">Rules</a>" : <i>[ &lt;a href=&#34;policies-rules.md&#34;&gt;Rules&lt;/a&gt;, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#displayname" title="DisplayName">DisplayName</a>: <i>String</i>
<a href="#policytype" title="PolicyType">PolicyType</a>: <i>String</i>
<a href="#capacity" title="Capacity">Capacity</a>: <i>
      - &lt;a href=&#34;policies-capacity.md&#34;&gt;Capacity&lt;/a&gt;</i>
<a href="#rules" title="Rules">Rules</a>: <i>
      - &lt;a href=&#34;policies-rules.md&#34;&gt;Rules&lt;/a&gt;</i>
</pre>

## Properties

#### DisplayName

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PolicyType

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Capacity

_Required_: No
_Type_: List of &lt;a href=&#34;policies-capacity.md&#34;&gt;Capacity&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Rules

_Required_: No
_Type_: List of &lt;a href=&#34;policies-rules.md&#34;&gt;Rules&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

