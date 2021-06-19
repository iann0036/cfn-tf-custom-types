# TF::Alicloud::WafDomain

Provides a WAF Domain resource to create domain in the Web Application Firewall.

For information about WAF and how to use it, see [What is Alibaba Cloud WAF](https://www.alibabacloud.com/help/doc-detail/28517.htm).

-> **NOTE:** Available in 1.82.0+ .

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Alicloud::WafDomain",
    "Properties" : {
        "<a href="#clustertype" title="ClusterType">ClusterType</a>" : <i>String</i>,
        "<a href="#connectiontime" title="ConnectionTime">ConnectionTime</a>" : <i>Double</i>,
        "<a href="#domain" title="Domain">Domain</a>" : <i>String</i>,
        "<a href="#domainname" title="DomainName">DomainName</a>" : <i>String</i>,
        "<a href="#http2port" title="Http2Port">Http2Port</a>" : <i>[ String, ... ]</i>,
        "<a href="#httpport" title="HttpPort">HttpPort</a>" : <i>[ String, ... ]</i>,
        "<a href="#httptouserip" title="HttpToUserIp">HttpToUserIp</a>" : <i>String</i>,
        "<a href="#httpsport" title="HttpsPort">HttpsPort</a>" : <i>[ String, ... ]</i>,
        "<a href="#httpsredirect" title="HttpsRedirect">HttpsRedirect</a>" : <i>String</i>,
        "<a href="#instanceid" title="InstanceId">InstanceId</a>" : <i>String</i>,
        "<a href="#isaccessproduct" title="IsAccessProduct">IsAccessProduct</a>" : <i>String</i>,
        "<a href="#loadbalancing" title="LoadBalancing">LoadBalancing</a>" : <i>String</i>,
        "<a href="#readtime" title="ReadTime">ReadTime</a>" : <i>Double</i>,
        "<a href="#resourcegroupid" title="ResourceGroupId">ResourceGroupId</a>" : <i>String</i>,
        "<a href="#sourceips" title="SourceIps">SourceIps</a>" : <i>[ String, ... ]</i>,
        "<a href="#writetime" title="WriteTime">WriteTime</a>" : <i>Double</i>,
        "<a href="#logheaders" title="LogHeaders">LogHeaders</a>" : <i>[ <a href="logheadersdefinition.md">LogHeadersDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Alicloud::WafDomain
Properties:
    <a href="#clustertype" title="ClusterType">ClusterType</a>: <i>String</i>
    <a href="#connectiontime" title="ConnectionTime">ConnectionTime</a>: <i>Double</i>
    <a href="#domain" title="Domain">Domain</a>: <i>String</i>
    <a href="#domainname" title="DomainName">DomainName</a>: <i>String</i>
    <a href="#http2port" title="Http2Port">Http2Port</a>: <i>
      - String</i>
    <a href="#httpport" title="HttpPort">HttpPort</a>: <i>
      - String</i>
    <a href="#httptouserip" title="HttpToUserIp">HttpToUserIp</a>: <i>String</i>
    <a href="#httpsport" title="HttpsPort">HttpsPort</a>: <i>
      - String</i>
    <a href="#httpsredirect" title="HttpsRedirect">HttpsRedirect</a>: <i>String</i>
    <a href="#instanceid" title="InstanceId">InstanceId</a>: <i>String</i>
    <a href="#isaccessproduct" title="IsAccessProduct">IsAccessProduct</a>: <i>String</i>
    <a href="#loadbalancing" title="LoadBalancing">LoadBalancing</a>: <i>String</i>
    <a href="#readtime" title="ReadTime">ReadTime</a>: <i>Double</i>
    <a href="#resourcegroupid" title="ResourceGroupId">ResourceGroupId</a>: <i>String</i>
    <a href="#sourceips" title="SourceIps">SourceIps</a>: <i>
      - String</i>
    <a href="#writetime" title="WriteTime">WriteTime</a>: <i>Double</i>
    <a href="#logheaders" title="LogHeaders">LogHeaders</a>: <i>
      - <a href="logheadersdefinition.md">LogHeadersDefinition</a></i>
</pre>

## Properties

#### ClusterType

The type of the WAF cluster. Valid values: `PhysicalCluster` and `VirtualCluster`. Default to `PhysicalCluster`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConnectionTime

The connection timeout for WAF exclusive clusters. Unit: seconds.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Domain

Field `domain` has been deprecated from version 1.94.0. Use `domain_name` instead.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DomainName

The domain that you want to add to WAF.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Http2Port

List of the HTTP 2.0 ports.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HttpPort

List of the HTTP ports.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HttpToUserIp

Specifies whether to enable the HTTP back-to-origin feature. After this feature is enabled, the WAF instance can use HTTP to forward HTTPS requests to the origin server.
By default, port 80 is used to forward the requests to the origin server. Valid values: `On` and `Off`. Default to `Off`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HttpsPort

List of the HTTPS ports.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HttpsRedirect

Specifies whether to redirect HTTP requests as HTTPS requests. Valid values: "On" and `Off`. Default to `Off`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InstanceId

The ID of the WAF instance.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsAccessProduct

Specifies whether to configure a Layer-7 proxy, such as Anti-DDoS Pro or CDN, to filter the inbound traffic before it is forwarded to WAF. Valid values: `On` and `Off`. Default to `Off`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LoadBalancing

The load balancing algorithm that is used to forward requests to the origin. Valid values: `IpHash` and `RoundRobin`. Default to `IpHash`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReadTime

The read timeout of a WAF exclusive cluster. Unit: seconds.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourceGroupId

The ID of the resource group to which the queried domain belongs in Resource Management. By default, no value is specified, indicating that the domain belongs to the default resource group.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceIps

List of the IP address or domain of the origin server to which the specified domain points.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WriteTime

The timeout period for a WAF exclusive cluster write connection. Unit: seconds.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LogHeaders

_Required_: No

_Type_: List of <a href="logheadersdefinition.md">LogHeadersDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Cname

Returns the <code>Cname</code> value.

#### Id

Returns the <code>Id</code> value.

