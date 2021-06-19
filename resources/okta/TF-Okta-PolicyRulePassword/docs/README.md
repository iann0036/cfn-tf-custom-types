# TF::Okta::PolicyRulePassword

Creates a Password Policy Rule.

This resource allows you to create and configure a Password Policy Rule.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Okta::PolicyRulePassword",
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
Type: TF::Okta::PolicyRulePassword
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

Policy Rule Name.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetworkConnection

Network selection mode: `"ANYWHERE"`, `"ZONE"`, `"ON_NETWORK"`, or `"OFF_NETWORK"`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetworkExcludes

The network zones to exclude. Conflicts with `network_includes`.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetworkIncludes

The network zones to include. Conflicts with `network_excludes`.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PasswordChange

Allow or deny a user to change their password: `"ALLOW"` or `"DENY"`. By default, it is `"ALLOW"`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PasswordReset

Allow or deny a user to reset their password: `"ALLOW"` or `"DENY"`. By default, it is `"ALLOW"`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PasswordUnlock

Allow or deny a user to unlock: `"ALLOW"` or `"DENY"`. By default, it is `"DENY"`,.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Policyid

Policy ID.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Priority

Policy Rule Priority, this attribute can be set to a valid priority. To avoid endless diff situation we error if an invalid priority is provided. API defaults it to the last (lowest) if not there.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Status

Policy Rule Status: `"ACTIVE"` or `"INACTIVE"`.

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

