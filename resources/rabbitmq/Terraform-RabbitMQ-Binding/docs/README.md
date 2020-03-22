# Terraform::RabbitMQ::Binding

The ``rabbitmq_binding`` resource creates and manages a binding relationship
between a queue an exchange.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::RabbitMQ::Binding",
    "Properties" : {
        "<a href="#arguments" title="Arguments">Arguments</a>" : <i>[ <a href="arguments.md">Arguments</a>, ... ]</i>,
        "<a href="#destination" title="Destination">Destination</a>" : <i>String</i>,
        "<a href="#destinationtype" title="DestinationType">DestinationType</a>" : <i>String</i>,
        "<a href="#routingkey" title="RoutingKey">RoutingKey</a>" : <i>String</i>,
        "<a href="#source" title="Source">Source</a>" : <i>String</i>,
        "<a href="#vhost" title="Vhost">Vhost</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::RabbitMQ::Binding
Properties:
    <a href="#arguments" title="Arguments">Arguments</a>: <i>
      - <a href="arguments.md">Arguments</a></i>
    <a href="#destination" title="Destination">Destination</a>: <i>String</i>
    <a href="#destinationtype" title="DestinationType">DestinationType</a>: <i>String</i>
    <a href="#routingkey" title="RoutingKey">RoutingKey</a>: <i>String</i>
    <a href="#source" title="Source">Source</a>: <i>String</i>
    <a href="#vhost" title="Vhost">Vhost</a>: <i>String</i>
</pre>

## Properties

#### Arguments

Additional key/value arguments for the binding.

_Required_: No

_Type_: List of <a href="arguments.md">Arguments</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Destination

The destination queue or exchange.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DestinationType

The type of destination (queue or exchange).

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RoutingKey

A routing key for the binding.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Source

The source exchange.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vhost

The vhost to create the resource in.

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

#### PropertiesKey

Returns the <code>PropertiesKey</code> value.

