# Terraform::OVH::DedicatedServerUpdate

Update various properties of your Dedicated Server.

~> __WARNING__: `rescue_mail` and `root_device` properties aren't
updated consistently. This is an issue on the OVH API which 
has been reported. Meanwhile, these properties aren't not mapped
on this terraform resource.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::OVH::DedicatedServerUpdate",
    "Properties" : {
        "<a href="#bootid" title="BootId">BootId</a>" : <i>Double</i>,
        "<a href="#monitoring" title="Monitoring">Monitoring</a>" : <i>Boolean</i>,
        "<a href="#servicename" title="ServiceName">ServiceName</a>" : <i>String</i>,
        "<a href="#state" title="State">State</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::OVH::DedicatedServerUpdate
Properties:
    <a href="#bootid" title="BootId">BootId</a>: <i>Double</i>
    <a href="#monitoring" title="Monitoring">Monitoring</a>: <i>Boolean</i>
    <a href="#servicename" title="ServiceName">ServiceName</a>: <i>String</i>
    <a href="#state" title="State">State</a>: <i>String</i>
</pre>

## Properties

#### BootId

boot id of the server.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Monitoring

Icmp monitoring state.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceName

The service_name of your dedicated server.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### State

error, hacked, hackedBlocked, ok.

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

