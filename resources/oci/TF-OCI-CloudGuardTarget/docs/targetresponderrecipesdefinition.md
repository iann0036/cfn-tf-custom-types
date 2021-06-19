# TF::OCI::CloudGuardTarget TargetResponderRecipesDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#responderrecipeid" title="ResponderRecipeId">ResponderRecipeId</a>" : <i>String</i>,
    "<a href="#responderrules" title="ResponderRules">ResponderRules</a>" : <i>[ <a href="responderrulesdefinition.md">ResponderRulesDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#responderrecipeid" title="ResponderRecipeId">ResponderRecipeId</a>: <i>String</i>
<a href="#responderrules" title="ResponderRules">ResponderRules</a>: <i>
      - <a href="responderrulesdefinition.md">ResponderRulesDefinition</a></i>
</pre>

## Properties

#### ResponderRecipeId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResponderRules

_Required_: No

_Type_: List of <a href="responderrulesdefinition.md">ResponderRulesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

