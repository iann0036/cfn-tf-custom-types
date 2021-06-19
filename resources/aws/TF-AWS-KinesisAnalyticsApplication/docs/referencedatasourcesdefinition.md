# TF::AWS::KinesisAnalyticsApplication ReferenceDataSourcesDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#tablename" title="TableName">TableName</a>" : <i>String</i>,
    "<a href="#s3" title="S3">S3</a>" : <i>[ <a href="s3definition.md">S3Definition</a>, ... ]</i>,
    "<a href="#schema" title="Schema">Schema</a>" : <i>[ <a href="schemadefinition.md">SchemaDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#tablename" title="TableName">TableName</a>: <i>String</i>
<a href="#s3" title="S3">S3</a>: <i>
      - <a href="s3definition.md">S3Definition</a></i>
<a href="#schema" title="Schema">Schema</a>: <i>
      - <a href="schemadefinition.md">SchemaDefinition</a></i>
</pre>

## Properties

#### TableName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### S3

_Required_: No

_Type_: List of <a href="s3definition.md">S3Definition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Schema

_Required_: No

_Type_: List of <a href="schemadefinition.md">SchemaDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

