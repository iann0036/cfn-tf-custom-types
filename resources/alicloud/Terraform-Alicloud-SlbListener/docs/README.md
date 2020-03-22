# Terraform::Alicloud::SlbListener

Provides an Application Load Balancer Listener resource.

For information about slb and how to use it, see [What is Server Load Balancer](https://www.alibabacloud.com/help/doc-detail/27539.htm).

For information about listener and how to use it, to see the following:

* [Configure a HTTP Listener](https://www.alibabacloud.com/help/doc-detail/27592.htm).
* [Configure a HTTPS Listener](https://www.alibabacloud.com/help/doc-detail/27593.htm).
* [Configure a TCP Listener](https://www.alibabacloud.com/help/doc-detail/27594.htm).
* [Configure a UDP Listener](https://www.alibabacloud.com/help/doc-detail/27595.htm).

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Alicloud::SlbListener",
    "Properties" : {
        "<a href="#aclid" title="AclId">AclId</a>" : <i>String</i>,
        "<a href="#aclstatus" title="AclStatus">AclStatus</a>" : <i>String</i>,
        "<a href="#acltype" title="AclType">AclType</a>" : <i>String</i>,
        "<a href="#backendport" title="BackendPort">BackendPort</a>" : <i>Double</i>,
        "<a href="#bandwidth" title="Bandwidth">Bandwidth</a>" : <i>Double</i>,
        "<a href="#cookie" title="Cookie">Cookie</a>" : <i>String</i>,
        "<a href="#cookietimeout" title="CookieTimeout">CookieTimeout</a>" : <i>Double</i>,
        "<a href="#deleteprotectionvalidation" title="DeleteProtectionValidation">DeleteProtectionValidation</a>" : <i>Boolean</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#enablehttp2" title="EnableHttp2">EnableHttp2</a>" : <i>String</i>,
        "<a href="#establishedtimeout" title="EstablishedTimeout">EstablishedTimeout</a>" : <i>Double</i>,
        "<a href="#forwardport" title="ForwardPort">ForwardPort</a>" : <i>Double</i>,
        "<a href="#frontendport" title="FrontendPort">FrontendPort</a>" : <i>Double</i>,
        "<a href="#gzip" title="Gzip">Gzip</a>" : <i>Boolean</i>,
        "<a href="#healthcheck" title="HealthCheck">HealthCheck</a>" : <i>String</i>,
        "<a href="#healthcheckconnectport" title="HealthCheckConnectPort">HealthCheckConnectPort</a>" : <i>Double</i>,
        "<a href="#healthcheckdomain" title="HealthCheckDomain">HealthCheckDomain</a>" : <i>String</i>,
        "<a href="#healthcheckhttpcode" title="HealthCheckHttpCode">HealthCheckHttpCode</a>" : <i>String</i>,
        "<a href="#healthcheckinterval" title="HealthCheckInterval">HealthCheckInterval</a>" : <i>Double</i>,
        "<a href="#healthcheckmethod" title="HealthCheckMethod">HealthCheckMethod</a>" : <i>String</i>,
        "<a href="#healthchecktimeout" title="HealthCheckTimeout">HealthCheckTimeout</a>" : <i>Double</i>,
        "<a href="#healthchecktype" title="HealthCheckType">HealthCheckType</a>" : <i>String</i>,
        "<a href="#healthcheckuri" title="HealthCheckUri">HealthCheckUri</a>" : <i>String</i>,
        "<a href="#healthythreshold" title="HealthyThreshold">HealthyThreshold</a>" : <i>Double</i>,
        "<a href="#idletimeout" title="IdleTimeout">IdleTimeout</a>" : <i>Double</i>,
        "<a href="#instanceport" title="InstancePort">InstancePort</a>" : <i>Double</i>,
        "<a href="#lbport" title="LbPort">LbPort</a>" : <i>Double</i>,
        "<a href="#lbprotocol" title="LbProtocol">LbProtocol</a>" : <i>String</i>,
        "<a href="#listenerforward" title="ListenerForward">ListenerForward</a>" : <i>String</i>,
        "<a href="#loadbalancerid" title="LoadBalancerId">LoadBalancerId</a>" : <i>String</i>,
        "<a href="#masterslaveservergroupid" title="MasterSlaveServerGroupId">MasterSlaveServerGroupId</a>" : <i>String</i>,
        "<a href="#persistencetimeout" title="PersistenceTimeout">PersistenceTimeout</a>" : <i>Double</i>,
        "<a href="#protocol" title="Protocol">Protocol</a>" : <i>String</i>,
        "<a href="#requesttimeout" title="RequestTimeout">RequestTimeout</a>" : <i>Double</i>,
        "<a href="#scheduler" title="Scheduler">Scheduler</a>" : <i>String</i>,
        "<a href="#servercertificateid" title="ServerCertificateId">ServerCertificateId</a>" : <i>String</i>,
        "<a href="#servergroupid" title="ServerGroupId">ServerGroupId</a>" : <i>String</i>,
        "<a href="#sslcertificateid" title="SslCertificateId">SslCertificateId</a>" : <i>String</i>,
        "<a href="#stickysession" title="StickySession">StickySession</a>" : <i>String</i>,
        "<a href="#stickysessiontype" title="StickySessionType">StickySessionType</a>" : <i>String</i>,
        "<a href="#tlscipherpolicy" title="TlsCipherPolicy">TlsCipherPolicy</a>" : <i>String</i>,
        "<a href="#unhealthythreshold" title="UnhealthyThreshold">UnhealthyThreshold</a>" : <i>Double</i>,
        "<a href="#xforwardedfor" title="XForwardedFor">XForwardedFor</a>" : <i>[ <a href="xforwardedfor.md">XForwardedFor</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Alicloud::SlbListener
Properties:
    <a href="#aclid" title="AclId">AclId</a>: <i>String</i>
    <a href="#aclstatus" title="AclStatus">AclStatus</a>: <i>String</i>
    <a href="#acltype" title="AclType">AclType</a>: <i>String</i>
    <a href="#backendport" title="BackendPort">BackendPort</a>: <i>Double</i>
    <a href="#bandwidth" title="Bandwidth">Bandwidth</a>: <i>Double</i>
    <a href="#cookie" title="Cookie">Cookie</a>: <i>String</i>
    <a href="#cookietimeout" title="CookieTimeout">CookieTimeout</a>: <i>Double</i>
    <a href="#deleteprotectionvalidation" title="DeleteProtectionValidation">DeleteProtectionValidation</a>: <i>Boolean</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#enablehttp2" title="EnableHttp2">EnableHttp2</a>: <i>String</i>
    <a href="#establishedtimeout" title="EstablishedTimeout">EstablishedTimeout</a>: <i>Double</i>
    <a href="#forwardport" title="ForwardPort">ForwardPort</a>: <i>Double</i>
    <a href="#frontendport" title="FrontendPort">FrontendPort</a>: <i>Double</i>
    <a href="#gzip" title="Gzip">Gzip</a>: <i>Boolean</i>
    <a href="#healthcheck" title="HealthCheck">HealthCheck</a>: <i>String</i>
    <a href="#healthcheckconnectport" title="HealthCheckConnectPort">HealthCheckConnectPort</a>: <i>Double</i>
    <a href="#healthcheckdomain" title="HealthCheckDomain">HealthCheckDomain</a>: <i>String</i>
    <a href="#healthcheckhttpcode" title="HealthCheckHttpCode">HealthCheckHttpCode</a>: <i>String</i>
    <a href="#healthcheckinterval" title="HealthCheckInterval">HealthCheckInterval</a>: <i>Double</i>
    <a href="#healthcheckmethod" title="HealthCheckMethod">HealthCheckMethod</a>: <i>String</i>
    <a href="#healthchecktimeout" title="HealthCheckTimeout">HealthCheckTimeout</a>: <i>Double</i>
    <a href="#healthchecktype" title="HealthCheckType">HealthCheckType</a>: <i>String</i>
    <a href="#healthcheckuri" title="HealthCheckUri">HealthCheckUri</a>: <i>String</i>
    <a href="#healthythreshold" title="HealthyThreshold">HealthyThreshold</a>: <i>Double</i>
    <a href="#idletimeout" title="IdleTimeout">IdleTimeout</a>: <i>Double</i>
    <a href="#instanceport" title="InstancePort">InstancePort</a>: <i>Double</i>
    <a href="#lbport" title="LbPort">LbPort</a>: <i>Double</i>
    <a href="#lbprotocol" title="LbProtocol">LbProtocol</a>: <i>String</i>
    <a href="#listenerforward" title="ListenerForward">ListenerForward</a>: <i>String</i>
    <a href="#loadbalancerid" title="LoadBalancerId">LoadBalancerId</a>: <i>String</i>
    <a href="#masterslaveservergroupid" title="MasterSlaveServerGroupId">MasterSlaveServerGroupId</a>: <i>String</i>
    <a href="#persistencetimeout" title="PersistenceTimeout">PersistenceTimeout</a>: <i>Double</i>
    <a href="#protocol" title="Protocol">Protocol</a>: <i>String</i>
    <a href="#requesttimeout" title="RequestTimeout">RequestTimeout</a>: <i>Double</i>
    <a href="#scheduler" title="Scheduler">Scheduler</a>: <i>String</i>
    <a href="#servercertificateid" title="ServerCertificateId">ServerCertificateId</a>: <i>String</i>
    <a href="#servergroupid" title="ServerGroupId">ServerGroupId</a>: <i>String</i>
    <a href="#sslcertificateid" title="SslCertificateId">SslCertificateId</a>: <i>String</i>
    <a href="#stickysession" title="StickySession">StickySession</a>: <i>String</i>
    <a href="#stickysessiontype" title="StickySessionType">StickySessionType</a>: <i>String</i>
    <a href="#tlscipherpolicy" title="TlsCipherPolicy">TlsCipherPolicy</a>: <i>String</i>
    <a href="#unhealthythreshold" title="UnhealthyThreshold">UnhealthyThreshold</a>: <i>Double</i>
    <a href="#xforwardedfor" title="XForwardedFor">XForwardedFor</a>: <i>
      - <a href="xforwardedfor.md">XForwardedFor</a></i>
</pre>

## Properties

#### AclId

the id of access control list to be apply on the listener, is the id of resource alicloud_slb_acl. If `acl_status` is "on", it is mandatory. Otherwise, it will be ignored.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AclStatus

Whether to enable "acl(access control list)", the acl is specified by `acl_id`. Valid values are `on` and `off`. Default to `off`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AclType

Mode for handling the acl specified by acl_id. If `acl_status` is "on", it is mandatory. Otherwise, it will be ignored. Valid values are `white` and `black`. `white` means the Listener can only be accessed by client ip belongs to the acl; `black` means the Listener can not be accessed by client ip belongs to the acl.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BackendPort

Port used by the Server Load Balancer instance backend. Valid value range: [1-65535].

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Bandwidth

Bandwidth peak of Listener. For the public network instance charged per traffic consumed, the Bandwidth on Listener can be set to -1, indicating the bandwidth peak is unlimited. Valid values are [-1, 1-1000] in Mbps.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Cookie

The cookie configured on the server. It is mandatory when `sticky_session` is "on" and `sticky_session_type` is "server". Otherwise, it will be ignored. Valid value：String in line with RFC 2965, with length being 1- 200. It only contains characters such as ASCII codes, English letters and digits instead of the comma, semicolon or spacing, and it cannot start with $.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CookieTimeout

Cookie timeout. It is mandatory when `sticky_session` is "on" and `sticky_session_type` is "insert". Otherwise, it will be ignored. Valid value range: [1-86400] in seconds.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeleteProtectionValidation

Checking DeleteProtection of SLB instance before deleting. If true, this resource will not be deleted when its SLB instance enabled DeleteProtection. Default to false.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

The description of slb listener. This description can have a string of 1 to 80 characters. Default value: null.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableHttp2

Whether to enable https listener support http2 or not. Valid values are `on` and `off`. Default to `on`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EstablishedTimeout

Timeout of tcp listener established connection idle timeout. Valid value range: [10-900] in seconds. Default to 900.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ForwardPort

The port that http redirect to https.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FrontendPort

Port used by the Server Load Balancer instance frontend. Valid value range: [1-65535].

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Gzip

Whether to enable "Gzip Compression". If enabled, files of specific file types will be compressed, otherwise, no files will be compressed. Default to true. Available in v1.13.0+.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HealthCheck

Whether to enable health check. Valid values are`on` and `off`. TCP and UDP listener's HealthCheck is always on, so it will be ignore when launching TCP or UDP listener.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HealthCheckConnectPort

Port used for health check. Valid value range: [1-65535]. Default to "None" means the backend server port is used.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HealthCheckDomain

Domain name used for health check. When it used to launch TCP listener, `health_check_type` must be "http". Its length is limited to 1-80 and only characters such as letters, digits, ‘-‘ and ‘.’ are allowed. When it is not set or empty,  Server Load Balancer uses the private network IP address of each backend server as Domain used for health check.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HealthCheckHttpCode

Regular health check HTTP status code. Multiple codes are segmented by “,”. It is required when `health_check` is on. Default to `http_2xx`.  Valid values are: `http_2xx`,  `http_3xx`, `http_4xx` and `http_5xx`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HealthCheckInterval

Time interval of health checks. It is required when `health_check` is on. Valid value range: [1-50] in seconds. Default to 2.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HealthCheckMethod

The method of health check. Valid values: ["head", "get"].

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HealthCheckTimeout

Maximum timeout of each health check response. It is required when `health_check` is on. Valid value range: [1-300] in seconds. Default to 5. Note: If `health_check_timeout` < `health_check_interval`, its will be replaced by `health_check_interval`.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HealthCheckType

Type of health check. Valid values are: `tcp` and `http`. Default to `tcp` . TCP supports TCP and HTTP health check mode, you can select the particular mode depending on your application.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HealthCheckUri

URI used for health check. When it used to launch TCP listener, `health_check_type` must be "http". Its length is limited to 1-80 and it must start with /. Only characters such as letters, digits, ‘-’, ‘/’, ‘.’, ‘%’, ‘?’, #’ and ‘&’ are allowed.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HealthyThreshold

Threshold determining the result of the health check is success. It is required when `health_check` is on. Valid value range: [1-10] in seconds. Default to 3.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IdleTimeout

Timeout of http or https listener established connection idle timeout. Valid value range: [1-60] in seconds. Default to 15.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InstancePort

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LbPort

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LbProtocol

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ListenerForward

Whether to enable http redirect to https, Valid values are `on` and `off`. Default to `off`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LoadBalancerId

The Load Balancer ID which is used to launch a new listener.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MasterSlaveServerGroupId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PersistenceTimeout

Timeout of connection persistence. Valid value range: [0-3600] in seconds. Default to 0 and means closing it.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Protocol

The protocol to listen on. Valid values are [`http`, `https`, `tcp`, `udp`].

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RequestTimeout

Timeout of http or https listener request (which does not get response from backend) timeout. Valid value range: [1-180] in seconds. Default to 60.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Scheduler

Scheduling algorithm, Valid values are `wrr`, `rr` and `wlc`.  Default to "wrr".

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServerCertificateId

SLB Server certificate ID. It is required when `protocol` is `https`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServerGroupId

the id of server group to be apply on the listener, is the id of resource `alicloud_slb_server_group`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SslCertificateId

It has been deprecated from 1.59.0 and using `server_certificate_id` instead.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StickySession

Whether to enable session persistence, Valid values are `on` and `off`. Default to `off`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StickySessionType

Mode for handling the cookie. If `sticky_session` is "on", it is mandatory. Otherwise, it will be ignored. Valid values are `insert` and `server`. `insert` means it is inserted from Server Load Balancer; `server` means the Server Load Balancer learns from the backend server.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TlsCipherPolicy

Https listener TLS cipher policy. Valid values are `tls_cipher_policy_1_0`, `tls_cipher_policy_1_1`, `tls_cipher_policy_1_2`, `tls_cipher_policy_1_2_strict`. Default to `tls_cipher_policy_1_0`. Currently the `tls_cipher_policy` can not be updated when load balancer instance is "Shared-Performance".

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UnhealthyThreshold

Threshold determining the result of the health check is fail. It is required when `health_check` is on. Valid value range: [1-10] in seconds. Default to 3.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### XForwardedFor

_Required_: No

_Type_: List of <a href="xforwardedfor.md">XForwardedFor</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the Id.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Id

Returns the <code>Id</code> value.

