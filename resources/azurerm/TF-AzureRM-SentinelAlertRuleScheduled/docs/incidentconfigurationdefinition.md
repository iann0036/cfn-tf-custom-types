# TF::AzureRM::SentinelAlertRuleScheduled IncidentConfigurationDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#createincident" title="CreateIncident">CreateIncident</a>" : <i>Boolean</i>,
    "<a href="#grouping" title="Grouping">Grouping</a>" : <i>[ <a href="groupingdefinition.md">GroupingDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#createincident" title="CreateIncident">CreateIncident</a>: <i>Boolean</i>
<a href="#grouping" title="Grouping">Grouping</a>: <i>
      - <a href="groupingdefinition.md">GroupingDefinition</a></i>
</pre>

## Properties

#### CreateIncident

_Required_: Yes

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Grouping

_Required_: No

_Type_: List of <a href="groupingdefinition.md">GroupingDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

