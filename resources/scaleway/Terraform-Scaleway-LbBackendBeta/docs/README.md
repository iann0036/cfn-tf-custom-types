# Terraform::Scaleway::LbBackendBeta

CloudFormation equivalent of scaleway_lb_backend_beta

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Scaleway::LbBackendBeta",
    "Properties" : {
        "<a href="#tfcfnid" title="tfcfnid">tfcfnid</a>" : <i>String</i>,
        "<a href="#forwardport" title="ForwardPort">ForwardPort</a>" : <i>Double</i>,
        "<a href="#forwardportalgorithm" title="ForwardPortAlgorithm">ForwardPortAlgorithm</a>" : <i>String</i>,
        "<a href="#forwardprotocol" title="ForwardProtocol">ForwardProtocol</a>" : <i>String</i>,
        "<a href="#healthcheckdelay" title="HealthCheckDelay">HealthCheckDelay</a>" : <i>String</i>,
        "<a href="#healthcheckmaxretries" title="HealthCheckMaxRetries">HealthCheckMaxRetries</a>" : <i>Double</i>,
        "<a href="#healthcheckport" title="HealthCheckPort">HealthCheckPort</a>" : <i>Double</i>,
        "<a href="#healthchecktimeout" title="HealthCheckTimeout">HealthCheckTimeout</a>" : <i>String</i>,
        "<a href="#lbid" title="LbId">LbId</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#onmarkeddownaction" title="OnMarkedDownAction">OnMarkedDownAction</a>" : <i>String</i>,
        "<a href="#sendproxyv2" title="SendProxyV2">SendProxyV2</a>" : <i>Boolean</i>,
        "<a href="#serverips" title="ServerIps">ServerIps</a>" : <i>[ String, ... ]</i>,
        "<a href="#stickysessions" title="StickySessions">StickySessions</a>" : <i>String</i>,
        "<a href="#stickysessionscookiename" title="StickySessionsCookieName">StickySessionsCookieName</a>" : <i>String</i>,
        "<a href="#timeoutconnect" title="TimeoutConnect">TimeoutConnect</a>" : <i>String</i>,
        "<a href="#timeoutserver" title="TimeoutServer">TimeoutServer</a>" : <i>String</i>,
        "<a href="#timeouttunnel" title="TimeoutTunnel">TimeoutTunnel</a>" : <i>String</i>,
        "<a href="#healthcheckhttp" title="HealthCheckHttp">HealthCheckHttp</a>" : <i>[ &lt;a href=&#34;healthcheckhttp.md&#34;&gt;HealthCheckHttp&lt;/a&gt;, ... ]</i>,
        "<a href="#healthcheckhttps" title="HealthCheckHttps">HealthCheckHttps</a>" : <i>[ &lt;a href=&#34;healthcheckhttps.md&#34;&gt;HealthCheckHttps&lt;/a&gt;, ... ]</i>,
        "<a href="#healthchecktcp" title="HealthCheckTcp">HealthCheckTcp</a>" : <i>[ &lt;a href=&#34;healthchecktcp.md&#34;&gt;HealthCheckTcp&lt;/a&gt;, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Scaleway::LbBackendBeta
Properties:
    <a href="#tfcfnid" title="tfcfnid">tfcfnid</a>: <i>String</i>
    <a href="#forwardport" title="ForwardPort">ForwardPort</a>: <i>Double</i>
    <a href="#forwardportalgorithm" title="ForwardPortAlgorithm">ForwardPortAlgorithm</a>: <i>String</i>
    <a href="#forwardprotocol" title="ForwardProtocol">ForwardProtocol</a>: <i>String</i>
    <a href="#healthcheckdelay" title="HealthCheckDelay">HealthCheckDelay</a>: <i>String</i>
    <a href="#healthcheckmaxretries" title="HealthCheckMaxRetries">HealthCheckMaxRetries</a>: <i>Double</i>
    <a href="#healthcheckport" title="HealthCheckPort">HealthCheckPort</a>: <i>Double</i>
    <a href="#healthchecktimeout" title="HealthCheckTimeout">HealthCheckTimeout</a>: <i>String</i>
    <a href="#lbid" title="LbId">LbId</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#onmarkeddownaction" title="OnMarkedDownAction">OnMarkedDownAction</a>: <i>String</i>
    <a href="#sendproxyv2" title="SendProxyV2">SendProxyV2</a>: <i>Boolean</i>
    <a href="#serverips" title="ServerIps">ServerIps</a>: <i>
      - String</i>
    <a href="#stickysessions" title="StickySessions">StickySessions</a>: <i>String</i>
    <a href="#stickysessionscookiename" title="StickySessionsCookieName">StickySessionsCookieName</a>: <i>String</i>
    <a href="#timeoutconnect" title="TimeoutConnect">TimeoutConnect</a>: <i>String</i>
    <a href="#timeoutserver" title="TimeoutServer">TimeoutServer</a>: <i>String</i>
    <a href="#timeouttunnel" title="TimeoutTunnel">TimeoutTunnel</a>: <i>String</i>
    <a href="#healthcheckhttp" title="HealthCheckHttp">HealthCheckHttp</a>: <i>
      - &lt;a href=&#34;healthcheckhttp.md&#34;&gt;HealthCheckHttp&lt;/a&gt;</i>
    <a href="#healthcheckhttps" title="HealthCheckHttps">HealthCheckHttps</a>: <i>
      - &lt;a href=&#34;healthcheckhttps.md&#34;&gt;HealthCheckHttps&lt;/a&gt;</i>
    <a href="#healthchecktcp" title="HealthCheckTcp">HealthCheckTcp</a>: <i>
      - &lt;a href=&#34;healthchecktcp.md&#34;&gt;HealthCheckTcp&lt;/a&gt;</i>
</pre>

## Properties

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ForwardPort

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ForwardPortAlgorithm

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ForwardProtocol

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HealthCheckDelay

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HealthCheckMaxRetries

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HealthCheckPort

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HealthCheckTimeout

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LbId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OnMarkedDownAction

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SendProxyV2

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServerIps

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StickySessions

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StickySessionsCookieName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TimeoutConnect

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TimeoutServer

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TimeoutTunnel

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HealthCheckHttp

_Required_: No

_Type_: List of &lt;a href=&#34;healthcheckhttp.md&#34;&gt;HealthCheckHttp&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HealthCheckHttps

_Required_: No

_Type_: List of &lt;a href=&#34;healthcheckhttps.md&#34;&gt;HealthCheckHttps&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HealthCheckTcp

_Required_: No

_Type_: List of &lt;a href=&#34;healthchecktcp.md&#34;&gt;HealthCheckTcp&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

