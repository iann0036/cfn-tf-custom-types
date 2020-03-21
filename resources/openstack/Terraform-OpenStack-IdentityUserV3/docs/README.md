# Terraform::OpenStack::IdentityUserV3

Manages a V3 User resource within OpenStack Keystone.

Note: You _must_ have admin privileges in your OpenStack cloud to use
this resource.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::OpenStack::IdentityUserV3",
    "Properties" : {
        "<a href="#defaultprojectid" title="DefaultProjectId">DefaultProjectId</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#domainid" title="DomainId">DomainId</a>" : <i>String</i>,
        "<a href="#enabled" title="Enabled">Enabled</a>" : <i>Boolean</i>,
        "<a href="#extra" title="Extra">Extra</a>" : <i>[ <a href="extra.md">Extra</a>, ... ]</i>,
        "<a href="#ignorechangepassworduponfirstuse" title="IgnoreChangePasswordUponFirstUse">IgnoreChangePasswordUponFirstUse</a>" : <i>Boolean</i>,
        "<a href="#ignorelockoutfailureattempts" title="IgnoreLockoutFailureAttempts">IgnoreLockoutFailureAttempts</a>" : <i>Boolean</i>,
        "<a href="#ignorepasswordexpiry" title="IgnorePasswordExpiry">IgnorePasswordExpiry</a>" : <i>Boolean</i>,
        "<a href="#multifactorauthenabled" title="MultiFactorAuthEnabled">MultiFactorAuthEnabled</a>" : <i>Boolean</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#password" title="Password">Password</a>" : <i>String</i>,
        "<a href="#region" title="Region">Region</a>" : <i>String</i>,
        "<a href="#multifactorauthrule" title="MultiFactorAuthRule">MultiFactorAuthRule</a>" : <i>[ <a href="multifactorauthrule.md">MultiFactorAuthRule</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::OpenStack::IdentityUserV3
Properties:
    <a href="#defaultprojectid" title="DefaultProjectId">DefaultProjectId</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#domainid" title="DomainId">DomainId</a>: <i>String</i>
    <a href="#enabled" title="Enabled">Enabled</a>: <i>Boolean</i>
    <a href="#extra" title="Extra">Extra</a>: <i>
      - <a href="extra.md">Extra</a></i>
    <a href="#ignorechangepassworduponfirstuse" title="IgnoreChangePasswordUponFirstUse">IgnoreChangePasswordUponFirstUse</a>: <i>Boolean</i>
    <a href="#ignorelockoutfailureattempts" title="IgnoreLockoutFailureAttempts">IgnoreLockoutFailureAttempts</a>: <i>Boolean</i>
    <a href="#ignorepasswordexpiry" title="IgnorePasswordExpiry">IgnorePasswordExpiry</a>: <i>Boolean</i>
    <a href="#multifactorauthenabled" title="MultiFactorAuthEnabled">MultiFactorAuthEnabled</a>: <i>Boolean</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#password" title="Password">Password</a>: <i>String</i>
    <a href="#region" title="Region">Region</a>: <i>String</i>
    <a href="#multifactorauthrule" title="MultiFactorAuthRule">MultiFactorAuthRule</a>: <i>
      - <a href="multifactorauthrule.md">MultiFactorAuthRule</a></i>
</pre>

## Properties

#### DefaultProjectId

The default project this user belongs to.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

A description of the user.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DomainId

The domain this user belongs to.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Enabled

Whether the user is enabled or disabled. Valid
values are `true` and `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Extra

Free-form key/value pairs of extra information.

_Required_: No

_Type_: List of <a href="extra.md">Extra</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IgnoreChangePasswordUponFirstUse

User will not have to
change their password upon first use. Valid values are `true` and `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IgnoreLockoutFailureAttempts

User will not have a failure
lockout placed on their account. Valid values are `true` and `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IgnorePasswordExpiry

User's password will not expire.
Valid values are `true` and `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MultiFactorAuthEnabled

Whether to enable multi-factor
authentication. Valid values are `true` and `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the user.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Password

The password for the user.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Region

The region in which to obtain the V3 Keystone client.
If omitted, the `region` argument of the provider is used. Changing this
creates a new User.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MultiFactorAuthRule

_Required_: No

_Type_: List of <a href="multifactorauthrule.md">MultiFactorAuthRule</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

