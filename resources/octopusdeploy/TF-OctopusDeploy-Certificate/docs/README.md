# TF::OctopusDeploy::Certificate

CloudFormation equivalent of octopusdeploy_certificate

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::OctopusDeploy::Certificate",
    "Properties" : {
        "<a href="#archived" title="Archived">Archived</a>" : <i>String</i>,
        "<a href="#certificatedata" title="CertificateData">CertificateData</a>" : <i>String</i>,
        "<a href="#certificatedataformat" title="CertificateDataFormat">CertificateDataFormat</a>" : <i>String</i>,
        "<a href="#environments" title="Environments">Environments</a>" : <i>[ String, ... ]</i>,
        "<a href="#hasprivatekey" title="HasPrivateKey">HasPrivateKey</a>" : <i>Boolean</i>,
        "<a href="#isexpired" title="IsExpired">IsExpired</a>" : <i>Boolean</i>,
        "<a href="#issuercommonname" title="IssuerCommonName">IssuerCommonName</a>" : <i>String</i>,
        "<a href="#issuerdistinguishedname" title="IssuerDistinguishedName">IssuerDistinguishedName</a>" : <i>String</i>,
        "<a href="#issuerorganization" title="IssuerOrganization">IssuerOrganization</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#notafter" title="NotAfter">NotAfter</a>" : <i>String</i>,
        "<a href="#notbefore" title="NotBefore">NotBefore</a>" : <i>String</i>,
        "<a href="#notes" title="Notes">Notes</a>" : <i>String</i>,
        "<a href="#password" title="Password">Password</a>" : <i>String</i>,
        "<a href="#replacedby" title="ReplacedBy">ReplacedBy</a>" : <i>String</i>,
        "<a href="#selfsigned" title="SelfSigned">SelfSigned</a>" : <i>Boolean</i>,
        "<a href="#serialnumber" title="SerialNumber">SerialNumber</a>" : <i>String</i>,
        "<a href="#signaturealgorithmname" title="SignatureAlgorithmName">SignatureAlgorithmName</a>" : <i>String</i>,
        "<a href="#subjectalternativenames" title="SubjectAlternativeNames">SubjectAlternativeNames</a>" : <i>[ String, ... ]</i>,
        "<a href="#subjectcommonname" title="SubjectCommonName">SubjectCommonName</a>" : <i>String</i>,
        "<a href="#subjectdistinguishedname" title="SubjectDistinguishedName">SubjectDistinguishedName</a>" : <i>String</i>,
        "<a href="#subjectorganization" title="SubjectOrganization">SubjectOrganization</a>" : <i>String</i>,
        "<a href="#tenanttags" title="TenantTags">TenantTags</a>" : <i>[ String, ... ]</i>,
        "<a href="#tenanteddeploymentparticipation" title="TenantedDeploymentParticipation">TenantedDeploymentParticipation</a>" : <i>String</i>,
        "<a href="#tenants" title="Tenants">Tenants</a>" : <i>[ String, ... ]</i>,
        "<a href="#thumbprint" title="Thumbprint">Thumbprint</a>" : <i>String</i>,
        "<a href="#version" title="Version">Version</a>" : <i>Double</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::OctopusDeploy::Certificate
Properties:
    <a href="#archived" title="Archived">Archived</a>: <i>String</i>
    <a href="#certificatedata" title="CertificateData">CertificateData</a>: <i>String</i>
    <a href="#certificatedataformat" title="CertificateDataFormat">CertificateDataFormat</a>: <i>String</i>
    <a href="#environments" title="Environments">Environments</a>: <i>
      - String</i>
    <a href="#hasprivatekey" title="HasPrivateKey">HasPrivateKey</a>: <i>Boolean</i>
    <a href="#isexpired" title="IsExpired">IsExpired</a>: <i>Boolean</i>
    <a href="#issuercommonname" title="IssuerCommonName">IssuerCommonName</a>: <i>String</i>
    <a href="#issuerdistinguishedname" title="IssuerDistinguishedName">IssuerDistinguishedName</a>: <i>String</i>
    <a href="#issuerorganization" title="IssuerOrganization">IssuerOrganization</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#notafter" title="NotAfter">NotAfter</a>: <i>String</i>
    <a href="#notbefore" title="NotBefore">NotBefore</a>: <i>String</i>
    <a href="#notes" title="Notes">Notes</a>: <i>String</i>
    <a href="#password" title="Password">Password</a>: <i>String</i>
    <a href="#replacedby" title="ReplacedBy">ReplacedBy</a>: <i>String</i>
    <a href="#selfsigned" title="SelfSigned">SelfSigned</a>: <i>Boolean</i>
    <a href="#serialnumber" title="SerialNumber">SerialNumber</a>: <i>String</i>
    <a href="#signaturealgorithmname" title="SignatureAlgorithmName">SignatureAlgorithmName</a>: <i>String</i>
    <a href="#subjectalternativenames" title="SubjectAlternativeNames">SubjectAlternativeNames</a>: <i>
      - String</i>
    <a href="#subjectcommonname" title="SubjectCommonName">SubjectCommonName</a>: <i>String</i>
    <a href="#subjectdistinguishedname" title="SubjectDistinguishedName">SubjectDistinguishedName</a>: <i>String</i>
    <a href="#subjectorganization" title="SubjectOrganization">SubjectOrganization</a>: <i>String</i>
    <a href="#tenanttags" title="TenantTags">TenantTags</a>: <i>
      - String</i>
    <a href="#tenanteddeploymentparticipation" title="TenantedDeploymentParticipation">TenantedDeploymentParticipation</a>: <i>String</i>
    <a href="#tenants" title="Tenants">Tenants</a>: <i>
      - String</i>
    <a href="#thumbprint" title="Thumbprint">Thumbprint</a>: <i>String</i>
    <a href="#version" title="Version">Version</a>: <i>Double</i>
</pre>

## Properties

#### Archived

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CertificateData

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CertificateDataFormat

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Environments

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HasPrivateKey

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsExpired

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IssuerCommonName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IssuerDistinguishedName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IssuerOrganization

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NotAfter

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NotBefore

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Notes

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Password

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReplacedBy

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SelfSigned

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SerialNumber

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SignatureAlgorithmName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SubjectAlternativeNames

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SubjectCommonName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SubjectDistinguishedName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SubjectOrganization

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TenantTags

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TenantedDeploymentParticipation

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tenants

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Thumbprint

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Version

_Required_: No

_Type_: Double

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

