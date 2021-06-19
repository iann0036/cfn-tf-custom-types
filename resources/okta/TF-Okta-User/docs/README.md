# TF::Okta::User

Creates an Okta User.

This resource allows you to create and configure an Okta User.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Okta::User",
    "Properties" : {
        "<a href="#adminroles" title="AdminRoles">AdminRoles</a>" : <i>[ String, ... ]</i>,
        "<a href="#city" title="City">City</a>" : <i>String</i>,
        "<a href="#costcenter" title="CostCenter">CostCenter</a>" : <i>String</i>,
        "<a href="#countrycode" title="CountryCode">CountryCode</a>" : <i>String</i>,
        "<a href="#customprofileattributes" title="CustomProfileAttributes">CustomProfileAttributes</a>" : <i>String</i>,
        "<a href="#department" title="Department">Department</a>" : <i>String</i>,
        "<a href="#displayname" title="DisplayName">DisplayName</a>" : <i>String</i>,
        "<a href="#division" title="Division">Division</a>" : <i>String</i>,
        "<a href="#email" title="Email">Email</a>" : <i>String</i>,
        "<a href="#employeenumber" title="EmployeeNumber">EmployeeNumber</a>" : <i>String</i>,
        "<a href="#firstname" title="FirstName">FirstName</a>" : <i>String</i>,
        "<a href="#groupmemberships" title="GroupMemberships">GroupMemberships</a>" : <i>[ String, ... ]</i>,
        "<a href="#honorificprefix" title="HonorificPrefix">HonorificPrefix</a>" : <i>String</i>,
        "<a href="#honorificsuffix" title="HonorificSuffix">HonorificSuffix</a>" : <i>String</i>,
        "<a href="#lastname" title="LastName">LastName</a>" : <i>String</i>,
        "<a href="#locale" title="Locale">Locale</a>" : <i>String</i>,
        "<a href="#login" title="Login">Login</a>" : <i>String</i>,
        "<a href="#manager" title="Manager">Manager</a>" : <i>String</i>,
        "<a href="#managerid" title="ManagerId">ManagerId</a>" : <i>String</i>,
        "<a href="#middlename" title="MiddleName">MiddleName</a>" : <i>String</i>,
        "<a href="#mobilephone" title="MobilePhone">MobilePhone</a>" : <i>String</i>,
        "<a href="#nickname" title="NickName">NickName</a>" : <i>String</i>,
        "<a href="#organization" title="Organization">Organization</a>" : <i>String</i>,
        "<a href="#password" title="Password">Password</a>" : <i>String</i>,
        "<a href="#postaladdress" title="PostalAddress">PostalAddress</a>" : <i>String</i>,
        "<a href="#preferredlanguage" title="PreferredLanguage">PreferredLanguage</a>" : <i>String</i>,
        "<a href="#primaryphone" title="PrimaryPhone">PrimaryPhone</a>" : <i>String</i>,
        "<a href="#profileurl" title="ProfileUrl">ProfileUrl</a>" : <i>String</i>,
        "<a href="#recoveryanswer" title="RecoveryAnswer">RecoveryAnswer</a>" : <i>String</i>,
        "<a href="#recoveryquestion" title="RecoveryQuestion">RecoveryQuestion</a>" : <i>String</i>,
        "<a href="#secondemail" title="SecondEmail">SecondEmail</a>" : <i>String</i>,
        "<a href="#state" title="State">State</a>" : <i>String</i>,
        "<a href="#status" title="Status">Status</a>" : <i>String</i>,
        "<a href="#streetaddress" title="StreetAddress">StreetAddress</a>" : <i>String</i>,
        "<a href="#timezone" title="Timezone">Timezone</a>" : <i>String</i>,
        "<a href="#title" title="Title">Title</a>" : <i>String</i>,
        "<a href="#usertype" title="UserType">UserType</a>" : <i>String</i>,
        "<a href="#zipcode" title="ZipCode">ZipCode</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Okta::User
Properties:
    <a href="#adminroles" title="AdminRoles">AdminRoles</a>: <i>
      - String</i>
    <a href="#city" title="City">City</a>: <i>String</i>
    <a href="#costcenter" title="CostCenter">CostCenter</a>: <i>String</i>
    <a href="#countrycode" title="CountryCode">CountryCode</a>: <i>String</i>
    <a href="#customprofileattributes" title="CustomProfileAttributes">CustomProfileAttributes</a>: <i>String</i>
    <a href="#department" title="Department">Department</a>: <i>String</i>
    <a href="#displayname" title="DisplayName">DisplayName</a>: <i>String</i>
    <a href="#division" title="Division">Division</a>: <i>String</i>
    <a href="#email" title="Email">Email</a>: <i>String</i>
    <a href="#employeenumber" title="EmployeeNumber">EmployeeNumber</a>: <i>String</i>
    <a href="#firstname" title="FirstName">FirstName</a>: <i>String</i>
    <a href="#groupmemberships" title="GroupMemberships">GroupMemberships</a>: <i>
      - String</i>
    <a href="#honorificprefix" title="HonorificPrefix">HonorificPrefix</a>: <i>String</i>
    <a href="#honorificsuffix" title="HonorificSuffix">HonorificSuffix</a>: <i>String</i>
    <a href="#lastname" title="LastName">LastName</a>: <i>String</i>
    <a href="#locale" title="Locale">Locale</a>: <i>String</i>
    <a href="#login" title="Login">Login</a>: <i>String</i>
    <a href="#manager" title="Manager">Manager</a>: <i>String</i>
    <a href="#managerid" title="ManagerId">ManagerId</a>: <i>String</i>
    <a href="#middlename" title="MiddleName">MiddleName</a>: <i>String</i>
    <a href="#mobilephone" title="MobilePhone">MobilePhone</a>: <i>String</i>
    <a href="#nickname" title="NickName">NickName</a>: <i>String</i>
    <a href="#organization" title="Organization">Organization</a>: <i>String</i>
    <a href="#password" title="Password">Password</a>: <i>String</i>
    <a href="#postaladdress" title="PostalAddress">PostalAddress</a>: <i>String</i>
    <a href="#preferredlanguage" title="PreferredLanguage">PreferredLanguage</a>: <i>String</i>
    <a href="#primaryphone" title="PrimaryPhone">PrimaryPhone</a>: <i>String</i>
    <a href="#profileurl" title="ProfileUrl">ProfileUrl</a>: <i>String</i>
    <a href="#recoveryanswer" title="RecoveryAnswer">RecoveryAnswer</a>: <i>String</i>
    <a href="#recoveryquestion" title="RecoveryQuestion">RecoveryQuestion</a>: <i>String</i>
    <a href="#secondemail" title="SecondEmail">SecondEmail</a>: <i>String</i>
    <a href="#state" title="State">State</a>: <i>String</i>
    <a href="#status" title="Status">Status</a>: <i>String</i>
    <a href="#streetaddress" title="StreetAddress">StreetAddress</a>: <i>String</i>
    <a href="#timezone" title="Timezone">Timezone</a>: <i>String</i>
    <a href="#title" title="Title">Title</a>: <i>String</i>
    <a href="#usertype" title="UserType">UserType</a>: <i>String</i>
    <a href="#zipcode" title="ZipCode">ZipCode</a>: <i>String</i>
</pre>

## Properties

#### AdminRoles

Administrator roles assigned to User.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### City

User profile property.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CostCenter

User profile property.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CountryCode

User profile property.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CustomProfileAttributes

raw JSON containing all custom profile attributes.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Department

User profile property.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisplayName

User profile property.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Division

User profile property.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Email

User profile property.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EmployeeNumber

User profile property.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FirstName

User's First Name, required by default.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GroupMemberships

User profile property.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HonorificPrefix

User profile property.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HonorificSuffix

User profile property.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LastName

User's Last Name, required by default.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Locale

User profile property.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Login

User profile property.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Manager

User profile property.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ManagerId

User profile property.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MiddleName

User profile property.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MobilePhone

User profile property.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NickName

User profile property.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Organization

User profile property.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Password

User password.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PostalAddress

User profile property.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PreferredLanguage

User profile property.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrimaryPhone

User profile property.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProfileUrl

User profile property.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RecoveryAnswer

User password recovery answer.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RecoveryQuestion

User password recovery question.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecondEmail

User profile property.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### State

User profile property.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Status

User profile property.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StreetAddress

User profile property.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timezone

User profile property.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Title

User profile property.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserType

User profile property.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ZipCode

User profile property.

_Required_: No

_Type_: String

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

#### RawStatus

Returns the <code>RawStatus</code> value.

