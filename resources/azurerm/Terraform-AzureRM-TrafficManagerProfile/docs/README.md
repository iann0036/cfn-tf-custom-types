# Terraform::AzureRM::TrafficManagerProfile

Manages a Traffic Manager Profile to which multiple endpoints can be attached.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AzureRM::TrafficManagerProfile",
    "Properties" : {
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#profilestatus" title="ProfileStatus">ProfileStatus</a>" : <i>String</i>,
        "<a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tags.md">Tags</a>, ... ]</i>,
        "<a href="#trafficroutingmethod" title="TrafficRoutingMethod">TrafficRoutingMethod</a>" : <i>String</i>,
        "<a href="#dnsconfig" title="DnsConfig">DnsConfig</a>" : <i>[ <a href="dnsconfig.md">DnsConfig</a>, ... ]</i>,
        "<a href="#monitorconfig" title="MonitorConfig">MonitorConfig</a>" : <i>[ <a href="monitorconfig.md">MonitorConfig</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeouts.md">Timeouts</a></i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AzureRM::TrafficManagerProfile
Properties:
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#profilestatus" title="ProfileStatus">ProfileStatus</a>: <i>String</i>
    <a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tags.md">Tags</a></i>
    <a href="#trafficroutingmethod" title="TrafficRoutingMethod">TrafficRoutingMethod</a>: <i>String</i>
    <a href="#dnsconfig" title="DnsConfig">DnsConfig</a>: <i>
      - <a href="dnsconfig.md">DnsConfig</a></i>
    <a href="#monitorconfig" title="MonitorConfig">MonitorConfig</a>: <i>
      - <a href="monitorconfig.md">MonitorConfig</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeouts.md">Timeouts</a></i>
</pre>

## Properties

#### Name

The name of the Traffic Manager profile. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProfileStatus

The status of the profile, can be set to either `Enabled` or `Disabled`. Defaults to `Enabled`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourceGroupName

The name of the resource group in which to create the Traffic Manager profile.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

A mapping of tags to assign to the resource.

_Required_: No

_Type_: List of <a href="tags.md">Tags</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TrafficRoutingMethod

Specifies the algorithm used to route traffic, possible values are:
* `Geographic` - Traffic is routed based on Geographic regions specified in the Endpoint.
* `MultiValue` - All healthy Endpoints are returned.  MultiValue routing method works only if all the endpoints of type ‘External’ and are specified as IPv4 or IPv6 addresses.
* `Performance` - Traffic is routed via the User's closest Endpoint
* `Priority` - Traffic is routed to the Endpoint with the lowest `priority` value.
* `Subnet` - Traffic is routed based on a mapping of sets of end-user IP address ranges to a specific Endpoint within a Traffic Manager profile.
* `Weighted` - Traffic is spread across Endpoints proportional to their `weight` value.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DnsConfig

_Required_: No

_Type_: List of <a href="dnsconfig.md">DnsConfig</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MonitorConfig

_Required_: No

_Type_: List of <a href="monitorconfig.md">MonitorConfig</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeouts.md">Timeouts</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the Id.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Fqdn

Returns the <code>Fqdn</code> value.

#### Id

Returns the <code>Id</code> value.

