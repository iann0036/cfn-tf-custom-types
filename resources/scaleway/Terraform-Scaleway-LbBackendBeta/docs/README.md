# Terraform::Scaleway::LbBackendBeta

-> **Note:** This terraform resource is flagged beta and might include breaking change in future releases.

Creates and manages Scaleway Load-Balancer Backends. For more information, see [the documentation](https://developers.scaleway.com/en/products/lb/api).

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Scaleway::LbBackendBeta",
    "Properties" : {
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
        "<a href="#healthcheckhttp" title="HealthCheckHttp">HealthCheckHttp</a>" : <i>[ <a href="healthcheckhttp.md">HealthCheckHttp</a>, ... ]</i>,
        "<a href="#healthcheckhttps" title="HealthCheckHttps">HealthCheckHttps</a>" : <i>[ <a href="healthcheckhttps.md">HealthCheckHttps</a>, ... ]</i>,
        "<a href="#healthchecktcp" title="HealthCheckTcp">HealthCheckTcp</a>" : <i>[ <a href="healthchecktcp.md">HealthCheckTcp</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Scaleway::LbBackendBeta
Properties:
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
      - <a href="healthcheckhttp.md">HealthCheckHttp</a></i>
    <a href="#healthcheckhttps" title="HealthCheckHttps">HealthCheckHttps</a>: <i>
      - <a href="healthcheckhttps.md">HealthCheckHttps</a></i>
    <a href="#healthchecktcp" title="HealthCheckTcp">HealthCheckTcp</a>: <i>
      - <a href="healthchecktcp.md">HealthCheckTcp</a></i>
</pre>

## Properties

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

_Type_: List of <a href="healthcheckhttp.md">HealthCheckHttp</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HealthCheckHttps

_Required_: No

_Type_: List of <a href="healthcheckhttps.md">HealthCheckHttps</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HealthCheckTcp

_Required_: No

_Type_: List of <a href="healthchecktcp.md">HealthCheckTcp</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

