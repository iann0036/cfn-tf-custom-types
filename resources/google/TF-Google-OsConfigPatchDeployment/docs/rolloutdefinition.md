# TF::Google::OsConfigPatchDeployment RolloutDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#mode" title="Mode">Mode</a>" : <i>String</i>,
    "<a href="#disruptionbudget" title="DisruptionBudget">DisruptionBudget</a>" : <i>[ <a href="disruptionbudgetdefinition.md">DisruptionBudgetDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#mode" title="Mode">Mode</a>: <i>String</i>
<a href="#disruptionbudget" title="DisruptionBudget">DisruptionBudget</a>: <i>
      - <a href="disruptionbudgetdefinition.md">DisruptionBudgetDefinition</a></i>
</pre>

## Properties

#### Mode

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisruptionBudget

_Required_: No

_Type_: List of <a href="disruptionbudgetdefinition.md">DisruptionBudgetDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

