# TF::AzureRM::SentinelAlertRuleScheduled GroupingDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#enabled" title="Enabled">Enabled</a>" : <i>Boolean</i>,
    "<a href="#entitymatchingmethod" title="EntityMatchingMethod">EntityMatchingMethod</a>" : <i>String</i>,
    "<a href="#groupby" title="GroupBy">GroupBy</a>" : <i>[ String, ... ]</i>,
    "<a href="#lookbackduration" title="LookbackDuration">LookbackDuration</a>" : <i>String</i>,
    "<a href="#reopenclosedincidents" title="ReopenClosedIncidents">ReopenClosedIncidents</a>" : <i>Boolean</i>
}
</pre>

### YAML

<pre>
<a href="#enabled" title="Enabled">Enabled</a>: <i>Boolean</i>
<a href="#entitymatchingmethod" title="EntityMatchingMethod">EntityMatchingMethod</a>: <i>String</i>
<a href="#groupby" title="GroupBy">GroupBy</a>: <i>
      - String</i>
<a href="#lookbackduration" title="LookbackDuration">LookbackDuration</a>: <i>String</i>
<a href="#reopenclosedincidents" title="ReopenClosedIncidents">ReopenClosedIncidents</a>: <i>Boolean</i>
</pre>

## Properties

#### Enabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EntityMatchingMethod

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GroupBy

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LookbackDuration

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReopenClosedIncidents

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

