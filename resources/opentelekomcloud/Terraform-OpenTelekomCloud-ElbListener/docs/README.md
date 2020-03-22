# Terraform::OpenTelekomCloud::ElbListener

Manages a classic loadbalancer listener resource within OpentelekomCloud.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::OpenTelekomCloud::ElbListener",
    "Properties" : {
        "<a href="#backendport" title="BackendPort">BackendPort</a>" : <i>Double</i>,
        "<a href="#backendprotocol" title="BackendProtocol">BackendProtocol</a>" : <i>String</i>,
        "<a href="#certificateid" title="CertificateId">CertificateId</a>" : <i>String</i>,
        "<a href="#certificates" title="Certificates">Certificates</a>" : <i>[ String, ... ]</i>,
        "<a href="#cookietimeout" title="CookieTimeout">CookieTimeout</a>" : <i>Double</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#lbalgorithm" title="LbAlgorithm">LbAlgorithm</a>" : <i>String</i>,
        "<a href="#loadbalancerid" title="LoadbalancerId">LoadbalancerId</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#protocol" title="Protocol">Protocol</a>" : <i>String</i>,
        "<a href="#protocolport" title="ProtocolPort">ProtocolPort</a>" : <i>Double</i>,
        "<a href="#region" title="Region">Region</a>" : <i>String</i>,
        "<a href="#sessionsticky" title="SessionSticky">SessionSticky</a>" : <i>Boolean</i>,
        "<a href="#sessionstickytype" title="SessionStickyType">SessionStickyType</a>" : <i>String</i>,
        "<a href="#sslciphers" title="SslCiphers">SslCiphers</a>" : <i>String</i>,
        "<a href="#sslprotocols" title="SslProtocols">SslProtocols</a>" : <i>String</i>,
        "<a href="#tcpdraining" title="TcpDraining">TcpDraining</a>" : <i>Boolean</i>,
        "<a href="#tcpdrainingtimeout" title="TcpDrainingTimeout">TcpDrainingTimeout</a>" : <i>Double</i>,
        "<a href="#tcptimeout" title="TcpTimeout">TcpTimeout</a>" : <i>Double</i>,
        "<a href="#udptimeout" title="UdpTimeout">UdpTimeout</a>" : <i>Double</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeouts.md">Timeouts</a></i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::OpenTelekomCloud::ElbListener
Properties:
    <a href="#backendport" title="BackendPort">BackendPort</a>: <i>Double</i>
    <a href="#backendprotocol" title="BackendProtocol">BackendProtocol</a>: <i>String</i>
    <a href="#certificateid" title="CertificateId">CertificateId</a>: <i>String</i>
    <a href="#certificates" title="Certificates">Certificates</a>: <i>
      - String</i>
    <a href="#cookietimeout" title="CookieTimeout">CookieTimeout</a>: <i>Double</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#lbalgorithm" title="LbAlgorithm">LbAlgorithm</a>: <i>String</i>
    <a href="#loadbalancerid" title="LoadbalancerId">LoadbalancerId</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#protocol" title="Protocol">Protocol</a>: <i>String</i>
    <a href="#protocolport" title="ProtocolPort">ProtocolPort</a>: <i>Double</i>
    <a href="#region" title="Region">Region</a>: <i>String</i>
    <a href="#sessionsticky" title="SessionSticky">SessionSticky</a>: <i>Boolean</i>
    <a href="#sessionstickytype" title="SessionStickyType">SessionStickyType</a>: <i>String</i>
    <a href="#sslciphers" title="SslCiphers">SslCiphers</a>: <i>String</i>
    <a href="#sslprotocols" title="SslProtocols">SslProtocols</a>: <i>String</i>
    <a href="#tcpdraining" title="TcpDraining">TcpDraining</a>: <i>Boolean</i>
    <a href="#tcpdrainingtimeout" title="TcpDrainingTimeout">TcpDrainingTimeout</a>: <i>Double</i>
    <a href="#tcptimeout" title="TcpTimeout">TcpTimeout</a>: <i>Double</i>
    <a href="#udptimeout" title="UdpTimeout">UdpTimeout</a>: <i>Double</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeouts.md">Timeouts</a></i>
</pre>

## Properties

#### BackendPort

Specifies the backend port. The value ranges from
1 to 65535.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BackendProtocol

Specifies the backend protocol. If the value
of protocol is UDP, the value of this parameter can only be UDP. The value can
be HTTP, TCP, or UDP.  Changing this creates a new elb listener.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CertificateId

Specifies the ID of the SSL certificate used
for security authentication when HTTPS is used to make API calls. This parameter
is mandatory if the value of protocol is HTTPS. The value can be obtained by
viewing the details of the SSL certificate.  Changing this creates a new elb
listener.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Certificates

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CookieTimeout

Specifies the cookie timeout period (minutes).
This parameter is valid when protocol is set to HTTP, session_sticky to true,
and session_sticky_type to insert. This parameter is invalid when protocol is
set to TCP or UDP. The value ranges from 1 to 1440.  Changing this creates a
new elb listener.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

Provides supplementary information about the listener.
The value is a string of 0 to 128 characters and cannot be <>.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LbAlgorithm

Specifies the load balancing algorithm for the
listener. The value can be roundrobin, leastconn, or source.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LoadbalancerId

Specifies the ID of the load balancer to which
the listener belongs.  Changing this creates a new elb listener.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Specifies the load balancer name. The name is a string
of 1 to 64 characters that consist of letters, digits, underscores (_), and
hyphens (-).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Protocol

Specifies the listening protocol used for layer 4
or 7. The value can be HTTP, TCP, HTTPS, or UDP.  Changing this creates a
new elb listener.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProtocolPort

Specifies the listening port. The value ranges from 1
to 65535.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Region

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SessionSticky

Specifies whether to enable sticky session.
The value can be true or false. The Sticky session is enabled when the value
is true, and is disabled when the value is false. If the value of protocol is
HTTP, HTTPS, or TCP, and the value of lb_algorithm is not roundrobin, the value
of this parameter can only be false.  Changing this creates a new elb listener.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SessionStickyType

Specifies the cookie processing method.
The value is insert. insert indicates that the cookie is inserted by the load
balancer. This parameter is valid when protocol is set to HTTP, and session_sticky
to true. The default value is insert. This parameter is invalid when protocol
is set to TCP or UDP, which means the parameter is empty.  Changing this creates
a new elb listener.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SslCiphers

Specifies the cipher suite of an encryption protocol.
This parameter is valid only when the value of protocol is set to HTTPS. The
value is Default, Extended, or Strict. The default value is Default. The value
can only be set to Extended if the value of ssl_protocols is set to TLSv1.2
TLSv1.1 TLSv1.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SslProtocols

Specifies the SSL protocol standard supported
by a tracker, which is used for enabling specified encryption protocols. This
parameter is valid only when the value of protocol is set to HTTPS. The value
is TLSv1.2 or TLSv1.2 TLSv1.1 TLSv1. The default value is TLSv1.2. Changing
this creates a new elb listener.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TcpDraining

Specifies whether to maintain the TCP connection
to the backend ECS after the ECS is deleted. This parameter is valid when protocol
is set to TCP. The value can be true or false.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TcpDrainingTimeout

Specifies the timeout duration (minutes)
for the TCP connection to the backend ECS after the ECS is deleted. This parameter
is valid when protocol is set to TCP, and tcp_draining to true. The value ranges
from 0 to 60.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TcpTimeout

Specifies the TCP timeout period (minutes). This
parameter is valid when protocol is set to TCP. The value ranges from 1 to 5.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UdpTimeout

Specifies the UDP timeout duration (minutes). This
parameter is valid when protocol is set to UDP. The value ranges from 1 to 1440.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeouts.md">Timeouts</a>

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

