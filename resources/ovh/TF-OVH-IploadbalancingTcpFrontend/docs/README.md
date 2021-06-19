# TF::OVH::IploadbalancingTcpFrontend

Creates a backend server group (frontend) to be used by loadbalancing frontend(s)

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::OVH::IploadbalancingTcpFrontend",
    "Properties" : {
        "<a href="#allowedsource" title="AllowedSource">AllowedSource</a>" : <i>[ String, ... ]</i>,
        "<a href="#dedicatedipfo" title="DedicatedIpfo">DedicatedIpfo</a>" : <i>[ String, ... ]</i>,
        "<a href="#defaultfarmid" title="DefaultFarmId">DefaultFarmId</a>" : <i>Double</i>,
        "<a href="#defaultsslid" title="DefaultSslId">DefaultSslId</a>" : <i>Double</i>,
        "<a href="#disabled" title="Disabled">Disabled</a>" : <i>Boolean</i>,
        "<a href="#displayname" title="DisplayName">DisplayName</a>" : <i>String</i>,
        "<a href="#port" title="Port">Port</a>" : <i>String</i>,
        "<a href="#servicename" title="ServiceName">ServiceName</a>" : <i>String</i>,
        "<a href="#ssl" title="Ssl">Ssl</a>" : <i>Boolean</i>,
        "<a href="#zone" title="Zone">Zone</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::OVH::IploadbalancingTcpFrontend
Properties:
    <a href="#allowedsource" title="AllowedSource">AllowedSource</a>: <i>
      - String</i>
    <a href="#dedicatedipfo" title="DedicatedIpfo">DedicatedIpfo</a>: <i>
      - String</i>
    <a href="#defaultfarmid" title="DefaultFarmId">DefaultFarmId</a>: <i>Double</i>
    <a href="#defaultsslid" title="DefaultSslId">DefaultSslId</a>: <i>Double</i>
    <a href="#disabled" title="Disabled">Disabled</a>: <i>Boolean</i>
    <a href="#displayname" title="DisplayName">DisplayName</a>: <i>String</i>
    <a href="#port" title="Port">Port</a>: <i>String</i>
    <a href="#servicename" title="ServiceName">ServiceName</a>: <i>String</i>
    <a href="#ssl" title="Ssl">Ssl</a>: <i>Boolean</i>
    <a href="#zone" title="Zone">Zone</a>: <i>String</i>
</pre>

## Properties

#### AllowedSource

Restrict IP Load Balancing access to these ip block. No restriction if null. List of IP blocks.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DedicatedIpfo

Only attach frontend on these ip. No restriction if null. List of Ip blocks.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefaultFarmId

Default TCP Farm of your frontend.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefaultSslId

Default ssl served to your customer.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Disabled

Disable your frontend. Default: 'false'.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisplayName

Human readable name for your frontend, this field is for you.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Port

Port(s) attached to your frontend. Supports single port (numerical value),
range (2 dash-delimited increasing ports) and comma-separated list of 'single port'
and/or 'range'. Each port must be in the [1;49151] range.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceName

The internal name of your IP load balancing.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ssl

SSL deciphering. Default: 'false'.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Zone

Zone where the frontend will be defined (ie. `gra`, `bhs` also supports `all`).

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

