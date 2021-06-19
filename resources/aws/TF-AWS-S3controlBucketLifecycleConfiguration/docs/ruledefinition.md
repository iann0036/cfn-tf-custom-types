# TF::AWS::S3controlBucketLifecycleConfiguration RuleDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#id" title="Id">Id</a>" : <i>String</i>,
    "<a href="#status" title="Status">Status</a>" : <i>String</i>,
    "<a href="#abortincompletemultipartupload" title="AbortIncompleteMultipartUpload">AbortIncompleteMultipartUpload</a>" : <i>[ <a href="abortincompletemultipartuploaddefinition.md">AbortIncompleteMultipartUploadDefinition</a>, ... ]</i>,
    "<a href="#expiration" title="Expiration">Expiration</a>" : <i>[ <a href="expirationdefinition.md">ExpirationDefinition</a>, ... ]</i>,
    "<a href="#filter" title="Filter">Filter</a>" : <i>[ <a href="filterdefinition.md">FilterDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#id" title="Id">Id</a>: <i>String</i>
<a href="#status" title="Status">Status</a>: <i>String</i>
<a href="#abortincompletemultipartupload" title="AbortIncompleteMultipartUpload">AbortIncompleteMultipartUpload</a>: <i>
      - <a href="abortincompletemultipartuploaddefinition.md">AbortIncompleteMultipartUploadDefinition</a></i>
<a href="#expiration" title="Expiration">Expiration</a>: <i>
      - <a href="expirationdefinition.md">ExpirationDefinition</a></i>
<a href="#filter" title="Filter">Filter</a>: <i>
      - <a href="filterdefinition.md">FilterDefinition</a></i>
</pre>

## Properties

#### Id

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Status

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AbortIncompleteMultipartUpload

_Required_: No

_Type_: List of <a href="abortincompletemultipartuploaddefinition.md">AbortIncompleteMultipartUploadDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Expiration

_Required_: No

_Type_: List of <a href="expirationdefinition.md">ExpirationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Filter

_Required_: No

_Type_: List of <a href="filterdefinition.md">FilterDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

