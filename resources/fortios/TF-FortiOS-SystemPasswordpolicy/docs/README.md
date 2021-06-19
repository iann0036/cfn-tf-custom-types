# TF::FortiOS::SystemPasswordpolicy

Configure password policy for locally defined administrator passwords and IPsec VPN pre-shared keys.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::FortiOS::SystemPasswordpolicy",
    "Properties" : {
        "<a href="#applyto" title="ApplyTo">ApplyTo</a>" : <i>String</i>,
        "<a href="#change4characters" title="Change4Characters">Change4Characters</a>" : <i>String</i>,
        "<a href="#expireday" title="ExpireDay">ExpireDay</a>" : <i>Double</i>,
        "<a href="#expirestatus" title="ExpireStatus">ExpireStatus</a>" : <i>String</i>,
        "<a href="#minlowercaseletter" title="MinLowerCaseLetter">MinLowerCaseLetter</a>" : <i>Double</i>,
        "<a href="#minnonalphanumeric" title="MinNonAlphanumeric">MinNonAlphanumeric</a>" : <i>Double</i>,
        "<a href="#minnumber" title="MinNumber">MinNumber</a>" : <i>Double</i>,
        "<a href="#minuppercaseletter" title="MinUpperCaseLetter">MinUpperCaseLetter</a>" : <i>Double</i>,
        "<a href="#minimumlength" title="MinimumLength">MinimumLength</a>" : <i>Double</i>,
        "<a href="#reusepassword" title="ReusePassword">ReusePassword</a>" : <i>String</i>,
        "<a href="#status" title="Status">Status</a>" : <i>String</i>,
        "<a href="#vdomparam" title="Vdomparam">Vdomparam</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::FortiOS::SystemPasswordpolicy
Properties:
    <a href="#applyto" title="ApplyTo">ApplyTo</a>: <i>String</i>
    <a href="#change4characters" title="Change4Characters">Change4Characters</a>: <i>String</i>
    <a href="#expireday" title="ExpireDay">ExpireDay</a>: <i>Double</i>
    <a href="#expirestatus" title="ExpireStatus">ExpireStatus</a>: <i>String</i>
    <a href="#minlowercaseletter" title="MinLowerCaseLetter">MinLowerCaseLetter</a>: <i>Double</i>
    <a href="#minnonalphanumeric" title="MinNonAlphanumeric">MinNonAlphanumeric</a>: <i>Double</i>
    <a href="#minnumber" title="MinNumber">MinNumber</a>: <i>Double</i>
    <a href="#minuppercaseletter" title="MinUpperCaseLetter">MinUpperCaseLetter</a>: <i>Double</i>
    <a href="#minimumlength" title="MinimumLength">MinimumLength</a>: <i>Double</i>
    <a href="#reusepassword" title="ReusePassword">ReusePassword</a>: <i>String</i>
    <a href="#status" title="Status">Status</a>: <i>String</i>
    <a href="#vdomparam" title="Vdomparam">Vdomparam</a>: <i>String</i>
</pre>

## Properties

#### ApplyTo

Apply password policy to administrator passwords or IPsec pre-shared keys or both. Separate entries with a space. Valid values: `admin-password`, `ipsec-preshared-key`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Change4Characters

Enable/disable changing at least 4 characters for a new password (This attribute overrides reuse-password if both are enabled). Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExpireDay

Number of days after which passwords expire (1 - 999 days, default = 90).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExpireStatus

Enable/disable password expiration. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MinLowerCaseLetter

Minimum number of lowercase characters in password (0 - 128, default = 0).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MinNonAlphanumeric

Minimum number of non-alphanumeric characters in password (0 - 128, default = 0).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MinNumber

Minimum number of numeric characters in password (0 - 128, default = 0).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MinUpperCaseLetter

Minimum number of uppercase characters in password (0 - 128, default = 0).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MinimumLength

Minimum password length (8 - 128, default = 8).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReusePassword

Enable/disable reusing of password (if both reuse-password and change-4-characters are enabled, change-4-characters overrides). Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Status

Enable/disable setting a password policy for locally defined administrator passwords and IPsec VPN pre-shared keys. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vdomparam

Specifies the vdom to which the resource will be applied when the FortiGate unit is running in VDOM mode. Only one vdom can be specified. If you want to inherit the vdom configuration of the provider, please do not set this parameter.

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

