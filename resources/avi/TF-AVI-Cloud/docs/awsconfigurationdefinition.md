# TF::AVI::Cloud AwsConfigurationDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#accesskeyid" title="AccessKeyId">AccessKeyId</a>" : <i>String</i>,
    "<a href="#asgpollinterval" title="AsgPollInterval">AsgPollInterval</a>" : <i>Double</i>,
    "<a href="#freeelasticips" title="FreeElasticips">FreeElasticips</a>" : <i>Boolean</i>,
    "<a href="#iamassumerole" title="IamAssumeRole">IamAssumeRole</a>" : <i>String</i>,
    "<a href="#publishviptopubliczone" title="PublishVipToPublicZone">PublishVipToPublicZone</a>" : <i>Boolean</i>,
    "<a href="#region" title="Region">Region</a>" : <i>String</i>,
    "<a href="#route53integration" title="Route53Integration">Route53Integration</a>" : <i>Boolean</i>,
    "<a href="#secretaccesskey" title="SecretAccessKey">SecretAccessKey</a>" : <i>String</i>,
    "<a href="#ttl" title="Ttl">Ttl</a>" : <i>Double</i>,
    "<a href="#useiamroles" title="UseIamRoles">UseIamRoles</a>" : <i>Boolean</i>,
    "<a href="#usesnssqs" title="UseSnsSqs">UseSnsSqs</a>" : <i>Boolean</i>,
    "<a href="#vpc" title="Vpc">Vpc</a>" : <i>String</i>,
    "<a href="#vpcid" title="VpcId">VpcId</a>" : <i>String</i>,
    "<a href="#ebsencryption" title="EbsEncryption">EbsEncryption</a>" : <i>[ <a href="ebsencryptiondefinition.md">EbsEncryptionDefinition</a>, ... ]</i>,
    "<a href="#s3encryption" title="S3Encryption">S3Encryption</a>" : <i>[ <a href="s3encryptiondefinition.md">S3EncryptionDefinition</a>, ... ]</i>,
    "<a href="#sqsencryption" title="SqsEncryption">SqsEncryption</a>" : <i>[ <a href="sqsencryptiondefinition.md">SqsEncryptionDefinition</a>, ... ]</i>,
    "<a href="#zones" title="Zones">Zones</a>" : <i>[ <a href="zonesdefinition.md">ZonesDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#accesskeyid" title="AccessKeyId">AccessKeyId</a>: <i>String</i>
<a href="#asgpollinterval" title="AsgPollInterval">AsgPollInterval</a>: <i>Double</i>
<a href="#freeelasticips" title="FreeElasticips">FreeElasticips</a>: <i>Boolean</i>
<a href="#iamassumerole" title="IamAssumeRole">IamAssumeRole</a>: <i>String</i>
<a href="#publishviptopubliczone" title="PublishVipToPublicZone">PublishVipToPublicZone</a>: <i>Boolean</i>
<a href="#region" title="Region">Region</a>: <i>String</i>
<a href="#route53integration" title="Route53Integration">Route53Integration</a>: <i>Boolean</i>
<a href="#secretaccesskey" title="SecretAccessKey">SecretAccessKey</a>: <i>String</i>
<a href="#ttl" title="Ttl">Ttl</a>: <i>Double</i>
<a href="#useiamroles" title="UseIamRoles">UseIamRoles</a>: <i>Boolean</i>
<a href="#usesnssqs" title="UseSnsSqs">UseSnsSqs</a>: <i>Boolean</i>
<a href="#vpc" title="Vpc">Vpc</a>: <i>String</i>
<a href="#vpcid" title="VpcId">VpcId</a>: <i>String</i>
<a href="#ebsencryption" title="EbsEncryption">EbsEncryption</a>: <i>
      - <a href="ebsencryptiondefinition.md">EbsEncryptionDefinition</a></i>
<a href="#s3encryption" title="S3Encryption">S3Encryption</a>: <i>
      - <a href="s3encryptiondefinition.md">S3EncryptionDefinition</a></i>
<a href="#sqsencryption" title="SqsEncryption">SqsEncryption</a>: <i>
      - <a href="sqsencryptiondefinition.md">SqsEncryptionDefinition</a></i>
<a href="#zones" title="Zones">Zones</a>: <i>
      - <a href="zonesdefinition.md">ZonesDefinition</a></i>
</pre>

## Properties

#### AccessKeyId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AsgPollInterval

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FreeElasticips

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IamAssumeRole

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PublishVipToPublicZone

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Region

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Route53Integration

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecretAccessKey

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ttl

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UseIamRoles

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UseSnsSqs

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vpc

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VpcId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EbsEncryption

_Required_: No

_Type_: List of <a href="ebsencryptiondefinition.md">EbsEncryptionDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### S3Encryption

_Required_: No

_Type_: List of <a href="s3encryptiondefinition.md">S3EncryptionDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SqsEncryption

_Required_: No

_Type_: List of <a href="sqsencryptiondefinition.md">SqsEncryptionDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Zones

_Required_: No

_Type_: List of <a href="zonesdefinition.md">ZonesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

