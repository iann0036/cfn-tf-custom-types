# TF::Thunder::SlbResourceUsage

`thunder_slb_resource_usage` Provides details about thunder slb resource usage

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Thunder::SlbResourceUsage",
    "Properties" : {
        "<a href="#cachetemplatecount" title="CacheTemplateCount">CacheTemplateCount</a>" : <i>Double</i>,
        "<a href="#clientssltemplatecount" title="ClientSslTemplateCount">ClientSslTemplateCount</a>" : <i>Double</i>,
        "<a href="#connreusetemplatecount" title="ConnReuseTemplateCount">ConnReuseTemplateCount</a>" : <i>Double</i>,
        "<a href="#fasttcptemplatecount" title="FastTcpTemplateCount">FastTcpTemplateCount</a>" : <i>Double</i>,
        "<a href="#fastudptemplatecount" title="FastUdpTemplateCount">FastUdpTemplateCount</a>" : <i>Double</i>,
        "<a href="#healthmonitorcount" title="HealthMonitorCount">HealthMonitorCount</a>" : <i>Double</i>,
        "<a href="#httptemplatecount" title="HttpTemplateCount">HttpTemplateCount</a>" : <i>Double</i>,
        "<a href="#natpooladdrcount" title="NatPoolAddrCount">NatPoolAddrCount</a>" : <i>Double</i>,
        "<a href="#pbslbsubnetcount" title="PbslbSubnetCount">PbslbSubnetCount</a>" : <i>Double</i>,
        "<a href="#persistcookietemplatecount" title="PersistCookieTemplateCount">PersistCookieTemplateCount</a>" : <i>Double</i>,
        "<a href="#persistsrciptemplatecount" title="PersistSrcipTemplateCount">PersistSrcipTemplateCount</a>" : <i>Double</i>,
        "<a href="#proxytemplatecount" title="ProxyTemplateCount">ProxyTemplateCount</a>" : <i>Double</i>,
        "<a href="#realportcount" title="RealPortCount">RealPortCount</a>" : <i>Double</i>,
        "<a href="#realservercount" title="RealServerCount">RealServerCount</a>" : <i>Double</i>,
        "<a href="#serverssltemplatecount" title="ServerSslTemplateCount">ServerSslTemplateCount</a>" : <i>Double</i>,
        "<a href="#servicegroupcount" title="ServiceGroupCount">ServiceGroupCount</a>" : <i>Double</i>,
        "<a href="#slbthresholdresusagepercent" title="SlbThresholdResUsagePercent">SlbThresholdResUsagePercent</a>" : <i>Double</i>,
        "<a href="#streamtemplatecount" title="StreamTemplateCount">StreamTemplateCount</a>" : <i>Double</i>,
        "<a href="#virtualportcount" title="VirtualPortCount">VirtualPortCount</a>" : <i>Double</i>,
        "<a href="#virtualservercount" title="VirtualServerCount">VirtualServerCount</a>" : <i>Double</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Thunder::SlbResourceUsage
Properties:
    <a href="#cachetemplatecount" title="CacheTemplateCount">CacheTemplateCount</a>: <i>Double</i>
    <a href="#clientssltemplatecount" title="ClientSslTemplateCount">ClientSslTemplateCount</a>: <i>Double</i>
    <a href="#connreusetemplatecount" title="ConnReuseTemplateCount">ConnReuseTemplateCount</a>: <i>Double</i>
    <a href="#fasttcptemplatecount" title="FastTcpTemplateCount">FastTcpTemplateCount</a>: <i>Double</i>
    <a href="#fastudptemplatecount" title="FastUdpTemplateCount">FastUdpTemplateCount</a>: <i>Double</i>
    <a href="#healthmonitorcount" title="HealthMonitorCount">HealthMonitorCount</a>: <i>Double</i>
    <a href="#httptemplatecount" title="HttpTemplateCount">HttpTemplateCount</a>: <i>Double</i>
    <a href="#natpooladdrcount" title="NatPoolAddrCount">NatPoolAddrCount</a>: <i>Double</i>
    <a href="#pbslbsubnetcount" title="PbslbSubnetCount">PbslbSubnetCount</a>: <i>Double</i>
    <a href="#persistcookietemplatecount" title="PersistCookieTemplateCount">PersistCookieTemplateCount</a>: <i>Double</i>
    <a href="#persistsrciptemplatecount" title="PersistSrcipTemplateCount">PersistSrcipTemplateCount</a>: <i>Double</i>
    <a href="#proxytemplatecount" title="ProxyTemplateCount">ProxyTemplateCount</a>: <i>Double</i>
    <a href="#realportcount" title="RealPortCount">RealPortCount</a>: <i>Double</i>
    <a href="#realservercount" title="RealServerCount">RealServerCount</a>: <i>Double</i>
    <a href="#serverssltemplatecount" title="ServerSslTemplateCount">ServerSslTemplateCount</a>: <i>Double</i>
    <a href="#servicegroupcount" title="ServiceGroupCount">ServiceGroupCount</a>: <i>Double</i>
    <a href="#slbthresholdresusagepercent" title="SlbThresholdResUsagePercent">SlbThresholdResUsagePercent</a>: <i>Double</i>
    <a href="#streamtemplatecount" title="StreamTemplateCount">StreamTemplateCount</a>: <i>Double</i>
    <a href="#virtualportcount" title="VirtualPortCount">VirtualPortCount</a>: <i>Double</i>
    <a href="#virtualservercount" title="VirtualServerCount">VirtualServerCount</a>: <i>Double</i>
</pre>

## Properties

#### CacheTemplateCount

Total configurable HTTP Cache Templates in the System.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClientSslTemplateCount

Total configurable Client SSL Templates in the System.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConnReuseTemplateCount

Total configurable Connection reuse Templates in the System.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FastTcpTemplateCount

Total configurable Fast TCP Templates in the System.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FastUdpTemplateCount

Total configurable Fast UDP Templates in the System.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HealthMonitorCount

Total Health Monitors in the System.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HttpTemplateCount

Total configurable HTTP Templates in the System.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NatPoolAddrCount

Total configurable NAT Pool addresses in the System.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PbslbSubnetCount

Total PBSLB Subnets in the System.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PersistCookieTemplateCount

Total configurable Persistent cookie Templates in the System.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PersistSrcipTemplateCount

Total configurable Source IP Persistent Templates in the System.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProxyTemplateCount

Total configurable Proxy Templates in the System.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RealPortCount

Total Real Server Ports in the System.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RealServerCount

Total Real Servers in the System.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServerSslTemplateCount

Total configurable Server SSL Templates in the System.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceGroupCount

Total Service Groups in the System.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SlbThresholdResUsagePercent

Enter the threshold as a percentage (Threshold in percentage(default is 0%)).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StreamTemplateCount

Total configurable Streaming media in the System.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VirtualPortCount

Total Virtual Server Ports in the System.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VirtualServerCount

Total Virtual Servers in the System.

_Required_: No

_Type_: Double

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

