# Terraform::Vault::PkiSecretBackendRole

Creates a role on an PKI Secret Backend for Vault.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Vault::PkiSecretBackendRole",
    "Properties" : {
        "<a href="#allowanyname" title="AllowAnyName">AllowAnyName</a>" : <i>Boolean</i>,
        "<a href="#allowbaredomains" title="AllowBareDomains">AllowBareDomains</a>" : <i>Boolean</i>,
        "<a href="#allowglobdomains" title="AllowGlobDomains">AllowGlobDomains</a>" : <i>Boolean</i>,
        "<a href="#allowipsans" title="AllowIpSans">AllowIpSans</a>" : <i>Boolean</i>,
        "<a href="#allowlocalhost" title="AllowLocalhost">AllowLocalhost</a>" : <i>Boolean</i>,
        "<a href="#allowsubdomains" title="AllowSubdomains">AllowSubdomains</a>" : <i>Boolean</i>,
        "<a href="#alloweddomains" title="AllowedDomains">AllowedDomains</a>" : <i>[ String, ... ]</i>,
        "<a href="#allowedothersans" title="AllowedOtherSans">AllowedOtherSans</a>" : <i>[ String, ... ]</i>,
        "<a href="#allowedurisans" title="AllowedUriSans">AllowedUriSans</a>" : <i>[ String, ... ]</i>,
        "<a href="#backend" title="Backend">Backend</a>" : <i>String</i>,
        "<a href="#basicconstraintsvalidfornonca" title="BasicConstraintsValidForNonCa">BasicConstraintsValidForNonCa</a>" : <i>Boolean</i>,
        "<a href="#clientflag" title="ClientFlag">ClientFlag</a>" : <i>Boolean</i>,
        "<a href="#codesigningflag" title="CodeSigningFlag">CodeSigningFlag</a>" : <i>Boolean</i>,
        "<a href="#country" title="Country">Country</a>" : <i>[ String, ... ]</i>,
        "<a href="#emailprotectionflag" title="EmailProtectionFlag">EmailProtectionFlag</a>" : <i>Boolean</i>,
        "<a href="#enforcehostnames" title="EnforceHostnames">EnforceHostnames</a>" : <i>Boolean</i>,
        "<a href="#extkeyusage" title="ExtKeyUsage">ExtKeyUsage</a>" : <i>[ String, ... ]</i>,
        "<a href="#generatelease" title="GenerateLease">GenerateLease</a>" : <i>Boolean</i>,
        "<a href="#keybits" title="KeyBits">KeyBits</a>" : <i>Double</i>,
        "<a href="#keytype" title="KeyType">KeyType</a>" : <i>String</i>,
        "<a href="#keyusage" title="KeyUsage">KeyUsage</a>" : <i>[ String, ... ]</i>,
        "<a href="#locality" title="Locality">Locality</a>" : <i>[ String, ... ]</i>,
        "<a href="#maxttl" title="MaxTtl">MaxTtl</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#nostore" title="NoStore">NoStore</a>" : <i>Boolean</i>,
        "<a href="#notbeforeduration" title="NotBeforeDuration">NotBeforeDuration</a>" : <i>String</i>,
        "<a href="#organization" title="Organization">Organization</a>" : <i>[ String, ... ]</i>,
        "<a href="#ou" title="Ou">Ou</a>" : <i>[ String, ... ]</i>,
        "<a href="#policyidentifiers" title="PolicyIdentifiers">PolicyIdentifiers</a>" : <i>[ String, ... ]</i>,
        "<a href="#postalcode" title="PostalCode">PostalCode</a>" : <i>[ String, ... ]</i>,
        "<a href="#province" title="Province">Province</a>" : <i>[ String, ... ]</i>,
        "<a href="#requirecn" title="RequireCn">RequireCn</a>" : <i>Boolean</i>,
        "<a href="#serverflag" title="ServerFlag">ServerFlag</a>" : <i>Boolean</i>,
        "<a href="#streetaddress" title="StreetAddress">StreetAddress</a>" : <i>[ String, ... ]</i>,
        "<a href="#ttl" title="Ttl">Ttl</a>" : <i>String</i>,
        "<a href="#usecsrcommonname" title="UseCsrCommonName">UseCsrCommonName</a>" : <i>Boolean</i>,
        "<a href="#usecsrsans" title="UseCsrSans">UseCsrSans</a>" : <i>Boolean</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Vault::PkiSecretBackendRole
Properties:
    <a href="#allowanyname" title="AllowAnyName">AllowAnyName</a>: <i>Boolean</i>
    <a href="#allowbaredomains" title="AllowBareDomains">AllowBareDomains</a>: <i>Boolean</i>
    <a href="#allowglobdomains" title="AllowGlobDomains">AllowGlobDomains</a>: <i>Boolean</i>
    <a href="#allowipsans" title="AllowIpSans">AllowIpSans</a>: <i>Boolean</i>
    <a href="#allowlocalhost" title="AllowLocalhost">AllowLocalhost</a>: <i>Boolean</i>
    <a href="#allowsubdomains" title="AllowSubdomains">AllowSubdomains</a>: <i>Boolean</i>
    <a href="#alloweddomains" title="AllowedDomains">AllowedDomains</a>: <i>
      - String</i>
    <a href="#allowedothersans" title="AllowedOtherSans">AllowedOtherSans</a>: <i>
      - String</i>
    <a href="#allowedurisans" title="AllowedUriSans">AllowedUriSans</a>: <i>
      - String</i>
    <a href="#backend" title="Backend">Backend</a>: <i>String</i>
    <a href="#basicconstraintsvalidfornonca" title="BasicConstraintsValidForNonCa">BasicConstraintsValidForNonCa</a>: <i>Boolean</i>
    <a href="#clientflag" title="ClientFlag">ClientFlag</a>: <i>Boolean</i>
    <a href="#codesigningflag" title="CodeSigningFlag">CodeSigningFlag</a>: <i>Boolean</i>
    <a href="#country" title="Country">Country</a>: <i>
      - String</i>
    <a href="#emailprotectionflag" title="EmailProtectionFlag">EmailProtectionFlag</a>: <i>Boolean</i>
    <a href="#enforcehostnames" title="EnforceHostnames">EnforceHostnames</a>: <i>Boolean</i>
    <a href="#extkeyusage" title="ExtKeyUsage">ExtKeyUsage</a>: <i>
      - String</i>
    <a href="#generatelease" title="GenerateLease">GenerateLease</a>: <i>Boolean</i>
    <a href="#keybits" title="KeyBits">KeyBits</a>: <i>Double</i>
    <a href="#keytype" title="KeyType">KeyType</a>: <i>String</i>
    <a href="#keyusage" title="KeyUsage">KeyUsage</a>: <i>
      - String</i>
    <a href="#locality" title="Locality">Locality</a>: <i>
      - String</i>
    <a href="#maxttl" title="MaxTtl">MaxTtl</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#nostore" title="NoStore">NoStore</a>: <i>Boolean</i>
    <a href="#notbeforeduration" title="NotBeforeDuration">NotBeforeDuration</a>: <i>String</i>
    <a href="#organization" title="Organization">Organization</a>: <i>
      - String</i>
    <a href="#ou" title="Ou">Ou</a>: <i>
      - String</i>
    <a href="#policyidentifiers" title="PolicyIdentifiers">PolicyIdentifiers</a>: <i>
      - String</i>
    <a href="#postalcode" title="PostalCode">PostalCode</a>: <i>
      - String</i>
    <a href="#province" title="Province">Province</a>: <i>
      - String</i>
    <a href="#requirecn" title="RequireCn">RequireCn</a>: <i>Boolean</i>
    <a href="#serverflag" title="ServerFlag">ServerFlag</a>: <i>Boolean</i>
    <a href="#streetaddress" title="StreetAddress">StreetAddress</a>: <i>
      - String</i>
    <a href="#ttl" title="Ttl">Ttl</a>: <i>String</i>
    <a href="#usecsrcommonname" title="UseCsrCommonName">UseCsrCommonName</a>: <i>Boolean</i>
    <a href="#usecsrsans" title="UseCsrSans">UseCsrSans</a>: <i>Boolean</i>
</pre>

## Properties

#### AllowAnyName

Flag to allow any name.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AllowBareDomains

Flag to allow certificates matching the actual domain.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AllowGlobDomains

Flag to allow names containing glob patterns.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AllowIpSans

Flag to allow IP SANs.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AllowLocalhost

Flag to allow certificates for localhost.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AllowSubdomains

Flag to allow certificates matching subdomains.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AllowedDomains

List of allowed domains for certificates.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AllowedOtherSans

Defines allowed custom SANs.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AllowedUriSans

Defines allowed URI SANs.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Backend

The path the PKI secret backend is mounted at, with no leading or trailing `/`s.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BasicConstraintsValidForNonCa

Flag to mark basic constraints valid when issuing non-CA certificates.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClientFlag

Flag to specify certificates for client use.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CodeSigningFlag

Flag to specify certificates for code signing use.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Country

The country of generated certificates.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EmailProtectionFlag

Flag to specify certificates for email protection use.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnforceHostnames

Flag to allow only valid host names.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExtKeyUsage

Specify the allowed extended key usage constraint on issued certificates.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GenerateLease

Flag to generate leases with certificates.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KeyBits

The number of bits of generated keys.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KeyType

The type of generated keys.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KeyUsage

Specify the allowed key usage constraint on issued certificates.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Locality

The locality of generated certificates.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxTtl

The maximum TTL.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name to identify this role within the backend. Must be unique within the backend.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NoStore

Flag to not store certificates in the storage backend.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NotBeforeDuration

Specifies the duration by which to backdate the NotBefore property.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Organization

The organization of generated certificates.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ou

The organization unit of generated certificates.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PolicyIdentifiers

Specify the list of allowed policies IODs.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PostalCode

The postal code of generated certificates.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Province

The province of generated certificates.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RequireCn

Flag to force CN usage.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServerFlag

Flag to specify certificates for server use.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StreetAddress

The street address of generated certificates.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ttl

The TTL.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UseCsrCommonName

Flag to use the CN in the CSR.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UseCsrSans

Flag to use the SANs in the CSR.

_Required_: No

_Type_: Boolean

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

