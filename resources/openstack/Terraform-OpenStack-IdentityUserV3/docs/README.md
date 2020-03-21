# Terraform::OpenStack::IdentityUserV3

CloudFormation equivalent of openstack_identity_user_v3

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::OpenStack::IdentityUserV3",
    "Properties" : {
        "<a href="#tfcfnid" title="tfcfnid">tfcfnid</a>" : <i>String</i>,
        "<a href="#defaultprojectid" title="DefaultProjectId">DefaultProjectId</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#domainid" title="DomainId">DomainId</a>" : <i>String</i>,
        "<a href="#enabled" title="Enabled">Enabled</a>" : <i>Boolean</i>,
        "<a href="#extra" title="Extra">Extra</a>" : <i>[ &lt;a href=&#34;extra.md&#34;&gt;Extra&lt;/a&gt;, ... ]</i>,
        "<a href="#ignorechangepassworduponfirstuse" title="IgnoreChangePasswordUponFirstUse">IgnoreChangePasswordUponFirstUse</a>" : <i>Boolean</i>,
        "<a href="#ignorelockoutfailureattempts" title="IgnoreLockoutFailureAttempts">IgnoreLockoutFailureAttempts</a>" : <i>Boolean</i>,
        "<a href="#ignorepasswordexpiry" title="IgnorePasswordExpiry">IgnorePasswordExpiry</a>" : <i>Boolean</i>,
        "<a href="#multifactorauthenabled" title="MultiFactorAuthEnabled">MultiFactorAuthEnabled</a>" : <i>Boolean</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#password" title="Password">Password</a>" : <i>String</i>,
        "<a href="#region" title="Region">Region</a>" : <i>String</i>,
        "<a href="#multifactorauthrule" title="MultiFactorAuthRule">MultiFactorAuthRule</a>" : <i>[ &lt;a href=&#34;multifactorauthrule.md&#34;&gt;MultiFactorAuthRule&lt;/a&gt;, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::OpenStack::IdentityUserV3
Properties:
    <a href="#tfcfnid" title="tfcfnid">tfcfnid</a>: <i>String</i>
    <a href="#defaultprojectid" title="DefaultProjectId">DefaultProjectId</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#domainid" title="DomainId">DomainId</a>: <i>String</i>
    <a href="#enabled" title="Enabled">Enabled</a>: <i>Boolean</i>
    <a href="#extra" title="Extra">Extra</a>: <i>
      - &lt;a href=&#34;extra.md&#34;&gt;Extra&lt;/a&gt;</i>
    <a href="#ignorechangepassworduponfirstuse" title="IgnoreChangePasswordUponFirstUse">IgnoreChangePasswordUponFirstUse</a>: <i>Boolean</i>
    <a href="#ignorelockoutfailureattempts" title="IgnoreLockoutFailureAttempts">IgnoreLockoutFailureAttempts</a>: <i>Boolean</i>
    <a href="#ignorepasswordexpiry" title="IgnorePasswordExpiry">IgnorePasswordExpiry</a>: <i>Boolean</i>
    <a href="#multifactorauthenabled" title="MultiFactorAuthEnabled">MultiFactorAuthEnabled</a>: <i>Boolean</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#password" title="Password">Password</a>: <i>String</i>
    <a href="#region" title="Region">Region</a>: <i>String</i>
    <a href="#multifactorauthrule" title="MultiFactorAuthRule">MultiFactorAuthRule</a>: <i>
      - &lt;a href=&#34;multifactorauthrule.md&#34;&gt;MultiFactorAuthRule&lt;/a&gt;</i>
</pre>

## Properties

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefaultProjectId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DomainId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Enabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Extra

_Required_: No

_Type_: List of &lt;a href=&#34;extra.md&#34;&gt;Extra&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IgnoreChangePasswordUponFirstUse

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IgnoreLockoutFailureAttempts

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IgnorePasswordExpiry

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MultiFactorAuthEnabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Password

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Region

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MultiFactorAuthRule

_Required_: No

_Type_: List of &lt;a href=&#34;multifactorauthrule.md&#34;&gt;MultiFactorAuthRule&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

