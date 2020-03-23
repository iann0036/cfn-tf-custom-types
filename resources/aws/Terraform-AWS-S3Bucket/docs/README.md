# Terraform::AWS::S3Bucket

Provides a S3 bucket resource.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AWS::S3Bucket",
    "Properties" : {
        "<a href="#accelerationstatus" title="AccelerationStatus">AccelerationStatus</a>" : <i>String</i>,
        "<a href="#acl" title="Acl">Acl</a>" : <i>String</i>,
        "<a href="#arn" title="Arn">Arn</a>" : <i>String</i>,
        "<a href="#bucket" title="Bucket">Bucket</a>" : <i>String</i>,
        "<a href="#bucketprefix" title="BucketPrefix">BucketPrefix</a>" : <i>String</i>,
        "<a href="#forcedestroy" title="ForceDestroy">ForceDestroy</a>" : <i>Boolean</i>,
        "<a href="#hostedzoneid" title="HostedZoneId">HostedZoneId</a>" : <i>String</i>,
        "<a href="#policy" title="Policy">Policy</a>" : <i>String</i>,
        "<a href="#region" title="Region">Region</a>" : <i>String</i>,
        "<a href="#requestpayer" title="RequestPayer">RequestPayer</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tags.md">Tags</a>, ... ]</i>,
        "<a href="#websitedomain" title="WebsiteDomain">WebsiteDomain</a>" : <i>String</i>,
        "<a href="#websiteendpoint" title="WebsiteEndpoint">WebsiteEndpoint</a>" : <i>String</i>,
        "<a href="#corsrule" title="CorsRule">CorsRule</a>" : <i>[ <a href="corsrule.md">CorsRule</a>, ... ]</i>,
        "<a href="#grant" title="Grant">Grant</a>" : <i>[ <a href="grant.md">Grant</a>, ... ]</i>,
        "<a href="#lifecyclerule" title="LifecycleRule">LifecycleRule</a>" : <i>[ <a href="lifecyclerule.md">LifecycleRule</a>, ... ]</i>,
        "<a href="#logging" title="Logging">Logging</a>" : <i>[ <a href="logging.md">Logging</a>, ... ]</i>,
        "<a href="#objectlockconfiguration" title="ObjectLockConfiguration">ObjectLockConfiguration</a>" : <i>[ <a href="objectlockconfiguration.md">ObjectLockConfiguration</a>, ... ]</i>,
        "<a href="#replicationconfiguration" title="ReplicationConfiguration">ReplicationConfiguration</a>" : <i>[ <a href="replicationconfiguration.md">ReplicationConfiguration</a>, ... ]</i>,
        "<a href="#serversideencryptionconfiguration" title="ServerSideEncryptionConfiguration">ServerSideEncryptionConfiguration</a>" : <i>[ <a href="serversideencryptionconfiguration.md">ServerSideEncryptionConfiguration</a>, ... ]</i>,
        "<a href="#versioning" title="Versioning">Versioning</a>" : <i>[ <a href="versioning.md">Versioning</a>, ... ]</i>,
        "<a href="#website" title="Website">Website</a>" : <i>[ <a href="website.md">Website</a>, ... ]</i>,
        "<a href="#expiration" title="Expiration">Expiration</a>" : <i>[ <a href="expiration.md">Expiration</a>, ... ]</i>,
        "<a href="#noncurrentversionexpiration" title="NoncurrentVersionExpiration">NoncurrentVersionExpiration</a>" : <i>[ <a href="noncurrentversionexpiration.md">NoncurrentVersionExpiration</a>, ... ]</i>,
        "<a href="#noncurrentversiontransition" title="NoncurrentVersionTransition">NoncurrentVersionTransition</a>" : <i>[ <a href="noncurrentversiontransition.md">NoncurrentVersionTransition</a>, ... ]</i>,
        "<a href="#transition" title="Transition">Transition</a>" : <i>[ <a href="transition.md">Transition</a>, ... ]</i>,
        "<a href="#rule" title="Rule">Rule</a>" : <i>[ <a href="rule.md">Rule</a>, ... ]</i>,
        "<a href="#rules" title="Rules">Rules</a>" : <i>[ <a href="rules.md">Rules</a>, ... ]</i>,
        "<a href="#applyserversideencryptionbydefault" title="ApplyServerSideEncryptionByDefault">ApplyServerSideEncryptionByDefault</a>" : <i>[ <a href="applyserversideencryptionbydefault.md">ApplyServerSideEncryptionByDefault</a>, ... ]</i>,
        "<a href="#destination" title="Destination">Destination</a>" : <i>[ <a href="destination.md">Destination</a>, ... ]</i>,
        "<a href="#filter" title="Filter">Filter</a>" : <i>[ <a href="filter.md">Filter</a>, ... ]</i>,
        "<a href="#sourceselectioncriteria" title="SourceSelectionCriteria">SourceSelectionCriteria</a>" : <i>[ <a href="sourceselectioncriteria.md">SourceSelectionCriteria</a>, ... ]</i>,
        "<a href="#accesscontroltranslation" title="AccessControlTranslation">AccessControlTranslation</a>" : <i>[ <a href="accesscontroltranslation.md">AccessControlTranslation</a>, ... ]</i>,
        "<a href="#ssekmsencryptedobjects" title="SseKmsEncryptedObjects">SseKmsEncryptedObjects</a>" : <i>[ <a href="ssekmsencryptedobjects.md">SseKmsEncryptedObjects</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AWS::S3Bucket
Properties:
    <a href="#accelerationstatus" title="AccelerationStatus">AccelerationStatus</a>: <i>String</i>
    <a href="#acl" title="Acl">Acl</a>: <i>String</i>
    <a href="#arn" title="Arn">Arn</a>: <i>String</i>
    <a href="#bucket" title="Bucket">Bucket</a>: <i>String</i>
    <a href="#bucketprefix" title="BucketPrefix">BucketPrefix</a>: <i>String</i>
    <a href="#forcedestroy" title="ForceDestroy">ForceDestroy</a>: <i>Boolean</i>
    <a href="#hostedzoneid" title="HostedZoneId">HostedZoneId</a>: <i>String</i>
    <a href="#policy" title="Policy">Policy</a>: <i>String</i>
    <a href="#region" title="Region">Region</a>: <i>String</i>
    <a href="#requestpayer" title="RequestPayer">RequestPayer</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tags.md">Tags</a></i>
    <a href="#websitedomain" title="WebsiteDomain">WebsiteDomain</a>: <i>String</i>
    <a href="#websiteendpoint" title="WebsiteEndpoint">WebsiteEndpoint</a>: <i>String</i>
    <a href="#corsrule" title="CorsRule">CorsRule</a>: <i>
      - <a href="corsrule.md">CorsRule</a></i>
    <a href="#grant" title="Grant">Grant</a>: <i>
      - <a href="grant.md">Grant</a></i>
    <a href="#lifecyclerule" title="LifecycleRule">LifecycleRule</a>: <i>
      - <a href="lifecyclerule.md">LifecycleRule</a></i>
    <a href="#logging" title="Logging">Logging</a>: <i>
      - <a href="logging.md">Logging</a></i>
    <a href="#objectlockconfiguration" title="ObjectLockConfiguration">ObjectLockConfiguration</a>: <i>
      - <a href="objectlockconfiguration.md">ObjectLockConfiguration</a></i>
    <a href="#replicationconfiguration" title="ReplicationConfiguration">ReplicationConfiguration</a>: <i>
      - <a href="replicationconfiguration.md">ReplicationConfiguration</a></i>
    <a href="#serversideencryptionconfiguration" title="ServerSideEncryptionConfiguration">ServerSideEncryptionConfiguration</a>: <i>
      - <a href="serversideencryptionconfiguration.md">ServerSideEncryptionConfiguration</a></i>
    <a href="#versioning" title="Versioning">Versioning</a>: <i>
      - <a href="versioning.md">Versioning</a></i>
    <a href="#website" title="Website">Website</a>: <i>
      - <a href="website.md">Website</a></i>
    <a href="#expiration" title="Expiration">Expiration</a>: <i>
      - <a href="expiration.md">Expiration</a></i>
    <a href="#noncurrentversionexpiration" title="NoncurrentVersionExpiration">NoncurrentVersionExpiration</a>: <i>
      - <a href="noncurrentversionexpiration.md">NoncurrentVersionExpiration</a></i>
    <a href="#noncurrentversiontransition" title="NoncurrentVersionTransition">NoncurrentVersionTransition</a>: <i>
      - <a href="noncurrentversiontransition.md">NoncurrentVersionTransition</a></i>
    <a href="#transition" title="Transition">Transition</a>: <i>
      - <a href="transition.md">Transition</a></i>
    <a href="#rule" title="Rule">Rule</a>: <i>
      - <a href="rule.md">Rule</a></i>
    <a href="#rules" title="Rules">Rules</a>: <i>
      - <a href="rules.md">Rules</a></i>
    <a href="#applyserversideencryptionbydefault" title="ApplyServerSideEncryptionByDefault">ApplyServerSideEncryptionByDefault</a>: <i>
      - <a href="applyserversideencryptionbydefault.md">ApplyServerSideEncryptionByDefault</a></i>
    <a href="#destination" title="Destination">Destination</a>: <i>
      - <a href="destination.md">Destination</a></i>
    <a href="#filter" title="Filter">Filter</a>: <i>
      - <a href="filter.md">Filter</a></i>
    <a href="#sourceselectioncriteria" title="SourceSelectionCriteria">SourceSelectionCriteria</a>: <i>
      - <a href="sourceselectioncriteria.md">SourceSelectionCriteria</a></i>
    <a href="#accesscontroltranslation" title="AccessControlTranslation">AccessControlTranslation</a>: <i>
      - <a href="accesscontroltranslation.md">AccessControlTranslation</a></i>
    <a href="#ssekmsencryptedobjects" title="SseKmsEncryptedObjects">SseKmsEncryptedObjects</a>: <i>
      - <a href="ssekmsencryptedobjects.md">SseKmsEncryptedObjects</a></i>
</pre>

## Properties

#### AccelerationStatus

Sets the accelerate configuration of an existing bucket. Can be `Enabled` or `Suspended`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Acl

The [canned ACL](https://docs.aws.amazon.com/AmazonS3/latest/dev/acl-overview.html#canned-acl) to apply. Defaults to "private".  Conflicts with `grant`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Arn

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Bucket

The name of the bucket. If omitted, Terraform will assign a random, unique name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BucketPrefix

Creates a unique bucket name beginning with the specified prefix. Conflicts with `bucket`.

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

#### Region

If specified, the AWS region this bucket should reside in. Otherwise, the region used by the callee.

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

A mapping of tags to assign to the bucket.

_Required_: No

_Type_: List of <a href="tags.md">Tags</a>

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

_Type_: List of <a href="corsrule.md">CorsRule</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Grant

_Required_: No

_Type_: List of <a href="grant.md">Grant</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LifecycleRule

_Required_: No

_Type_: List of <a href="lifecyclerule.md">LifecycleRule</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Logging

_Required_: No

_Type_: List of <a href="logging.md">Logging</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ObjectLockConfiguration

_Required_: No

_Type_: List of <a href="objectlockconfiguration.md">ObjectLockConfiguration</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReplicationConfiguration

_Required_: No

_Type_: List of <a href="replicationconfiguration.md">ReplicationConfiguration</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServerSideEncryptionConfiguration

_Required_: No

_Type_: List of <a href="serversideencryptionconfiguration.md">ServerSideEncryptionConfiguration</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Versioning

_Required_: No

_Type_: List of <a href="versioning.md">Versioning</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Website

_Required_: No

_Type_: List of <a href="website.md">Website</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Expiration

_Required_: No

_Type_: List of <a href="expiration.md">Expiration</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NoncurrentVersionExpiration

_Required_: No

_Type_: List of <a href="noncurrentversionexpiration.md">NoncurrentVersionExpiration</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NoncurrentVersionTransition

_Required_: No

_Type_: List of <a href="noncurrentversiontransition.md">NoncurrentVersionTransition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Transition

_Required_: No

_Type_: List of <a href="transition.md">Transition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Rule

_Required_: No

_Type_: List of <a href="rule.md">Rule</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Rules

_Required_: No

_Type_: List of <a href="rules.md">Rules</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ApplyServerSideEncryptionByDefault

_Required_: No

_Type_: List of <a href="applyserversideencryptionbydefault.md">ApplyServerSideEncryptionByDefault</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Destination

_Required_: No

_Type_: List of <a href="destination.md">Destination</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Filter

_Required_: No

_Type_: List of <a href="filter.md">Filter</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceSelectionCriteria

_Required_: No

_Type_: List of <a href="sourceselectioncriteria.md">SourceSelectionCriteria</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AccessControlTranslation

_Required_: No

_Type_: List of <a href="accesscontroltranslation.md">AccessControlTranslation</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SseKmsEncryptedObjects

_Required_: No

_Type_: List of <a href="ssekmsencryptedobjects.md">SseKmsEncryptedObjects</a>

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

