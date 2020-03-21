# Terraform::AzureRM::KeyVaultCertificate

CloudFormation equivalent of azurerm_key_vault_certificate

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AzureRM::KeyVaultCertificate",
    "Properties" : {
        "<a href="#keyvaultid" title="KeyVaultId">KeyVaultId</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tags.md">Tags</a>, ... ]</i>,
        "<a href="#certificate" title="Certificate">Certificate</a>" : <i>[ <a href="certificate.md">Certificate</a>, ... ]</i>,
        "<a href="#certificatepolicy" title="CertificatePolicy">CertificatePolicy</a>" : <i>[ <a href="certificatepolicy.md">CertificatePolicy</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeouts.md">Timeouts</a></i>,
        "<a href="#issuerparameters" title="IssuerParameters">IssuerParameters</a>" : <i>[ <a href="issuerparameters.md">IssuerParameters</a>, ... ]</i>,
        "<a href="#keyproperties" title="KeyProperties">KeyProperties</a>" : <i>[ <a href="keyproperties.md">KeyProperties</a>, ... ]</i>,
        "<a href="#lifetimeaction" title="LifetimeAction">LifetimeAction</a>" : <i>[ <a href="lifetimeaction.md">LifetimeAction</a>, ... ]</i>,
        "<a href="#secretproperties" title="SecretProperties">SecretProperties</a>" : <i>[ <a href="secretproperties.md">SecretProperties</a>, ... ]</i>,
        "<a href="#x509certificateproperties" title="X509CertificateProperties">X509CertificateProperties</a>" : <i>[ <a href="x509certificateproperties.md">X509CertificateProperties</a>, ... ]</i>,
        "<a href="#action" title="Action">Action</a>" : <i>[ <a href="action.md">Action</a>, ... ]</i>,
        "<a href="#trigger" title="Trigger">Trigger</a>" : <i>[ <a href="trigger.md">Trigger</a>, ... ]</i>,
        "<a href="#subjectalternativenames" title="SubjectAlternativeNames">SubjectAlternativeNames</a>" : <i>[ <a href="subjectalternativenames.md">SubjectAlternativeNames</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AzureRM::KeyVaultCertificate
Properties:
    <a href="#keyvaultid" title="KeyVaultId">KeyVaultId</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tags.md">Tags</a></i>
    <a href="#certificate" title="Certificate">Certificate</a>: <i>
      - <a href="certificate.md">Certificate</a></i>
    <a href="#certificatepolicy" title="CertificatePolicy">CertificatePolicy</a>: <i>
      - <a href="certificatepolicy.md">CertificatePolicy</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeouts.md">Timeouts</a></i>
    <a href="#issuerparameters" title="IssuerParameters">IssuerParameters</a>: <i>
      - <a href="issuerparameters.md">IssuerParameters</a></i>
    <a href="#keyproperties" title="KeyProperties">KeyProperties</a>: <i>
      - <a href="keyproperties.md">KeyProperties</a></i>
    <a href="#lifetimeaction" title="LifetimeAction">LifetimeAction</a>: <i>
      - <a href="lifetimeaction.md">LifetimeAction</a></i>
    <a href="#secretproperties" title="SecretProperties">SecretProperties</a>: <i>
      - <a href="secretproperties.md">SecretProperties</a></i>
    <a href="#x509certificateproperties" title="X509CertificateProperties">X509CertificateProperties</a>: <i>
      - <a href="x509certificateproperties.md">X509CertificateProperties</a></i>
    <a href="#action" title="Action">Action</a>: <i>
      - <a href="action.md">Action</a></i>
    <a href="#trigger" title="Trigger">Trigger</a>: <i>
      - <a href="trigger.md">Trigger</a></i>
    <a href="#subjectalternativenames" title="SubjectAlternativeNames">SubjectAlternativeNames</a>: <i>
      - <a href="subjectalternativenames.md">SubjectAlternativeNames</a></i>
</pre>

## Properties

#### KeyVaultId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

_Required_: No

_Type_: List of <a href="tags.md">Tags</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Certificate

_Required_: No

_Type_: List of <a href="certificate.md">Certificate</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CertificatePolicy

_Required_: No

_Type_: List of <a href="certificatepolicy.md">CertificatePolicy</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeouts.md">Timeouts</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IssuerParameters

_Required_: No

_Type_: List of <a href="issuerparameters.md">IssuerParameters</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KeyProperties

_Required_: No

_Type_: List of <a href="keyproperties.md">KeyProperties</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LifetimeAction

_Required_: No

_Type_: List of <a href="lifetimeaction.md">LifetimeAction</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecretProperties

_Required_: No

_Type_: List of <a href="secretproperties.md">SecretProperties</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### X509CertificateProperties

_Required_: No

_Type_: List of <a href="x509certificateproperties.md">X509CertificateProperties</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Action

_Required_: No

_Type_: List of <a href="action.md">Action</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Trigger

_Required_: No

_Type_: List of <a href="trigger.md">Trigger</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SubjectAlternativeNames

_Required_: No

_Type_: List of <a href="subjectalternativenames.md">SubjectAlternativeNames</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### CertificateData

Returns the <code>CertificateData</code> value.

#### SecretId

Returns the <code>SecretId</code> value.

#### Thumbprint

Returns the <code>Thumbprint</code> value.

#### Version

Returns the <code>Version</code> value.

