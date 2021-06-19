# TF::PrismaCloud::Policy RuleDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#apiname" title="ApiName">ApiName</a>" : <i>String</i>,
    "<a href="#cloudaccount" title="CloudAccount">CloudAccount</a>" : <i>String</i>,
    "<a href="#cloudtype" title="CloudType">CloudType</a>" : <i>String</i>,
    "<a href="#criteria" title="Criteria">Criteria</a>" : <i>String</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#parameters" title="Parameters">Parameters</a>" : <i>[ <a href="parametersdefinition.md">ParametersDefinition</a>, ... ]</i>,
    "<a href="#resourceidpath" title="ResourceIdPath">ResourceIdPath</a>" : <i>String</i>,
    "<a href="#resourcetype" title="ResourceType">ResourceType</a>" : <i>String</i>,
    "<a href="#ruletype" title="RuleType">RuleType</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#apiname" title="ApiName">ApiName</a>: <i>String</i>
<a href="#cloudaccount" title="CloudAccount">CloudAccount</a>: <i>String</i>
<a href="#cloudtype" title="CloudType">CloudType</a>: <i>String</i>
<a href="#criteria" title="Criteria">Criteria</a>: <i>String</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#parameters" title="Parameters">Parameters</a>: <i>
      - <a href="parametersdefinition.md">ParametersDefinition</a></i>
<a href="#resourceidpath" title="ResourceIdPath">ResourceIdPath</a>: <i>String</i>
<a href="#resourcetype" title="ResourceType">ResourceType</a>: <i>String</i>
<a href="#ruletype" title="RuleType">RuleType</a>: <i>String</i>
</pre>

## Properties

#### ApiName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CloudAccount

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CloudType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Criteria

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Parameters

_Required_: Yes

_Type_: List of <a href="parametersdefinition.md">ParametersDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourceIdPath

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourceType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RuleType

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

