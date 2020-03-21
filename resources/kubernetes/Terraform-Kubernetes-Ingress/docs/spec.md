# Terraform::Kubernetes::Ingress Spec

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#backend" title="Backend">Backend</a>" : <i>[ &lt;a href=&#34;spec-backend.md&#34;&gt;Backend&lt;/a&gt;, ... ]</i>,
    "<a href="#rule" title="Rule">Rule</a>" : <i>[ &lt;a href=&#34;spec-rule.md&#34;&gt;Rule&lt;/a&gt;, ... ]</i>,
    "<a href="#tls" title="Tls">Tls</a>" : <i>[ &lt;a href=&#34;spec-tls.md&#34;&gt;Tls&lt;/a&gt;, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#backend" title="Backend">Backend</a>: <i>
      - &lt;a href=&#34;spec-backend.md&#34;&gt;Backend&lt;/a&gt;</i>
<a href="#rule" title="Rule">Rule</a>: <i>
      - &lt;a href=&#34;spec-rule.md&#34;&gt;Rule&lt;/a&gt;</i>
<a href="#tls" title="Tls">Tls</a>: <i>
      - &lt;a href=&#34;spec-tls.md&#34;&gt;Tls&lt;/a&gt;</i>
</pre>

## Properties

#### Backend

_Required_: No
_Type_: List of &lt;a href=&#34;spec-backend.md&#34;&gt;Backend&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Rule

_Required_: No
_Type_: List of &lt;a href=&#34;spec-rule.md&#34;&gt;Rule&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tls

_Required_: No
_Type_: List of &lt;a href=&#34;spec-tls.md&#34;&gt;Tls&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

