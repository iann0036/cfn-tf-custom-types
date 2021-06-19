# TF::FortiOS::Wirelesscontrollerhotspot20Anqpnairealm AuthParamDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#id" title="Id">Id</a>" : <i>String</i>,
    "<a href="#index" title="Index">Index</a>" : <i>Double</i>,
    "<a href="#val" title="Val">Val</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#id" title="Id">Id</a>: <i>String</i>
<a href="#index" title="Index">Index</a>: <i>Double</i>
<a href="#val" title="Val">Val</a>: <i>String</i>
</pre>

## Properties

#### Id

ID of authentication parameter. Valid values: `non-eap-inner-auth`, `inner-auth-eap`, `credential`, `tunneled-credential`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Index

Param index.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Val

Value of authentication parameter. Valid values: `eap-identity`, `eap-md5`, `eap-tls`, `eap-ttls`, `eap-peap`, `eap-sim`, `eap-aka`, `eap-aka-prime`, `non-eap-pap`, `non-eap-chap`, `non-eap-mschap`, `non-eap-mschapv2`, `cred-sim`, `cred-usim`, `cred-nfc`, `cred-hardware-token`, `cred-softoken`, `cred-certificate`, `cred-user-pwd`, `cred-none`, `cred-vendor-specific`, `tun-cred-sim`, `tun-cred-usim`, `tun-cred-nfc`, `tun-cred-hardware-token`, `tun-cred-softoken`, `tun-cred-certificate`, `tun-cred-user-pwd`, `tun-cred-anonymous`, `tun-cred-vendor-specific`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

