# Terraform::AzureRM::KeyVaultCertificate

CloudFormation equivalent of azurerm_key_vault_certificate

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AzureRM::KeyVaultCertificate",
    "Properties" : {
        "<a href="#tfcfnid" title="tfcfnid">tfcfnid</a>" : <i>String</i>,
        "<a href="#certificatedata" title="CertificateData">CertificateData</a>" : <i>String</i>,
        "<a href="#keyvaultid" title="KeyVaultId">KeyVaultId</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#secretid" title="SecretId">SecretId</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ &lt;a href=&#34;tags.md&#34;&gt;Tags&lt;/a&gt;, ... ]</i>,
        "<a href="#thumbprint" title="Thumbprint">Thumbprint</a>" : <i>String</i>,
        "<a href="#version" title="Version">Version</a>" : <i>String</i>,
        "<a href="#certificate" title="Certificate">Certificate</a>" : <i>[ &lt;a href=&#34;certificate.md&#34;&gt;Certificate&lt;/a&gt;, ... ]</i>,
        "<a href="#certificatepolicy" title="CertificatePolicy">CertificatePolicy</a>" : <i>[ &lt;a href=&#34;certificatepolicy.md&#34;&gt;CertificatePolicy&lt;/a&gt;, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i>&lt;a href=&#34;timeouts.md&#34;&gt;Timeouts&lt;/a&gt;</i>,
        "<a href="#issuerparameters" title="IssuerParameters">IssuerParameters</a>" : <i>[ &lt;a href=&#34;issuerparameters.md&#34;&gt;IssuerParameters&lt;/a&gt;, ... ]</i>,
        "<a href="#keyproperties" title="KeyProperties">KeyProperties</a>" : <i>[ &lt;a href=&#34;keyproperties.md&#34;&gt;KeyProperties&lt;/a&gt;, ... ]</i>,
        "<a href="#lifetimeaction" title="LifetimeAction">LifetimeAction</a>" : <i>[ &lt;a href=&#34;lifetimeaction.md&#34;&gt;LifetimeAction&lt;/a&gt;, ... ]</i>,
        "<a href="#secretproperties" title="SecretProperties">SecretProperties</a>" : <i>[ &lt;a href=&#34;secretproperties.md&#34;&gt;SecretProperties&lt;/a&gt;, ... ]</i>,
        "<a href="#x509certificateproperties" title="X509CertificateProperties">X509CertificateProperties</a>" : <i>[ &lt;a href=&#34;x509certificateproperties.md&#34;&gt;X509CertificateProperties&lt;/a&gt;, ... ]</i>,
        "<a href="#action" title="Action">Action</a>" : <i>[ &lt;a href=&#34;action.md&#34;&gt;Action&lt;/a&gt;, ... ]</i>,
        "<a href="#trigger" title="Trigger">Trigger</a>" : <i>[ &lt;a href=&#34;trigger.md&#34;&gt;Trigger&lt;/a&gt;, ... ]</i>,
        "<a href="#subjectalternativenames" title="SubjectAlternativeNames">SubjectAlternativeNames</a>" : <i>[ &lt;a href=&#34;subjectalternativenames.md&#34;&gt;SubjectAlternativeNames&lt;/a&gt;, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AzureRM::KeyVaultCertificate
Properties:
    <a href="#tfcfnid" title="tfcfnid">tfcfnid</a>: <i>String</i>
    <a href="#certificatedata" title="CertificateData">CertificateData</a>: <i>String</i>
    <a href="#keyvaultid" title="KeyVaultId">KeyVaultId</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#secretid" title="SecretId">SecretId</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - &lt;a href=&#34;tags.md&#34;&gt;Tags&lt;/a&gt;</i>
    <a href="#thumbprint" title="Thumbprint">Thumbprint</a>: <i>String</i>
    <a href="#version" title="Version">Version</a>: <i>String</i>
    <a href="#certificate" title="Certificate">Certificate</a>: <i>
      - &lt;a href=&#34;certificate.md&#34;&gt;Certificate&lt;/a&gt;</i>
    <a href="#certificatepolicy" title="CertificatePolicy">CertificatePolicy</a>: <i>
      - &lt;a href=&#34;certificatepolicy.md&#34;&gt;CertificatePolicy&lt;/a&gt;</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i>&lt;a href=&#34;timeouts.md&#34;&gt;Timeouts&lt;/a&gt;</i>
    <a href="#issuerparameters" title="IssuerParameters">IssuerParameters</a>: <i>
      - &lt;a href=&#34;issuerparameters.md&#34;&gt;IssuerParameters&lt;/a&gt;</i>
    <a href="#keyproperties" title="KeyProperties">KeyProperties</a>: <i>
      - &lt;a href=&#34;keyproperties.md&#34;&gt;KeyProperties&lt;/a&gt;</i>
    <a href="#lifetimeaction" title="LifetimeAction">LifetimeAction</a>: <i>
      - &lt;a href=&#34;lifetimeaction.md&#34;&gt;LifetimeAction&lt;/a&gt;</i>
    <a href="#secretproperties" title="SecretProperties">SecretProperties</a>: <i>
      - &lt;a href=&#34;secretproperties.md&#34;&gt;SecretProperties&lt;/a&gt;</i>
    <a href="#x509certificateproperties" title="X509CertificateProperties">X509CertificateProperties</a>: <i>
      - &lt;a href=&#34;x509certificateproperties.md&#34;&gt;X509CertificateProperties&lt;/a&gt;</i>
    <a href="#action" title="Action">Action</a>: <i>
      - &lt;a href=&#34;action.md&#34;&gt;Action&lt;/a&gt;</i>
    <a href="#trigger" title="Trigger">Trigger</a>: <i>
      - &lt;a href=&#34;trigger.md&#34;&gt;Trigger&lt;/a&gt;</i>
    <a href="#subjectalternativenames" title="SubjectAlternativeNames">SubjectAlternativeNames</a>: <i>
      - &lt;a href=&#34;subjectalternativenames.md&#34;&gt;SubjectAlternativeNames&lt;/a&gt;</i>
</pre>

## Properties

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CertificateData

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KeyVaultId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecretId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

_Required_: No

_Type_: List of &lt;a href=&#34;tags.md&#34;&gt;Tags&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Thumbprint

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Version

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Certificate

_Required_: No

_Type_: List of &lt;a href=&#34;certificate.md&#34;&gt;Certificate&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CertificatePolicy

_Required_: No

_Type_: List of &lt;a href=&#34;certificatepolicy.md&#34;&gt;CertificatePolicy&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: &lt;a href=&#34;timeouts.md&#34;&gt;Timeouts&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IssuerParameters

_Required_: No

_Type_: List of &lt;a href=&#34;issuerparameters.md&#34;&gt;IssuerParameters&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KeyProperties

_Required_: No

_Type_: List of &lt;a href=&#34;keyproperties.md&#34;&gt;KeyProperties&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LifetimeAction

_Required_: No

_Type_: List of &lt;a href=&#34;lifetimeaction.md&#34;&gt;LifetimeAction&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecretProperties

_Required_: No

_Type_: List of &lt;a href=&#34;secretproperties.md&#34;&gt;SecretProperties&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### X509CertificateProperties

_Required_: No

_Type_: List of &lt;a href=&#34;x509certificateproperties.md&#34;&gt;X509CertificateProperties&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Action

_Required_: No

_Type_: List of &lt;a href=&#34;action.md&#34;&gt;Action&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Trigger

_Required_: No

_Type_: List of &lt;a href=&#34;trigger.md&#34;&gt;Trigger&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SubjectAlternativeNames

_Required_: No

_Type_: List of &lt;a href=&#34;subjectalternativenames.md&#34;&gt;SubjectAlternativeNames&lt;/a&gt;

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

Returns the &lt;code&gt;CertificateData&lt;/code&gt; value.

#### SecretId

Returns the &lt;code&gt;SecretId&lt;/code&gt; value.

#### Thumbprint

Returns the &lt;code&gt;Thumbprint&lt;/code&gt; value.

#### Version

Returns the &lt;code&gt;Version&lt;/code&gt; value.

