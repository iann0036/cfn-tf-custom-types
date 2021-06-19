# TF::AWS::S3Bucket

Provides a S3 bucket resource.

-> This functionality is for managing S3 in an AWS Partition. To manage [S3 on Outposts](https://docs.aws.amazon.com/AmazonS3/latest/dev/S3onOutposts.html), see the [`aws_s3control_bucket`](/docs/providers/aws/r/s3control_bucket.html) resource.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AWS::S3Bucket",
    "Properties" : {
        "<a href="#accelerationstatus" title="AccelerationStatus">AccelerationStatus</a>" : <i>String</i>,
        "<a href="#acl" title="Acl">Acl</a>" : <i>String</i>,
        "<a href="#arn" title="Arn">Arn</a>" : <i>String</i>,
        "<a href="#bucket" title="Bucket">Bucket</a>" : <i>String</i>,
        "<a href="#bucketprefix" title="BucketPrefix">BucketPrefix</a>" : <i>String</i>,
        "<a href="#forcedestroy" title="ForceDestroy">ForceDestroy</a>" : <i>Boolean</i>,
        "<a href="#hostedzoneid" title="HostedZoneId">HostedZoneId</a>" : <i>String</i>,
        "<a href="#policy" title="Policy">Policy</a>" : <i>String</i>,
        "<a href="#requestpayer" title="RequestPayer">RequestPayer</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tagsdefinition.md">TagsDefinition</a>, ... ]</i>,
        "<a href="#tagsall" title="TagsAll">TagsAll</a>" : <i>[ <a href="tagsalldefinition.md">TagsAllDefinition</a>, ... ]</i>,
        "<a href="#websitedomain" title="WebsiteDomain">WebsiteDomain</a>" : <i>String</i>,
        "<a href="#websiteendpoint" title="WebsiteEndpoint">WebsiteEndpoint</a>" : <i>String</i>,
        "<a href="#corsrule" title="CorsRule">CorsRule</a>" : <i>[ <a href="corsruledefinition.md">CorsRuleDefinition</a>, ... ]</i>,
        "<a href="#grant" title="Grant">Grant</a>" : <i>[ <a href="grantdefinition.md">GrantDefinition</a>, ... ]</i>,
        "<a href="#lifecyclerule" title="LifecycleRule">LifecycleRule</a>" : <i>[ <a href="lifecycleruledefinition.md">LifecycleRuleDefinition</a>, ... ]</i>,
        "<a href="#logging" title="Logging">Logging</a>" : <i>[ <a href="loggingdefinition.md">LoggingDefinition</a>, ... ]</i>,
        "<a href="#objectlockconfiguration" title="ObjectLockConfiguration">ObjectLockConfiguration</a>" : <i>[ <a href="objectlockconfigurationdefinition.md">ObjectLockConfigurationDefinition</a>, ... ]</i>,
        "<a href="#replicationconfiguration" title="ReplicationConfiguration">ReplicationConfiguration</a>" : <i>[ <a href="replicationconfigurationdefinition.md">ReplicationConfigurationDefinition</a>, ... ]</i>,
        "<a href="#serversideencryptionconfiguration" title="ServerSideEncryptionConfiguration">ServerSideEncryptionConfiguration</a>" : <i>[ <a href="serversideencryptionconfigurationdefinition.md">ServerSideEncryptionConfigurationDefinition</a>, ... ]</i>,
        "<a href="#versioning" title="Versioning">Versioning</a>" : <i>[ <a href="versioningdefinition.md">VersioningDefinition</a>, ... ]</i>,
        "<a href="#website" title="Website">Website</a>" : <i>[ <a href="websitedefinition.md">WebsiteDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AWS::S3Bucket
Properties:
    <a href="#accelerationstatus" title="AccelerationStatus">AccelerationStatus</a>: <i>String</i>
    <a href="#acl" title="Acl">Acl</a>: <i>String</i>
    <a href="#arn" title="Arn">Arn</a>: <i>String</i>
    <a href="#bucket" title="Bucket">Bucket</a>: <i>String</i>
    <a href="#bucketprefix" title="BucketPrefix">BucketPrefix</a>: <i>String</i>
    <a href="#forcedestroy" title="ForceDestroy">ForceDestroy</a>: <i>Boolean</i>
    <a href="#hostedzoneid" title="HostedZoneId">HostedZoneId</a>: <i>String</i>
    <a href="#policy" title="Policy">Policy</a>: <i>String</i>
    <a href="#requestpayer" title="RequestPayer">RequestPayer</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tagsdefinition.md">TagsDefinition</a></i>
    <a href="#tagsall" title="TagsAll">TagsAll</a>: <i>
      - <a href="tagsalldefinition.md">TagsAllDefinition</a></i>
    <a href="#websitedomain" title="WebsiteDomain">WebsiteDomain</a>: <i>String</i>
    <a href="#websiteendpoint" title="WebsiteEndpoint">WebsiteEndpoint</a>: <i>String</i>
    <a href="#corsrule" title="CorsRule">CorsRule</a>: <i>
      - <a href="corsruledefinition.md">CorsRuleDefinition</a></i>
    <a href="#grant" title="Grant">Grant</a>: <i>
      - <a href="grantdefinition.md">GrantDefinition</a></i>
    <a href="#lifecyclerule" title="LifecycleRule">LifecycleRule</a>: <i>
      - <a href="lifecycleruledefinition.md">LifecycleRuleDefinition</a></i>
    <a href="#logging" title="Logging">Logging</a>: <i>
      - <a href="loggingdefinition.md">LoggingDefinition</a></i>
    <a href="#objectlockconfiguration" title="ObjectLockConfiguration">ObjectLockConfiguration</a>: <i>
      - <a href="objectlockconfigurationdefinition.md">ObjectLockConfigurationDefinition</a></i>
    <a href="#replicationconfiguration" title="ReplicationConfiguration">ReplicationConfiguration</a>: <i>
      - <a href="replicationconfigurationdefinition.md">ReplicationConfigurationDefinition</a></i>
    <a href="#serversideencryptionconfiguration" title="ServerSideEncryptionConfiguration">ServerSideEncryptionConfiguration</a>: <i>
      - <a href="serversideencryptionconfigurationdefinition.md">ServerSideEncryptionConfigurationDefinition</a></i>
    <a href="#versioning" title="Versioning">Versioning</a>: <i>
      - <a href="versioningdefinition.md">VersioningDefinition</a></i>
    <a href="#website" title="Website">Website</a>: <i>
      - <a href="websitedefinition.md">WebsiteDefinition</a></i>
</pre>

## Properties

#### AccelerationStatus

Sets the accelerate configuration of an existing bucket. Can be `Enabled` or `Suspended`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Acl

The [canned ACL](https://docs.aws.amazon.com/AmazonS3/latest/dev/acl-overview.html#canned-acl) to apply. Valid values are `private`, `public-read`, `public-read-write`, `aws-exec-read`, `authenticated-read`, and `log-delivery-write`. Defaults to `private`.  Conflicts with `grant`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Arn

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Bucket

The name of the bucket. If omitted, Terraform will assign a random, unique name. Must be less than or equal to 63 characters in length.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BucketPrefix

Creates a unique bucket name beginning with the specified prefix. Conflicts with `bucket`. Must be less than or equal to 37 characters in length.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ForceDestroy

A boolean that indicates all objects (including any [locked objects](https://docs.aws.amazon.com/AmazonS3/latest/dev/object-lock-overview.html)) should be deleted from the bucket so that the bucket can be destroyed without error. These objects are *not* recoverable.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HostedZoneId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Policy

A valid [bucket policy](https://docs.aws.amazon.com/AmazonS3/latest/dev/example-bucket-policies.html) JSON document. Note that if the policy document is not specific enough (but still valid), Terraform may view the policy as constantly changing in a `terraform plan`. In this case, please make sure you use the verbose/specific version of the policy. For more information about building AWS IAM policy documents with Terraform, see the [AWS IAM Policy Document Guide](https://learn.hashicorp.com/terraform/aws/iam-policy).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RequestPayer

Specifies who should bear the cost of Amazon S3 data transfer.
Can be either `BucketOwner` or `Requester`. By default, the owner of the S3 bucket would incur
the costs of any data transfer. See [Requester Pays Buckets](http://docs.aws.amazon.com/AmazonS3/latest/dev/RequesterPaysBuckets.html)
developer guide for more information.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

A map of tags to assign to the bucket. If configured with a provider [`default_tags` configuration block](/docs/providers/aws/index.html#default_tags-configuration-block) present, tags with matching keys will overwrite those defined at the provider-level.

_Required_: No

_Type_: List of <a href="tagsdefinition.md">TagsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TagsAll

_Required_: No

_Type_: List of <a href="tagsalldefinition.md">TagsAllDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WebsiteDomain

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WebsiteEndpoint

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CorsRule

_Required_: No

_Type_: List of <a href="corsruledefinition.md">CorsRuleDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Grant

_Required_: No

_Type_: List of <a href="grantdefinition.md">GrantDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LifecycleRule

_Required_: No

_Type_: List of <a href="lifecycleruledefinition.md">LifecycleRuleDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Logging

_Required_: No

_Type_: List of <a href="loggingdefinition.md">LoggingDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ObjectLockConfiguration

_Required_: No

_Type_: List of <a href="objectlockconfigurationdefinition.md">ObjectLockConfigurationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReplicationConfiguration

_Required_: No

_Type_: List of <a href="replicationconfigurationdefinition.md">ReplicationConfigurationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServerSideEncryptionConfiguration

_Required_: No

_Type_: List of <a href="serversideencryptionconfigurationdefinition.md">ServerSideEncryptionConfigurationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Versioning

_Required_: No

_Type_: List of <a href="versioningdefinition.md">VersioningDefinition</a>

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

#### BucketDomainName

Returns the <code>BucketDomainName</code> value.

#### BucketRegionalDomainName

Returns the <code>BucketRegionalDomainName</code> value.

#### Id

Returns the <code>Id</code> value.

#### Region

Returns the <code>Region</code> value.

