# TF::Alicloud::OssBucket LifecycleRuleDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#enabled" title="Enabled">Enabled</a>" : <i>Boolean</i>,
    "<a href="#id" title="Id">Id</a>" : <i>String</i>,
    "<a href="#prefix" title="Prefix">Prefix</a>" : <i>String</i>,
    "<a href="#abortmultipartupload" title="AbortMultipartUpload">AbortMultipartUpload</a>" : <i>[ <a href="abortmultipartuploaddefinition.md">AbortMultipartUploadDefinition</a>, ... ]</i>,
    "<a href="#expiration" title="Expiration">Expiration</a>" : <i>[ <a href="expirationdefinition.md">ExpirationDefinition</a>, ... ]</i>,
    "<a href="#noncurrentversionexpiration" title="NoncurrentVersionExpiration">NoncurrentVersionExpiration</a>" : <i>[ <a href="noncurrentversionexpirationdefinition.md">NoncurrentVersionExpirationDefinition</a>, ... ]</i>,
    "<a href="#noncurrentversiontransition" title="NoncurrentVersionTransition">NoncurrentVersionTransition</a>" : <i>[ <a href="noncurrentversiontransitiondefinition.md">NoncurrentVersionTransitionDefinition</a>, ... ]</i>,
    "<a href="#transitions" title="Transitions">Transitions</a>" : <i>[ <a href="transitionsdefinition.md">TransitionsDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#enabled" title="Enabled">Enabled</a>: <i>Boolean</i>
<a href="#id" title="Id">Id</a>: <i>String</i>
<a href="#prefix" title="Prefix">Prefix</a>: <i>String</i>
<a href="#abortmultipartupload" title="AbortMultipartUpload">AbortMultipartUpload</a>: <i>
      - <a href="abortmultipartuploaddefinition.md">AbortMultipartUploadDefinition</a></i>
<a href="#expiration" title="Expiration">Expiration</a>: <i>
      - <a href="expirationdefinition.md">ExpirationDefinition</a></i>
<a href="#noncurrentversionexpiration" title="NoncurrentVersionExpiration">NoncurrentVersionExpiration</a>: <i>
      - <a href="noncurrentversionexpirationdefinition.md">NoncurrentVersionExpirationDefinition</a></i>
<a href="#noncurrentversiontransition" title="NoncurrentVersionTransition">NoncurrentVersionTransition</a>: <i>
      - <a href="noncurrentversiontransitiondefinition.md">NoncurrentVersionTransitionDefinition</a></i>
<a href="#transitions" title="Transitions">Transitions</a>: <i>
      - <a href="transitionsdefinition.md">TransitionsDefinition</a></i>
</pre>

## Properties

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

#### AbortMultipartUpload

_Required_: No

_Type_: List of <a href="abortmultipartuploaddefinition.md">AbortMultipartUploadDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Expiration

_Required_: No

_Type_: List of <a href="expirationdefinition.md">ExpirationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NoncurrentVersionExpiration

_Required_: No

_Type_: List of <a href="noncurrentversionexpirationdefinition.md">NoncurrentVersionExpirationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NoncurrentVersionTransition

_Required_: No

_Type_: List of <a href="noncurrentversiontransitiondefinition.md">NoncurrentVersionTransitionDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Transitions

_Required_: No

_Type_: List of <a href="transitionsdefinition.md">TransitionsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

