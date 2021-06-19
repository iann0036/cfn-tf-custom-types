# TF::ECL::SssUserV1

Manages a V1 user resource within Enterprise Cloud.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::ECL::SssUserV1",
    "Properties" : {
        "<a href="#loginid" title="LoginId">LoginId</a>" : <i>String</i>,
        "<a href="#mailaddress" title="MailAddress">MailAddress</a>" : <i>String</i>,
        "<a href="#notifypassword" title="NotifyPassword">NotifyPassword</a>" : <i>String</i>,
        "<a href="#password" title="Password">Password</a>" : <i>String</i>,
    }
}
</pre>

### YAML

<pre>
Type: TF::ECL::SssUserV1
Properties:
    <a href="#loginid" title="LoginId">LoginId</a>: <i>String</i>
    <a href="#mailaddress" title="MailAddress">MailAddress</a>: <i>String</i>
    <a href="#notifypassword" title="NotifyPassword">NotifyPassword</a>: <i>String</i>
    <a href="#password" title="Password">Password</a>: <i>String</i>
</pre>

## Properties

#### LoginId

Login id of new user.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MailAddress

Mail address of new user.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NotifyPassword

If this flag is set 'true',
notification email will be sent to new user's email address.
Even this parameter is optional, you must specify this in case "Creation".

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Password

Initial password of new user.
If this parameter is not designated,
random initial password is generated and applied to new user.

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

#### BrandId

Returns the <code>BrandId</code> value.

#### ContractId

Returns the <code>ContractId</code> value.

#### ContractOwner

Returns the <code>ContractOwner</code> value.

#### ExternalReferenceId

Returns the <code>ExternalReferenceId</code> value.

#### Id

Returns the <code>Id</code> value.

#### KeystoneEndpoint

Returns the <code>KeystoneEndpoint</code> value.

#### KeystoneName

Returns the <code>KeystoneName</code> value.

#### KeystonePassword

Returns the <code>KeystonePassword</code> value.

#### LoginIntegration

Returns the <code>LoginIntegration</code> value.

#### SssEndpoint

Returns the <code>SssEndpoint</code> value.

#### StartTime

Returns the <code>StartTime</code> value.

#### UserId

Returns the <code>UserId</code> value.

