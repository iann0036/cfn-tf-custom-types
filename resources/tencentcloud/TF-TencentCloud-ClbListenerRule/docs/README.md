# TF::TencentCloud::ClbListenerRule

Provides a resource to create a CLB listener rule.

-> **NOTE:** This resource only be applied to the HTTP or HTTPS listeners.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::TencentCloud::ClbListenerRule",
    "Properties" : {
        "<a href="#certificatecaid" title="CertificateCaId">CertificateCaId</a>" : <i>String</i>,
        "<a href="#certificateid" title="CertificateId">CertificateId</a>" : <i>String</i>,
        "<a href="#certificatesslmode" title="CertificateSslMode">CertificateSslMode</a>" : <i>String</i>,
        "<a href="#clbid" title="ClbId">ClbId</a>" : <i>String</i>,
        "<a href="#domain" title="Domain">Domain</a>" : <i>String</i>,
        "<a href="#forwardtype" title="ForwardType">ForwardType</a>" : <i>String</i>,
        "<a href="#healthcheckhealthnum" title="HealthCheckHealthNum">HealthCheckHealthNum</a>" : <i>Double</i>,
        "<a href="#healthcheckhttpcode" title="HealthCheckHttpCode">HealthCheckHttpCode</a>" : <i>Double</i>,
        "<a href="#healthcheckhttpdomain" title="HealthCheckHttpDomain">HealthCheckHttpDomain</a>" : <i>String</i>,
        "<a href="#healthcheckhttpmethod" title="HealthCheckHttpMethod">HealthCheckHttpMethod</a>" : <i>String</i>,
        "<a href="#healthcheckhttppath" title="HealthCheckHttpPath">HealthCheckHttpPath</a>" : <i>String</i>,
        "<a href="#healthcheckintervaltime" title="HealthCheckIntervalTime">HealthCheckIntervalTime</a>" : <i>Double</i>,
        "<a href="#healthcheckswitch" title="HealthCheckSwitch">HealthCheckSwitch</a>" : <i>Boolean</i>,
        "<a href="#healthcheckunhealthnum" title="HealthCheckUnhealthNum">HealthCheckUnhealthNum</a>" : <i>Double</i>,
        "<a href="#http2switch" title="Http2Switch">Http2Switch</a>" : <i>Boolean</i>,
        "<a href="#listenerid" title="ListenerId">ListenerId</a>" : <i>String</i>,
        "<a href="#scheduler" title="Scheduler">Scheduler</a>" : <i>String</i>,
        "<a href="#sessionexpiretime" title="SessionExpireTime">SessionExpireTime</a>" : <i>Double</i>,
        "<a href="#targettype" title="TargetType">TargetType</a>" : <i>String</i>,
        "<a href="#url" title="Url">Url</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::TencentCloud::ClbListenerRule
Properties:
    <a href="#certificatecaid" title="CertificateCaId">CertificateCaId</a>: <i>String</i>
    <a href="#certificateid" title="CertificateId">CertificateId</a>: <i>String</i>
    <a href="#certificatesslmode" title="CertificateSslMode">CertificateSslMode</a>: <i>String</i>
    <a href="#clbid" title="ClbId">ClbId</a>: <i>String</i>
    <a href="#domain" title="Domain">Domain</a>: <i>String</i>
    <a href="#forwardtype" title="ForwardType">ForwardType</a>: <i>String</i>
    <a href="#healthcheckhealthnum" title="HealthCheckHealthNum">HealthCheckHealthNum</a>: <i>Double</i>
    <a href="#healthcheckhttpcode" title="HealthCheckHttpCode">HealthCheckHttpCode</a>: <i>Double</i>
    <a href="#healthcheckhttpdomain" title="HealthCheckHttpDomain">HealthCheckHttpDomain</a>: <i>String</i>
    <a href="#healthcheckhttpmethod" title="HealthCheckHttpMethod">HealthCheckHttpMethod</a>: <i>String</i>
    <a href="#healthcheckhttppath" title="HealthCheckHttpPath">HealthCheckHttpPath</a>: <i>String</i>
    <a href="#healthcheckintervaltime" title="HealthCheckIntervalTime">HealthCheckIntervalTime</a>: <i>Double</i>
    <a href="#healthcheckswitch" title="HealthCheckSwitch">HealthCheckSwitch</a>: <i>Boolean</i>
    <a href="#healthcheckunhealthnum" title="HealthCheckUnhealthNum">HealthCheckUnhealthNum</a>: <i>Double</i>
    <a href="#http2switch" title="Http2Switch">Http2Switch</a>: <i>Boolean</i>
    <a href="#listenerid" title="ListenerId">ListenerId</a>: <i>String</i>
    <a href="#scheduler" title="Scheduler">Scheduler</a>: <i>String</i>
    <a href="#sessionexpiretime" title="SessionExpireTime">SessionExpireTime</a>: <i>Double</i>
    <a href="#targettype" title="TargetType">TargetType</a>: <i>String</i>
    <a href="#url" title="Url">Url</a>: <i>String</i>
</pre>

## Properties

#### CertificateCaId

ID of the client certificate. NOTES: Only supports listeners of HTTPS protocol.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CertificateId

ID of the server certificate. NOTES: Only supports listeners of HTTPS protocol.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CertificateSslMode

Type of certificate. Valid values: `UNIDIRECTIONAL`, `MUTUAL`. NOTES: Only supports listeners of HTTPS protocol.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClbId

ID of CLB instance.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Domain

Domain name of the listener rule.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ForwardType

Forwarding protocol between the CLB instance and real server. Valid values: `HTTP`, `HTTPS`, `TRPC`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HealthCheckHealthNum

Health threshold of health check, and the default is `3`. If a success result is returned for the health check 3 consecutive times, indicates that the forwarding is normal. The value range is [2-10]. NOTES: TCP/UDP/TCP_SSL listener allows direct configuration, HTTP/HTTPS listener needs to be configured in `tencentcloud_clb_listener_rule`.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HealthCheckHttpCode

HTTP Status Code. The default is 31. Valid value ranges: [1~31]. `1 means the return value '1xx' is health. `2` means the return value '2xx' is health. `4` means the return value '3xx' is health. `8` means the return value '4xx' is health. 16 means the return value '5xx' is health. If you want multiple return codes to indicate health, need to add the corresponding values. NOTES: The 'HTTP' health check of the 'TCP' listener only supports specifying one health check status code. NOTES: Only supports listeners of 'HTTP' and 'HTTPS' protocol.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HealthCheckHttpDomain

Domain name of health check. NOTES: Only supports listeners of `HTTP` and `HTTPS` protocol.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HealthCheckHttpMethod

Methods of health check. NOTES: Only supports listeners of `HTTP` and `HTTPS` protocol. The default is `HEAD`, the available value are `HEAD` and `GET`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HealthCheckHttpPath

Path of health check. NOTES: Only supports listeners of `HTTP` and `HTTPS` protocol.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HealthCheckIntervalTime

Interval time of health check. Valid value ranges: (5~300) sec. and the default is `5` sec. NOTES: TCP/UDP/TCP_SSL listener allows direct configuration, HTTP/HTTPS listener needs to be configured in `tencentcloud_clb_listener_rule`.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HealthCheckSwitch

Indicates whether health check is enabled.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HealthCheckUnhealthNum

Unhealthy threshold of health check, and the default is `3`. If the unhealthy result is returned 3 consecutive times, indicates that the forwarding is abnormal. The value range is [2-10].  NOTES: TCP/UDP/TCP_SSL listener allows direct configuration, HTTP/HTTPS listener needs to be configured in `tencentcloud_clb_listener_rule`.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Http2Switch

Indicate to apply HTTP2.0 protocol or not.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ListenerId

ID of CLB listener.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Scheduler

Scheduling method of the CLB listener rules. Valid values: `WRR`, `IP HASH`, `LEAST_CONN`. The default is `WRR`.  NOTES: TCP/UDP/TCP_SSL listener allows direct configuration, HTTP/HTTPS listener needs to be configured in `tencentcloud_clb_listener_rule`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SessionExpireTime

Time of session persistence within the CLB listener. NOTES: Available when scheduler is specified as `WRR`, and not available when listener protocol is `TCP_SSL`.  NOTES: TCP/UDP/TCP_SSL listener allows direct configuration, HTTP/HTTPS listener needs to be configured in `tencentcloud_clb_listener_rule`.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TargetType

Backend target type. Valid values: `NODE`, `TARGETGROUP`. `NODE` means to bind ordinary nodes, `TARGETGROUP` means to bind target group.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Url

Url of the listener rule.

_Required_: Yes

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

#### RuleId

Returns the <code>RuleId</code> value.

