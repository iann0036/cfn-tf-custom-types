# Terraform::RabbitMQ::Permissions

The ``rabbitmq_permissions`` resource creates and manages a user's set of
permissions.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::RabbitMQ::Permissions",
    "Properties" : {
        "<a href="#user" title="User">User</a>" : <i>String</i>,
        "<a href="#vhost" title="Vhost">Vhost</a>" : <i>String</i>,
        "<a href="#permissions" title="Permissions">Permissions</a>" : <i>[ <a href="permissions.md">Permissions</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::RabbitMQ::Permissions
Properties:
    <a href="#user" title="User">User</a>: <i>String</i>
    <a href="#vhost" title="Vhost">Vhost</a>: <i>String</i>
    <a href="#permissions" title="Permissions">Permissions</a>: <i>
      - <a href="permissions.md">Permissions</a></i>
</pre>

## Properties

#### User

The user to apply the permissions to.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vhost

The vhost to create the resource in.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Permissions

_Required_: No

_Type_: List of <a href="permissions.md">Permissions</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

