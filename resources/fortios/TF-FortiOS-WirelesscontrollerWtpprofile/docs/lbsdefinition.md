# TF::FortiOS::WirelesscontrollerWtpprofile LbsDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#aeroscout" title="Aeroscout">Aeroscout</a>" : <i>String</i>,
    "<a href="#aeroscoutapmac" title="AeroscoutApMac">AeroscoutApMac</a>" : <i>String</i>,
    "<a href="#aeroscoutmmureport" title="AeroscoutMmuReport">AeroscoutMmuReport</a>" : <i>String</i>,
    "<a href="#aeroscoutmu" title="AeroscoutMu">AeroscoutMu</a>" : <i>String</i>,
    "<a href="#aeroscoutmufactor" title="AeroscoutMuFactor">AeroscoutMuFactor</a>" : <i>Double</i>,
    "<a href="#aeroscoutmutimeout" title="AeroscoutMuTimeout">AeroscoutMuTimeout</a>" : <i>Double</i>,
    "<a href="#aeroscoutserverip" title="AeroscoutServerIp">AeroscoutServerIp</a>" : <i>String</i>,
    "<a href="#aeroscoutserverport" title="AeroscoutServerPort">AeroscoutServerPort</a>" : <i>Double</i>,
    "<a href="#ekahaublinkmode" title="EkahauBlinkMode">EkahauBlinkMode</a>" : <i>String</i>,
    "<a href="#ekahautag" title="EkahauTag">EkahauTag</a>" : <i>String</i>,
    "<a href="#ercserverip" title="ErcServerIp">ErcServerIp</a>" : <i>String</i>,
    "<a href="#ercserverport" title="ErcServerPort">ErcServerPort</a>" : <i>Double</i>,
    "<a href="#fortipresence" title="Fortipresence">Fortipresence</a>" : <i>String</i>,
    "<a href="#fortipresenceble" title="FortipresenceBle">FortipresenceBle</a>" : <i>String</i>,
    "<a href="#fortipresencefrequency" title="FortipresenceFrequency">FortipresenceFrequency</a>" : <i>Double</i>,
    "<a href="#fortipresenceport" title="FortipresencePort">FortipresencePort</a>" : <i>Double</i>,
    "<a href="#fortipresenceproject" title="FortipresenceProject">FortipresenceProject</a>" : <i>String</i>,
    "<a href="#fortipresencerogue" title="FortipresenceRogue">FortipresenceRogue</a>" : <i>String</i>,
    "<a href="#fortipresencesecret" title="FortipresenceSecret">FortipresenceSecret</a>" : <i>String</i>,
    "<a href="#fortipresenceserver" title="FortipresenceServer">FortipresenceServer</a>" : <i>String</i>,
    "<a href="#fortipresenceunassoc" title="FortipresenceUnassoc">FortipresenceUnassoc</a>" : <i>String</i>,
    "<a href="#stationlocate" title="StationLocate">StationLocate</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#aeroscout" title="Aeroscout">Aeroscout</a>: <i>String</i>
<a href="#aeroscoutapmac" title="AeroscoutApMac">AeroscoutApMac</a>: <i>String</i>
<a href="#aeroscoutmmureport" title="AeroscoutMmuReport">AeroscoutMmuReport</a>: <i>String</i>
<a href="#aeroscoutmu" title="AeroscoutMu">AeroscoutMu</a>: <i>String</i>
<a href="#aeroscoutmufactor" title="AeroscoutMuFactor">AeroscoutMuFactor</a>: <i>Double</i>
<a href="#aeroscoutmutimeout" title="AeroscoutMuTimeout">AeroscoutMuTimeout</a>: <i>Double</i>
<a href="#aeroscoutserverip" title="AeroscoutServerIp">AeroscoutServerIp</a>: <i>String</i>
<a href="#aeroscoutserverport" title="AeroscoutServerPort">AeroscoutServerPort</a>: <i>Double</i>
<a href="#ekahaublinkmode" title="EkahauBlinkMode">EkahauBlinkMode</a>: <i>String</i>
<a href="#ekahautag" title="EkahauTag">EkahauTag</a>: <i>String</i>
<a href="#ercserverip" title="ErcServerIp">ErcServerIp</a>: <i>String</i>
<a href="#ercserverport" title="ErcServerPort">ErcServerPort</a>: <i>Double</i>
<a href="#fortipresence" title="Fortipresence">Fortipresence</a>: <i>String</i>
<a href="#fortipresenceble" title="FortipresenceBle">FortipresenceBle</a>: <i>String</i>
<a href="#fortipresencefrequency" title="FortipresenceFrequency">FortipresenceFrequency</a>: <i>Double</i>
<a href="#fortipresenceport" title="FortipresencePort">FortipresencePort</a>: <i>Double</i>
<a href="#fortipresenceproject" title="FortipresenceProject">FortipresenceProject</a>: <i>String</i>
<a href="#fortipresencerogue" title="FortipresenceRogue">FortipresenceRogue</a>: <i>String</i>
<a href="#fortipresencesecret" title="FortipresenceSecret">FortipresenceSecret</a>: <i>String</i>
<a href="#fortipresenceserver" title="FortipresenceServer">FortipresenceServer</a>: <i>String</i>
<a href="#fortipresenceunassoc" title="FortipresenceUnassoc">FortipresenceUnassoc</a>: <i>String</i>
<a href="#stationlocate" title="StationLocate">StationLocate</a>: <i>String</i>
</pre>

## Properties

#### Aeroscout

Enable/disable AeroScout Real Time Location Service (RTLS) support. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AeroscoutApMac

Use BSSID or board MAC address as AP MAC address in the Aeroscout AP message. Valid values: `bssid`, `board-mac`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AeroscoutMmuReport

Enable/disable MU compounded report. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AeroscoutMu

Enable/disable AeroScout support. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AeroscoutMuFactor

AeroScout Mobile Unit (MU) mode dilution factor (default = 20).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AeroscoutMuTimeout

AeroScout MU mode timeout (0 - 65535 sec, default = 5).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AeroscoutServerIp

IP address of AeroScout server.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AeroscoutServerPort

AeroScout server UDP listening port.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EkahauBlinkMode

Enable/disable Ekahua blink mode (also called AiRISTA Flow Blink Mode) to find the location of devices connected to a wireless LAN (default = disable). Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EkahauTag

WiFi frame MAC address or WiFi Tag.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ErcServerIp

IP address of Ekahua RTLS Controller (ERC).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ErcServerPort

Ekahua RTLS Controller (ERC) UDP listening port.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Fortipresence

Enable/disable FortiPresence to monitor the location and activity of WiFi clients even if they don't connect to this WiFi network (default = disable). Valid values: `foreign`, `both`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FortipresenceBle

Enable/disable FortiPresence finding and reporting BLE devices. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FortipresenceFrequency

FortiPresence report transmit frequency (5 - 65535 sec, default = 30).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FortipresencePort

FortiPresence server UDP listening port (default = 3000).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FortipresenceProject

FortiPresence project name (max. 16 characters, default = fortipresence).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FortipresenceRogue

Enable/disable FortiPresence finding and reporting rogue APs. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FortipresenceSecret

FortiPresence secret password (max. 16 characters).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FortipresenceServer

FortiPresence server IP address.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FortipresenceUnassoc

Enable/disable FortiPresence finding and reporting unassociated stations. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StationLocate

Enable/disable client station locating services for all clients, whether associated or not (default = disable). Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

