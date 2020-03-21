# Terraform::AWS::DbInstance S3Import

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#bucketname" title="BucketName">BucketName</a>" : <i>String</i>,
    "<a href="#bucketprefix" title="BucketPrefix">BucketPrefix</a>" : <i>String</i>,
    "<a href="#ingestionrole" title="IngestionRole">IngestionRole</a>" : <i>String</i>,
    "<a href="#sourceengine" title="SourceEngine">SourceEngine</a>" : <i>String</i>,
    "<a href="#sourceengineversion" title="SourceEngineVersion">SourceEngineVersion</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#bucketname" title="BucketName">BucketName</a>: <i>String</i>
<a href="#bucketprefix" title="BucketPrefix">BucketPrefix</a>: <i>String</i>
<a href="#ingestionrole" title="IngestionRole">IngestionRole</a>: <i>String</i>
<a href="#sourceengine" title="SourceEngine">SourceEngine</a>: <i>String</i>
<a href="#sourceengineversion" title="SourceEngineVersion">SourceEngineVersion</a>: <i>String</i>
</pre>

## Properties

#### BucketName

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BucketPrefix

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IngestionRole

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceEngine

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceEngineVersion

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

