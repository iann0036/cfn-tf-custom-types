# TF::TencentCloud::ClbListener

Provides a resource to create a CLB listener.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::TencentCloud::ClbListener",
    "Properties" : {
        "<a href="#certificatecaid" title="CertificateCaId">CertificateCaId</a>" : <i>String</i>,
        "<a href="#certificateid" title="CertificateId">CertificateId</a>" : <i>String</i>,
        "<a href="#certificatesslmode" title="CertificateSslMode">CertificateSslMode</a>" : <i>String</i>,
        "<a href="#clbid" title="ClbId">ClbId</a>" : <i>String</i>,
        "<a href="#healthcheckcontexttype" title="HealthCheckContextType">HealthCheckContextType</a>" : <i>String</i>,
        "<a href="#healthcheckhealthnum" title="HealthCheckHealthNum">HealthCheckHealthNum</a>" : <i>Double</i>,
        "<a href="#healthcheckhttpcode" title="HealthCheckHttpCode">HealthCheckHttpCode</a>" : <i>Double</i>,
        "<a href="#healthcheckhttpdomain" title="HealthCheckHttpDomain">HealthCheckHttpDomain</a>" : <i>String</i>,
        "<a href="#healthcheckhttpmethod" title="HealthCheckHttpMethod">HealthCheckHttpMethod</a>" : <i>String</i>,
        "<a href="#healthcheckhttppath" title="HealthCheckHttpPath">HealthCheckHttpPath</a>" : <i>String</i>,
        "<a href="#healthcheckhttpversion" title="HealthCheckHttpVersion">HealthCheckHttpVersion</a>" : <i>String</i>,
        "<a href="#healthcheckintervaltime" title="HealthCheckIntervalTime">HealthCheckIntervalTime</a>" : <i>Double</i>,
        "<a href="#healthcheckport" title="HealthCheckPort">HealthCheckPort</a>" : <i>Double</i>,
        "<a href="#healthcheckrecvcontext" title="HealthCheckRecvContext">HealthCheckRecvContext</a>" : <i>String</i>,
        "<a href="#healthchecksendcontext" title="HealthCheckSendContext">HealthCheckSendContext</a>" : <i>String</i>,
        "<a href="#healthcheckswitch" title="HealthCheckSwitch">HealthCheckSwitch</a>" : <i>Boolean</i>,
        "<a href="#healthchecktimeout" title="HealthCheckTimeOut">HealthCheckTimeOut</a>" : <i>Double</i>,
        "<a href="#healthchecktype" title="HealthCheckType">HealthCheckType</a>" : <i>String</i>,
        "<a href="#healthcheckunhealthnum" title="HealthCheckUnhealthNum">HealthCheckUnhealthNum</a>" : <i>Double</i>,
        "<a href="#listenername" title="ListenerName">ListenerName</a>" : <i>String</i>,
        "<a href="#port" title="Port">Port</a>" : <i>Double</i>,
        "<a href="#protocol" title="Protocol">Protocol</a>" : <i>String</i>,
        "<a href="#scheduler" title="Scheduler">Scheduler</a>" : <i>String</i>,
        "<a href="#sessionexpiretime" title="SessionExpireTime">SessionExpireTime</a>" : <i>Double</i>,
        "<a href="#sniswitch" title="SniSwitch">SniSwitch</a>" : <i>Boolean</i>,
        "<a href="#targettype" title="TargetType">TargetType</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::TencentCloud::ClbListener
Properties:
    <a href="#certificatecaid" title="CertificateCaId">CertificateCaId</a>: <i>String</i>
    <a href="#certificateid" title="CertificateId">CertificateId</a>: <i>String</i>
    <a href="#certificatesslmode" title="CertificateSslMode">CertificateSslMode</a>: <i>String</i>
    <a href="#clbid" title="ClbId">ClbId</a>: <i>String</i>
    <a href="#healthcheckcontexttype" title="HealthCheckContextType">HealthCheckContextType</a>: <i>String</i>
    <a href="#healthcheckhealthnum" title="HealthCheckHealthNum">HealthCheckHealthNum</a>: <i>Double</i>
    <a href="#healthcheckhttpcode" title="HealthCheckHttpCode">HealthCheckHttpCode</a>: <i>Double</i>
    <a href="#healthcheckhttpdomain" title="HealthCheckHttpDomain">HealthCheckHttpDomain</a>: <i>String</i>
    <a href="#healthcheckhttpmethod" title="HealthCheckHttpMethod">HealthCheckHttpMethod</a>: <i>String</i>
    <a href="#healthcheckhttppath" title="HealthCheckHttpPath">HealthCheckHttpPath</a>: <i>String</i>
    <a href="#healthcheckhttpversion" title="HealthCheckHttpVersion">HealthCheckHttpVersion</a>: <i>String</i>
    <a href="#healthcheckintervaltime" title="HealthCheckIntervalTime">HealthCheckIntervalTime</a>: <i>Double</i>
    <a href="#healthcheckport" title="HealthCheckPort">HealthCheckPort</a>: <i>Double</i>
    <a href="#healthcheckrecvcontext" title="HealthCheckRecvContext">HealthCheckRecvContext</a>: <i>String</i>
    <a href="#healthchecksendcontext" title="HealthCheckSendContext">HealthCheckSendContext</a>: <i>String</i>
    <a href="#healthcheckswitch" title="HealthCheckSwitch">HealthCheckSwitch</a>: <i>Boolean</i>
    <a href="#healthchecktimeout" title="HealthCheckTimeOut">HealthCheckTimeOut</a>: <i>Double</i>
    <a href="#healthchecktype" title="HealthCheckType">HealthCheckType</a>: <i>String</i>
    <a href="#healthcheckunhealthnum" title="HealthCheckUnhealthNum">HealthCheckUnhealthNum</a>: <i>Double</i>
    <a href="#listenername" title="ListenerName">ListenerName</a>: <i>String</i>
    <a href="#port" title="Port">Port</a>: <i>Double</i>
    <a href="#protocol" title="Protocol">Protocol</a>: <i>String</i>
    <a href="#scheduler" title="Scheduler">Scheduler</a>: <i>String</i>
    <a href="#sessionexpiretime" title="SessionExpireTime">SessionExpireTime</a>: <i>Double</i>
    <a href="#sniswitch" title="SniSwitch">SniSwitch</a>: <i>Boolean</i>
    <a href="#targettype" title="TargetType">TargetType</a>: <i>String</i>
</pre>

## Properties

#### CertificateCaId

ID of the client certificate. NOTES: Only supports listeners of `HTTPS` and `TCP_SSL` protocol and must be set when the ssl mode is `MUTUAL`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CertificateId

ID of the server certificate. NOTES: Only supports listeners of `HTTPS` and `TCP_SSL` protocol and must be set when it is available.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CertificateSslMode

Type of certificate. Valid values: `UNIDIRECTIONAL`, `MUTUAL`. NOTES: Only supports listeners of `HTTPS` and `TCP_SSL` protocol and must be set when it is available.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClbId

ID of the CLB.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HealthCheckContextType

Health check protocol. When the value of `health_check_type` of the health check protocol is `CUSTOM`, this field is required, which represents the input format of the health check. Valid values: `HEX`, `TEXT`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HealthCheckHealthNum

Health threshold of health check, and the default is `3`. If a success result is returned for the health check for 3 consecutive times, the backend CVM is identified as healthy. The value range is 2-10. NOTES: TCP/UDP/TCP_SSL listener allows direct configuration, HTTP/HTTPS listener needs to be configured in tencentcloud_clb_listener_rule.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HealthCheckHttpCode

HTTP health check code of TCP listener. When the value of `health_check_type` of the health check protocol is `HTTP`, this field is required. Valid values: `1`, `2`, `4`, `8`, `16`. `1` means http_1xx, `2` means http_2xx, `4` means http_3xx, `8` means http_4xx, `16` means http_5xx.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HealthCheckHttpDomain

HTTP health check domain of TCP listener.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HealthCheckHttpMethod

HTTP health check method of TCP listener. Valid values: `HEAD`, `GET`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HealthCheckHttpPath

HTTP health check path of TCP listener.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HealthCheckHttpVersion

The HTTP version of the backend service. When the value of `health_check_type` of the health check protocol is `HTTP`, this field is required. Valid values: `HTTP/1.0`, `HTTP/1.1`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HealthCheckIntervalTime

Interval time of health check. Valid value ranges: [5~300] sec. and the default is 5 sec. NOTES: TCP/UDP/TCP_SSL listener allows direct configuration, HTTP/HTTPS listener needs to be configured in `tencentcloud_clb_listener_rule`.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HealthCheckPort

The health check port is the port of the backend service by default. Unless you want to specify a specific port, it is recommended to leave it blank. Only applicable to TCP/UDP listener.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HealthCheckRecvContext

It represents the result returned by the health check. When the value of `health_check_type` of the health check protocol is `CUSTOM`, this field is required. Only ASCII visible characters are allowed and the maximum length is 500. When `health_check_context_type` value is `HEX`, the characters of SendContext and RecvContext can only be selected in `0123456789ABCDEF` and the length must be even digits.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HealthCheckSendContext

It represents the content of the request sent by the health check. When the value of `health_check_type` of the health check protocol is `CUSTOM`, this field is required. Only visible ASCII characters are allowed and the maximum length is 500. When `health_check_context_type` value is `HEX`, the characters of SendContext and RecvContext can only be selected in `0123456789ABCDEF` and the length must be even digits.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HealthCheckSwitch

Indicates whether health check is enabled.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HealthCheckTimeOut

Response timeout of health check. Valid value ranges: [2~60] sec. Default is 2 sec. Response timeout needs to be less than check interval. NOTES: Only supports listeners of `TCP`,`UDP`,`TCP_SSL` protocol.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HealthCheckType

Protocol used for health check. Valid values: `CUSTOM`, `TCP`, `HTTP`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HealthCheckUnhealthNum

Unhealthy threshold of health check, and the default is `3`. If a success result is returned for the health check 3 consecutive times, the CVM is identified as unhealthy. The value range is [2-10]. NOTES: TCP/UDP/TCP_SSL listener allows direct configuration, HTTP/HTTPS listener needs to be configured in `tencentcloud_clb_listener_rule`.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ListenerName

Name of the CLB listener, and available values can only be Chinese characters, English letters, numbers, underscore and hyphen '-'.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Port

Port of the CLB listener.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Protocol

Type of protocol within the listener. Valid values: `TCP`, `UDP`, `HTTP`, `HTTPS` and `TCP_SSL`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Scheduler

Scheduling method of the CLB listener, and available values are 'WRR' and 'LEAST_CONN'. The default is 'WRR'. NOTES: The listener of `HTTP` and `HTTPS` protocol additionally supports the `IP Hash` method. NOTES: TCP/UDP/TCP_SSL listener allows direct configuration, HTTP/HTTPS listener needs to be configured in `tencentcloud_clb_listener_rule`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SessionExpireTime

Time of session persistence within the CLB listener. NOTES: Available when scheduler is specified as `WRR`, and not available when listener protocol is `TCP_SSL`. NOTES: TCP/UDP/TCP_SSL listener allows direct configuration, HTTP/HTTPS listener needs to be configured in `tencentcloud_clb_listener_rule`.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SniSwitch

Indicates whether SNI is enabled, and only supported with protocol `HTTPS`. If enabled, you can set a certificate for each rule in `tencentcloud_clb_listener_rule`, otherwise all rules have a certificate.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TargetType

Backend target type. Valid values: `NODE`, `TARGETGROUP`. `NODE` means to bind ordinary nodes, `TARGETGROUP` means to bind target group. NOTES: TCP/UDP/TCP_SSL listener must configuration, HTTP/HTTPS listener needs to be configured in tencentcloud_clb_listener_rule.

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

#### ListenerId

Returns the <code>ListenerId</code> value.

