# TF::AWS::S3Bucket RuleDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#bucketkeyenabled" title="BucketKeyEnabled">BucketKeyEnabled</a>" : <i>Boolean</i>,
    "<a href="#applyserversideencryptionbydefault" title="ApplyServerSideEncryptionByDefault">ApplyServerSideEncryptionByDefault</a>" : <i>[ <a href="applyserversideencryptionbydefaultdefinition.md">ApplyServerSideEncryptionByDefaultDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#bucketkeyenabled" title="BucketKeyEnabled">BucketKeyEnabled</a>: <i>Boolean</i>
<a href="#applyserversideencryptionbydefault" title="ApplyServerSideEncryptionByDefault">ApplyServerSideEncryptionByDefault</a>: <i>
      - <a href="applyserversideencryptionbydefaultdefinition.md">ApplyServerSideEncryptionByDefaultDefinition</a></i>
</pre>

## Properties

#### BucketKeyEnabled

Whether or not to use [Amazon S3 Bucket Keys](https://docs.aws.amazon.com/AmazonS3/latest/dev/bucket-key.html) for SSE-KMS.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ApplyServerSideEncryptionByDefault

_Required_: No

_Type_: List of <a href="applyserversideencryptionbydefaultdefinition.md">ApplyServerSideEncryptionByDefaultDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

