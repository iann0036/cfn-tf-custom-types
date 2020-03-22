# Terraform::CloudStack::PortForward

Creates port forwards.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::CloudStack::PortForward",
    "Properties" : {
        "<a href="#ipaddressid" title="IpAddressId">IpAddressId</a>" : <i>String</i>,
        "<a href="#managed" title="Managed">Managed</a>" : <i>Boolean</i>,
        "<a href="#project" title="Project">Project</a>" : <i>String</i>,
        "<a href="#forward" title="Forward">Forward</a>" : <i>[ <a href="forward.md">Forward</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::CloudStack::PortForward
Properties:
    <a href="#ipaddressid" title="IpAddressId">IpAddressId</a>: <i>String</i>
    <a href="#managed" title="Managed">Managed</a>: <i>Boolean</i>
    <a href="#project" title="Project">Project</a>: <i>String</i>
    <a href="#forward" title="Forward">Forward</a>: <i>
      - <a href="forward.md">Forward</a></i>
</pre>

## Properties

#### IpAddressId

The IP address ID for which to create the port
forwards. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Managed

USE WITH CAUTION! If enabled all the port forwards for
this IP address will be managed by this resource. This means it will delete
all port forwards that are not in your config! (defaults false).

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Project

The name or ID of the project to create this port forward
in. Changing this forces a new resource to be created.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Forward

_Required_: No

_Type_: List of <a href="forward.md">Forward</a>

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

