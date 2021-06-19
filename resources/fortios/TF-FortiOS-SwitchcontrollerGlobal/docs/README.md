# TF::FortiOS::SwitchcontrollerGlobal

Configure FortiSwitch global settings.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::FortiOS::SwitchcontrollerGlobal",
    "Properties" : {
        "<a href="#allowmultipleinterfaces" title="AllowMultipleInterfaces">AllowMultipleInterfaces</a>" : <i>String</i>,
        "<a href="#bouncequarantinedlink" title="BounceQuarantinedLink">BounceQuarantinedLink</a>" : <i>String</i>,
        "<a href="#defaultvirtualswitchvlan" title="DefaultVirtualSwitchVlan">DefaultVirtualSwitchVlan</a>" : <i>String</i>,
        "<a href="#dynamicsortsubtable" title="DynamicSortSubtable">DynamicSortSubtable</a>" : <i>String</i>,
        "<a href="#httpsimagepush" title="HttpsImagePush">HttpsImagePush</a>" : <i>String</i>,
        "<a href="#logmaclimitviolations" title="LogMacLimitViolations">LogMacLimitViolations</a>" : <i>String</i>,
        "<a href="#macaginginterval" title="MacAgingInterval">MacAgingInterval</a>" : <i>Double</i>,
        "<a href="#maceventlogging" title="MacEventLogging">MacEventLogging</a>" : <i>String</i>,
        "<a href="#macretentionperiod" title="MacRetentionPeriod">MacRetentionPeriod</a>" : <i>Double</i>,
        "<a href="#macviolationtimer" title="MacViolationTimer">MacViolationTimer</a>" : <i>Double</i>,
        "<a href="#quarantinemode" title="QuarantineMode">QuarantineMode</a>" : <i>String</i>,
        "<a href="#sndnsresolution" title="SnDnsResolution">SnDnsResolution</a>" : <i>String</i>,
        "<a href="#updateuserdevice" title="UpdateUserDevice">UpdateUserDevice</a>" : <i>String</i>,
        "<a href="#vdomparam" title="Vdomparam">Vdomparam</a>" : <i>String</i>,
        "<a href="#vlanallmode" title="VlanAllMode">VlanAllMode</a>" : <i>String</i>,
        "<a href="#vlanoptimization" title="VlanOptimization">VlanOptimization</a>" : <i>String</i>,
        "<a href="#customcommand" title="CustomCommand">CustomCommand</a>" : <i>[ <a href="customcommanddefinition.md">CustomCommandDefinition</a>, ... ]</i>,
        "<a href="#disablediscovery" title="DisableDiscovery">DisableDiscovery</a>" : <i>[ <a href="disablediscoverydefinition.md">DisableDiscoveryDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::FortiOS::SwitchcontrollerGlobal
Properties:
    <a href="#allowmultipleinterfaces" title="AllowMultipleInterfaces">AllowMultipleInterfaces</a>: <i>String</i>
    <a href="#bouncequarantinedlink" title="BounceQuarantinedLink">BounceQuarantinedLink</a>: <i>String</i>
    <a href="#defaultvirtualswitchvlan" title="DefaultVirtualSwitchVlan">DefaultVirtualSwitchVlan</a>: <i>String</i>
    <a href="#dynamicsortsubtable" title="DynamicSortSubtable">DynamicSortSubtable</a>: <i>String</i>
    <a href="#httpsimagepush" title="HttpsImagePush">HttpsImagePush</a>: <i>String</i>
    <a href="#logmaclimitviolations" title="LogMacLimitViolations">LogMacLimitViolations</a>: <i>String</i>
    <a href="#macaginginterval" title="MacAgingInterval">MacAgingInterval</a>: <i>Double</i>
    <a href="#maceventlogging" title="MacEventLogging">MacEventLogging</a>: <i>String</i>
    <a href="#macretentionperiod" title="MacRetentionPeriod">MacRetentionPeriod</a>: <i>Double</i>
    <a href="#macviolationtimer" title="MacViolationTimer">MacViolationTimer</a>: <i>Double</i>
    <a href="#quarantinemode" title="QuarantineMode">QuarantineMode</a>: <i>String</i>
    <a href="#sndnsresolution" title="SnDnsResolution">SnDnsResolution</a>: <i>String</i>
    <a href="#updateuserdevice" title="UpdateUserDevice">UpdateUserDevice</a>: <i>String</i>
    <a href="#vdomparam" title="Vdomparam">Vdomparam</a>: <i>String</i>
    <a href="#vlanallmode" title="VlanAllMode">VlanAllMode</a>: <i>String</i>
    <a href="#vlanoptimization" title="VlanOptimization">VlanOptimization</a>: <i>String</i>
    <a href="#customcommand" title="CustomCommand">CustomCommand</a>: <i>
      - <a href="customcommanddefinition.md">CustomCommandDefinition</a></i>
    <a href="#disablediscovery" title="DisableDiscovery">DisableDiscovery</a>: <i>
      - <a href="disablediscoverydefinition.md">DisableDiscoveryDefinition</a></i>
</pre>

## Properties

#### AllowMultipleInterfaces

Enable/disable multiple FortiLink interfaces for redundant connections between a managed FortiSwitch and FortiGate. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BounceQuarantinedLink

Enable/disable bouncing (administratively bring the link down, up) of a switch port where a quarantined device was seen last. Helps to re-initiate the DHCP process for a device. Valid values: `disable`, `enable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefaultVirtualSwitchVlan

Default VLAN for ports when added to the virtual-switch.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DynamicSortSubtable

true or false, set this parameter to true when using dynamic for_each + toset to configure and sort sub-tables, please do not set this parameter when configuring static sub-tables.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HttpsImagePush

Enable/disable image push to FortiSwitch using HTTPS. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LogMacLimitViolations

Enable/disable logs for Learning Limit Violations. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MacAgingInterval

Time after which an inactive MAC is aged out (10 - 1000000 sec, default = 300, 0 = disable).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MacEventLogging

Enable/disable MAC address event logging. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MacRetentionPeriod

Time in hours after which an inactive MAC is removed from client DB.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MacViolationTimer

Set timeout for Learning Limit Violations (0 = disabled).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### QuarantineMode

Quarantine mode. Valid values: `by-vlan`, `by-redirect`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SnDnsResolution

Enable/disable DNS resolution of the FortiSwitch unit's IP address by use of its serial number. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UpdateUserDevice

Control which sources update the device user list. Valid values: `mac-cache`, `lldp`, `dhcp-snooping`, `l2-db`, `l3-db`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vdomparam

Specifies the vdom to which the resource will be applied when the FortiGate unit is running in VDOM mode. Only one vdom can be specified. If you want to inherit the vdom configuration of the provider, please do not set this parameter.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VlanAllMode

VLAN configuration mode, user-defined-vlans or all-possible-vlans. Valid values: `all`, `defined`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VlanOptimization

FortiLink VLAN optimization. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CustomCommand

_Required_: No

_Type_: List of <a href="customcommanddefinition.md">CustomCommandDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisableDiscovery

_Required_: No

_Type_: List of <a href="disablediscoverydefinition.md">DisableDiscoveryDefinition</a>

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

