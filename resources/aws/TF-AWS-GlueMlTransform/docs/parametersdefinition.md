# TF::AWS::GlueMlTransform ParametersDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#transformtype" title="TransformType">TransformType</a>" : <i>String</i>,
    "<a href="#findmatchesparameters" title="FindMatchesParameters">FindMatchesParameters</a>" : <i>[ <a href="findmatchesparametersdefinition.md">FindMatchesParametersDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#transformtype" title="TransformType">TransformType</a>: <i>String</i>
<a href="#findmatchesparameters" title="FindMatchesParameters">FindMatchesParameters</a>: <i>
      - <a href="findmatchesparametersdefinition.md">FindMatchesParametersDefinition</a></i>
</pre>

## Properties

#### TransformType

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FindMatchesParameters

_Required_: No

_Type_: List of <a href="findmatchesparametersdefinition.md">FindMatchesParametersDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

