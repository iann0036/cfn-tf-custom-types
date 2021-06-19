# TF::AWS::ElastictranscoderPipeline ContentConfigDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#bucket" title="Bucket">Bucket</a>" : <i>String</i>,
    "<a href="#storageclass" title="StorageClass">StorageClass</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#bucket" title="Bucket">Bucket</a>: <i>String</i>
<a href="#storageclass" title="StorageClass">StorageClass</a>: <i>String</i>
</pre>

## Properties

#### Bucket

The Amazon S3 bucket in which you want Elastic Transcoder to save transcoded files and playlists.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StorageClass

The Amazon S3 storage class, `Standard` or `ReducedRedundancy`, that you want Elastic Transcoder to assign to the files and playlists that it stores in your Amazon S3 bucket.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

