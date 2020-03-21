# Terraform::AzureRM::StorageManagementPolicy Rule Filters

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#blobtypes" title="BlobTypes">BlobTypes</a>" : <i>[ String, ... ]</i>,
    "<a href="#prefixmatch" title="PrefixMatch">PrefixMatch</a>" : <i>[ String, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#blobtypes" title="BlobTypes">BlobTypes</a>: <i>
      - String</i>
<a href="#prefixmatch" title="PrefixMatch">PrefixMatch</a>: <i>
      - String</i>
</pre>

## Properties

#### BlobTypes

An array of predefined values. Only `blockBlob` is supported.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrefixMatch

An array of strings for prefixes to be matched.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

