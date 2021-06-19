# TF::AzureRM::AppService AzureBlobStorageDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#retentionindays" title="RetentionInDays">RetentionInDays</a>" : <i>Double</i>,
    "<a href="#sasurl" title="SasUrl">SasUrl</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#retentionindays" title="RetentionInDays">RetentionInDays</a>: <i>Double</i>
<a href="#sasurl" title="SasUrl">SasUrl</a>: <i>String</i>
</pre>

## Properties

#### RetentionInDays

The number of days to retain logs for.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SasUrl

The URL to the storage container with a shared access signature token appended.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

