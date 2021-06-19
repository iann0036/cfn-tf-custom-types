# TF::FortiOS::WirelesscontrollerBonjourprofile PolicyListDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#description" title="Description">Description</a>" : <i>String</i>,
    "<a href="#fromvlan" title="FromVlan">FromVlan</a>" : <i>String</i>,
    "<a href="#policyid" title="PolicyId">PolicyId</a>" : <i>Double</i>,
    "<a href="#services" title="Services">Services</a>" : <i>String</i>,
    "<a href="#tovlan" title="ToVlan">ToVlan</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#description" title="Description">Description</a>: <i>String</i>
<a href="#fromvlan" title="FromVlan">FromVlan</a>: <i>String</i>
<a href="#policyid" title="PolicyId">PolicyId</a>: <i>Double</i>
<a href="#services" title="Services">Services</a>: <i>String</i>
<a href="#tovlan" title="ToVlan">ToVlan</a>: <i>String</i>
</pre>

## Properties

#### Description

Description.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FromVlan

VLAN ID from which the Bonjour service is advertised (0 - 4094, default = 0).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PolicyId

Policy ID.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Services

Bonjour services for the VLAN connecting to the Bonjour network. Valid values: `all`, `airplay`, `afp`, `bit-torrent`, `ftp`, `ichat`, `itunes`, `printers`, `samba`, `scanners`, `ssh`, `chromecast`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ToVlan

VLAN ID to which the Bonjour service is made available (0 - 4094, default = all).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

