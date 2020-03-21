# Terraform::AWS::S3BucketAnalyticsConfiguration

CloudFormation equivalent of aws_s3_bucket_analytics_configuration

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AWS::S3BucketAnalyticsConfiguration",
    "Properties" : {
        "<a href="#bucket" title="Bucket">Bucket</a>" : <i>String</i>,
        "<a href="#id" title="Id">Id</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#filter" title="Filter">Filter</a>" : <i>[ &lt;a href=&#34;filter.md&#34;&gt;Filter&lt;/a&gt;, ... ]</i>,
        "<a href="#storageclassanalysis" title="StorageClassAnalysis">StorageClassAnalysis</a>" : <i>[ &lt;a href=&#34;storageclassanalysis.md&#34;&gt;StorageClassAnalysis&lt;/a&gt;, ... ]</i>,
        "<a href="#dataexport" title="DataExport">DataExport</a>" : <i>[ &lt;a href=&#34;dataexport.md&#34;&gt;DataExport&lt;/a&gt;, ... ]</i>,
        "<a href="#destination" title="Destination">Destination</a>" : <i>[ &lt;a href=&#34;destination.md&#34;&gt;Destination&lt;/a&gt;, ... ]</i>,
        "<a href="#s3bucketdestination" title="S3BucketDestination">S3BucketDestination</a>" : <i>[ &lt;a href=&#34;s3bucketdestination.md&#34;&gt;S3BucketDestination&lt;/a&gt;, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AWS::S3BucketAnalyticsConfiguration
Properties:
    <a href="#bucket" title="Bucket">Bucket</a>: <i>String</i>
    <a href="#id" title="Id">Id</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#filter" title="Filter">Filter</a>: <i>
      - &lt;a href=&#34;filter.md&#34;&gt;Filter&lt;/a&gt;</i>
    <a href="#storageclassanalysis" title="StorageClassAnalysis">StorageClassAnalysis</a>: <i>
      - &lt;a href=&#34;storageclassanalysis.md&#34;&gt;StorageClassAnalysis&lt;/a&gt;</i>
    <a href="#dataexport" title="DataExport">DataExport</a>: <i>
      - &lt;a href=&#34;dataexport.md&#34;&gt;DataExport&lt;/a&gt;</i>
    <a href="#destination" title="Destination">Destination</a>: <i>
      - &lt;a href=&#34;destination.md&#34;&gt;Destination&lt;/a&gt;</i>
    <a href="#s3bucketdestination" title="S3BucketDestination">S3BucketDestination</a>: <i>
      - &lt;a href=&#34;s3bucketdestination.md&#34;&gt;S3BucketDestination&lt;/a&gt;</i>
</pre>

## Properties

#### Bucket

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Id

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Filter

_Required_: No

_Type_: List of &lt;a href=&#34;filter.md&#34;&gt;Filter&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StorageClassAnalysis

_Required_: No

_Type_: List of &lt;a href=&#34;storageclassanalysis.md&#34;&gt;StorageClassAnalysis&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DataExport

_Required_: No

_Type_: List of &lt;a href=&#34;dataexport.md&#34;&gt;DataExport&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Destination

_Required_: No

_Type_: List of &lt;a href=&#34;destination.md&#34;&gt;Destination&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### S3BucketDestination

_Required_: No

_Type_: List of &lt;a href=&#34;s3bucketdestination.md&#34;&gt;S3BucketDestination&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

