# TF::AzureRM::StorageBlobInventoryPolicy FilterDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#blobtypes" title="BlobTypes">BlobTypes</a>" : <i>[ String, ... ]</i>,
    "<a href="#includeblobversions" title="IncludeBlobVersions">IncludeBlobVersions</a>" : <i>Boolean</i>,
    "<a href="#includesnapshots" title="IncludeSnapshots">IncludeSnapshots</a>" : <i>Boolean</i>,
    "<a href="#prefixmatch" title="PrefixMatch">PrefixMatch</a>" : <i>[ String, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#blobtypes" title="BlobTypes">BlobTypes</a>: <i>
      - String</i>
<a href="#includeblobversions" title="IncludeBlobVersions">IncludeBlobVersions</a>: <i>Boolean</i>
<a href="#includesnapshots" title="IncludeSnapshots">IncludeSnapshots</a>: <i>Boolean</i>
<a href="#prefixmatch" title="PrefixMatch">PrefixMatch</a>: <i>
      - String</i>
</pre>

## Properties

#### BlobTypes

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IncludeBlobVersions

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IncludeSnapshots

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrefixMatch

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

