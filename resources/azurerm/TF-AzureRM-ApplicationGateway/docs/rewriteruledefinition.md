# TF::AzureRM::ApplicationGateway RewriteRuleDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#rulesequence" title="RuleSequence">RuleSequence</a>" : <i>Double</i>,
    "<a href="#condition" title="Condition">Condition</a>" : <i>[ <a href="conditiondefinition.md">ConditionDefinition</a>, ... ]</i>,
    "<a href="#requestheaderconfiguration" title="RequestHeaderConfiguration">RequestHeaderConfiguration</a>" : <i>[ <a href="requestheaderconfigurationdefinition.md">RequestHeaderConfigurationDefinition</a>, ... ]</i>,
    "<a href="#responseheaderconfiguration" title="ResponseHeaderConfiguration">ResponseHeaderConfiguration</a>" : <i>[ <a href="responseheaderconfigurationdefinition.md">ResponseHeaderConfigurationDefinition</a>, ... ]</i>,
    "<a href="#url" title="Url">Url</a>" : <i>[ <a href="urldefinition.md">UrlDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#rulesequence" title="RuleSequence">RuleSequence</a>: <i>Double</i>
<a href="#condition" title="Condition">Condition</a>: <i>
      - <a href="conditiondefinition.md">ConditionDefinition</a></i>
<a href="#requestheaderconfiguration" title="RequestHeaderConfiguration">RequestHeaderConfiguration</a>: <i>
      - <a href="requestheaderconfigurationdefinition.md">RequestHeaderConfigurationDefinition</a></i>
<a href="#responseheaderconfiguration" title="ResponseHeaderConfiguration">ResponseHeaderConfiguration</a>: <i>
      - <a href="responseheaderconfigurationdefinition.md">ResponseHeaderConfigurationDefinition</a></i>
<a href="#url" title="Url">Url</a>: <i>
      - <a href="urldefinition.md">UrlDefinition</a></i>
</pre>

## Properties

#### Name

Unique name of the rewrite rule block.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RuleSequence

Rule sequence of the rewrite rule that determines the order of execution in a set.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Condition

_Required_: No

_Type_: List of <a href="conditiondefinition.md">ConditionDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RequestHeaderConfiguration

_Required_: No

_Type_: List of <a href="requestheaderconfigurationdefinition.md">RequestHeaderConfigurationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResponseHeaderConfiguration

_Required_: No

_Type_: List of <a href="responseheaderconfigurationdefinition.md">ResponseHeaderConfigurationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Url

_Required_: No

_Type_: List of <a href="urldefinition.md">UrlDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

