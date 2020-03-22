# Terraform::AzureAD::User

Manages a User within Azure Active Directory.

-> **NOTE:** If you're authenticating using a Service Principal then it must have permissions to `Directory.ReadWrite.All` within the `Windows Azure Active Directory` API.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AzureAD::User",
    "Properties" : {
        "<a href="#accountenabled" title="AccountEnabled">AccountEnabled</a>" : <i>Boolean</i>,
        "<a href="#displayname" title="DisplayName">DisplayName</a>" : <i>String</i>,
        "<a href="#forcepasswordchange" title="ForcePasswordChange">ForcePasswordChange</a>" : <i>Boolean</i>,
        "<a href="#immutableid" title="ImmutableId">ImmutableId</a>" : <i>String</i>,
        "<a href="#mailnickname" title="MailNickname">MailNickname</a>" : <i>String</i>,
        "<a href="#password" title="Password">Password</a>" : <i>String</i>,
        "<a href="#usagelocation" title="UsageLocation">UsageLocation</a>" : <i>String</i>,
        "<a href="#userprincipalname" title="UserPrincipalName">UserPrincipalName</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AzureAD::User
Properties:
    <a href="#accountenabled" title="AccountEnabled">AccountEnabled</a>: <i>Boolean</i>
    <a href="#displayname" title="DisplayName">DisplayName</a>: <i>String</i>
    <a href="#forcepasswordchange" title="ForcePasswordChange">ForcePasswordChange</a>: <i>Boolean</i>
    <a href="#immutableid" title="ImmutableId">ImmutableId</a>: <i>String</i>
    <a href="#mailnickname" title="MailNickname">MailNickname</a>: <i>String</i>
    <a href="#password" title="Password">Password</a>: <i>String</i>
    <a href="#usagelocation" title="UsageLocation">UsageLocation</a>: <i>String</i>
    <a href="#userprincipalname" title="UserPrincipalName">UserPrincipalName</a>: <i>String</i>
</pre>

## Properties

#### AccountEnabled

`true` if the account should be enabled, otherwise `false`. Defaults to `true`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisplayName

The name to display in the address book for the user.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ForcePasswordChange

`true` if the User is forced to change the password during the next sign-in. Defaults to `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ImmutableId

The value used to associate an on-premises Active Directory user account with their Azure AD user object. This must be specified if you are using a federated domain for the user's userPrincipalName (UPN) property when creating a new user account.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MailNickname

The mail alias for the user. Defaults to the user name part of the User Principal Name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Password

The password for the User. The password must satisfy minimum requirements as specified by the password policy. The maximum length is 256 characters.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UsageLocation

The usage location of the User. Required for users that will be assigned licenses due to legal requirement to check for availability of services in countries. The usage location is a two letter country code (ISO standard 3166). Examples include: `NO`, `JP`, and `GB`. Cannot be reset to null once set.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserPrincipalName

The User Principal Name of the Azure AD User.

_Required_: Yes

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

#### Mail

Returns the <code>Mail</code> value.

#### ObjectId

Returns the <code>ObjectId</code> value.

#### OnpremisesSamAccountName

Returns the <code>OnpremisesSamAccountName</code> value.

#### OnpremisesUserPrincipalName

Returns the <code>OnpremisesUserPrincipalName</code> value.

