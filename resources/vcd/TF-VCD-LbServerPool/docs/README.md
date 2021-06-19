# TF::VCD::LbServerPool

Provides a vCloud Director Edge Gateway Load Balancer Server Pool resource. A Server Pool can have a group of backend
servers set (defined as pool members), manages load balancer distribution methods, and may have a service monitor
attached to it for health check parameters.

~> **Note:** To make load balancing work one must ensure that load balancing is enabled on edge gateway. This depends 
on NSX version to work properly. Please refer to [VMware Product Interoperability Matrices](https://www.vmware.com/resources/compatibility/sim/interop_matrix.php#interop&29=&93=) 
to check supported vCloud director and NSX for vSphere configurations.

~> **Note:** The vCloud Director API for NSX supports a subset of the operations and objects defined in the NSX vSphere 
API Guide. The API supports NSX 6.2, 6.3, and 6.4.

Supported in provider *v2.4+*

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::VCD::LbServerPool",
    "Properties" : {
        "<a href="#algorithm" title="Algorithm">Algorithm</a>" : <i>String</i>,
        "<a href="#algorithmparameters" title="AlgorithmParameters">AlgorithmParameters</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#edgegateway" title="EdgeGateway">EdgeGateway</a>" : <i>String</i>,
        "<a href="#enabletransparency" title="EnableTransparency">EnableTransparency</a>" : <i>Boolean</i>,
        "<a href="#monitorid" title="MonitorId">MonitorId</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#org" title="Org">Org</a>" : <i>String</i>,
        "<a href="#vdc" title="Vdc">Vdc</a>" : <i>String</i>,
        "<a href="#member" title="Member">Member</a>" : <i>[ <a href="memberdefinition.md">MemberDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::VCD::LbServerPool
Properties:
    <a href="#algorithm" title="Algorithm">Algorithm</a>: <i>String</i>
    <a href="#algorithmparameters" title="AlgorithmParameters">AlgorithmParameters</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#edgegateway" title="EdgeGateway">EdgeGateway</a>: <i>String</i>
    <a href="#enabletransparency" title="EnableTransparency">EnableTransparency</a>: <i>Boolean</i>
    <a href="#monitorid" title="MonitorId">MonitorId</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#org" title="Org">Org</a>: <i>String</i>
    <a href="#vdc" title="Vdc">Vdc</a>: <i>String</i>
    <a href="#member" title="Member">Member</a>: <i>
      - <a href="memberdefinition.md">MemberDefinition</a></i>
</pre>

## Properties

#### Algorithm

Server Pool load balancing method. Can be one of `ip-hash`, `round-robin`, `uri`, `leastconn`, `url`, or `httpheader`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AlgorithmParameters

Valid only when `algorithm` is `httpheader` or `url`. The `httpheader` algorithm
parameter has one option `headerName=<name>` while the `url` algorithm parameter has option `urlParam=<url>`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

Server Pool description.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EdgeGateway

The name of the edge gateway on which the server pool is to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableTransparency

When transparency is `false` (default) backend servers see the IP address of the
traffic source as the internal IP address of the load balancer. When it is `true` the source IP address is the actual IP
address of the client and the edge gateway must be set as the default gateway to ensure that return packets go through
the edge gateway.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MonitorId

`vcd_lb_service_monitor` resource `id` to attach to server pool for health check parameters.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Server Pool name.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Org

The name of organization to use, optional if defined at provider level. Useful when connected as sysadmin working across different organisations.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vdc

The name of VDC to use, optional if defined at provider level.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Member

_Required_: No

_Type_: List of <a href="memberdefinition.md">MemberDefinition</a>

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

