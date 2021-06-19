# TF::FortiOS::EndpointcontrolSettings

Configure endpoint control settings.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::FortiOS::EndpointcontrolSettings",
    "Properties" : {
        "<a href="#downloadcustomlink" title="DownloadCustomLink">DownloadCustomLink</a>" : <i>String</i>,
        "<a href="#downloadlocation" title="DownloadLocation">DownloadLocation</a>" : <i>String</i>,
        "<a href="#forticlientavdbupdateinterval" title="ForticlientAvdbUpdateInterval">ForticlientAvdbUpdateInterval</a>" : <i>Double</i>,
        "<a href="#forticlientderegunsupportedclient" title="ForticlientDeregUnsupportedClient">ForticlientDeregUnsupportedClient</a>" : <i>String</i>,
        "<a href="#forticlientdisconnectunsupportedclient" title="ForticlientDisconnectUnsupportedClient">ForticlientDisconnectUnsupportedClient</a>" : <i>String</i>,
        "<a href="#forticlientemsrestapicalltimeout" title="ForticlientEmsRestApiCallTimeout">ForticlientEmsRestApiCallTimeout</a>" : <i>Double</i>,
        "<a href="#forticlientkeepaliveinterval" title="ForticlientKeepaliveInterval">ForticlientKeepaliveInterval</a>" : <i>Double</i>,
        "<a href="#forticlientofflinegrace" title="ForticlientOfflineGrace">ForticlientOfflineGrace</a>" : <i>String</i>,
        "<a href="#forticlientofflinegraceinterval" title="ForticlientOfflineGraceInterval">ForticlientOfflineGraceInterval</a>" : <i>Double</i>,
        "<a href="#forticlientregkey" title="ForticlientRegKey">ForticlientRegKey</a>" : <i>String</i>,
        "<a href="#forticlientregkeyenforce" title="ForticlientRegKeyEnforce">ForticlientRegKeyEnforce</a>" : <i>String</i>,
        "<a href="#forticlientregtimeout" title="ForticlientRegTimeout">ForticlientRegTimeout</a>" : <i>Double</i>,
        "<a href="#forticlientsysupdateinterval" title="ForticlientSysUpdateInterval">ForticlientSysUpdateInterval</a>" : <i>Double</i>,
        "<a href="#forticlientuseravatar" title="ForticlientUserAvatar">ForticlientUserAvatar</a>" : <i>String</i>,
        "<a href="#forticlientwarninginterval" title="ForticlientWarningInterval">ForticlientWarningInterval</a>" : <i>Double</i>,
        "<a href="#vdomparam" title="Vdomparam">Vdomparam</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::FortiOS::EndpointcontrolSettings
Properties:
    <a href="#downloadcustomlink" title="DownloadCustomLink">DownloadCustomLink</a>: <i>String</i>
    <a href="#downloadlocation" title="DownloadLocation">DownloadLocation</a>: <i>String</i>
    <a href="#forticlientavdbupdateinterval" title="ForticlientAvdbUpdateInterval">ForticlientAvdbUpdateInterval</a>: <i>Double</i>
    <a href="#forticlientderegunsupportedclient" title="ForticlientDeregUnsupportedClient">ForticlientDeregUnsupportedClient</a>: <i>String</i>
    <a href="#forticlientdisconnectunsupportedclient" title="ForticlientDisconnectUnsupportedClient">ForticlientDisconnectUnsupportedClient</a>: <i>String</i>
    <a href="#forticlientemsrestapicalltimeout" title="ForticlientEmsRestApiCallTimeout">ForticlientEmsRestApiCallTimeout</a>: <i>Double</i>
    <a href="#forticlientkeepaliveinterval" title="ForticlientKeepaliveInterval">ForticlientKeepaliveInterval</a>: <i>Double</i>
    <a href="#forticlientofflinegrace" title="ForticlientOfflineGrace">ForticlientOfflineGrace</a>: <i>String</i>
    <a href="#forticlientofflinegraceinterval" title="ForticlientOfflineGraceInterval">ForticlientOfflineGraceInterval</a>: <i>Double</i>
    <a href="#forticlientregkey" title="ForticlientRegKey">ForticlientRegKey</a>: <i>String</i>
    <a href="#forticlientregkeyenforce" title="ForticlientRegKeyEnforce">ForticlientRegKeyEnforce</a>: <i>String</i>
    <a href="#forticlientregtimeout" title="ForticlientRegTimeout">ForticlientRegTimeout</a>: <i>Double</i>
    <a href="#forticlientsysupdateinterval" title="ForticlientSysUpdateInterval">ForticlientSysUpdateInterval</a>: <i>Double</i>
    <a href="#forticlientuseravatar" title="ForticlientUserAvatar">ForticlientUserAvatar</a>: <i>String</i>
    <a href="#forticlientwarninginterval" title="ForticlientWarningInterval">ForticlientWarningInterval</a>: <i>Double</i>
    <a href="#vdomparam" title="Vdomparam">Vdomparam</a>: <i>String</i>
</pre>

## Properties

#### DownloadCustomLink

Customized URL for downloading FortiClient.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DownloadLocation

FortiClient download location (FortiGuard or custom). Valid values: `fortiguard`, `custom`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ForticlientAvdbUpdateInterval

Period of time between FortiClient AntiVirus database updates (0 - 24 hours, default = 8).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ForticlientDeregUnsupportedClient

Enable/disable deregistering unsupported FortiClient endpoints. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ForticlientDisconnectUnsupportedClient

Enable/disable disconnecting of unsupported FortiClient endpoints. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ForticlientEmsRestApiCallTimeout

FortiClient EMS call timeout in milliseconds (500 - 30000 milliseconds, default = 5000).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ForticlientKeepaliveInterval

Interval between two KeepAlive messages from FortiClient (20 - 300 sec, default = 60).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ForticlientOfflineGrace

Enable/disable grace period for offline registered clients. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ForticlientOfflineGraceInterval

Grace period for offline registered FortiClient (60 - 600 sec, default = 120).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ForticlientRegKey

FortiClient registration key.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ForticlientRegKeyEnforce

Enable/disable requiring or enforcing FortiClient registration keys. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ForticlientRegTimeout

FortiClient registration license timeout (days, min = 1, max = 180, 0 means unlimited).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ForticlientSysUpdateInterval

Interval between two system update messages from FortiClient (30 - 1440 min, default = 720).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ForticlientUserAvatar

Enable/disable uploading FortiClient user avatars. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ForticlientWarningInterval

Period of time between FortiClient portal warnings (0 - 24 hours, default = 1).

_Required_: No

_Type_: Double

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

