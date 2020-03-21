# Terraform::AzureRM::ApplicationGateway RewriteRule

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#rulesequence" title="RuleSequence">RuleSequence</a>" : <i>Double</i>,
    "<a href="#condition" title="Condition">Condition</a>" : <i>[ &lt;a href=&#34;rewriterule-condition.md&#34;&gt;Condition&lt;/a&gt;, ... ]</i>,
    "<a href="#requestheaderconfiguration" title="RequestHeaderConfiguration">RequestHeaderConfiguration</a>" : <i>[ &lt;a href=&#34;rewriterule-requestheaderconfiguration.md&#34;&gt;RequestHeaderConfiguration&lt;/a&gt;, ... ]</i>,
    "<a href="#responseheaderconfiguration" title="ResponseHeaderConfiguration">ResponseHeaderConfiguration</a>" : <i>[ &lt;a href=&#34;rewriterule-responseheaderconfiguration.md&#34;&gt;ResponseHeaderConfiguration&lt;/a&gt;, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#rulesequence" title="RuleSequence">RuleSequence</a>: <i>Double</i>
<a href="#condition" title="Condition">Condition</a>: <i>
      - &lt;a href=&#34;rewriterule-condition.md&#34;&gt;Condition&lt;/a&gt;</i>
<a href="#requestheaderconfiguration" title="RequestHeaderConfiguration">RequestHeaderConfiguration</a>: <i>
      - &lt;a href=&#34;rewriterule-requestheaderconfiguration.md&#34;&gt;RequestHeaderConfiguration&lt;/a&gt;</i>
<a href="#responseheaderconfiguration" title="ResponseHeaderConfiguration">ResponseHeaderConfiguration</a>: <i>
      - &lt;a href=&#34;rewriterule-responseheaderconfiguration.md&#34;&gt;ResponseHeaderConfiguration&lt;/a&gt;</i>
</pre>

## Properties

#### Name

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RuleSequence

_Required_: Yes
_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Condition

_Required_: No
_Type_: List of &lt;a href=&#34;rewriterule-condition.md&#34;&gt;Condition&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RequestHeaderConfiguration

_Required_: No
_Type_: List of &lt;a href=&#34;rewriterule-requestheaderconfiguration.md&#34;&gt;RequestHeaderConfiguration&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResponseHeaderConfiguration

_Required_: No
_Type_: List of &lt;a href=&#34;rewriterule-responseheaderconfiguration.md&#34;&gt;ResponseHeaderConfiguration&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

