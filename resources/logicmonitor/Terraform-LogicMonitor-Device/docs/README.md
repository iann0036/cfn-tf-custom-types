# Terraform::LogicMonitor::Device

Provides a LogicMonitor device resource. This can be used to create and manage LogicMonitor devices

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::LogicMonitor::Device",
    "Properties" : {
        "<a href="#collector" title="Collector">Collector</a>" : <i>Double</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#disablealerting" title="DisableAlerting">DisableAlerting</a>" : <i>Boolean</i>,
        "<a href="#displayname" title="DisplayName">DisplayName</a>" : <i>String</i>,
        "<a href="#hostgroupid" title="HostgroupId">HostgroupId</a>" : <i>String</i>,
        "<a href="#ipaddr" title="IpAddr">IpAddr</a>" : <i>String</i>,
        "<a href="#properties" title="Properties">Properties</a>" : <i>[ <a href="properties.md">Properties</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::LogicMonitor::Device
Properties:
    <a href="#collector" title="Collector">Collector</a>: <i>Double</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#disablealerting" title="DisableAlerting">DisableAlerting</a>: <i>Boolean</i>
    <a href="#displayname" title="DisplayName">DisplayName</a>: <i>String</i>
    <a href="#hostgroupid" title="HostgroupId">HostgroupId</a>: <i>String</i>
    <a href="#ipaddr" title="IpAddr">IpAddr</a>: <i>String</i>
    <a href="#properties" title="Properties">Properties</a>: <i>
      - <a href="properties.md">Properties</a></i>
</pre>

## Properties

#### Collector

The id of the collector that will monitoring the device.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisableAlerting

The host is created with alerting disabled (default is true).

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisplayName

Display name of device, (default is ip_addr).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HostgroupId

The host group id that specifies which group the device belongs to (multiple host group ids can be added, represented by a comma separated string).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpAddr

Ip Address/Hostname of device.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Properties

The properties associated with this device group. Any string value pair will work (see example).

_Required_: No

_Type_: List of <a href="properties.md">Properties</a>

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

