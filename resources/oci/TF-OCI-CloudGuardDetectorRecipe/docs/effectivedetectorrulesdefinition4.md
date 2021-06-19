# TF::OCI::CloudGuardDetectorRecipe EffectiveDetectorRulesDefinition4

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#condition" title="Condition">Condition</a>" : <i>String</i>,
    "<a href="#configurations" title="Configurations">Configurations</a>" : <i>[ <a href="effectivedetectorrulesdefinition3.md">EffectiveDetectorRulesDefinition3</a>, ... ]</i>,
    "<a href="#isconfigurationallowed" title="IsConfigurationAllowed">IsConfigurationAllowed</a>" : <i>Boolean</i>,
    "<a href="#isenabled" title="IsEnabled">IsEnabled</a>" : <i>Boolean</i>,
    "<a href="#labels" title="Labels">Labels</a>" : <i>[ String, ... ]</i>,
    "<a href="#risklevel" title="RiskLevel">RiskLevel</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#condition" title="Condition">Condition</a>: <i>String</i>
<a href="#configurations" title="Configurations">Configurations</a>: <i>
      - <a href="effectivedetectorrulesdefinition3.md">EffectiveDetectorRulesDefinition3</a></i>
<a href="#isconfigurationallowed" title="IsConfigurationAllowed">IsConfigurationAllowed</a>: <i>Boolean</i>
<a href="#isenabled" title="IsEnabled">IsEnabled</a>: <i>Boolean</i>
<a href="#labels" title="Labels">Labels</a>: <i>
      - String</i>
<a href="#risklevel" title="RiskLevel">RiskLevel</a>: <i>String</i>
</pre>

## Properties

#### Condition

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Configurations

_Required_: No

_Type_: List of <a href="effectivedetectorrulesdefinition3.md">EffectiveDetectorRulesDefinition3</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsConfigurationAllowed

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsEnabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Labels

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RiskLevel

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

