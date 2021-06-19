# TF::FortiOS::SystemManagementtunnel

Management tunnel configuration.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::FortiOS::SystemManagementtunnel",
    "Properties" : {
        "<a href="#allowcollectstatistics" title="AllowCollectStatistics">AllowCollectStatistics</a>" : <i>String</i>,
        "<a href="#allowconfigrestore" title="AllowConfigRestore">AllowConfigRestore</a>" : <i>String</i>,
        "<a href="#allowpushconfiguration" title="AllowPushConfiguration">AllowPushConfiguration</a>" : <i>String</i>,
        "<a href="#allowpushfirmware" title="AllowPushFirmware">AllowPushFirmware</a>" : <i>String</i>,
        "<a href="#authorizedmanageronly" title="AuthorizedManagerOnly">AuthorizedManagerOnly</a>" : <i>String</i>,
        "<a href="#serialnumber" title="SerialNumber">SerialNumber</a>" : <i>String</i>,
        "<a href="#status" title="Status">Status</a>" : <i>String</i>,
        "<a href="#vdomparam" title="Vdomparam">Vdomparam</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::FortiOS::SystemManagementtunnel
Properties:
    <a href="#allowcollectstatistics" title="AllowCollectStatistics">AllowCollectStatistics</a>: <i>String</i>
    <a href="#allowconfigrestore" title="AllowConfigRestore">AllowConfigRestore</a>: <i>String</i>
    <a href="#allowpushconfiguration" title="AllowPushConfiguration">AllowPushConfiguration</a>: <i>String</i>
    <a href="#allowpushfirmware" title="AllowPushFirmware">AllowPushFirmware</a>: <i>String</i>
    <a href="#authorizedmanageronly" title="AuthorizedManagerOnly">AuthorizedManagerOnly</a>: <i>String</i>
    <a href="#serialnumber" title="SerialNumber">SerialNumber</a>: <i>String</i>
    <a href="#status" title="Status">Status</a>: <i>String</i>
    <a href="#vdomparam" title="Vdomparam">Vdomparam</a>: <i>String</i>
</pre>

## Properties

#### AllowCollectStatistics

Enable/disable collection of run time statistics. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AllowConfigRestore

Enable/disable allow config restore. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AllowPushConfiguration

Enable/disable push configuration. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AllowPushFirmware

Enable/disable push firmware. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AuthorizedManagerOnly

Enable/disable restriction of authorized manager only. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SerialNumber

Serial number.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Status

Enable/disable FGFM tunnel. Valid values: `enable`, `disable`.

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

