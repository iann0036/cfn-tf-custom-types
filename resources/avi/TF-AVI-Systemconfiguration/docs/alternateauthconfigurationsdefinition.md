# TF::AVI::Systemconfiguration AlternateAuthConfigurationsDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#authprofileref" title="AuthProfileRef">AuthProfileRef</a>" : <i>String</i>,
    "<a href="#index" title="Index">Index</a>" : <i>Double</i>,
    "<a href="#mappingrules" title="MappingRules">MappingRules</a>" : <i>[ <a href="mappingrulesdefinition.md">MappingRulesDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#authprofileref" title="AuthProfileRef">AuthProfileRef</a>: <i>String</i>
<a href="#index" title="Index">Index</a>: <i>Double</i>
<a href="#mappingrules" title="MappingRules">MappingRules</a>: <i>
      - <a href="mappingrulesdefinition.md">MappingRulesDefinition</a></i>
</pre>

## Properties

#### AuthProfileRef

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Index

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MappingRules

_Required_: No

_Type_: List of <a href="mappingrulesdefinition.md">MappingRulesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

