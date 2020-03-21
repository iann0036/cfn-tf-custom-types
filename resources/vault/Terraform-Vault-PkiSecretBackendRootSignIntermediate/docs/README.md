# Terraform::Vault::PkiSecretBackendRootSignIntermediate

Creates an PKI certificate.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Vault::PkiSecretBackendRootSignIntermediate",
    "Properties" : {
        "<a href="#altnames" title="AltNames">AltNames</a>" : <i>[ String, ... ]</i>,
        "<a href="#backend" title="Backend">Backend</a>" : <i>String</i>,
        "<a href="#commonname" title="CommonName">CommonName</a>" : <i>String</i>,
        "<a href="#country" title="Country">Country</a>" : <i>String</i>,
        "<a href="#csr" title="Csr">Csr</a>" : <i>String</i>,
        "<a href="#excludecnfromsans" title="ExcludeCnFromSans">ExcludeCnFromSans</a>" : <i>Boolean</i>,
        "<a href="#format" title="Format">Format</a>" : <i>String</i>,
        "<a href="#ipsans" title="IpSans">IpSans</a>" : <i>[ String, ... ]</i>,
        "<a href="#locality" title="Locality">Locality</a>" : <i>String</i>,
        "<a href="#maxpathlength" title="MaxPathLength">MaxPathLength</a>" : <i>Double</i>,
        "<a href="#organization" title="Organization">Organization</a>" : <i>String</i>,
        "<a href="#othersans" title="OtherSans">OtherSans</a>" : <i>[ String, ... ]</i>,
        "<a href="#ou" title="Ou">Ou</a>" : <i>String</i>,
        "<a href="#permitteddnsdomains" title="PermittedDnsDomains">PermittedDnsDomains</a>" : <i>[ String, ... ]</i>,
        "<a href="#postalcode" title="PostalCode">PostalCode</a>" : <i>String</i>,
        "<a href="#province" title="Province">Province</a>" : <i>String</i>,
        "<a href="#streetaddress" title="StreetAddress">StreetAddress</a>" : <i>String</i>,
        "<a href="#ttl" title="Ttl">Ttl</a>" : <i>String</i>,
        "<a href="#urisans" title="UriSans">UriSans</a>" : <i>[ String, ... ]</i>,
        "<a href="#usecsrvalues" title="UseCsrValues">UseCsrValues</a>" : <i>Boolean</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Vault::PkiSecretBackendRootSignIntermediate
Properties:
    <a href="#altnames" title="AltNames">AltNames</a>: <i>
      - String</i>
    <a href="#backend" title="Backend">Backend</a>: <i>String</i>
    <a href="#commonname" title="CommonName">CommonName</a>: <i>String</i>
    <a href="#country" title="Country">Country</a>: <i>String</i>
    <a href="#csr" title="Csr">Csr</a>: <i>String</i>
    <a href="#excludecnfromsans" title="ExcludeCnFromSans">ExcludeCnFromSans</a>: <i>Boolean</i>
    <a href="#format" title="Format">Format</a>: <i>String</i>
    <a href="#ipsans" title="IpSans">IpSans</a>: <i>
      - String</i>
    <a href="#locality" title="Locality">Locality</a>: <i>String</i>
    <a href="#maxpathlength" title="MaxPathLength">MaxPathLength</a>: <i>Double</i>
    <a href="#organization" title="Organization">Organization</a>: <i>String</i>
    <a href="#othersans" title="OtherSans">OtherSans</a>: <i>
      - String</i>
    <a href="#ou" title="Ou">Ou</a>: <i>String</i>
    <a href="#permitteddnsdomains" title="PermittedDnsDomains">PermittedDnsDomains</a>: <i>
      - String</i>
    <a href="#postalcode" title="PostalCode">PostalCode</a>: <i>String</i>
    <a href="#province" title="Province">Province</a>: <i>String</i>
    <a href="#streetaddress" title="StreetAddress">StreetAddress</a>: <i>String</i>
    <a href="#ttl" title="Ttl">Ttl</a>: <i>String</i>
    <a href="#urisans" title="UriSans">UriSans</a>: <i>
      - String</i>
    <a href="#usecsrvalues" title="UseCsrValues">UseCsrValues</a>: <i>Boolean</i>
</pre>

## Properties

#### AltNames

List of alternative names.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Backend

The PKI secret backend the resource belongs to.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CommonName

CN of intermediate to create.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Country

The country.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Csr

The CSR.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExcludeCnFromSans

Flag to exclude CN from SANs.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Format

The format of data.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpSans

List of alternative IPs.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Locality

The locality.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxPathLength

The maximum path length to encode in the generated certificate.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Organization

The organization.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OtherSans

List of other SANs.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ou

The organization unit.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PermittedDnsDomains

List of domains for which certificates are allowed to be issued.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PostalCode

The postal code.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Province

The province.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StreetAddress

The street address.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ttl

Time to live.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UriSans

List of alternative URIs.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UseCsrValues

Preserve CSR values.

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

#### CaChain

Returns the <code>CaChain</code> value.

#### Certificate

Returns the <code>Certificate</code> value.

#### IssuingCa

Returns the <code>IssuingCa</code> value.

#### Serial

Returns the <code>Serial</code> value.

