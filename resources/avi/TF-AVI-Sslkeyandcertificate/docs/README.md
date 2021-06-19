# TF::AVI::Sslkeyandcertificate

The SSLKeyAndCertificate resource allows the creation and management of Avi SSLKeyAndCertificate

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AVI::Sslkeyandcertificate",
    "Properties" : {
        "<a href="#certificatebase64" title="CertificateBase64">CertificateBase64</a>" : <i>Boolean</i>,
        "<a href="#certificatemanagementprofileref" title="CertificateManagementProfileRef">CertificateManagementProfileRef</a>" : <i>String</i>,
        "<a href="#createdby" title="CreatedBy">CreatedBy</a>" : <i>String</i>,
        "<a href="#enableocspstapling" title="EnableOcspStapling">EnableOcspStapling</a>" : <i>Boolean</i>,
        "<a href="#enckeybase64" title="EnckeyBase64">EnckeyBase64</a>" : <i>String</i>,
        "<a href="#enckeyname" title="EnckeyName">EnckeyName</a>" : <i>String</i>,
        "<a href="#format" title="Format">Format</a>" : <i>String</i>,
        "<a href="#hardwaresecuritymodulegroupref" title="HardwaresecuritymodulegroupRef">HardwaresecuritymodulegroupRef</a>" : <i>String</i>,
        "<a href="#key" title="Key">Key</a>" : <i>String</i>,
        "<a href="#keybase64" title="KeyBase64">KeyBase64</a>" : <i>Boolean</i>,
        "<a href="#keypassphrase" title="KeyPassphrase">KeyPassphrase</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#status" title="Status">Status</a>" : <i>String</i>,
        "<a href="#tenantref" title="TenantRef">TenantRef</a>" : <i>String</i>,
        "<a href="#type" title="Type">Type</a>" : <i>String</i>,
        "<a href="#uuid" title="Uuid">Uuid</a>" : <i>String</i>,
        "<a href="#cacerts" title="CaCerts">CaCerts</a>" : <i>[ <a href="cacertsdefinition.md">CaCertsDefinition</a>, ... ]</i>,
        "<a href="#certificate" title="Certificate">Certificate</a>" : <i>[ <a href="certificatedefinition.md">CertificateDefinition</a>, ... ]</i>,
        "<a href="#dynamicparams" title="DynamicParams">DynamicParams</a>" : <i>[ <a href="dynamicparamsdefinition.md">DynamicParamsDefinition</a>, ... ]</i>,
        "<a href="#keyparams" title="KeyParams">KeyParams</a>" : <i>[ <a href="keyparamsdefinition.md">KeyParamsDefinition</a>, ... ]</i>,
        "<a href="#markers" title="Markers">Markers</a>" : <i>[ <a href="markersdefinition.md">MarkersDefinition</a>, ... ]</i>,
        "<a href="#ocspconfig" title="OcspConfig">OcspConfig</a>" : <i>[ <a href="ocspconfigdefinition.md">OcspConfigDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AVI::Sslkeyandcertificate
Properties:
    <a href="#certificatebase64" title="CertificateBase64">CertificateBase64</a>: <i>Boolean</i>
    <a href="#certificatemanagementprofileref" title="CertificateManagementProfileRef">CertificateManagementProfileRef</a>: <i>String</i>
    <a href="#createdby" title="CreatedBy">CreatedBy</a>: <i>String</i>
    <a href="#enableocspstapling" title="EnableOcspStapling">EnableOcspStapling</a>: <i>Boolean</i>
    <a href="#enckeybase64" title="EnckeyBase64">EnckeyBase64</a>: <i>String</i>
    <a href="#enckeyname" title="EnckeyName">EnckeyName</a>: <i>String</i>
    <a href="#format" title="Format">Format</a>: <i>String</i>
    <a href="#hardwaresecuritymodulegroupref" title="HardwaresecuritymodulegroupRef">HardwaresecuritymodulegroupRef</a>: <i>String</i>
    <a href="#key" title="Key">Key</a>: <i>String</i>
    <a href="#keybase64" title="KeyBase64">KeyBase64</a>: <i>Boolean</i>
    <a href="#keypassphrase" title="KeyPassphrase">KeyPassphrase</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#status" title="Status">Status</a>: <i>String</i>
    <a href="#tenantref" title="TenantRef">TenantRef</a>: <i>String</i>
    <a href="#type" title="Type">Type</a>: <i>String</i>
    <a href="#uuid" title="Uuid">Uuid</a>: <i>String</i>
    <a href="#cacerts" title="CaCerts">CaCerts</a>: <i>
      - <a href="cacertsdefinition.md">CaCertsDefinition</a></i>
    <a href="#certificate" title="Certificate">Certificate</a>: <i>
      - <a href="certificatedefinition.md">CertificateDefinition</a></i>
    <a href="#dynamicparams" title="DynamicParams">DynamicParams</a>: <i>
      - <a href="dynamicparamsdefinition.md">DynamicParamsDefinition</a></i>
    <a href="#keyparams" title="KeyParams">KeyParams</a>: <i>
      - <a href="keyparamsdefinition.md">KeyParamsDefinition</a></i>
    <a href="#markers" title="Markers">Markers</a>: <i>
      - <a href="markersdefinition.md">MarkersDefinition</a></i>
    <a href="#ocspconfig" title="OcspConfig">OcspConfig</a>: <i>
      - <a href="ocspconfigdefinition.md">OcspConfigDefinition</a></i>
</pre>

## Properties

#### CertificateBase64

States if the certificate is base64 encoded.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CertificateManagementProfileRef

It is a reference to an object of type certificatemanagementprofile.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CreatedBy

Creator name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableOcspStapling

Enables ocsp stapling. Field introduced in 20.1.1. Allowed in basic(allowed values- false) edition, essentials(allowed values- false) edition, enterprise edition.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnckeyBase64

Encrypted private key corresponding to the private key (e.g. Those generated by an hsm such as thales nshield).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnckeyName

Name of the encrypted private key (e.g. Those generated by an hsm such as thales nshield).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Format

Format of the key/certificate file. Enum options - SSL_PEM, SSL_PKCS12.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HardwaresecuritymodulegroupRef

It is a reference to an object of type hardwaresecuritymodulegroup.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Key

Private key.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KeyBase64

States if the private key is base64 encoded.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KeyPassphrase

Passphrase used to encrypt the private key.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Name of the object.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Status

Enum options - ssl_certificate_finished, ssl_certificate_pending.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TenantRef

It is a reference to an object of type tenant.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

Enum options - ssl_certificate_type_virtualservice, ssl_certificate_type_system, ssl_certificate_type_ca.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Uuid

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CaCerts

_Required_: No

_Type_: List of <a href="cacertsdefinition.md">CaCertsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Certificate

_Required_: No

_Type_: List of <a href="certificatedefinition.md">CertificateDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DynamicParams

_Required_: No

_Type_: List of <a href="dynamicparamsdefinition.md">DynamicParamsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KeyParams

_Required_: No

_Type_: List of <a href="keyparamsdefinition.md">KeyParamsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Markers

_Required_: No

_Type_: List of <a href="markersdefinition.md">MarkersDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OcspConfig

_Required_: No

_Type_: List of <a href="ocspconfigdefinition.md">OcspConfigDefinition</a>

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

