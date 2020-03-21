# Terraform::AzureRM::ApplicationGateway RewriteRuleSet RewriteRule

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#rulesequence" title="RuleSequence">RuleSequence</a>" : <i>Double</i>,
    "<a href="#condition" title="Condition">Condition</a>" : <i>[ <a href="rewriteruleset-rewriterule-condition.md">Condition</a>, ... ]</i>,
    "<a href="#requestheaderconfiguration" title="RequestHeaderConfiguration">RequestHeaderConfiguration</a>" : <i>[ <a href="rewriteruleset-rewriterule-requestheaderconfiguration.md">RequestHeaderConfiguration</a>, ... ]</i>,
    "<a href="#responseheaderconfiguration" title="ResponseHeaderConfiguration">ResponseHeaderConfiguration</a>" : <i>[ <a href="rewriteruleset-rewriterule-responseheaderconfiguration.md">ResponseHeaderConfiguration</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#rulesequence" title="RuleSequence">RuleSequence</a>: <i>Double</i>
<a href="#condition" title="Condition">Condition</a>: <i>
      - <a href="rewriteruleset-rewriterule-condition.md">Condition</a></i>
<a href="#requestheaderconfiguration" title="RequestHeaderConfiguration">RequestHeaderConfiguration</a>: <i>
      - <a href="rewriteruleset-rewriterule-requestheaderconfiguration.md">RequestHeaderConfiguration</a></i>
<a href="#responseheaderconfiguration" title="ResponseHeaderConfiguration">ResponseHeaderConfiguration</a>: <i>
      - <a href="rewriteruleset-rewriterule-responseheaderconfiguration.md">ResponseHeaderConfiguration</a></i>
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

_Type_: List of <a href="rewriteruleset-rewriterule-condition.md">Condition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RequestHeaderConfiguration

_Required_: No

_Type_: List of <a href="rewriteruleset-rewriterule-requestheaderconfiguration.md">RequestHeaderConfiguration</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResponseHeaderConfiguration

_Required_: No

_Type_: List of <a href="rewriteruleset-rewriterule-responseheaderconfiguration.md">ResponseHeaderConfiguration</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

