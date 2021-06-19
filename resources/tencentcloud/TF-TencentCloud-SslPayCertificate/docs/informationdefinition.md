# TF::TencentCloud::SslPayCertificate InformationDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#adminemail" title="AdminEmail">AdminEmail</a>" : <i>String</i>,
    "<a href="#adminfirstname" title="AdminFirstName">AdminFirstName</a>" : <i>String</i>,
    "<a href="#adminlastname" title="AdminLastName">AdminLastName</a>" : <i>String</i>,
    "<a href="#adminphonenum" title="AdminPhoneNum">AdminPhoneNum</a>" : <i>String</i>,
    "<a href="#adminposition" title="AdminPosition">AdminPosition</a>" : <i>String</i>,
    "<a href="#certificatedomain" title="CertificateDomain">CertificateDomain</a>" : <i>String</i>,
    "<a href="#contactemail" title="ContactEmail">ContactEmail</a>" : <i>String</i>,
    "<a href="#contactfirstname" title="ContactFirstName">ContactFirstName</a>" : <i>String</i>,
    "<a href="#contactlastname" title="ContactLastName">ContactLastName</a>" : <i>String</i>,
    "<a href="#contactnumber" title="ContactNumber">ContactNumber</a>" : <i>String</i>,
    "<a href="#contactposition" title="ContactPosition">ContactPosition</a>" : <i>String</i>,
    "<a href="#csrcontent" title="CsrContent">CsrContent</a>" : <i>String</i>,
    "<a href="#csrtype" title="CsrType">CsrType</a>" : <i>String</i>,
    "<a href="#domainlist" title="DomainList">DomainList</a>" : <i>[ String, ... ]</i>,
    "<a href="#keypassword" title="KeyPassword">KeyPassword</a>" : <i>String</i>,
    "<a href="#organizationaddress" title="OrganizationAddress">OrganizationAddress</a>" : <i>String</i>,
    "<a href="#organizationcity" title="OrganizationCity">OrganizationCity</a>" : <i>String</i>,
    "<a href="#organizationcountry" title="OrganizationCountry">OrganizationCountry</a>" : <i>String</i>,
    "<a href="#organizationdivision" title="OrganizationDivision">OrganizationDivision</a>" : <i>String</i>,
    "<a href="#organizationname" title="OrganizationName">OrganizationName</a>" : <i>String</i>,
    "<a href="#organizationregion" title="OrganizationRegion">OrganizationRegion</a>" : <i>String</i>,
    "<a href="#phoneareacode" title="PhoneAreaCode">PhoneAreaCode</a>" : <i>String</i>,
    "<a href="#phonenumber" title="PhoneNumber">PhoneNumber</a>" : <i>String</i>,
    "<a href="#postalcode" title="PostalCode">PostalCode</a>" : <i>String</i>,
    "<a href="#verifytype" title="VerifyType">VerifyType</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#adminemail" title="AdminEmail">AdminEmail</a>: <i>String</i>
<a href="#adminfirstname" title="AdminFirstName">AdminFirstName</a>: <i>String</i>
<a href="#adminlastname" title="AdminLastName">AdminLastName</a>: <i>String</i>
<a href="#adminphonenum" title="AdminPhoneNum">AdminPhoneNum</a>: <i>String</i>
<a href="#adminposition" title="AdminPosition">AdminPosition</a>: <i>String</i>
<a href="#certificatedomain" title="CertificateDomain">CertificateDomain</a>: <i>String</i>
<a href="#contactemail" title="ContactEmail">ContactEmail</a>: <i>String</i>
<a href="#contactfirstname" title="ContactFirstName">ContactFirstName</a>: <i>String</i>
<a href="#contactlastname" title="ContactLastName">ContactLastName</a>: <i>String</i>
<a href="#contactnumber" title="ContactNumber">ContactNumber</a>: <i>String</i>
<a href="#contactposition" title="ContactPosition">ContactPosition</a>: <i>String</i>
<a href="#csrcontent" title="CsrContent">CsrContent</a>: <i>String</i>
<a href="#csrtype" title="CsrType">CsrType</a>: <i>String</i>
<a href="#domainlist" title="DomainList">DomainList</a>: <i>
      - String</i>
<a href="#keypassword" title="KeyPassword">KeyPassword</a>: <i>String</i>
<a href="#organizationaddress" title="OrganizationAddress">OrganizationAddress</a>: <i>String</i>
<a href="#organizationcity" title="OrganizationCity">OrganizationCity</a>: <i>String</i>
<a href="#organizationcountry" title="OrganizationCountry">OrganizationCountry</a>: <i>String</i>
<a href="#organizationdivision" title="OrganizationDivision">OrganizationDivision</a>: <i>String</i>
<a href="#organizationname" title="OrganizationName">OrganizationName</a>: <i>String</i>
<a href="#organizationregion" title="OrganizationRegion">OrganizationRegion</a>: <i>String</i>
<a href="#phoneareacode" title="PhoneAreaCode">PhoneAreaCode</a>: <i>String</i>
<a href="#phonenumber" title="PhoneNumber">PhoneNumber</a>: <i>String</i>
<a href="#postalcode" title="PostalCode">PostalCode</a>: <i>String</i>
<a href="#verifytype" title="VerifyType">VerifyType</a>: <i>String</i>
</pre>

## Properties

#### AdminEmail

The administrator's email address.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AdminFirstName

The first name of the administrator.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AdminLastName

The last name of the administrator.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AdminPhoneNum

Manager mobile phone number.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AdminPosition

Manager position.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CertificateDomain

Domain name for binding certificate.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ContactEmail

Contact email address.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ContactFirstName

Contact first name.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ContactLastName

Contact last name.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ContactNumber

Contact phone number.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ContactPosition

Contact position.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CsrContent

CSR content uploaded.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CsrType

CSR generation method. Valid values: `online`, `parse`. `online` means online generation, `parse` means manual upload.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DomainList

Array of uploaded domain names, multi-domain certificates can be uploaded.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KeyPassword

Private key password.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OrganizationAddress

Company address.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OrganizationCity

Company city.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OrganizationCountry

Country name, such as China: CN.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OrganizationDivision

Department name.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OrganizationName

Company name.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OrganizationRegion

The province where the company is located.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PhoneAreaCode

Company landline area code.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PhoneNumber

Company landline number.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PostalCode

Company postal code.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VerifyType

Certificate verification method. Valid values: `DNS_AUTO`, `DNS`, `FILE`. `DNS_AUTO` means automatic DNS verification, this verification type is only supported for domain names resolved by Tencent Cloud and the resolution status is normal, `DNS` means manual DNS verification, `FILE` means file verification.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

