# Terraform::Scaleway::Server

**DEPRECATED**: This resource is deprecated and will be removed in `v2.0+`.
Please use `scaleway_instance_server` instead.

Provides servers. This allows servers to be created, updated and deleted.
For additional details please refer to [API documentation](https://developer.scaleway.com/#servers).

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Scaleway::Server",
    "Properties" : {
        "<a href="#boottype" title="BootType">BootType</a>" : <i>String</i>,
        "<a href="#bootscript" title="Bootscript">Bootscript</a>" : <i>String</i>,
        "<a href="#cloudinit" title="Cloudinit">Cloudinit</a>" : <i>String</i>,
        "<a href="#dynamiciprequired" title="DynamicIpRequired">DynamicIpRequired</a>" : <i>Boolean</i>,
        "<a href="#enableipv6" title="EnableIpv6">EnableIpv6</a>" : <i>Boolean</i>,
        "<a href="#image" title="Image">Image</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#publicip" title="PublicIp">PublicIp</a>" : <i>String</i>,
        "<a href="#securitygroup" title="SecurityGroup">SecurityGroup</a>" : <i>String</i>,
        "<a href="#state" title="State">State</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ String, ... ]</i>,
        "<a href="#type" title="Type">Type</a>" : <i>String</i>,
        "<a href="#volume" title="Volume">Volume</a>" : <i>[ <a href="volume.md">Volume</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Scaleway::Server
Properties:
    <a href="#boottype" title="BootType">BootType</a>: <i>String</i>
    <a href="#bootscript" title="Bootscript">Bootscript</a>: <i>String</i>
    <a href="#cloudinit" title="Cloudinit">Cloudinit</a>: <i>String</i>
    <a href="#dynamiciprequired" title="DynamicIpRequired">DynamicIpRequired</a>: <i>Boolean</i>
    <a href="#enableipv6" title="EnableIpv6">EnableIpv6</a>: <i>Boolean</i>
    <a href="#image" title="Image">Image</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#publicip" title="PublicIp">PublicIp</a>: <i>String</i>
    <a href="#securitygroup" title="SecurityGroup">SecurityGroup</a>: <i>String</i>
    <a href="#state" title="State">State</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - String</i>
    <a href="#type" title="Type">Type</a>: <i>String</i>
    <a href="#volume" title="Volume">Volume</a>: <i>
      - <a href="volume.md">Volume</a></i>
</pre>

## Properties

#### BootType

the boot mechanism for this server. Possible values include `local` and `bootscript`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Bootscript

server bootscript.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Cloudinit

allows you to define cloudinit script for this server.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DynamicIpRequired

make server publicly available.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableIpv6

enable ipv6.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Image

base image of server.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

name of server.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PublicIp

set a public ip previously created (a real ip is expected here, not its resource id).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecurityGroup

assign security group to server.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### State

allows you to define the desired state of your server. Valid values include (`stopped`, `running`).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

list of tags for server.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

type of server.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Volume

_Required_: No

_Type_: List of <a href="volume.md">Volume</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### PrivateIp

Returns the <code>PrivateIp</code> value.

#### PublicIpv6

if `enable_ipv6` is set this contains the ipv6 address of your instance.

#### StateDetail

contains details from the scaleway API the state of your instance.

