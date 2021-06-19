# TF::Google::SecretManagerSecret ReplicasDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#location" title="Location">Location</a>" : <i>String</i>,
    "<a href="#customermanagedencryption" title="CustomerManagedEncryption">CustomerManagedEncryption</a>" : <i>[ <a href="customermanagedencryptiondefinition.md">CustomerManagedEncryptionDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#location" title="Location">Location</a>: <i>String</i>
<a href="#customermanagedencryption" title="CustomerManagedEncryption">CustomerManagedEncryption</a>: <i>
      - <a href="customermanagedencryptiondefinition.md">CustomerManagedEncryptionDefinition</a></i>
</pre>

## Properties

#### Location

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CustomerManagedEncryption

_Required_: No

_Type_: List of <a href="customermanagedencryptiondefinition.md">CustomerManagedEncryptionDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

