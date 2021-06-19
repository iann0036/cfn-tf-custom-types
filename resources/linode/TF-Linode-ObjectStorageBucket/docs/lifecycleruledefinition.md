# TF::Linode::ObjectStorageBucket LifecycleRuleDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#abortincompletemultipartuploaddays" title="AbortIncompleteMultipartUploadDays">AbortIncompleteMultipartUploadDays</a>" : <i>Double</i>,
    "<a href="#enabled" title="Enabled">Enabled</a>" : <i>Boolean</i>,
    "<a href="#id" title="Id">Id</a>" : <i>String</i>,
    "<a href="#prefix" title="Prefix">Prefix</a>" : <i>String</i>,
    "<a href="#expiration" title="Expiration">Expiration</a>" : <i>[ <a href="expirationdefinition.md">ExpirationDefinition</a>, ... ]</i>,
    "<a href="#noncurrentversionexpiration" title="NoncurrentVersionExpiration">NoncurrentVersionExpiration</a>" : <i>[ <a href="noncurrentversionexpirationdefinition.md">NoncurrentVersionExpirationDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#abortincompletemultipartuploaddays" title="AbortIncompleteMultipartUploadDays">AbortIncompleteMultipartUploadDays</a>: <i>Double</i>
<a href="#enabled" title="Enabled">Enabled</a>: <i>Boolean</i>
<a href="#id" title="Id">Id</a>: <i>String</i>
<a href="#prefix" title="Prefix">Prefix</a>: <i>String</i>
<a href="#expiration" title="Expiration">Expiration</a>: <i>
      - <a href="expirationdefinition.md">ExpirationDefinition</a></i>
<a href="#noncurrentversionexpiration" title="NoncurrentVersionExpiration">NoncurrentVersionExpiration</a>: <i>
      - <a href="noncurrentversionexpirationdefinition.md">NoncurrentVersionExpirationDefinition</a></i>
</pre>

## Properties

#### AbortIncompleteMultipartUploadDays

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Enabled

_Required_: Yes

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Id

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Prefix

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Expiration

_Required_: No

_Type_: List of <a href="expirationdefinition.md">ExpirationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NoncurrentVersionExpiration

_Required_: No

_Type_: List of <a href="noncurrentversionexpirationdefinition.md">NoncurrentVersionExpirationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

