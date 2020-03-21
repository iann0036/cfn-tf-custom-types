# Terraform::AzureAD::User

CloudFormation equivalent of azuread_user

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

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisplayName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ForcePasswordChange

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ImmutableId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MailNickname

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Password

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UsageLocation

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserPrincipalName

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

#### Mail

Returns the <code>Mail</code> value.

#### ObjectId

Returns the <code>ObjectId</code> value.

#### OnpremisesSamAccountName

Returns the <code>OnpremisesSamAccountName</code> value.

#### OnpremisesUserPrincipalName

Returns the <code>OnpremisesUserPrincipalName</code> value.

