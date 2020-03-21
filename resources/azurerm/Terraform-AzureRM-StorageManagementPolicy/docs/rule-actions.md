# Terraform::AzureRM::StorageManagementPolicy Rule Actions

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#baseblob" title="BaseBlob">BaseBlob</a>" : <i>[ <a href="rule-actions-baseblob.md">BaseBlob</a>, ... ]</i>,
    "<a href="#snapshot" title="Snapshot">Snapshot</a>" : <i>[ <a href="rule-actions-snapshot.md">Snapshot</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#baseblob" title="BaseBlob">BaseBlob</a>: <i>
      - <a href="rule-actions-baseblob.md">BaseBlob</a></i>
<a href="#snapshot" title="Snapshot">Snapshot</a>: <i>
      - <a href="rule-actions-snapshot.md">Snapshot</a></i>
</pre>

## Properties

#### BaseBlob

_Required_: No
_Type_: List of <a href="rule-actions-baseblob.md">BaseBlob</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Snapshot

_Required_: No
_Type_: List of <a href="rule-actions-snapshot.md">Snapshot</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

