# TF::AzureRM::KeyVaultCertificate CertificatePolicyDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#issuerparameters" title="IssuerParameters">IssuerParameters</a>" : <i>[ <a href="issuerparametersdefinition.md">IssuerParametersDefinition</a>, ... ]</i>,
    "<a href="#keyproperties" title="KeyProperties">KeyProperties</a>" : <i>[ <a href="keypropertiesdefinition.md">KeyPropertiesDefinition</a>, ... ]</i>,
    "<a href="#lifetimeaction" title="LifetimeAction">LifetimeAction</a>" : <i>[ <a href="lifetimeactiondefinition.md">LifetimeActionDefinition</a>, ... ]</i>,
    "<a href="#secretproperties" title="SecretProperties">SecretProperties</a>" : <i>[ <a href="secretpropertiesdefinition.md">SecretPropertiesDefinition</a>, ... ]</i>,
    "<a href="#x509certificateproperties" title="X509CertificateProperties">X509CertificateProperties</a>" : <i>[ <a href="x509certificatepropertiesdefinition.md">X509CertificatePropertiesDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#issuerparameters" title="IssuerParameters">IssuerParameters</a>: <i>
      - <a href="issuerparametersdefinition.md">IssuerParametersDefinition</a></i>
<a href="#keyproperties" title="KeyProperties">KeyProperties</a>: <i>
      - <a href="keypropertiesdefinition.md">KeyPropertiesDefinition</a></i>
<a href="#lifetimeaction" title="LifetimeAction">LifetimeAction</a>: <i>
      - <a href="lifetimeactiondefinition.md">LifetimeActionDefinition</a></i>
<a href="#secretproperties" title="SecretProperties">SecretProperties</a>: <i>
      - <a href="secretpropertiesdefinition.md">SecretPropertiesDefinition</a></i>
<a href="#x509certificateproperties" title="X509CertificateProperties">X509CertificateProperties</a>: <i>
      - <a href="x509certificatepropertiesdefinition.md">X509CertificatePropertiesDefinition</a></i>
</pre>

## Properties

#### IssuerParameters

_Required_: No

_Type_: List of <a href="issuerparametersdefinition.md">IssuerParametersDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KeyProperties

_Required_: No

_Type_: List of <a href="keypropertiesdefinition.md">KeyPropertiesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LifetimeAction

_Required_: No

_Type_: List of <a href="lifetimeactiondefinition.md">LifetimeActionDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecretProperties

_Required_: No

_Type_: List of <a href="secretpropertiesdefinition.md">SecretPropertiesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### X509CertificateProperties

_Required_: No

_Type_: List of <a href="x509certificatepropertiesdefinition.md">X509CertificatePropertiesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

