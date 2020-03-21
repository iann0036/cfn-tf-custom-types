# Terraform::Kubernetes::ResourceQuota Spec

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#hard" title="Hard">Hard</a>" : <i>[ &lt;a href=&#34;spec-hard.md&#34;&gt;Hard&lt;/a&gt;, ... ]</i>,
    "<a href="#scopes" title="Scopes">Scopes</a>" : <i>[ String, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#hard" title="Hard">Hard</a>: <i>
      - &lt;a href=&#34;spec-hard.md&#34;&gt;Hard&lt;/a&gt;</i>
<a href="#scopes" title="Scopes">Scopes</a>: <i>
      - String</i>
</pre>

## Properties

#### Hard

_Required_: No
_Type_: List of &lt;a href=&#34;spec-hard.md&#34;&gt;Hard&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Scopes

_Required_: No
_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

