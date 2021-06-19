# TF::TencentCloud::CosBucket

Provides a COS resource to create a COS bucket and set its attributes.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::TencentCloud::CosBucket",
    "Properties" : {
        "<a href="#acl" title="Acl">Acl</a>" : <i>String</i>,
        "<a href="#bucket" title="Bucket">Bucket</a>" : <i>String</i>,
        "<a href="#encryptionalgorithm" title="EncryptionAlgorithm">EncryptionAlgorithm</a>" : <i>String</i>,
        "<a href="#logenable" title="LogEnable">LogEnable</a>" : <i>Boolean</i>,
        "<a href="#logprefix" title="LogPrefix">LogPrefix</a>" : <i>String</i>,
        "<a href="#logtargetbucket" title="LogTargetBucket">LogTargetBucket</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tagsdefinition.md">TagsDefinition</a>, ... ]</i>,
        "<a href="#versioningenable" title="VersioningEnable">VersioningEnable</a>" : <i>Boolean</i>,
        "<a href="#corsrules" title="CorsRules">CorsRules</a>" : <i>[ <a href="corsrulesdefinition.md">CorsRulesDefinition</a>, ... ]</i>,
        "<a href="#lifecyclerules" title="LifecycleRules">LifecycleRules</a>" : <i>[ <a href="lifecyclerulesdefinition.md">LifecycleRulesDefinition</a>, ... ]</i>,
        "<a href="#website" title="Website">Website</a>" : <i>[ <a href="websitedefinition.md">WebsiteDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::TencentCloud::CosBucket
Properties:
    <a href="#acl" title="Acl">Acl</a>: <i>String</i>
    <a href="#bucket" title="Bucket">Bucket</a>: <i>String</i>
    <a href="#encryptionalgorithm" title="EncryptionAlgorithm">EncryptionAlgorithm</a>: <i>String</i>
    <a href="#logenable" title="LogEnable">LogEnable</a>: <i>Boolean</i>
    <a href="#logprefix" title="LogPrefix">LogPrefix</a>: <i>String</i>
    <a href="#logtargetbucket" title="LogTargetBucket">LogTargetBucket</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tagsdefinition.md">TagsDefinition</a></i>
    <a href="#versioningenable" title="VersioningEnable">VersioningEnable</a>: <i>Boolean</i>
    <a href="#corsrules" title="CorsRules">CorsRules</a>: <i>
      - <a href="corsrulesdefinition.md">CorsRulesDefinition</a></i>
    <a href="#lifecyclerules" title="LifecycleRules">LifecycleRules</a>: <i>
      - <a href="lifecyclerulesdefinition.md">LifecycleRulesDefinition</a></i>
    <a href="#website" title="Website">Website</a>: <i>
      - <a href="websitedefinition.md">WebsiteDefinition</a></i>
</pre>

## Properties

#### Acl

The canned ACL to apply. Valid values: private, public-read, and public-read-write. Defaults to private.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Bucket

The name of a bucket to be created. Bucket format should be [custom name]-[appid], for example `mycos-1258798060`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EncryptionAlgorithm

The server-side encryption algorithm to use. Valid value is `AES256`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LogEnable

Indicate the access log of this bucket to be saved or not. Default is `false`. If set `true`, the access log will be saved with `log_target_bucket`. To enable log, the full access of log service must be granted. [Full Access Role Policy](https://intl.cloud.tencent.com/document/product/436/16920).

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LogPrefix

The prefix log name which saves the access log of this bucket per 5 minutes. Eg. `MyLogPrefix/`. The log access file format is `log_target_bucket`/`log_prefix`{YYYY}/{MM}/{DD}/{time}_{random}_{index}.gz. Only valid when `log_enable` is `true`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LogTargetBucket

The target bucket name which saves the access log of this bucket per 5 minutes. The log access file format is `log_target_bucket`/`log_prefix`{YYYY}/{MM}/{DD}/{time}_{random}_{index}.gz. Only valid when `log_enable` is `true`. User must have full access on this bucket.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

The tags of a bucket.

_Required_: No

_Type_: List of <a href="tagsdefinition.md">TagsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VersioningEnable

Enable bucket versioning.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CorsRules

_Required_: No

_Type_: List of <a href="corsrulesdefinition.md">CorsRulesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LifecycleRules

_Required_: No

_Type_: List of <a href="lifecyclerulesdefinition.md">LifecycleRulesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Website

_Required_: No

_Type_: List of <a href="websitedefinition.md">WebsiteDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### CosBucketUrl

Returns the <code>CosBucketUrl</code> value.

#### Id

Returns the <code>Id</code> value.

