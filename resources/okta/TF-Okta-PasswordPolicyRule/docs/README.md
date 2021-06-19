# TF::Okta::PasswordPolicyRule

CloudFormation equivalent of okta_password_policy_rule

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Okta::PasswordPolicyRule",
    "Properties" : {
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#networkconnection" title="NetworkConnection">NetworkConnection</a>" : <i>String</i>,
        "<a href="#networkexcludes" title="NetworkExcludes">NetworkExcludes</a>" : <i>[ String, ... ]</i>,
        "<a href="#networkincludes" title="NetworkIncludes">NetworkIncludes</a>" : <i>[ String, ... ]</i>,
        "<a href="#passwordchange" title="PasswordChange">PasswordChange</a>" : <i>String</i>,
        "<a href="#passwordreset" title="PasswordReset">PasswordReset</a>" : <i>String</i>,
        "<a href="#passwordunlock" title="PasswordUnlock">PasswordUnlock</a>" : <i>String</i>,
        "<a href="#policyid" title="Policyid">Policyid</a>" : <i>String</i>,
        "<a href="#priority" title="Priority">Priority</a>" : <i>Double</i>,
        "<a href="#status" title="Status">Status</a>" : <i>String</i>,
        "<a href="#usersexcluded" title="UsersExcluded">UsersExcluded</a>" : <i>[ String, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Okta::PasswordPolicyRule
Properties:
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#networkconnection" title="NetworkConnection">NetworkConnection</a>: <i>String</i>
    <a href="#networkexcludes" title="NetworkExcludes">NetworkExcludes</a>: <i>
      - String</i>
    <a href="#networkincludes" title="NetworkIncludes">NetworkIncludes</a>: <i>
      - String</i>
    <a href="#passwordchange" title="PasswordChange">PasswordChange</a>: <i>String</i>
    <a href="#passwordreset" title="PasswordReset">PasswordReset</a>: <i>String</i>
    <a href="#passwordunlock" title="PasswordUnlock">PasswordUnlock</a>: <i>String</i>
    <a href="#policyid" title="Policyid">Policyid</a>: <i>String</i>
    <a href="#priority" title="Priority">Priority</a>: <i>Double</i>
    <a href="#status" title="Status">Status</a>: <i>String</i>
    <a href="#usersexcluded" title="UsersExcluded">UsersExcluded</a>: <i>
      - String</i>
</pre>

## Properties

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetworkConnection

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetworkExcludes

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetworkIncludes

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PasswordChange

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PasswordReset

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PasswordUnlock

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Policyid

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Priority

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Status

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UsersExcluded

_Required_: No

_Type_: List of String

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

