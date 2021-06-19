# TF::Volterra::FastAcl LegacyAclDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#destinationtype" title="DestinationType">DestinationType</a>" : <i>[ <a href="destinationtypedefinition.md">DestinationTypeDefinition</a>, ... ]</i>,
    "<a href="#networktype" title="NetworkType">NetworkType</a>" : <i>[ <a href="networktypedefinition.md">NetworkTypeDefinition</a>, ... ]</i>,
    "<a href="#sourcerules" title="SourceRules">SourceRules</a>" : <i>[ <a href="sourcerulesdefinition.md">SourceRulesDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#destinationtype" title="DestinationType">DestinationType</a>: <i>
      - <a href="destinationtypedefinition.md">DestinationTypeDefinition</a></i>
<a href="#networktype" title="NetworkType">NetworkType</a>: <i>
      - <a href="networktypedefinition.md">NetworkTypeDefinition</a></i>
<a href="#sourcerules" title="SourceRules">SourceRules</a>: <i>
      - <a href="sourcerulesdefinition.md">SourceRulesDefinition</a></i>
</pre>

## Properties

#### DestinationType

_Required_: No

_Type_: List of <a href="destinationtypedefinition.md">DestinationTypeDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetworkType

_Required_: No

_Type_: List of <a href="networktypedefinition.md">NetworkTypeDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceRules

_Required_: No

_Type_: List of <a href="sourcerulesdefinition.md">SourceRulesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

