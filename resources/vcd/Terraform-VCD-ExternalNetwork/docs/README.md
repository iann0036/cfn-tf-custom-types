# Terraform::VCD::ExternalNetwork

Provides a vCloud Director external network resource.  This can be used to create and delete external networks.
Requires system administrator privileges.

Supported in provider *v2.2+*

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::VCD::ExternalNetwork",
    "Properties" : {
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#retainnetinfoacrossdeployments" title="RetainNetInfoAcrossDeployments">RetainNetInfoAcrossDeployments</a>" : <i>Boolean</i>,
        "<a href="#ipscope" title="IpScope">IpScope</a>" : <i>[ <a href="ipscope.md">IpScope</a>, ... ]</i>,
        "<a href="#vspherenetwork" title="VsphereNetwork">VsphereNetwork</a>" : <i>[ <a href="vspherenetwork.md">VsphereNetwork</a>, ... ]</i>,
        "<a href="#staticippool" title="StaticIpPool">StaticIpPool</a>" : <i>[ <a href="staticippool.md">StaticIpPool</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::VCD::ExternalNetwork
Properties:
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#retainnetinfoacrossdeployments" title="RetainNetInfoAcrossDeployments">RetainNetInfoAcrossDeployments</a>: <i>Boolean</i>
    <a href="#ipscope" title="IpScope">IpScope</a>: <i>
      - <a href="ipscope.md">IpScope</a></i>
    <a href="#vspherenetwork" title="VsphereNetwork">VsphereNetwork</a>: <i>
      - <a href="vspherenetwork.md">VsphereNetwork</a></i>
    <a href="#staticippool" title="StaticIpPool">StaticIpPool</a>: <i>
      - <a href="staticippool.md">StaticIpPool</a></i>
</pre>

## Properties

#### Description

Network friendly description.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

A unique name for the network.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RetainNetInfoAcrossDeployments

Specifies whether the network resources such as IP/MAC of router will be retained across deployments. Default is false.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpScope

_Required_: No

_Type_: List of <a href="ipscope.md">IpScope</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VsphereNetwork

_Required_: No

_Type_: List of <a href="vspherenetwork.md">VsphereNetwork</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StaticIpPool

_Required_: No

_Type_: List of <a href="staticippool.md">StaticIpPool</a>

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

