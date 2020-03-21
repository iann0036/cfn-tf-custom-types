# Terraform::OPC::LbaasListener

The `opc_lbaas_listener` resource creates and manages a Load Balancer Classic Listener for a Load Balancer Classic instance.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::OPC::LbaasListener",
    "Properties" : {
        "<a href="#balancerprotocol" title="BalancerProtocol">BalancerProtocol</a>" : <i>String</i>,
        "<a href="#certificates" title="Certificates">Certificates</a>" : <i>[ String, ... ]</i>,
        "<a href="#enabled" title="Enabled">Enabled</a>" : <i>Boolean</i>,
        "<a href="#loadbalancer" title="LoadBalancer">LoadBalancer</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#pathprefixes" title="PathPrefixes">PathPrefixes</a>" : <i>[ String, ... ]</i>,
        "<a href="#policies" title="Policies">Policies</a>" : <i>[ String, ... ]</i>,
        "<a href="#port" title="Port">Port</a>" : <i>Double</i>,
        "<a href="#serverpool" title="ServerPool">ServerPool</a>" : <i>String</i>,
        "<a href="#serverprotocol" title="ServerProtocol">ServerProtocol</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ String, ... ]</i>,
        "<a href="#virtualhosts" title="VirtualHosts">VirtualHosts</a>" : <i>[ String, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::OPC::LbaasListener
Properties:
    <a href="#balancerprotocol" title="BalancerProtocol">BalancerProtocol</a>: <i>String</i>
    <a href="#certificates" title="Certificates">Certificates</a>: <i>
      - String</i>
    <a href="#enabled" title="Enabled">Enabled</a>: <i>Boolean</i>
    <a href="#loadbalancer" title="LoadBalancer">LoadBalancer</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#pathprefixes" title="PathPrefixes">PathPrefixes</a>: <i>
      - String</i>
    <a href="#policies" title="Policies">Policies</a>: <i>
      - String</i>
    <a href="#port" title="Port">Port</a>: <i>Double</i>
    <a href="#serverpool" title="ServerPool">ServerPool</a>: <i>String</i>
    <a href="#serverprotocol" title="ServerProtocol">ServerProtocol</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - String</i>
    <a href="#virtualhosts" title="VirtualHosts">VirtualHosts</a>: <i>
      - String</i>
</pre>

## Properties

#### BalancerProtocol

transport protocol that will be accepted for all incoming requests to the selected load balancer listener. `HTTP` or `HTTPS`. If set to HTTPS then you must also set the server `certificates`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Certificates

The URI of the server security certificate.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Enabled

Boolean flag to enable or disable the Listener. Default is `true` (enabled).

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LoadBalancer

The parent Load Balancer the Listener.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the Listener.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PathPrefixes

List of paths to configure the listener to accept only requests that are targeted to a specific path within the URI of the request.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Policies

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Port

The port on which the Load Balancer is listening.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServerPool

URI of the Server Pool resource to which the load balancer distributes requests.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServerProtocol

The protocol to be used for routing traffic to the origin servers in the server pool. `HTTP` or `HTTPS`. If set to `HTTPS` then you must include a Trusted Certificate Policy in the `policies`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

List of tags.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VirtualHosts

Configure the listener to only accept URI requests that include the host names listed in this field.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### OperationDetails

Returns the <code>OperationDetails</code> value.

#### ParentListener

Returns the <code>ParentListener</code> value.

#### State

Returns the <code>State</code> value.

#### Uri

Returns the <code>Uri</code> value.

