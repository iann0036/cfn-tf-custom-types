# TF::VCD::ExternalNetworkV2

Provides a VMware Cloud Director External Network resource (version 2). New version of this resource 
uses new VCD API and is capable of creating NSX-T backed external networks as well as port group
backed ones.

-> **Note:** This resource uses new VMware Cloud Director
[OpenAPI](https://code.vmware.com/docs/11982/getting-started-with-vmware-cloud-director-openapi) and
requires at least VCD *10.0+*. It supports both NSX-T and NSX-V backed networks (NSX-T *3.0+* requires VCD *10.1.1+*)

Supported in provider *v3.0+*.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::VCD::ExternalNetworkV2",
    "Properties" : {
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#ipscope" title="IpScope">IpScope</a>" : <i>[ <a href="ipscopedefinition.md">IpScopeDefinition</a>, ... ]</i>,
        "<a href="#nsxtnetwork" title="NsxtNetwork">NsxtNetwork</a>" : <i>[ <a href="nsxtnetworkdefinition.md">NsxtNetworkDefinition</a>, ... ]</i>,
        "<a href="#vspherenetwork" title="VsphereNetwork">VsphereNetwork</a>" : <i>[ <a href="vspherenetworkdefinition.md">VsphereNetworkDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::VCD::ExternalNetworkV2
Properties:
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#ipscope" title="IpScope">IpScope</a>: <i>
      - <a href="ipscopedefinition.md">IpScopeDefinition</a></i>
    <a href="#nsxtnetwork" title="NsxtNetwork">NsxtNetwork</a>: <i>
      - <a href="nsxtnetworkdefinition.md">NsxtNetworkDefinition</a></i>
    <a href="#vspherenetwork" title="VsphereNetwork">VsphereNetwork</a>: <i>
      - <a href="vspherenetworkdefinition.md">VsphereNetworkDefinition</a></i>
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

#### IpScope

_Required_: No

_Type_: List of <a href="ipscopedefinition.md">IpScopeDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NsxtNetwork

_Required_: No

_Type_: List of <a href="nsxtnetworkdefinition.md">NsxtNetworkDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VsphereNetwork

_Required_: No

_Type_: List of <a href="vspherenetworkdefinition.md">VsphereNetworkDefinition</a>

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

