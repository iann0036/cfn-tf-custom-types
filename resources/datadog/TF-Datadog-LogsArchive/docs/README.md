# TF::Datadog::LogsArchive

CloudFormation equivalent of datadog_logs_archive

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Datadog::LogsArchive",
    "Properties" : {
        "<a href="#includetags" title="IncludeTags">IncludeTags</a>" : <i>Boolean</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#query" title="Query">Query</a>" : <i>String</i>,
        "<a href="#rehydrationtags" title="RehydrationTags">RehydrationTags</a>" : <i>[ String, ... ]</i>,
        "<a href="#azurearchive" title="AzureArchive">AzureArchive</a>" : <i>[ <a href="azurearchivedefinition.md">AzureArchiveDefinition</a>, ... ]</i>,
        "<a href="#gcsarchive" title="GcsArchive">GcsArchive</a>" : <i>[ <a href="gcsarchivedefinition.md">GcsArchiveDefinition</a>, ... ]</i>,
        "<a href="#s3archive" title="S3Archive">S3Archive</a>" : <i>[ <a href="s3archivedefinition.md">S3ArchiveDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Datadog::LogsArchive
Properties:
    <a href="#includetags" title="IncludeTags">IncludeTags</a>: <i>Boolean</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#query" title="Query">Query</a>: <i>String</i>
    <a href="#rehydrationtags" title="RehydrationTags">RehydrationTags</a>: <i>
      - String</i>
    <a href="#azurearchive" title="AzureArchive">AzureArchive</a>: <i>
      - <a href="azurearchivedefinition.md">AzureArchiveDefinition</a></i>
    <a href="#gcsarchive" title="GcsArchive">GcsArchive</a>: <i>
      - <a href="gcsarchivedefinition.md">GcsArchiveDefinition</a></i>
    <a href="#s3archive" title="S3Archive">S3Archive</a>: <i>
      - <a href="s3archivedefinition.md">S3ArchiveDefinition</a></i>
</pre>

## Properties

#### IncludeTags

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Query

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RehydrationTags

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AzureArchive

_Required_: No

_Type_: List of <a href="azurearchivedefinition.md">AzureArchiveDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GcsArchive

_Required_: No

_Type_: List of <a href="gcsarchivedefinition.md">GcsArchiveDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### S3Archive

_Required_: No

_Type_: List of <a href="s3archivedefinition.md">S3ArchiveDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Id

Returns the <code>Id</code> value.

