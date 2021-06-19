# TF::MongoDBAtlas::EncryptionAtRest

`mongodbatlas_encryption_at_rest` Allows management of encryption at rest for an Atlas project with one of the following providers:

[Amazon Web Services Key Management Service](https://docs.atlas.mongodb.com/security-aws-kms/#security-aws-kms)
[Azure Key Vault](https://docs.atlas.mongodb.com/security-azure-kms/#security-azure-kms)
[Google Cloud KMS](https://docs.atlas.mongodb.com/security-gcp-kms/#security-gcp-kms)

After configuring at least one Encryption at Rest provider for the Atlas project, Project Owners can enable Encryption at Rest for each Atlas cluster for which they require encryption. The Encryption at Rest provider does not have to match the cluster cloud service provider.

Atlas does not automatically rotate user-managed encryption keys. Defer to your preferred Encryption at Rest provider’s documentation and guidance for best practices on key rotation. Atlas automatically creates a 365-day key rotation alert when you configure Encryption at Rest using your Key Management in an Atlas projec...

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::MongoDBAtlas::EncryptionAtRest",
    "Properties" : {
        "<a href="#awskms" title="AwsKms">AwsKms</a>" : <i>[ <a href="awskmsdefinition.md">AwsKmsDefinition</a>, ... ]</i>,
        "<a href="#azurekeyvault" title="AzureKeyVault">AzureKeyVault</a>" : <i>[ <a href="azurekeyvaultdefinition.md">AzureKeyVaultDefinition</a>, ... ]</i>,
        "<a href="#googlecloudkms" title="GoogleCloudKms">GoogleCloudKms</a>" : <i>[ <a href="googlecloudkmsdefinition.md">GoogleCloudKmsDefinition</a>, ... ]</i>,
        "<a href="#projectid" title="ProjectId">ProjectId</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::MongoDBAtlas::EncryptionAtRest
Properties:
    <a href="#awskms" title="AwsKms">AwsKms</a>: <i>
      - <a href="awskmsdefinition.md">AwsKmsDefinition</a></i>
    <a href="#azurekeyvault" title="AzureKeyVault">AzureKeyVault</a>: <i>
      - <a href="azurekeyvaultdefinition.md">AzureKeyVaultDefinition</a></i>
    <a href="#googlecloudkms" title="GoogleCloudKms">GoogleCloudKms</a>: <i>
      - <a href="googlecloudkmsdefinition.md">GoogleCloudKmsDefinition</a></i>
    <a href="#projectid" title="ProjectId">ProjectId</a>: <i>String</i>
</pre>

## Properties

#### AwsKms

Specifies AWS KMS configuration details and whether Encryption at Rest is enabled for an Atlas project.

_Required_: No

_Type_: List of <a href="awskmsdefinition.md">AwsKmsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AzureKeyVault

Specifies Azure Key Vault configuration details and whether Encryption at Rest is enabled for an Atlas project.

_Required_: No

_Type_: List of <a href="azurekeyvaultdefinition.md">AzureKeyVaultDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GoogleCloudKms

Specifies GCP KMS configuration details and whether Encryption at Rest is enabled for an Atlas project.

_Required_: No

_Type_: List of <a href="googlecloudkmsdefinition.md">GoogleCloudKmsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProjectId

The unique identifier for the project.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Id

Returns the <code>Id</code> value.

