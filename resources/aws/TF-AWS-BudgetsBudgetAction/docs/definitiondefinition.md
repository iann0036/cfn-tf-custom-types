# TF::AWS::BudgetsBudgetAction DefinitionDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#iamactiondefinition" title="IamActionDefinition">IamActionDefinition</a>" : <i>[ <a href="iamactiondefinitiondefinition.md">IamActionDefinitionDefinition</a>, ... ]</i>,
    "<a href="#scpactiondefinition" title="ScpActionDefinition">ScpActionDefinition</a>" : <i>[ <a href="scpactiondefinitiondefinition.md">ScpActionDefinitionDefinition</a>, ... ]</i>,
    "<a href="#ssmactiondefinition" title="SsmActionDefinition">SsmActionDefinition</a>" : <i>[ <a href="ssmactiondefinitiondefinition.md">SsmActionDefinitionDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#iamactiondefinition" title="IamActionDefinition">IamActionDefinition</a>: <i>
      - <a href="iamactiondefinitiondefinition.md">IamActionDefinitionDefinition</a></i>
<a href="#scpactiondefinition" title="ScpActionDefinition">ScpActionDefinition</a>: <i>
      - <a href="scpactiondefinitiondefinition.md">ScpActionDefinitionDefinition</a></i>
<a href="#ssmactiondefinition" title="SsmActionDefinition">SsmActionDefinition</a>: <i>
      - <a href="ssmactiondefinitiondefinition.md">SsmActionDefinitionDefinition</a></i>
</pre>

## Properties

#### IamActionDefinition

_Required_: No

_Type_: List of <a href="iamactiondefinitiondefinition.md">IamActionDefinitionDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ScpActionDefinition

_Required_: No

_Type_: List of <a href="scpactiondefinitiondefinition.md">ScpActionDefinitionDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SsmActionDefinition

_Required_: No

_Type_: List of <a href="ssmactiondefinitiondefinition.md">SsmActionDefinitionDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

