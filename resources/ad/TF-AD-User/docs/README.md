# TF::AD::User

CloudFormation equivalent of ad_user

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AD::User",
    "Properties" : {
        "<a href="#cannotchangepassword" title="CannotChangePassword">CannotChangePassword</a>" : <i>Boolean</i>,
        "<a href="#city" title="City">City</a>" : <i>String</i>,
        "<a href="#company" title="Company">Company</a>" : <i>String</i>,
        "<a href="#container" title="Container">Container</a>" : <i>String</i>,
        "<a href="#country" title="Country">Country</a>" : <i>String</i>,
        "<a href="#customattributes" title="CustomAttributes">CustomAttributes</a>" : <i>String</i>,
        "<a href="#department" title="Department">Department</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#displayname" title="DisplayName">DisplayName</a>" : <i>String</i>,
        "<a href="#division" title="Division">Division</a>" : <i>String</i>,
        "<a href="#emailaddress" title="EmailAddress">EmailAddress</a>" : <i>String</i>,
        "<a href="#employeeid" title="EmployeeId">EmployeeId</a>" : <i>String</i>,
        "<a href="#employeenumber" title="EmployeeNumber">EmployeeNumber</a>" : <i>String</i>,
        "<a href="#enabled" title="Enabled">Enabled</a>" : <i>Boolean</i>,
        "<a href="#fax" title="Fax">Fax</a>" : <i>String</i>,
        "<a href="#givenname" title="GivenName">GivenName</a>" : <i>String</i>,
        "<a href="#homedirectory" title="HomeDirectory">HomeDirectory</a>" : <i>String</i>,
        "<a href="#homedrive" title="HomeDrive">HomeDrive</a>" : <i>String</i>,
        "<a href="#homepage" title="HomePage">HomePage</a>" : <i>String</i>,
        "<a href="#homephone" title="HomePhone">HomePhone</a>" : <i>String</i>,
        "<a href="#initialpassword" title="InitialPassword">InitialPassword</a>" : <i>String</i>,
        "<a href="#initials" title="Initials">Initials</a>" : <i>String</i>,
        "<a href="#mobilephone" title="MobilePhone">MobilePhone</a>" : <i>String</i>,
        "<a href="#office" title="Office">Office</a>" : <i>String</i>,
        "<a href="#officephone" title="OfficePhone">OfficePhone</a>" : <i>String</i>,
        "<a href="#organization" title="Organization">Organization</a>" : <i>String</i>,
        "<a href="#othername" title="OtherName">OtherName</a>" : <i>String</i>,
        "<a href="#passwordneverexpires" title="PasswordNeverExpires">PasswordNeverExpires</a>" : <i>Boolean</i>,
        "<a href="#pobox" title="PoBox">PoBox</a>" : <i>String</i>,
        "<a href="#postalcode" title="PostalCode">PostalCode</a>" : <i>String</i>,
        "<a href="#principalname" title="PrincipalName">PrincipalName</a>" : <i>String</i>,
        "<a href="#samaccountname" title="SamAccountName">SamAccountName</a>" : <i>String</i>,
        "<a href="#smartcardlogonrequired" title="SmartCardLogonRequired">SmartCardLogonRequired</a>" : <i>Boolean</i>,
        "<a href="#state" title="State">State</a>" : <i>String</i>,
        "<a href="#streetaddress" title="StreetAddress">StreetAddress</a>" : <i>String</i>,
        "<a href="#surname" title="Surname">Surname</a>" : <i>String</i>,
        "<a href="#title" title="Title">Title</a>" : <i>String</i>,
        "<a href="#trustedfordelegation" title="TrustedForDelegation">TrustedForDelegation</a>" : <i>Boolean</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AD::User
Properties:
    <a href="#cannotchangepassword" title="CannotChangePassword">CannotChangePassword</a>: <i>Boolean</i>
    <a href="#city" title="City">City</a>: <i>String</i>
    <a href="#company" title="Company">Company</a>: <i>String</i>
    <a href="#container" title="Container">Container</a>: <i>String</i>
    <a href="#country" title="Country">Country</a>: <i>String</i>
    <a href="#customattributes" title="CustomAttributes">CustomAttributes</a>: <i>String</i>
    <a href="#department" title="Department">Department</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#displayname" title="DisplayName">DisplayName</a>: <i>String</i>
    <a href="#division" title="Division">Division</a>: <i>String</i>
    <a href="#emailaddress" title="EmailAddress">EmailAddress</a>: <i>String</i>
    <a href="#employeeid" title="EmployeeId">EmployeeId</a>: <i>String</i>
    <a href="#employeenumber" title="EmployeeNumber">EmployeeNumber</a>: <i>String</i>
    <a href="#enabled" title="Enabled">Enabled</a>: <i>Boolean</i>
    <a href="#fax" title="Fax">Fax</a>: <i>String</i>
    <a href="#givenname" title="GivenName">GivenName</a>: <i>String</i>
    <a href="#homedirectory" title="HomeDirectory">HomeDirectory</a>: <i>String</i>
    <a href="#homedrive" title="HomeDrive">HomeDrive</a>: <i>String</i>
    <a href="#homepage" title="HomePage">HomePage</a>: <i>String</i>
    <a href="#homephone" title="HomePhone">HomePhone</a>: <i>String</i>
    <a href="#initialpassword" title="InitialPassword">InitialPassword</a>: <i>String</i>
    <a href="#initials" title="Initials">Initials</a>: <i>String</i>
    <a href="#mobilephone" title="MobilePhone">MobilePhone</a>: <i>String</i>
    <a href="#office" title="Office">Office</a>: <i>String</i>
    <a href="#officephone" title="OfficePhone">OfficePhone</a>: <i>String</i>
    <a href="#organization" title="Organization">Organization</a>: <i>String</i>
    <a href="#othername" title="OtherName">OtherName</a>: <i>String</i>
    <a href="#passwordneverexpires" title="PasswordNeverExpires">PasswordNeverExpires</a>: <i>Boolean</i>
    <a href="#pobox" title="PoBox">PoBox</a>: <i>String</i>
    <a href="#postalcode" title="PostalCode">PostalCode</a>: <i>String</i>
    <a href="#principalname" title="PrincipalName">PrincipalName</a>: <i>String</i>
    <a href="#samaccountname" title="SamAccountName">SamAccountName</a>: <i>String</i>
    <a href="#smartcardlogonrequired" title="SmartCardLogonRequired">SmartCardLogonRequired</a>: <i>Boolean</i>
    <a href="#state" title="State">State</a>: <i>String</i>
    <a href="#streetaddress" title="StreetAddress">StreetAddress</a>: <i>String</i>
    <a href="#surname" title="Surname">Surname</a>: <i>String</i>
    <a href="#title" title="Title">Title</a>: <i>String</i>
    <a href="#trustedfordelegation" title="TrustedForDelegation">TrustedForDelegation</a>: <i>Boolean</i>
</pre>

## Properties

#### CannotChangePassword

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### City

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Company

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Container

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Country

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CustomAttributes

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Department

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisplayName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Division

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EmailAddress

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EmployeeId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EmployeeNumber

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Enabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Fax

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GivenName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HomeDirectory

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HomeDrive

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HomePage

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HomePhone

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InitialPassword

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Initials

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MobilePhone

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Office

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OfficePhone

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Organization

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OtherName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PasswordNeverExpires

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PoBox

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PostalCode

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrincipalName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SamAccountName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SmartCardLogonRequired

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### State

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StreetAddress

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Surname

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Title

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TrustedForDelegation

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

#### Sid

Returns the <code>Sid</code> value.

