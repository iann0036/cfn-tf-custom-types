# TF::FortiOS::ExtendercontrollerExtender

Extender controller configuration.

-> The resource applies to FortiOS Version < 6.4.2. For FortiOS Version >= 6.4.2, see `fortios_extendercontroller_extender1`.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::FortiOS::ExtendercontrollerExtender",
    "Properties" : {
        "<a href="#aaasharedsecret" title="AaaSharedSecret">AaaSharedSecret</a>" : <i>String</i>,
        "<a href="#accesspointname" title="AccessPointName">AccessPointName</a>" : <i>String</i>,
        "<a href="#admin" title="Admin">Admin</a>" : <i>String</i>,
        "<a href="#atdialscript" title="AtDialScript">AtDialScript</a>" : <i>String</i>,
        "<a href="#billingstartday" title="BillingStartDay">BillingStartDay</a>" : <i>Double</i>,
        "<a href="#cdmaaaaspi" title="CdmaAaaSpi">CdmaAaaSpi</a>" : <i>String</i>,
        "<a href="#cdmahaspi" title="CdmaHaSpi">CdmaHaSpi</a>" : <i>String</i>,
        "<a href="#cdmanai" title="CdmaNai">CdmaNai</a>" : <i>String</i>,
        "<a href="#connstatus" title="ConnStatus">ConnStatus</a>" : <i>Double</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#dialmode" title="DialMode">DialMode</a>" : <i>String</i>,
        "<a href="#dialstatus" title="DialStatus">DialStatus</a>" : <i>Double</i>,
        "<a href="#extname" title="ExtName">ExtName</a>" : <i>String</i>,
        "<a href="#fosid" title="Fosid">Fosid</a>" : <i>String</i>,
        "<a href="#hasharedsecret" title="HaSharedSecret">HaSharedSecret</a>" : <i>String</i>,
        "<a href="#ifname" title="Ifname">Ifname</a>" : <i>String</i>,
        "<a href="#initiatedupdate" title="InitiatedUpdate">InitiatedUpdate</a>" : <i>String</i>,
        "<a href="#mode" title="Mode">Mode</a>" : <i>String</i>,
        "<a href="#modempasswd" title="ModemPasswd">ModemPasswd</a>" : <i>String</i>,
        "<a href="#modemtype" title="ModemType">ModemType</a>" : <i>String</i>,
        "<a href="#multimode" title="MultiMode">MultiMode</a>" : <i>String</i>,
        "<a href="#pppauthprotocol" title="PppAuthProtocol">PppAuthProtocol</a>" : <i>String</i>,
        "<a href="#pppechorequest" title="PppEchoRequest">PppEchoRequest</a>" : <i>String</i>,
        "<a href="#ppppassword" title="PppPassword">PppPassword</a>" : <i>String</i>,
        "<a href="#pppusername" title="PppUsername">PppUsername</a>" : <i>String</i>,
        "<a href="#primaryha" title="PrimaryHa">PrimaryHa</a>" : <i>String</i>,
        "<a href="#quotalimitmb" title="QuotaLimitMb">QuotaLimitMb</a>" : <i>Double</i>,
        "<a href="#redial" title="Redial">Redial</a>" : <i>String</i>,
        "<a href="#redundantintf" title="RedundantIntf">RedundantIntf</a>" : <i>String</i>,
        "<a href="#roaming" title="Roaming">Roaming</a>" : <i>String</i>,
        "<a href="#role" title="Role">Role</a>" : <i>String</i>,
        "<a href="#secondaryha" title="SecondaryHa">SecondaryHa</a>" : <i>String</i>,
        "<a href="#simpin" title="SimPin">SimPin</a>" : <i>String</i>,
        "<a href="#vdom" title="Vdom">Vdom</a>" : <i>Double</i>,
        "<a href="#vdomparam" title="Vdomparam">Vdomparam</a>" : <i>String</i>,
        "<a href="#wimaxauthprotocol" title="WimaxAuthProtocol">WimaxAuthProtocol</a>" : <i>String</i>,
        "<a href="#wimaxcarrier" title="WimaxCarrier">WimaxCarrier</a>" : <i>String</i>,
        "<a href="#wimaxrealm" title="WimaxRealm">WimaxRealm</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::FortiOS::ExtendercontrollerExtender
Properties:
    <a href="#aaasharedsecret" title="AaaSharedSecret">AaaSharedSecret</a>: <i>String</i>
    <a href="#accesspointname" title="AccessPointName">AccessPointName</a>: <i>String</i>
    <a href="#admin" title="Admin">Admin</a>: <i>String</i>
    <a href="#atdialscript" title="AtDialScript">AtDialScript</a>: <i>String</i>
    <a href="#billingstartday" title="BillingStartDay">BillingStartDay</a>: <i>Double</i>
    <a href="#cdmaaaaspi" title="CdmaAaaSpi">CdmaAaaSpi</a>: <i>String</i>
    <a href="#cdmahaspi" title="CdmaHaSpi">CdmaHaSpi</a>: <i>String</i>
    <a href="#cdmanai" title="CdmaNai">CdmaNai</a>: <i>String</i>
    <a href="#connstatus" title="ConnStatus">ConnStatus</a>: <i>Double</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#dialmode" title="DialMode">DialMode</a>: <i>String</i>
    <a href="#dialstatus" title="DialStatus">DialStatus</a>: <i>Double</i>
    <a href="#extname" title="ExtName">ExtName</a>: <i>String</i>
    <a href="#fosid" title="Fosid">Fosid</a>: <i>String</i>
    <a href="#hasharedsecret" title="HaSharedSecret">HaSharedSecret</a>: <i>String</i>
    <a href="#ifname" title="Ifname">Ifname</a>: <i>String</i>
    <a href="#initiatedupdate" title="InitiatedUpdate">InitiatedUpdate</a>: <i>String</i>
    <a href="#mode" title="Mode">Mode</a>: <i>String</i>
    <a href="#modempasswd" title="ModemPasswd">ModemPasswd</a>: <i>String</i>
    <a href="#modemtype" title="ModemType">ModemType</a>: <i>String</i>
    <a href="#multimode" title="MultiMode">MultiMode</a>: <i>String</i>
    <a href="#pppauthprotocol" title="PppAuthProtocol">PppAuthProtocol</a>: <i>String</i>
    <a href="#pppechorequest" title="PppEchoRequest">PppEchoRequest</a>: <i>String</i>
    <a href="#ppppassword" title="PppPassword">PppPassword</a>: <i>String</i>
    <a href="#pppusername" title="PppUsername">PppUsername</a>: <i>String</i>
    <a href="#primaryha" title="PrimaryHa">PrimaryHa</a>: <i>String</i>
    <a href="#quotalimitmb" title="QuotaLimitMb">QuotaLimitMb</a>: <i>Double</i>
    <a href="#redial" title="Redial">Redial</a>: <i>String</i>
    <a href="#redundantintf" title="RedundantIntf">RedundantIntf</a>: <i>String</i>
    <a href="#roaming" title="Roaming">Roaming</a>: <i>String</i>
    <a href="#role" title="Role">Role</a>: <i>String</i>
    <a href="#secondaryha" title="SecondaryHa">SecondaryHa</a>: <i>String</i>
    <a href="#simpin" title="SimPin">SimPin</a>: <i>String</i>
    <a href="#vdom" title="Vdom">Vdom</a>: <i>Double</i>
    <a href="#vdomparam" title="Vdomparam">Vdomparam</a>: <i>String</i>
    <a href="#wimaxauthprotocol" title="WimaxAuthProtocol">WimaxAuthProtocol</a>: <i>String</i>
    <a href="#wimaxcarrier" title="WimaxCarrier">WimaxCarrier</a>: <i>String</i>
    <a href="#wimaxrealm" title="WimaxRealm">WimaxRealm</a>: <i>String</i>
</pre>

## Properties

#### AaaSharedSecret

AAA shared secret.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AccessPointName

Access point name(APN).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Admin

FortiExtender Administration (enable or disable). Valid values: `disable`, `discovered`, `enable`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AtDialScript

Initialization AT commands specific to the MODEM.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BillingStartDay

Billing start day.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CdmaAaaSpi

CDMA AAA SPI.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CdmaHaSpi

CDMA HA SPI.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CdmaNai

NAI for CDMA MODEMS.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConnStatus

Connection status.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

Description.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DialMode

Dial mode (dial-on-demand or always-connect). Valid values: `dial-on-demand`, `always-connect`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DialStatus

Dial status.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExtName

FortiExtender name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Fosid

FortiExtender serial number.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HaSharedSecret

HA shared secret.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ifname

FortiExtender interface name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InitiatedUpdate

Allow/disallow network initiated updates to the MODEM. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Mode

FortiExtender mode. Valid values: `standalone`, `redundant`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ModemPasswd

MODEM password.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ModemType

MODEM type (CDMA, GSM/LTE or WIMAX). Valid values: `cdma`, `gsm/lte`, `wimax`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MultiMode

MODEM mode of operation(3G,LTE,etc). Valid values: `auto`, `auto-3g`, `force-lte`, `force-3g`, `force-2g`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PppAuthProtocol

PPP authentication protocol (PAP,CHAP or auto). Valid values: `auto`, `pap`, `chap`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PppEchoRequest

Enable/disable PPP echo request. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PppPassword

PPP password.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PppUsername

PPP username.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrimaryHa

Primary HA.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### QuotaLimitMb

Monthly quota limit (MB).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Redial

Number of redials allowed based on failed attempts. Valid values: `none`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9`, `10`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RedundantIntf

Redundant interface.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Roaming

Enable/disable MODEM roaming. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Role

FortiExtender work role(Primary, Secondary, None). Valid values: `none`, `primary`, `secondary`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecondaryHa

Secondary HA.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SimPin

SIM PIN.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vdom

VDOM.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vdomparam

Specifies the vdom to which the resource will be applied when the FortiGate unit is running in VDOM mode. Only one vdom can be specified. If you want to inherit the vdom configuration of the provider, please do not set this parameter.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WimaxAuthProtocol

WiMax authentication protocol(TLS or TTLS). Valid values: `tls`, `ttls`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WimaxCarrier

WiMax carrier.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WimaxRealm

WiMax realm.

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

