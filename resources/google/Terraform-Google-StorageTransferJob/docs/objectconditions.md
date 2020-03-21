# Terraform::Google::StorageTransferJob ObjectConditions

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#excludeprefixes" title="ExcludePrefixes">ExcludePrefixes</a>" : <i>[ String, ... ]</i>,
    "<a href="#includeprefixes" title="IncludePrefixes">IncludePrefixes</a>" : <i>[ String, ... ]</i>,
    "<a href="#maxtimeelapsedsincelastmodification" title="MaxTimeElapsedSinceLastModification">MaxTimeElapsedSinceLastModification</a>" : <i>String</i>,
    "<a href="#mintimeelapsedsincelastmodification" title="MinTimeElapsedSinceLastModification">MinTimeElapsedSinceLastModification</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#excludeprefixes" title="ExcludePrefixes">ExcludePrefixes</a>: <i>
      - String</i>
<a href="#includeprefixes" title="IncludePrefixes">IncludePrefixes</a>: <i>
      - String</i>
<a href="#maxtimeelapsedsincelastmodification" title="MaxTimeElapsedSinceLastModification">MaxTimeElapsedSinceLastModification</a>: <i>String</i>
<a href="#mintimeelapsedsincelastmodification" title="MinTimeElapsedSinceLastModification">MinTimeElapsedSinceLastModification</a>: <i>String</i>
</pre>

## Properties

#### ExcludePrefixes

`exclude_prefixes` must follow the requirements described for `include_prefixes`. See [Requirements](https://cloud.google.com/storage-transfer/docs/reference/rest/v1/TransferSpec#ObjectConditions).

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IncludePrefixes

If `include_refixes` is specified, objects that satisfy the object conditions must have names that start with one of the `include_prefixes` and that do not start with any of the `exclude_prefixes`. If `include_prefixes` is not specified, all objects except those that have names starting with one of the `exclude_prefixes` must satisfy the object conditions. See [Requirements](https://cloud.google.com/storage-transfer/docs/reference/rest/v1/TransferSpec#ObjectConditions).

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxTimeElapsedSinceLastModification

A duration in seconds with up to nine fractional digits, terminated by 's'. Example: "3.5s".

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MinTimeElapsedSinceLastModification

A duration in seconds with up to nine fractional digits, terminated by 's'. Example: "3.5s".

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

