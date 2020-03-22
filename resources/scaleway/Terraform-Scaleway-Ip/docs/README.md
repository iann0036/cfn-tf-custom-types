# Terraform::Scaleway::Ip

**DEPRECATED**: This resource is deprecated and will be removed in `v2.0+`.
Please use `scaleway_instance_ip` instead.

Provides IPs for servers. This allows IPs to be created, updated and deleted.
For additional details please refer to [API documentation](https://developer.scaleway.com/#ips).

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Scaleway::Ip",
    "Properties" : {
        "<a href="#reverse" title="Reverse">Reverse</a>" : <i>String</i>,
        "<a href="#server" title="Server">Server</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Scaleway::Ip
Properties:
    <a href="#reverse" title="Reverse">Reverse</a>: <i>String</i>
    <a href="#server" title="Server">Server</a>: <i>String</i>
</pre>

## Properties

#### Reverse

Please us the scaleway_ip_reverse_dns resource instead.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Server

ID of server to associate IP with.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the Id.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Id

Returns the <code>Id</code> value.

#### Ip

Returns the <code>Ip</code> value.

