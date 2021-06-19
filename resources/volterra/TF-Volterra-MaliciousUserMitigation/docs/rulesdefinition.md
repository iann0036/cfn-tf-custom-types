# TF::Volterra::MaliciousUserMitigation RulesDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#mitigationaction" title="MitigationAction">MitigationAction</a>" : <i>[ <a href="mitigationactiondefinition.md">MitigationActionDefinition</a>, ... ]</i>,
    "<a href="#threatlevel" title="ThreatLevel">ThreatLevel</a>" : <i>[ <a href="threatleveldefinition.md">ThreatLevelDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#mitigationaction" title="MitigationAction">MitigationAction</a>: <i>
      - <a href="mitigationactiondefinition.md">MitigationActionDefinition</a></i>
<a href="#threatlevel" title="ThreatLevel">ThreatLevel</a>: <i>
      - <a href="threatleveldefinition.md">ThreatLevelDefinition</a></i>
</pre>

## Properties

#### MitigationAction

_Required_: No

_Type_: List of <a href="mitigationactiondefinition.md">MitigationActionDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ThreatLevel

_Required_: No

_Type_: List of <a href="threatleveldefinition.md">ThreatLevelDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

