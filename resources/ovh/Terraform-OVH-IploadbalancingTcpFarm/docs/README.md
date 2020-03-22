# Terraform::OVH::IploadbalancingTcpFarm

Creates a backend server group (farm) to be used by loadbalancing frontend(s)

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::OVH::IploadbalancingTcpFarm",
    "Properties" : {
        "<a href="#balance" title="Balance">Balance</a>" : <i>String</i>,
        "<a href="#displayname" title="DisplayName">DisplayName</a>" : <i>String</i>,
        "<a href="#port" title="Port">Port</a>" : <i>Double</i>,
        "<a href="#servicename" title="ServiceName">ServiceName</a>" : <i>String</i>,
        "<a href="#stickiness" title="Stickiness">Stickiness</a>" : <i>String</i>,
        "<a href="#vracknetworkid" title="VrackNetworkId">VrackNetworkId</a>" : <i>Double</i>,
        "<a href="#zone" title="Zone">Zone</a>" : <i>String</i>,
        "<a href="#probe" title="Probe">Probe</a>" : <i>[ <a href="probe.md">Probe</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::OVH::IploadbalancingTcpFarm
Properties:
    <a href="#balance" title="Balance">Balance</a>: <i>String</i>
    <a href="#displayname" title="DisplayName">DisplayName</a>: <i>String</i>
    <a href="#port" title="Port">Port</a>: <i>Double</i>
    <a href="#servicename" title="ServiceName">ServiceName</a>: <i>String</i>
    <a href="#stickiness" title="Stickiness">Stickiness</a>: <i>String</i>
    <a href="#vracknetworkid" title="VrackNetworkId">VrackNetworkId</a>: <i>Double</i>
    <a href="#zone" title="Zone">Zone</a>: <i>String</i>
    <a href="#probe" title="Probe">Probe</a>: <i>
      - <a href="probe.md">Probe</a></i>
</pre>

## Properties

#### Balance

Load balancing algorithm. `roundrobin` if null (`first`, `leastconn`, `roundrobin`, `source`).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisplayName

Readable label for loadbalancer farm.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Port

Port for backends to recieve traffic on.
* `negate` - Negate probe result
* `pattern` - Pattern to match against `match`
* `force_ssl` - Force use of SSL (TLS)
* `url` - URL for HTTP probe type.
* `method` - HTTP probe method (`GET`, `HEAD`, `OPTIONS`, `internal`).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceName

The internal name of your IP load balancing.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Stickiness

Stickiness type. No stickiness if null (`sourceIp`).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VrackNetworkId

Internal Load Balancer identifier of the vRack private network to attach to your farm, mandatory when your Load Balancer is attached to a vRack.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Zone

Zone where the farm will be defined (ie. `GRA`, `BHS` also supports `ALL`).

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Probe

_Required_: No

_Type_: List of <a href="probe.md">Probe</a>

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

