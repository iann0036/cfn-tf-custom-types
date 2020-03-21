# Terraform::HuaweiCloud::S3Bucket LifecycleRule

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#abortincompletemultipartuploaddays" title="AbortIncompleteMultipartUploadDays">AbortIncompleteMultipartUploadDays</a>" : <i>Double</i>,
    "<a href="#enabled" title="Enabled">Enabled</a>" : <i>Boolean</i>,
    "<a href="#id" title="Id">Id</a>" : <i>String</i>,
    "<a href="#prefix" title="Prefix">Prefix</a>" : <i>String</i>,
    "<a href="#expiration" title="Expiration">Expiration</a>" : <i>[ &lt;a href=&#34;lifecyclerule-expiration.md&#34;&gt;Expiration&lt;/a&gt;, ... ]</i>,
    "<a href="#noncurrentversionexpiration" title="NoncurrentVersionExpiration">NoncurrentVersionExpiration</a>" : <i>[ &lt;a href=&#34;lifecyclerule-noncurrentversionexpiration.md&#34;&gt;NoncurrentVersionExpiration&lt;/a&gt;, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#abortincompletemultipartuploaddays" title="AbortIncompleteMultipartUploadDays">AbortIncompleteMultipartUploadDays</a>: <i>Double</i>
<a href="#enabled" title="Enabled">Enabled</a>: <i>Boolean</i>
<a href="#id" title="Id">Id</a>: <i>String</i>
<a href="#prefix" title="Prefix">Prefix</a>: <i>String</i>
<a href="#expiration" title="Expiration">Expiration</a>: <i>
      - &lt;a href=&#34;lifecyclerule-expiration.md&#34;&gt;Expiration&lt;/a&gt;</i>
<a href="#noncurrentversionexpiration" title="NoncurrentVersionExpiration">NoncurrentVersionExpiration</a>: <i>
      - &lt;a href=&#34;lifecyclerule-noncurrentversionexpiration.md&#34;&gt;NoncurrentVersionExpiration&lt;/a&gt;</i>
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
_Type_: List of &lt;a href=&#34;lifecyclerule-expiration.md&#34;&gt;Expiration&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NoncurrentVersionExpiration

_Required_: No
_Type_: List of &lt;a href=&#34;lifecyclerule-noncurrentversionexpiration.md&#34;&gt;NoncurrentVersionExpiration&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

