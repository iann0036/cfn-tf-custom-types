# Terraform::Alicloud::SlbRule

A forwarding rule is configured in `HTTP`/`HTTPS` listener and it used to listen a list of backend servers which in one specified virtual backend server group.
You can add forwarding rules to a listener to forward requests based on the domain names or the URL in the request.

-> **NOTE:** One virtual backend server group can be attached in multiple forwarding rules.

-> **NOTE:** At least one "Domain" or "Url" must be specified when creating a new rule.

-> **NOTE:** Having the same 'Domain' and 'Url' rule can not be created repeatedly in the one listener.

-> **NOTE:** Rule only be created in the `HTTP` or `HTTPS` listener.

-> **NOTE:** Only rule's virtual server group can be modified.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Alicloud::SlbRule",
    "Properties" : {
        "<a href="#cookie" title="Cookie">Cookie</a>" : <i>String</i>,
        "<a href="#cookietimeout" title="CookieTimeout">CookieTimeout</a>" : <i>Double</i>,
        "<a href="#deleteprotectionvalidation" title="DeleteProtectionValidation">DeleteProtectionValidation</a>" : <i>Boolean</i>,
        "<a href="#domain" title="Domain">Domain</a>" : <i>String</i>,
        "<a href="#frontendport" title="FrontendPort">FrontendPort</a>" : <i>Double</i>,
        "<a href="#healthcheck" title="HealthCheck">HealthCheck</a>" : <i>String</i>,
        "<a href="#healthcheckconnectport" title="HealthCheckConnectPort">HealthCheckConnectPort</a>" : <i>Double</i>,
        "<a href="#healthcheckdomain" title="HealthCheckDomain">HealthCheckDomain</a>" : <i>String</i>,
        "<a href="#healthcheckhttpcode" title="HealthCheckHttpCode">HealthCheckHttpCode</a>" : <i>String</i>,
        "<a href="#healthcheckinterval" title="HealthCheckInterval">HealthCheckInterval</a>" : <i>Double</i>,
        "<a href="#healthchecktimeout" title="HealthCheckTimeout">HealthCheckTimeout</a>" : <i>Double</i>,
        "<a href="#healthcheckuri" title="HealthCheckUri">HealthCheckUri</a>" : <i>String</i>,
        "<a href="#healthythreshold" title="HealthyThreshold">HealthyThreshold</a>" : <i>Double</i>,
        "<a href="#listenersync" title="ListenerSync">ListenerSync</a>" : <i>String</i>,
        "<a href="#loadbalancerid" title="LoadBalancerId">LoadBalancerId</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#scheduler" title="Scheduler">Scheduler</a>" : <i>String</i>,
        "<a href="#servergroupid" title="ServerGroupId">ServerGroupId</a>" : <i>String</i>,
        "<a href="#stickysession" title="StickySession">StickySession</a>" : <i>String</i>,
        "<a href="#stickysessiontype" title="StickySessionType">StickySessionType</a>" : <i>String</i>,
        "<a href="#unhealthythreshold" title="UnhealthyThreshold">UnhealthyThreshold</a>" : <i>Double</i>,
        "<a href="#url" title="Url">Url</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Alicloud::SlbRule
Properties:
    <a href="#cookie" title="Cookie">Cookie</a>: <i>String</i>
    <a href="#cookietimeout" title="CookieTimeout">CookieTimeout</a>: <i>Double</i>
    <a href="#deleteprotectionvalidation" title="DeleteProtectionValidation">DeleteProtectionValidation</a>: <i>Boolean</i>
    <a href="#domain" title="Domain">Domain</a>: <i>String</i>
    <a href="#frontendport" title="FrontendPort">FrontendPort</a>: <i>Double</i>
    <a href="#healthcheck" title="HealthCheck">HealthCheck</a>: <i>String</i>
    <a href="#healthcheckconnectport" title="HealthCheckConnectPort">HealthCheckConnectPort</a>: <i>Double</i>
    <a href="#healthcheckdomain" title="HealthCheckDomain">HealthCheckDomain</a>: <i>String</i>
    <a href="#healthcheckhttpcode" title="HealthCheckHttpCode">HealthCheckHttpCode</a>: <i>String</i>
    <a href="#healthcheckinterval" title="HealthCheckInterval">HealthCheckInterval</a>: <i>Double</i>
    <a href="#healthchecktimeout" title="HealthCheckTimeout">HealthCheckTimeout</a>: <i>Double</i>
    <a href="#healthcheckuri" title="HealthCheckUri">HealthCheckUri</a>: <i>String</i>
    <a href="#healthythreshold" title="HealthyThreshold">HealthyThreshold</a>: <i>Double</i>
    <a href="#listenersync" title="ListenerSync">ListenerSync</a>: <i>String</i>
    <a href="#loadbalancerid" title="LoadBalancerId">LoadBalancerId</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#scheduler" title="Scheduler">Scheduler</a>: <i>String</i>
    <a href="#servergroupid" title="ServerGroupId">ServerGroupId</a>: <i>String</i>
    <a href="#stickysession" title="StickySession">StickySession</a>: <i>String</i>
    <a href="#stickysessiontype" title="StickySessionType">StickySessionType</a>: <i>String</i>
    <a href="#unhealthythreshold" title="UnhealthyThreshold">UnhealthyThreshold</a>: <i>Double</i>
    <a href="#url" title="Url">Url</a>: <i>String</i>
</pre>

## Properties

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

#### Domain

Domain name of the forwarding rule. It can contain letters a-z, numbers 0-9, hyphens (-), and periods (.),
and wildcard characters. The following two domain name formats are supported:
- Standard domain name: www.test.com
- Wildcard domain name: *.test.com. wildcard (*) must be the first character in the format of (*.).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FrontendPort

The listener frontend port which is used to launch the new forwarding rule. Valid range: [1-65535].

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HealthCheck

Whether to enable health check. Valid values are`on` and `off`. TCP and UDP listener's HealthCheck is always on, so it will be ignore when launching TCP or UDP listener. This parameter is required  and takes effect only when ListenerSync is set to off.

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

#### HealthCheckTimeout

Maximum timeout of each health check response. It is required when `health_check` is on. Valid value range: [1-300] in seconds. Default to 5. Note: If `health_check_timeout` < `health_check_interval`, its will be replaced by `health_check_interval`.

_Required_: No

_Type_: Double

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

#### ListenerSync

Indicates whether a forwarding rule inherits the settings of a health check , session persistence, and scheduling algorithm from a listener. Default to on.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LoadBalancerId

The Load Balancer ID which is used to launch the new forwarding rule.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Name of the forwarding rule. Our plugin provides a default name: "tf-slb-rule".

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Scheduler

Scheduling algorithm, Valid values are `wrr`, `rr` and `wlc`.  Default to "wrr". This parameter is required  and takes effect only when ListenerSync is set to off.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServerGroupId

ID of a virtual server group that will be forwarded.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StickySession

Whether to enable session persistence, Valid values are `on` and `off`. Default to `off`. This parameter is required  and takes effect only when ListenerSync is set to off.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StickySessionType

Mode for handling the cookie. If `sticky_session` is "on", it is mandatory. Otherwise, it will be ignored. Valid values are `insert` and `server`. `insert` means it is inserted from Server Load Balancer; `server` means the Server Load Balancer learns from the backend server.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UnhealthyThreshold

Threshold determining the result of the health check is fail. It is required when `health_check` is on. Valid value range: [1-10] in seconds. Default to 3.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Url

Domain of the forwarding rule. It must be 2-80 characters in length. Only letters a-z, numbers 0-9,
and characters '-' '/' '?' '%' '#' and '&' are allowed. URLs must be started with the character '/', but cannot be '/' alone.

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

