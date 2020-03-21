# Terraform::Google::StorageTransferJob TransferSpec ObjectConditions

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

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IncludePrefixes

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxTimeElapsedSinceLastModification

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MinTimeElapsedSinceLastModification

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

