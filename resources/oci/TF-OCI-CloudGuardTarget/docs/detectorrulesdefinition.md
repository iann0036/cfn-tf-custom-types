# TF::OCI::CloudGuardTarget DetectorRulesDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#detectorruleid" title="DetectorRuleId">DetectorRuleId</a>" : <i>String</i>,
    "<a href="#details" title="Details">Details</a>" : <i>[ <a href="detailsdefinition.md">DetailsDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#detectorruleid" title="DetectorRuleId">DetectorRuleId</a>: <i>String</i>
<a href="#details" title="Details">Details</a>: <i>
      - <a href="detailsdefinition.md">DetailsDefinition</a></i>
</pre>

## Properties

#### DetectorRuleId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Details

_Required_: No

_Type_: List of <a href="detailsdefinition.md">DetailsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

