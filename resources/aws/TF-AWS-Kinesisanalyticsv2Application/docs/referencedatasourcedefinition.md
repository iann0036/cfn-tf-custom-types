# TF::AWS::Kinesisanalyticsv2Application ReferenceDataSourceDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#tablename" title="TableName">TableName</a>" : <i>String</i>,
    "<a href="#referenceschema" title="ReferenceSchema">ReferenceSchema</a>" : <i>[ <a href="referenceschemadefinition.md">ReferenceSchemaDefinition</a>, ... ]</i>,
    "<a href="#s3referencedatasource" title="S3ReferenceDataSource">S3ReferenceDataSource</a>" : <i>[ <a href="s3referencedatasourcedefinition.md">S3ReferenceDataSourceDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#tablename" title="TableName">TableName</a>: <i>String</i>
<a href="#referenceschema" title="ReferenceSchema">ReferenceSchema</a>: <i>
      - <a href="referenceschemadefinition.md">ReferenceSchemaDefinition</a></i>
<a href="#s3referencedatasource" title="S3ReferenceDataSource">S3ReferenceDataSource</a>: <i>
      - <a href="s3referencedatasourcedefinition.md">S3ReferenceDataSourceDefinition</a></i>
</pre>

## Properties

#### TableName

The name of the in-application table to create.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReferenceSchema

_Required_: No

_Type_: List of <a href="referenceschemadefinition.md">ReferenceSchemaDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### S3ReferenceDataSource

_Required_: No

_Type_: List of <a href="s3referencedatasourcedefinition.md">S3ReferenceDataSourceDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

