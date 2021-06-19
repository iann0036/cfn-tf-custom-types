# TF::AWS::Macie2ClassificationJob S3JobDefinitionDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#bucketdefinitions" title="BucketDefinitions">BucketDefinitions</a>" : <i>[ <a href="bucketdefinitionsdefinition.md">BucketDefinitionsDefinition</a>, ... ]</i>,
    "<a href="#scoping" title="Scoping">Scoping</a>" : <i>[ <a href="scopingdefinition.md">ScopingDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#bucketdefinitions" title="BucketDefinitions">BucketDefinitions</a>: <i>
      - <a href="bucketdefinitionsdefinition.md">BucketDefinitionsDefinition</a></i>
<a href="#scoping" title="Scoping">Scoping</a>: <i>
      - <a href="scopingdefinition.md">ScopingDefinition</a></i>
</pre>

## Properties

#### BucketDefinitions

_Required_: No

_Type_: List of <a href="bucketdefinitionsdefinition.md">BucketDefinitionsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Scoping

_Required_: No

_Type_: List of <a href="scopingdefinition.md">ScopingDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

