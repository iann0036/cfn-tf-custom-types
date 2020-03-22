# Terraform::AWS::S3Bucket

CloudFormation equivalent of aws_s3_bucket

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

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Acl

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Arn

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Bucket

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BucketPrefix

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ForceDestroy

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HostedZoneId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Policy

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Region

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RequestPayer

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

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

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the Id.

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

