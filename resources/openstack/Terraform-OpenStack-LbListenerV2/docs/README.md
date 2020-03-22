# Terraform::OpenStack::LbListenerV2

Manages a V2 listener resource within OpenStack.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::OpenStack::LbListenerV2",
    "Properties" : {
        "<a href="#adminstateup" title="AdminStateUp">AdminStateUp</a>" : <i>Boolean</i>,
        "<a href="#connectionlimit" title="ConnectionLimit">ConnectionLimit</a>" : <i>Double</i>,
        "<a href="#defaultpoolid" title="DefaultPoolId">DefaultPoolId</a>" : <i>String</i>,
        "<a href="#defaulttlscontainerref" title="DefaultTlsContainerRef">DefaultTlsContainerRef</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#insertheaders" title="InsertHeaders">InsertHeaders</a>" : <i>[ <a href="insertheaders.md">InsertHeaders</a>, ... ]</i>,
        "<a href="#loadbalancerid" title="LoadbalancerId">LoadbalancerId</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#protocol" title="Protocol">Protocol</a>" : <i>String</i>,
        "<a href="#protocolport" title="ProtocolPort">ProtocolPort</a>" : <i>Double</i>,
        "<a href="#region" title="Region">Region</a>" : <i>String</i>,
        "<a href="#snicontainerrefs" title="SniContainerRefs">SniContainerRefs</a>" : <i>[ String, ... ]</i>,
        "<a href="#tenantid" title="TenantId">TenantId</a>" : <i>String</i>,
        "<a href="#timeoutclientdata" title="TimeoutClientData">TimeoutClientData</a>" : <i>Double</i>,
        "<a href="#timeoutmemberconnect" title="TimeoutMemberConnect">TimeoutMemberConnect</a>" : <i>Double</i>,
        "<a href="#timeoutmemberdata" title="TimeoutMemberData">TimeoutMemberData</a>" : <i>Double</i>,
        "<a href="#timeouttcpinspect" title="TimeoutTcpInspect">TimeoutTcpInspect</a>" : <i>Double</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeouts.md">Timeouts</a></i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::OpenStack::LbListenerV2
Properties:
    <a href="#adminstateup" title="AdminStateUp">AdminStateUp</a>: <i>Boolean</i>
    <a href="#connectionlimit" title="ConnectionLimit">ConnectionLimit</a>: <i>Double</i>
    <a href="#defaultpoolid" title="DefaultPoolId">DefaultPoolId</a>: <i>String</i>
    <a href="#defaulttlscontainerref" title="DefaultTlsContainerRef">DefaultTlsContainerRef</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#insertheaders" title="InsertHeaders">InsertHeaders</a>: <i>
      - <a href="insertheaders.md">InsertHeaders</a></i>
    <a href="#loadbalancerid" title="LoadbalancerId">LoadbalancerId</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#protocol" title="Protocol">Protocol</a>: <i>String</i>
    <a href="#protocolport" title="ProtocolPort">ProtocolPort</a>: <i>Double</i>
    <a href="#region" title="Region">Region</a>: <i>String</i>
    <a href="#snicontainerrefs" title="SniContainerRefs">SniContainerRefs</a>: <i>
      - String</i>
    <a href="#tenantid" title="TenantId">TenantId</a>: <i>String</i>
    <a href="#timeoutclientdata" title="TimeoutClientData">TimeoutClientData</a>: <i>Double</i>
    <a href="#timeoutmemberconnect" title="TimeoutMemberConnect">TimeoutMemberConnect</a>: <i>Double</i>
    <a href="#timeoutmemberdata" title="TimeoutMemberData">TimeoutMemberData</a>: <i>Double</i>
    <a href="#timeouttcpinspect" title="TimeoutTcpInspect">TimeoutTcpInspect</a>: <i>Double</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeouts.md">Timeouts</a></i>
</pre>

## Properties

#### AdminStateUp

The administrative state of the Listener.
A valid value is true (UP) or false (DOWN).

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConnectionLimit

The maximum number of connections allowed
for the Listener.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefaultPoolId

The ID of the default pool with which the
Listener is associated.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefaultTlsContainerRef

A reference to a Barbican Secrets
container which stores TLS information. This is required if the protocol
is `TERMINATED_HTTPS`. See
[here](https://wiki.openstack.org/wiki/Network/LBaaS/docs/how-to-create-tls-loadbalancer)
for more information.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

Human-readable description for the Listener.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InsertHeaders

The list of key value pairs representing headers to insert
into the request before it is sent to the backend members. Changing this updates the headers of the
existing listener.

_Required_: No

_Type_: List of <a href="insertheaders.md">InsertHeaders</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LoadbalancerId

The load balancer on which to provision this
Listener. Changing this creates a new Listener.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Human-readable name for the Listener. Does not have
to be unique.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Protocol

The protocol - can either be TCP, HTTP, HTTPS,
TERMINATED_HTTPS or UDP (supported only in Octavia). Changing this creates a
new Listener.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProtocolPort

The port on which to listen for client traffic.
Changing this creates a new Listener.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Region

The region in which to obtain the V2 Networking client.
A Networking client is needed to create an . If omitted, the
`region` argument of the provider is used. Changing this creates a new
Listener.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SniContainerRefs

A list of references to Barbican Secrets
containers which store SNI information. See
[here](https://wiki.openstack.org/wiki/Network/LBaaS/docs/how-to-create-tls-loadbalancer)
for more information.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TenantId

Required for admins. The UUID of the tenant who owns
the Listener.  Only administrative users can specify a tenant UUID
other than their own. Changing this creates a new Listener.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TimeoutClientData

The client inactivity timeout in milliseconds.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TimeoutMemberConnect

The member connection timeout in milliseconds.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TimeoutMemberData

The member inactivity timeout in milliseconds.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TimeoutTcpInspect

The time in milliseconds, to wait for additional
TCP packets for content inspection.

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

