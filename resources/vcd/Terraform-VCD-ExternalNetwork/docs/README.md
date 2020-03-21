# Terraform::VCD::ExternalNetwork

CloudFormation equivalent of vcd_external_network

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::VCD::ExternalNetwork",
    "Properties" : {
        "<a href="#tfcfnid" title="tfcfnid">tfcfnid</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#retainnetinfoacrossdeployments" title="RetainNetInfoAcrossDeployments">RetainNetInfoAcrossDeployments</a>" : <i>Boolean</i>,
        "<a href="#ipscope" title="IpScope">IpScope</a>" : <i>[ &lt;a href=&#34;ipscope.md&#34;&gt;IpScope&lt;/a&gt;, ... ]</i>,
        "<a href="#vspherenetwork" title="VsphereNetwork">VsphereNetwork</a>" : <i>[ &lt;a href=&#34;vspherenetwork.md&#34;&gt;VsphereNetwork&lt;/a&gt;, ... ]</i>,
        "<a href="#staticippool" title="StaticIpPool">StaticIpPool</a>" : <i>[ &lt;a href=&#34;staticippool.md&#34;&gt;StaticIpPool&lt;/a&gt;, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::VCD::ExternalNetwork
Properties:
    <a href="#tfcfnid" title="tfcfnid">tfcfnid</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#retainnetinfoacrossdeployments" title="RetainNetInfoAcrossDeployments">RetainNetInfoAcrossDeployments</a>: <i>Boolean</i>
    <a href="#ipscope" title="IpScope">IpScope</a>: <i>
      - &lt;a href=&#34;ipscope.md&#34;&gt;IpScope&lt;/a&gt;</i>
    <a href="#vspherenetwork" title="VsphereNetwork">VsphereNetwork</a>: <i>
      - &lt;a href=&#34;vspherenetwork.md&#34;&gt;VsphereNetwork&lt;/a&gt;</i>
    <a href="#staticippool" title="StaticIpPool">StaticIpPool</a>: <i>
      - &lt;a href=&#34;staticippool.md&#34;&gt;StaticIpPool&lt;/a&gt;</i>
</pre>

## Properties

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RetainNetInfoAcrossDeployments

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpScope

_Required_: No

_Type_: List of &lt;a href=&#34;ipscope.md&#34;&gt;IpScope&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VsphereNetwork

_Required_: No

_Type_: List of &lt;a href=&#34;vspherenetwork.md&#34;&gt;VsphereNetwork&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StaticIpPool

_Required_: No

_Type_: List of &lt;a href=&#34;staticippool.md&#34;&gt;StaticIpPool&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

