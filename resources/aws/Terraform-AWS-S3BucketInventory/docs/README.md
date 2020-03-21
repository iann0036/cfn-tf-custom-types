# Terraform::AWS::S3BucketInventory

CloudFormation equivalent of aws_s3_bucket_inventory

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AWS::S3BucketInventory",
    "Properties" : {
        "<a href="#bucket" title="Bucket">Bucket</a>" : <i>[ &lt;a href=&#34;bucket.md&#34;&gt;Bucket&lt;/a&gt;, ... ]</i>,
        "<a href="#enabled" title="Enabled">Enabled</a>" : <i>Boolean</i>,
        "<a href="#id" title="Id">Id</a>" : <i>String</i>,
        "<a href="#includedobjectversions" title="IncludedObjectVersions">IncludedObjectVersions</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#optionalfields" title="OptionalFields">OptionalFields</a>" : <i>[ String, ... ]</i>,
        "<a href="#destination" title="Destination">Destination</a>" : <i>[ &lt;a href=&#34;destination.md&#34;&gt;Destination&lt;/a&gt;, ... ]</i>,
        "<a href="#filter" title="Filter">Filter</a>" : <i>[ &lt;a href=&#34;filter.md&#34;&gt;Filter&lt;/a&gt;, ... ]</i>,
        "<a href="#schedule" title="Schedule">Schedule</a>" : <i>[ &lt;a href=&#34;schedule.md&#34;&gt;Schedule&lt;/a&gt;, ... ]</i>,
        "<a href="#encryption" title="Encryption">Encryption</a>" : <i>[ &lt;a href=&#34;encryption.md&#34;&gt;Encryption&lt;/a&gt;, ... ]</i>,
        "<a href="#ssekms" title="SseKms">SseKms</a>" : <i>[ &lt;a href=&#34;ssekms.md&#34;&gt;SseKms&lt;/a&gt;, ... ]</i>,
        "<a href="#sses3" title="SseS3">SseS3</a>" : <i>[ &lt;a href=&#34;sses3.md&#34;&gt;SseS3&lt;/a&gt;, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AWS::S3BucketInventory
Properties:
    <a href="#bucket" title="Bucket">Bucket</a>: <i>
      - &lt;a href=&#34;bucket.md&#34;&gt;Bucket&lt;/a&gt;</i>
    <a href="#enabled" title="Enabled">Enabled</a>: <i>Boolean</i>
    <a href="#id" title="Id">Id</a>: <i>String</i>
    <a href="#includedobjectversions" title="IncludedObjectVersions">IncludedObjectVersions</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#optionalfields" title="OptionalFields">OptionalFields</a>: <i>
      - String</i>
    <a href="#destination" title="Destination">Destination</a>: <i>
      - &lt;a href=&#34;destination.md&#34;&gt;Destination&lt;/a&gt;</i>
    <a href="#filter" title="Filter">Filter</a>: <i>
      - &lt;a href=&#34;filter.md&#34;&gt;Filter&lt;/a&gt;</i>
    <a href="#schedule" title="Schedule">Schedule</a>: <i>
      - &lt;a href=&#34;schedule.md&#34;&gt;Schedule&lt;/a&gt;</i>
    <a href="#encryption" title="Encryption">Encryption</a>: <i>
      - &lt;a href=&#34;encryption.md&#34;&gt;Encryption&lt;/a&gt;</i>
    <a href="#ssekms" title="SseKms">SseKms</a>: <i>
      - &lt;a href=&#34;ssekms.md&#34;&gt;SseKms&lt;/a&gt;</i>
    <a href="#sses3" title="SseS3">SseS3</a>: <i>
      - &lt;a href=&#34;sses3.md&#34;&gt;SseS3&lt;/a&gt;</i>
</pre>

## Properties

#### Bucket

_Required_: Yes

_Type_: List of &lt;a href=&#34;bucket.md&#34;&gt;Bucket&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Enabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Id

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IncludedObjectVersions

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OptionalFields

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Destination

_Required_: No

_Type_: List of &lt;a href=&#34;destination.md&#34;&gt;Destination&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Filter

_Required_: No

_Type_: List of &lt;a href=&#34;filter.md&#34;&gt;Filter&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Schedule

_Required_: No

_Type_: List of &lt;a href=&#34;schedule.md&#34;&gt;Schedule&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Encryption

_Required_: No

_Type_: List of &lt;a href=&#34;encryption.md&#34;&gt;Encryption&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SseKms

_Required_: No

_Type_: List of &lt;a href=&#34;ssekms.md&#34;&gt;SseKms&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SseS3

_Required_: No

_Type_: List of &lt;a href=&#34;sses3.md&#34;&gt;SseS3&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

