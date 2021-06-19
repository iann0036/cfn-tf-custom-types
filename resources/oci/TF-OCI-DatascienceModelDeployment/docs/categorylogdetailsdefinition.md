# TF::OCI::DatascienceModelDeployment CategoryLogDetailsDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#access" title="Access">Access</a>" : <i>[ <a href="accessdefinition.md">AccessDefinition</a>, ... ]</i>,
    "<a href="#predict" title="Predict">Predict</a>" : <i>[ <a href="predictdefinition.md">PredictDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#access" title="Access">Access</a>: <i>
      - <a href="accessdefinition.md">AccessDefinition</a></i>
<a href="#predict" title="Predict">Predict</a>: <i>
      - <a href="predictdefinition.md">PredictDefinition</a></i>
</pre>

## Properties

#### Access

_Required_: No

_Type_: List of <a href="accessdefinition.md">AccessDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Predict

_Required_: No

_Type_: List of <a href="predictdefinition.md">PredictDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

