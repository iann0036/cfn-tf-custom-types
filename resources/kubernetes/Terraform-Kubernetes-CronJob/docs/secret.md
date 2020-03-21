# Terraform::Kubernetes::CronJob Secret

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#defaultmode" title="DefaultMode">DefaultMode</a>" : <i>String</i>,
    "<a href="#optional" title="Optional">Optional</a>" : <i>Boolean</i>,
    "<a href="#secretname" title="SecretName">SecretName</a>" : <i>String</i>,
    "<a href="#items" title="Items">Items</a>" : <i>[ &lt;a href=&#34;secret-items.md&#34;&gt;Items&lt;/a&gt;, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#defaultmode" title="DefaultMode">DefaultMode</a>: <i>String</i>
<a href="#optional" title="Optional">Optional</a>: <i>Boolean</i>
<a href="#secretname" title="SecretName">SecretName</a>: <i>String</i>
<a href="#items" title="Items">Items</a>: <i>
      - &lt;a href=&#34;secret-items.md&#34;&gt;Items&lt;/a&gt;</i>
</pre>

## Properties

#### DefaultMode

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Optional

_Required_: No
_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecretName

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Items

_Required_: No
_Type_: List of &lt;a href=&#34;secret-items.md&#34;&gt;Items&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

