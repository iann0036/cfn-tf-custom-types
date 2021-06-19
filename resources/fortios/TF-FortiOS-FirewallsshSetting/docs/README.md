# TF::FortiOS::FirewallsshSetting

SSH proxy settings.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::FortiOS::FirewallsshSetting",
    "Properties" : {
        "<a href="#caname" title="Caname">Caname</a>" : <i>String</i>,
        "<a href="#hosttrustedchecking" title="HostTrustedChecking">HostTrustedChecking</a>" : <i>String</i>,
        "<a href="#hostkeydsa1024" title="HostkeyDsa1024">HostkeyDsa1024</a>" : <i>String</i>,
        "<a href="#hostkeyecdsa256" title="HostkeyEcdsa256">HostkeyEcdsa256</a>" : <i>String</i>,
        "<a href="#hostkeyecdsa384" title="HostkeyEcdsa384">HostkeyEcdsa384</a>" : <i>String</i>,
        "<a href="#hostkeyecdsa521" title="HostkeyEcdsa521">HostkeyEcdsa521</a>" : <i>String</i>,
        "<a href="#hostkeyed25519" title="HostkeyEd25519">HostkeyEd25519</a>" : <i>String</i>,
        "<a href="#hostkeyrsa2048" title="HostkeyRsa2048">HostkeyRsa2048</a>" : <i>String</i>,
        "<a href="#untrustedcaname" title="UntrustedCaname">UntrustedCaname</a>" : <i>String</i>,
        "<a href="#vdomparam" title="Vdomparam">Vdomparam</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::FortiOS::FirewallsshSetting
Properties:
    <a href="#caname" title="Caname">Caname</a>: <i>String</i>
    <a href="#hosttrustedchecking" title="HostTrustedChecking">HostTrustedChecking</a>: <i>String</i>
    <a href="#hostkeydsa1024" title="HostkeyDsa1024">HostkeyDsa1024</a>: <i>String</i>
    <a href="#hostkeyecdsa256" title="HostkeyEcdsa256">HostkeyEcdsa256</a>: <i>String</i>
    <a href="#hostkeyecdsa384" title="HostkeyEcdsa384">HostkeyEcdsa384</a>: <i>String</i>
    <a href="#hostkeyecdsa521" title="HostkeyEcdsa521">HostkeyEcdsa521</a>: <i>String</i>
    <a href="#hostkeyed25519" title="HostkeyEd25519">HostkeyEd25519</a>: <i>String</i>
    <a href="#hostkeyrsa2048" title="HostkeyRsa2048">HostkeyRsa2048</a>: <i>String</i>
    <a href="#untrustedcaname" title="UntrustedCaname">UntrustedCaname</a>: <i>String</i>
    <a href="#vdomparam" title="Vdomparam">Vdomparam</a>: <i>String</i>
</pre>

## Properties

#### Caname

CA certificate used by SSH Inspection.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HostTrustedChecking

Enable/disable host trusted checking. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HostkeyDsa1024

DSA certificate used by SSH proxy.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HostkeyEcdsa256

ECDSA nid256 certificate used by SSH proxy.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HostkeyEcdsa384

ECDSA nid384 certificate used by SSH proxy.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HostkeyEcdsa521

ECDSA nid384 certificate used by SSH proxy.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HostkeyEd25519

ED25519 hostkey used by SSH proxy.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HostkeyRsa2048

RSA certificate used by SSH proxy.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UntrustedCaname

Untrusted CA certificate used by SSH Inspection.

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

