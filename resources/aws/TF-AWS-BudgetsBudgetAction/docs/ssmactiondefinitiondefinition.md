# TF::AWS::BudgetsBudgetAction SsmActionDefinitionDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#actionsubtype" title="ActionSubType">ActionSubType</a>" : <i>String</i>,
    "<a href="#instanceids" title="InstanceIds">InstanceIds</a>" : <i>[ String, ... ]</i>,
    "<a href="#region" title="Region">Region</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#actionsubtype" title="ActionSubType">ActionSubType</a>: <i>String</i>
<a href="#instanceids" title="InstanceIds">InstanceIds</a>: <i>
      - String</i>
<a href="#region" title="Region">Region</a>: <i>String</i>
</pre>

## Properties

#### ActionSubType

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InstanceIds

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Region

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

