# TF::OVH::IploadbalancingTcpFarmServer

Creates a backend server entry linked to loadbalancing group (farm)

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::OVH::IploadbalancingTcpFarmServer",
    "Properties" : {
        "<a href="#address" title="Address">Address</a>" : <i>String</i>,
        "<a href="#backup" title="Backup">Backup</a>" : <i>Boolean</i>,
        "<a href="#chain" title="Chain">Chain</a>" : <i>String</i>,
        "<a href="#displayname" title="DisplayName">DisplayName</a>" : <i>String</i>,
        "<a href="#farmid" title="FarmId">FarmId</a>" : <i>Double</i>,
        "<a href="#port" title="Port">Port</a>" : <i>Double</i>,
        "<a href="#probe" title="Probe">Probe</a>" : <i>Boolean</i>,
        "<a href="#proxyprotocolversion" title="ProxyProtocolVersion">ProxyProtocolVersion</a>" : <i>String</i>,
        "<a href="#servicename" title="ServiceName">ServiceName</a>" : <i>String</i>,
        "<a href="#ssl" title="Ssl">Ssl</a>" : <i>Boolean</i>,
        "<a href="#status" title="Status">Status</a>" : <i>String</i>,
        "<a href="#weight" title="Weight">Weight</a>" : <i>Double</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::OVH::IploadbalancingTcpFarmServer
Properties:
    <a href="#address" title="Address">Address</a>: <i>String</i>
    <a href="#backup" title="Backup">Backup</a>: <i>Boolean</i>
    <a href="#chain" title="Chain">Chain</a>: <i>String</i>
    <a href="#displayname" title="DisplayName">DisplayName</a>: <i>String</i>
    <a href="#farmid" title="FarmId">FarmId</a>: <i>Double</i>
    <a href="#port" title="Port">Port</a>: <i>Double</i>
    <a href="#probe" title="Probe">Probe</a>: <i>Boolean</i>
    <a href="#proxyprotocolversion" title="ProxyProtocolVersion">ProxyProtocolVersion</a>: <i>String</i>
    <a href="#servicename" title="ServiceName">ServiceName</a>: <i>String</i>
    <a href="#ssl" title="Ssl">Ssl</a>: <i>Boolean</i>
    <a href="#status" title="Status">Status</a>: <i>String</i>
    <a href="#weight" title="Weight">Weight</a>: <i>Double</i>
</pre>

## Properties

#### Address

Address of the backend server (IP from either internal or OVH network).

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Backup

is it a backup server used in case of failure of all the non-backup backends.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Chain

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisplayName

Label for the server.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FarmId

ID of the farm this server is attached to.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Port

Port that backend will respond on.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Probe

defines if backend will be probed to determine health and keep as active in farm if healthy.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProxyProtocolVersion

version of the PROXY protocol used to pass origin connection information from loadbalancer to recieving service (`v1`, `v2`, `v2-ssl`, `v2-ssl-cn`).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceName

The internal name of your IP load balancing.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ssl

is the connection ciphered with SSL (TLS).

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Status

backend status - `active` or `inactive`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Weight

used in loadbalancing algorithm.

_Required_: No

_Type_: Double

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

