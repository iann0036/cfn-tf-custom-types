# TF::AzureRM::PolicySetDefinition PolicyDefinitionReferenceDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#parametervalues" title="ParameterValues">ParameterValues</a>" : <i>String</i>,
    "<a href="#parameters" title="Parameters">Parameters</a>" : <i>[ <a href="parametersdefinition.md">ParametersDefinition</a>, ... ]</i>,
    "<a href="#policydefinitionid" title="PolicyDefinitionId">PolicyDefinitionId</a>" : <i>String</i>,
    "<a href="#policygroupnames" title="PolicyGroupNames">PolicyGroupNames</a>" : <i>[ String, ... ]</i>,
    "<a href="#referenceid" title="ReferenceId">ReferenceId</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#parametervalues" title="ParameterValues">ParameterValues</a>: <i>String</i>
<a href="#parameters" title="Parameters">Parameters</a>: <i>
      - <a href="parametersdefinition.md">ParametersDefinition</a></i>
<a href="#policydefinitionid" title="PolicyDefinitionId">PolicyDefinitionId</a>: <i>String</i>
<a href="#policygroupnames" title="PolicyGroupNames">PolicyGroupNames</a>: <i>
      - String</i>
<a href="#referenceid" title="ReferenceId">ReferenceId</a>: <i>String</i>
</pre>

## Properties

#### ParameterValues

Parameter values for the referenced policy rule. This field is a JSON string that allows you to assign parameters to this policy rule.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Parameters

_Required_: No

_Type_: List of <a href="parametersdefinition.md">ParametersDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PolicyDefinitionId

The ID of the policy definition or policy set definition that will be included in this policy set definition.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PolicyGroupNames

A list of names of the policy definition groups that this policy definition reference belongs to.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReferenceId

A unique ID within this policy set definition for this policy definition reference.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

