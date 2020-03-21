# Terraform::AzureRM::KeyVaultCertificate CertificatePolicy

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#issuerparameters" title="IssuerParameters">IssuerParameters</a>" : <i>[ <a href="certificatepolicy-issuerparameters.md">IssuerParameters</a>, ... ]</i>,
    "<a href="#keyproperties" title="KeyProperties">KeyProperties</a>" : <i>[ <a href="certificatepolicy-keyproperties.md">KeyProperties</a>, ... ]</i>,
    "<a href="#lifetimeaction" title="LifetimeAction">LifetimeAction</a>" : <i>[ <a href="certificatepolicy-lifetimeaction.md">LifetimeAction</a>, ... ]</i>,
    "<a href="#secretproperties" title="SecretProperties">SecretProperties</a>" : <i>[ <a href="certificatepolicy-secretproperties.md">SecretProperties</a>, ... ]</i>,
    "<a href="#x509certificateproperties" title="X509CertificateProperties">X509CertificateProperties</a>" : <i>[ <a href="certificatepolicy-x509certificateproperties.md">X509CertificateProperties</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#issuerparameters" title="IssuerParameters">IssuerParameters</a>: <i>
      - <a href="certificatepolicy-issuerparameters.md">IssuerParameters</a></i>
<a href="#keyproperties" title="KeyProperties">KeyProperties</a>: <i>
      - <a href="certificatepolicy-keyproperties.md">KeyProperties</a></i>
<a href="#lifetimeaction" title="LifetimeAction">LifetimeAction</a>: <i>
      - <a href="certificatepolicy-lifetimeaction.md">LifetimeAction</a></i>
<a href="#secretproperties" title="SecretProperties">SecretProperties</a>: <i>
      - <a href="certificatepolicy-secretproperties.md">SecretProperties</a></i>
<a href="#x509certificateproperties" title="X509CertificateProperties">X509CertificateProperties</a>: <i>
      - <a href="certificatepolicy-x509certificateproperties.md">X509CertificateProperties</a></i>
</pre>

## Properties

#### IssuerParameters

_Required_: No

_Type_: List of <a href="certificatepolicy-issuerparameters.md">IssuerParameters</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KeyProperties

_Required_: No

_Type_: List of <a href="certificatepolicy-keyproperties.md">KeyProperties</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LifetimeAction

_Required_: No

_Type_: List of <a href="certificatepolicy-lifetimeaction.md">LifetimeAction</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecretProperties

_Required_: No

_Type_: List of <a href="certificatepolicy-secretproperties.md">SecretProperties</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### X509CertificateProperties

_Required_: No

_Type_: List of <a href="certificatepolicy-x509certificateproperties.md">X509CertificateProperties</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

