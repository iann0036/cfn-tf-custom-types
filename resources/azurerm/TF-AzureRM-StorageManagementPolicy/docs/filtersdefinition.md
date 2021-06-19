# TF::AzureRM::StorageManagementPolicy FiltersDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#blobtypes" title="BlobTypes">BlobTypes</a>" : <i>[ String, ... ]</i>,
    "<a href="#prefixmatch" title="PrefixMatch">PrefixMatch</a>" : <i>[ String, ... ]</i>,
    "<a href="#matchblobindextag" title="MatchBlobIndexTag">MatchBlobIndexTag</a>" : <i>[ <a href="matchblobindextagdefinition.md">MatchBlobIndexTagDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#blobtypes" title="BlobTypes">BlobTypes</a>: <i>
      - String</i>
<a href="#prefixmatch" title="PrefixMatch">PrefixMatch</a>: <i>
      - String</i>
<a href="#matchblobindextag" title="MatchBlobIndexTag">MatchBlobIndexTag</a>: <i>
      - <a href="matchblobindextagdefinition.md">MatchBlobIndexTagDefinition</a></i>
</pre>

## Properties

#### BlobTypes

An array of predefined values. Valid options are `blockBlob` and `appendBlob`.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrefixMatch

An array of strings for prefixes to be matched.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MatchBlobIndexTag

_Required_: No

_Type_: List of <a href="matchblobindextagdefinition.md">MatchBlobIndexTagDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

