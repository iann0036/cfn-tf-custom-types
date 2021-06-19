# TF::AWS::Kinesisanalyticsv2Application SqlApplicationConfigurationDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#input" title="Input">Input</a>" : <i>[ <a href="inputdefinition.md">InputDefinition</a>, ... ]</i>,
    "<a href="#output" title="Output">Output</a>" : <i>[ <a href="outputdefinition.md">OutputDefinition</a>, ... ]</i>,
    "<a href="#referencedatasource" title="ReferenceDataSource">ReferenceDataSource</a>" : <i>[ <a href="referencedatasourcedefinition.md">ReferenceDataSourceDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#input" title="Input">Input</a>: <i>
      - <a href="inputdefinition.md">InputDefinition</a></i>
<a href="#output" title="Output">Output</a>: <i>
      - <a href="outputdefinition.md">OutputDefinition</a></i>
<a href="#referencedatasource" title="ReferenceDataSource">ReferenceDataSource</a>: <i>
      - <a href="referencedatasourcedefinition.md">ReferenceDataSourceDefinition</a></i>
</pre>

## Properties

#### Input

_Required_: No

_Type_: List of <a href="inputdefinition.md">InputDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Output

_Required_: No

_Type_: List of <a href="outputdefinition.md">OutputDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReferenceDataSource

_Required_: No

_Type_: List of <a href="referencedatasourcedefinition.md">ReferenceDataSourceDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

