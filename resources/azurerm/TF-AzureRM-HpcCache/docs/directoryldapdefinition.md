# TF::AzureRM::HpcCache DirectoryLdapDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#basedn" title="BaseDn">BaseDn</a>" : <i>String</i>,
    "<a href="#certificatevalidationuri" title="CertificateValidationUri">CertificateValidationUri</a>" : <i>String</i>,
    "<a href="#downloadcertificateautomatically" title="DownloadCertificateAutomatically">DownloadCertificateAutomatically</a>" : <i>Boolean</i>,
    "<a href="#encrypted" title="Encrypted">Encrypted</a>" : <i>Boolean</i>,
    "<a href="#server" title="Server">Server</a>" : <i>String</i>,
    "<a href="#bind" title="Bind">Bind</a>" : <i>[ <a href="binddefinition.md">BindDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#basedn" title="BaseDn">BaseDn</a>: <i>String</i>
<a href="#certificatevalidationuri" title="CertificateValidationUri">CertificateValidationUri</a>: <i>String</i>
<a href="#downloadcertificateautomatically" title="DownloadCertificateAutomatically">DownloadCertificateAutomatically</a>: <i>Boolean</i>
<a href="#encrypted" title="Encrypted">Encrypted</a>: <i>Boolean</i>
<a href="#server" title="Server">Server</a>: <i>String</i>
<a href="#bind" title="Bind">Bind</a>: <i>
      - <a href="binddefinition.md">BindDefinition</a></i>
</pre>

## Properties

#### BaseDn

The base distinguished name (DN) for the LDAP domain.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CertificateValidationUri

The URI of the CA certificate to validate the LDAP secure connection.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DownloadCertificateAutomatically

Whether the certificate should be automatically downloaded. This can be set to `true` only when `certificate_validation_uri` is provided. Defaults to `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Encrypted

Whether the LDAP connection should be encrypted? Defaults to `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Server

The FQDN or IP address of the LDAP server.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Bind

_Required_: No

_Type_: List of <a href="binddefinition.md">BindDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

