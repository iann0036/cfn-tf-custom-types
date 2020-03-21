# Terraform::Vault::PkiSecretBackendRootSignIntermediate

CloudFormation equivalent of vault_pki_secret_backend_root_sign_intermediate

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
        "<a href="#id" title="Id">Id</a>" : <i>String</i>,
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
    <a href="#id" title="Id">Id</a>: <i>String</i>
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

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Backend

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CommonName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Country

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Csr

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExcludeCnFromSans

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Format

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Id

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpSans

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Locality

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxPathLength

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Organization

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OtherSans

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ou

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PermittedDnsDomains

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PostalCode

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Province

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StreetAddress

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ttl

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UriSans

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UseCsrValues

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

Returns the &lt;code&gt;CaChain&lt;/code&gt; value.

#### Certificate

Returns the &lt;code&gt;Certificate&lt;/code&gt; value.

#### IssuingCa

Returns the &lt;code&gt;IssuingCa&lt;/code&gt; value.

#### Serial

Returns the &lt;code&gt;Serial&lt;/code&gt; value.

