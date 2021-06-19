# TF::AzureRM::CustomProvider ResourceTypeDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#endpoint" title="Endpoint">Endpoint</a>" : <i>String</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#routingtype" title="RoutingType">RoutingType</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#endpoint" title="Endpoint">Endpoint</a>: <i>String</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#routingtype" title="RoutingType">RoutingType</a>: <i>String</i>
</pre>

## Properties

#### Endpoint

Specifies the endpoint of the route definition.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Specifies the name of the route definition.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RoutingType

The routing type that is supported for the resource request. Valid values are `ResourceTypeRoutingProxy` or `ResourceTypeRoutingProxyCache`. This value defaults to `ResourceTypeRoutingProxy`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

