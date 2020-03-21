# Terraform::OPC::LbaasLoadBalancer

The `opc_lbaas_load_balancer` resource creates and manages a Load Balancer Classic instance in an Oracle Cloud Infrastructure Classic Compute region. You must define server pools, create at least one listener, and optionally define the policies for the load balancer before it will be operational.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::OPC::LbaasLoadBalancer",
    "Properties" : {
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#enabled" title="Enabled">Enabled</a>" : <i>Boolean</i>,
        "<a href="#ipnetwork" title="IpNetwork">IpNetwork</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#parentloadbalancer" title="ParentLoadBalancer">ParentLoadBalancer</a>" : <i>String</i>,
        "<a href="#permittedclients" title="PermittedClients">PermittedClients</a>" : <i>[ String, ... ]</i>,
        "<a href="#permittedmethods" title="PermittedMethods">PermittedMethods</a>" : <i>[ String, ... ]</i>,
        "<a href="#policies" title="Policies">Policies</a>" : <i>[ String, ... ]</i>,
        "<a href="#region" title="Region">Region</a>" : <i>String</i>,
        "<a href="#scheme" title="Scheme">Scheme</a>" : <i>String</i>,
        "<a href="#serverpool" title="ServerPool">ServerPool</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ String, ... ]</i>,
    }
}
</pre>

### YAML

<pre>
Type: Terraform::OPC::LbaasLoadBalancer
Properties:
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#enabled" title="Enabled">Enabled</a>: <i>Boolean</i>
    <a href="#ipnetwork" title="IpNetwork">IpNetwork</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#parentloadbalancer" title="ParentLoadBalancer">ParentLoadBalancer</a>: <i>String</i>
    <a href="#permittedclients" title="PermittedClients">PermittedClients</a>: <i>
      - String</i>
    <a href="#permittedmethods" title="PermittedMethods">PermittedMethods</a>: <i>
      - String</i>
    <a href="#policies" title="Policies">Policies</a>: <i>
      - String</i>
    <a href="#region" title="Region">Region</a>: <i>String</i>
    <a href="#scheme" title="Scheme">Scheme</a>: <i>String</i>
    <a href="#serverpool" title="ServerPool">ServerPool</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - String</i>
</pre>

## Properties

#### Description

A short description for the load balancer. The description must not exceed 1000 characters.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Enabled

Boolean flag to enable or disable the Load Balancer. Default is `true` (enabled).

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpNetwork

Fully qualified three part name of the IP network to be associated with the load balancer.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the Load Balancer.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ParentLoadBalancer

Select a parent load balancer if you want to create a dependent load balancer.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PermittedClients

List of permitted client IP addresses or CIDR ranges which can connect to this load balancer on the configured Listener ports. If not set all connections are permitted.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PermittedMethods

List of permitted HTTP methods. e.g. `GET`, `POST`, `PUT`, `PATCH`, `DELETE`, `HEAD` or you can also create your own custom methods. Requests with methods not listed in this field will result in a 403 (unauthorized access) response.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Policies

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Region

The region in which to create the Load Balancer, e.g. `uscom-central-1`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Scheme

Set to either `INTERNET_FACING` or `INTERNAL`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServerPool

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

List of tags.

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

#### BalancerVips

Returns the <code>BalancerVips</code> value.

#### CanonicalHostName

Returns the <code>CanonicalHostName</code> value.

#### CloudgateCapable

Returns the <code>CloudgateCapable</code> value.

#### Uri

Returns the <code>Uri</code> value.

