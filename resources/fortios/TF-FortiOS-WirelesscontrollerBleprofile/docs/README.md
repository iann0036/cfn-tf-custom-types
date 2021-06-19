# TF::FortiOS::WirelesscontrollerBleprofile

Configure Bluetooth Low Energy profile.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::FortiOS::WirelesscontrollerBleprofile",
    "Properties" : {
        "<a href="#advertising" title="Advertising">Advertising</a>" : <i>String</i>,
        "<a href="#beaconinterval" title="BeaconInterval">BeaconInterval</a>" : <i>Double</i>,
        "<a href="#blescanning" title="BleScanning">BleScanning</a>" : <i>String</i>,
        "<a href="#comment" title="Comment">Comment</a>" : <i>String</i>,
        "<a href="#eddystoneinstance" title="EddystoneInstance">EddystoneInstance</a>" : <i>String</i>,
        "<a href="#eddystonenamespace" title="EddystoneNamespace">EddystoneNamespace</a>" : <i>String</i>,
        "<a href="#eddystoneurl" title="EddystoneUrl">EddystoneUrl</a>" : <i>String</i>,
        "<a href="#eddystoneurlencodehex" title="EddystoneUrlEncodeHex">EddystoneUrlEncodeHex</a>" : <i>String</i>,
        "<a href="#ibeaconuuid" title="IbeaconUuid">IbeaconUuid</a>" : <i>String</i>,
        "<a href="#majorid" title="MajorId">MajorId</a>" : <i>Double</i>,
        "<a href="#minorid" title="MinorId">MinorId</a>" : <i>Double</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#txpower" title="Txpower">Txpower</a>" : <i>String</i>,
        "<a href="#vdomparam" title="Vdomparam">Vdomparam</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::FortiOS::WirelesscontrollerBleprofile
Properties:
    <a href="#advertising" title="Advertising">Advertising</a>: <i>String</i>
    <a href="#beaconinterval" title="BeaconInterval">BeaconInterval</a>: <i>Double</i>
    <a href="#blescanning" title="BleScanning">BleScanning</a>: <i>String</i>
    <a href="#comment" title="Comment">Comment</a>: <i>String</i>
    <a href="#eddystoneinstance" title="EddystoneInstance">EddystoneInstance</a>: <i>String</i>
    <a href="#eddystonenamespace" title="EddystoneNamespace">EddystoneNamespace</a>: <i>String</i>
    <a href="#eddystoneurl" title="EddystoneUrl">EddystoneUrl</a>: <i>String</i>
    <a href="#eddystoneurlencodehex" title="EddystoneUrlEncodeHex">EddystoneUrlEncodeHex</a>: <i>String</i>
    <a href="#ibeaconuuid" title="IbeaconUuid">IbeaconUuid</a>: <i>String</i>
    <a href="#majorid" title="MajorId">MajorId</a>: <i>Double</i>
    <a href="#minorid" title="MinorId">MinorId</a>: <i>Double</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#txpower" title="Txpower">Txpower</a>: <i>String</i>
    <a href="#vdomparam" title="Vdomparam">Vdomparam</a>: <i>String</i>
</pre>

## Properties

#### Advertising

Advertising type. Valid values: `ibeacon`, `eddystone-uid`, `eddystone-url`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BeaconInterval

Beacon interval (default = 100 msec).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BleScanning

Enable/disable Bluetooth Low Energy (BLE) scanning. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Comment

Comment.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EddystoneInstance

Eddystone instance ID.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EddystoneNamespace

Eddystone namespace ID.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EddystoneUrl

Eddystone URL.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EddystoneUrlEncodeHex

Eddystone encoded URL hexadecimal string.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IbeaconUuid

Universally Unique Identifier (UUID; automatically assigned but can be manually reset).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MajorId

Major ID.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MinorId

Minor ID.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Bluetooth Low Energy profile name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Txpower

Transmit power level (default = 0). Valid values: `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9`, `10`, `11`, `12`.

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

