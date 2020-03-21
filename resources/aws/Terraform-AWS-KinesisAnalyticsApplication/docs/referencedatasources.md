# Terraform::AWS::KinesisAnalyticsApplication ReferenceDataSources

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#tablename" title="TableName">TableName</a>" : <i>String</i>,
    "<a href="#s3" title="S3">S3</a>" : <i>[ <a href="referencedatasources-s3.md">S3</a>, ... ]</i>,
    "<a href="#schema" title="Schema">Schema</a>" : <i>[ <a href="referencedatasources-schema.md">Schema</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#tablename" title="TableName">TableName</a>: <i>String</i>
<a href="#s3" title="S3">S3</a>: <i>
      - <a href="referencedatasources-s3.md">S3</a></i>
<a href="#schema" title="Schema">Schema</a>: <i>
      - <a href="referencedatasources-schema.md">Schema</a></i>
</pre>

## Properties

#### TableName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### S3

_Required_: No

_Type_: List of <a href="referencedatasources-s3.md">S3</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Schema

_Required_: No

_Type_: List of <a href="referencedatasources-schema.md">Schema</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

