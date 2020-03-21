# Terraform::RabbitMQ::Policy

The ``rabbitmq_policy`` resource creates and manages policies for exchanges
and queues.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::RabbitMQ::Policy",
    "Properties" : {
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#vhost" title="Vhost">Vhost</a>" : <i>String</i>,
        "<a href="#policy" title="Policy">Policy</a>" : <i>[ <a href="policy.md">Policy</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::RabbitMQ::Policy
Properties:
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#vhost" title="Vhost">Vhost</a>: <i>String</i>
    <a href="#policy" title="Policy">Policy</a>: <i>
      - <a href="policy.md">Policy</a></i>
</pre>

## Properties

#### Name

The name of the policy.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vhost

The vhost to create the resource in.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Policy

_Required_: No

_Type_: List of <a href="policy.md">Policy</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

