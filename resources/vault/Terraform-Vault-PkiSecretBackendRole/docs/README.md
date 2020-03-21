# Terraform::Vault::PkiSecretBackendRole

CloudFormation equivalent of vault_pki_secret_backend_role

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

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AllowBareDomains

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AllowGlobDomains

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AllowIpSans

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AllowLocalhost

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AllowSubdomains

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AllowedDomains

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AllowedOtherSans

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AllowedUriSans

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Backend

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BasicConstraintsValidForNonCa

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClientFlag

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CodeSigningFlag

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Country

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EmailProtectionFlag

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnforceHostnames

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExtKeyUsage

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GenerateLease

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KeyBits

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KeyType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KeyUsage

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Locality

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxTtl

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NoStore

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NotBeforeDuration

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Organization

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ou

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PolicyIdentifiers

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PostalCode

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Province

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RequireCn

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServerFlag

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StreetAddress

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ttl

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UseCsrCommonName

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UseCsrSans

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

