# TF::FortiOS::Logsyslogd3Overridefilter

Override filters for remote system server.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::FortiOS::Logsyslogd3Overridefilter",
    "Properties" : {
        "<a href="#anomaly" title="Anomaly">Anomaly</a>" : <i>String</i>,
        "<a href="#dns" title="Dns">Dns</a>" : <i>String</i>,
        "<a href="#dynamicsortsubtable" title="DynamicSortSubtable">DynamicSortSubtable</a>" : <i>String</i>,
        "<a href="#filter" title="Filter">Filter</a>" : <i>String</i>,
        "<a href="#filtertype" title="FilterType">FilterType</a>" : <i>String</i>,
        "<a href="#forwardtraffic" title="ForwardTraffic">ForwardTraffic</a>" : <i>String</i>,
        "<a href="#gtp" title="Gtp">Gtp</a>" : <i>String</i>,
        "<a href="#localtraffic" title="LocalTraffic">LocalTraffic</a>" : <i>String</i>,
        "<a href="#multicasttraffic" title="MulticastTraffic">MulticastTraffic</a>" : <i>String</i>,
        "<a href="#netscandiscovery" title="NetscanDiscovery">NetscanDiscovery</a>" : <i>String</i>,
        "<a href="#netscanvulnerability" title="NetscanVulnerability">NetscanVulnerability</a>" : <i>String</i>,
        "<a href="#severity" title="Severity">Severity</a>" : <i>String</i>,
        "<a href="#sniffertraffic" title="SnifferTraffic">SnifferTraffic</a>" : <i>String</i>,
        "<a href="#ssh" title="Ssh">Ssh</a>" : <i>String</i>,
        "<a href="#vdomparam" title="Vdomparam">Vdomparam</a>" : <i>String</i>,
        "<a href="#voip" title="Voip">Voip</a>" : <i>String</i>,
        "<a href="#freestyle" title="FreeStyle">FreeStyle</a>" : <i>[ <a href="freestyledefinition.md">FreeStyleDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::FortiOS::Logsyslogd3Overridefilter
Properties:
    <a href="#anomaly" title="Anomaly">Anomaly</a>: <i>String</i>
    <a href="#dns" title="Dns">Dns</a>: <i>String</i>
    <a href="#dynamicsortsubtable" title="DynamicSortSubtable">DynamicSortSubtable</a>: <i>String</i>
    <a href="#filter" title="Filter">Filter</a>: <i>String</i>
    <a href="#filtertype" title="FilterType">FilterType</a>: <i>String</i>
    <a href="#forwardtraffic" title="ForwardTraffic">ForwardTraffic</a>: <i>String</i>
    <a href="#gtp" title="Gtp">Gtp</a>: <i>String</i>
    <a href="#localtraffic" title="LocalTraffic">LocalTraffic</a>: <i>String</i>
    <a href="#multicasttraffic" title="MulticastTraffic">MulticastTraffic</a>: <i>String</i>
    <a href="#netscandiscovery" title="NetscanDiscovery">NetscanDiscovery</a>: <i>String</i>
    <a href="#netscanvulnerability" title="NetscanVulnerability">NetscanVulnerability</a>: <i>String</i>
    <a href="#severity" title="Severity">Severity</a>: <i>String</i>
    <a href="#sniffertraffic" title="SnifferTraffic">SnifferTraffic</a>: <i>String</i>
    <a href="#ssh" title="Ssh">Ssh</a>: <i>String</i>
    <a href="#vdomparam" title="Vdomparam">Vdomparam</a>: <i>String</i>
    <a href="#voip" title="Voip">Voip</a>: <i>String</i>
    <a href="#freestyle" title="FreeStyle">FreeStyle</a>: <i>
      - <a href="freestyledefinition.md">FreeStyleDefinition</a></i>
</pre>

## Properties

#### Anomaly

Enable/disable anomaly logging. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Dns

Enable/disable detailed DNS event logging. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DynamicSortSubtable

true or false, set this parameter to true when using dynamic for_each + toset to configure and sort sub-tables, please do not set this parameter when configuring static sub-tables.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Filter

Syslog 3 filter.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FilterType

Include/exclude logs that match the filter. Valid values: `include`, `exclude`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ForwardTraffic

Enable/disable forward traffic logging. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Gtp

Enable/disable GTP messages logging. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LocalTraffic

Enable/disable local in or out traffic logging. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MulticastTraffic

Enable/disable multicast traffic logging. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetscanDiscovery

Enable/disable netscan discovery event logging.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetscanVulnerability

Enable/disable netscan vulnerability event logging.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Severity

Lowest severity level to log. Valid values: `emergency`, `alert`, `critical`, `error`, `warning`, `notification`, `information`, `debug`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SnifferTraffic

Enable/disable sniffer traffic logging. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ssh

Enable/disable SSH logging. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vdomparam

Specifies the vdom to which the resource will be applied when the FortiGate unit is running in VDOM mode. Only one vdom can be specified. If you want to inherit the vdom configuration of the provider, please do not set this parameter.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Voip

Enable/disable VoIP logging. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FreeStyle

_Required_: No

_Type_: List of <a href="freestyledefinition.md">FreeStyleDefinition</a>

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

