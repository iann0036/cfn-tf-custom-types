# TF::OCI::CloudGuardTarget TargetDetectorRecipesDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#detectorrecipeid" title="DetectorRecipeId">DetectorRecipeId</a>" : <i>String</i>,
    "<a href="#detectorrules" title="DetectorRules">DetectorRules</a>" : <i>[ <a href="detectorrulesdefinition.md">DetectorRulesDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#detectorrecipeid" title="DetectorRecipeId">DetectorRecipeId</a>: <i>String</i>
<a href="#detectorrules" title="DetectorRules">DetectorRules</a>: <i>
      - <a href="detectorrulesdefinition.md">DetectorRulesDefinition</a></i>
</pre>

## Properties

#### DetectorRecipeId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DetectorRules

_Required_: No

_Type_: List of <a href="detectorrulesdefinition.md">DetectorRulesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

