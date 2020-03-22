# Terraform::OCI::IdentityUiPassword

This resource provides the Ui Password resource in Oracle Cloud Infrastructure Identity service.

Creates a new Console one-time password for the specified user. For more information about user
credentials, see [User Credentials](https://docs.cloud.oracle.com/iaas/Content/Identity/Concepts/usercredentials.htm).

Use this operation after creating a new user, or if a user forgets their password. The new one-time
password is returned to you in the response, and you must securely deliver it to the user. They'll
be prompted to change this password the next time they sign in to the Console. If they don't change
it within 7 days, the password will expire and you'll need to create a new one-time password for the
user.

**Note:** The user's Console login is the unique name you specified when you created the user
(see [CreateUser](https://docs.cloud.oracle.com/iaas/api/#/en/identity/20160918/User/CreateUser)).

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::OCI::IdentityUiPassword",
    "Properties" : {
        "<a href="#userid" title="UserId">UserId</a>" : <i>String</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeouts.md">Timeouts</a></i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::OCI::IdentityUiPassword
Properties:
    <a href="#userid" title="UserId">UserId</a>: <i>String</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeouts.md">Timeouts</a></i>
</pre>

## Properties

#### UserId

The OCID of the user.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeouts.md">Timeouts</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the Id.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Id

Returns the <code>Id</code> value.

#### InactiveStatus

Returns the <code>InactiveStatus</code> value.

#### Password

Returns the <code>Password</code> value.

#### State

Returns the <code>State</code> value.

#### TimeCreated

Returns the <code>TimeCreated</code> value.

