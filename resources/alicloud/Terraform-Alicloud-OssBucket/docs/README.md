# Terraform::Alicloud::OssBucket

CloudFormation equivalent of alicloud_oss_bucket

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Alicloud::OssBucket",
    "Properties" : {
        "<a href="#acl" title="Acl">Acl</a>" : <i>String</i>,
        "<a href="#bucket" title="Bucket">Bucket</a>" : <i>String</i>,
        "<a href="#forcedestroy" title="ForceDestroy">ForceDestroy</a>" : <i>Boolean</i>,
        "<a href="#id" title="Id">Id</a>" : <i>String</i>,
        "<a href="#loggingisenable" title="LoggingIsenable">LoggingIsenable</a>" : <i>Boolean</i>,
        "<a href="#policy" title="Policy">Policy</a>" : <i>String</i>,
        "<a href="#storageclass" title="StorageClass">StorageClass</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ &lt;a href=&#34;tags.md&#34;&gt;Tags&lt;/a&gt;, ... ]</i>,
        "<a href="#corsrule" title="CorsRule">CorsRule</a>" : <i>[ &lt;a href=&#34;corsrule.md&#34;&gt;CorsRule&lt;/a&gt;, ... ]</i>,
        "<a href="#lifecyclerule" title="LifecycleRule">LifecycleRule</a>" : <i>[ &lt;a href=&#34;lifecyclerule.md&#34;&gt;LifecycleRule&lt;/a&gt;, ... ]</i>,
        "<a href="#logging" title="Logging">Logging</a>" : <i>[ &lt;a href=&#34;logging.md&#34;&gt;Logging&lt;/a&gt;, ... ]</i>,
        "<a href="#refererconfig" title="RefererConfig">RefererConfig</a>" : <i>[ &lt;a href=&#34;refererconfig.md&#34;&gt;RefererConfig&lt;/a&gt;, ... ]</i>,
        "<a href="#serversideencryptionrule" title="ServerSideEncryptionRule">ServerSideEncryptionRule</a>" : <i>[ &lt;a href=&#34;serversideencryptionrule.md&#34;&gt;ServerSideEncryptionRule&lt;/a&gt;, ... ]</i>,
        "<a href="#versioning" title="Versioning">Versioning</a>" : <i>[ &lt;a href=&#34;versioning.md&#34;&gt;Versioning&lt;/a&gt;, ... ]</i>,
        "<a href="#website" title="Website">Website</a>" : <i>[ &lt;a href=&#34;website.md&#34;&gt;Website&lt;/a&gt;, ... ]</i>,
        "<a href="#expiration" title="Expiration">Expiration</a>" : <i>[ &lt;a href=&#34;expiration.md&#34;&gt;Expiration&lt;/a&gt;, ... ]</i>,
        "<a href="#transitions" title="Transitions">Transitions</a>" : <i>[ &lt;a href=&#34;transitions.md&#34;&gt;Transitions&lt;/a&gt;, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Alicloud::OssBucket
Properties:
    <a href="#acl" title="Acl">Acl</a>: <i>String</i>
    <a href="#bucket" title="Bucket">Bucket</a>: <i>String</i>
    <a href="#forcedestroy" title="ForceDestroy">ForceDestroy</a>: <i>Boolean</i>
    <a href="#id" title="Id">Id</a>: <i>String</i>
    <a href="#loggingisenable" title="LoggingIsenable">LoggingIsenable</a>: <i>Boolean</i>
    <a href="#policy" title="Policy">Policy</a>: <i>String</i>
    <a href="#storageclass" title="StorageClass">StorageClass</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - &lt;a href=&#34;tags.md&#34;&gt;Tags&lt;/a&gt;</i>
    <a href="#corsrule" title="CorsRule">CorsRule</a>: <i>
      - &lt;a href=&#34;corsrule.md&#34;&gt;CorsRule&lt;/a&gt;</i>
    <a href="#lifecyclerule" title="LifecycleRule">LifecycleRule</a>: <i>
      - &lt;a href=&#34;lifecyclerule.md&#34;&gt;LifecycleRule&lt;/a&gt;</i>
    <a href="#logging" title="Logging">Logging</a>: <i>
      - &lt;a href=&#34;logging.md&#34;&gt;Logging&lt;/a&gt;</i>
    <a href="#refererconfig" title="RefererConfig">RefererConfig</a>: <i>
      - &lt;a href=&#34;refererconfig.md&#34;&gt;RefererConfig&lt;/a&gt;</i>
    <a href="#serversideencryptionrule" title="ServerSideEncryptionRule">ServerSideEncryptionRule</a>: <i>
      - &lt;a href=&#34;serversideencryptionrule.md&#34;&gt;ServerSideEncryptionRule&lt;/a&gt;</i>
    <a href="#versioning" title="Versioning">Versioning</a>: <i>
      - &lt;a href=&#34;versioning.md&#34;&gt;Versioning&lt;/a&gt;</i>
    <a href="#website" title="Website">Website</a>: <i>
      - &lt;a href=&#34;website.md&#34;&gt;Website&lt;/a&gt;</i>
    <a href="#expiration" title="Expiration">Expiration</a>: <i>
      - &lt;a href=&#34;expiration.md&#34;&gt;Expiration&lt;/a&gt;</i>
    <a href="#transitions" title="Transitions">Transitions</a>: <i>
      - &lt;a href=&#34;transitions.md&#34;&gt;Transitions&lt;/a&gt;</i>
</pre>

## Properties

#### Acl

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Bucket

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ForceDestroy

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Id

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LoggingIsenable

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Policy

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StorageClass

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

_Required_: No

_Type_: List of &lt;a href=&#34;tags.md&#34;&gt;Tags&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CorsRule

_Required_: No

_Type_: List of &lt;a href=&#34;corsrule.md&#34;&gt;CorsRule&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LifecycleRule

_Required_: No

_Type_: List of &lt;a href=&#34;lifecyclerule.md&#34;&gt;LifecycleRule&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Logging

_Required_: No

_Type_: List of &lt;a href=&#34;logging.md&#34;&gt;Logging&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RefererConfig

_Required_: No

_Type_: List of &lt;a href=&#34;refererconfig.md&#34;&gt;RefererConfig&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServerSideEncryptionRule

_Required_: No

_Type_: List of &lt;a href=&#34;serversideencryptionrule.md&#34;&gt;ServerSideEncryptionRule&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Versioning

_Required_: No

_Type_: List of &lt;a href=&#34;versioning.md&#34;&gt;Versioning&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Website

_Required_: No

_Type_: List of &lt;a href=&#34;website.md&#34;&gt;Website&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Expiration

_Required_: No

_Type_: List of &lt;a href=&#34;expiration.md&#34;&gt;Expiration&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Transitions

_Required_: No

_Type_: List of &lt;a href=&#34;transitions.md&#34;&gt;Transitions&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### CreationDate

Returns the &lt;code&gt;CreationDate&lt;/code&gt; value.

#### ExtranetEndpoint

Returns the &lt;code&gt;ExtranetEndpoint&lt;/code&gt; value.

#### IntranetEndpoint

Returns the &lt;code&gt;IntranetEndpoint&lt;/code&gt; value.

#### Location

Returns the &lt;code&gt;Location&lt;/code&gt; value.

#### Owner

Returns the &lt;code&gt;Owner&lt;/code&gt; value.

