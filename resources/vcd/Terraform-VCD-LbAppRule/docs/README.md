# Terraform::VCD::LbAppRule

Provides a vCloud Director Edge Gateway Load Balancer Application Rule resource. An application rule
allows to directly manipulate and manage IP application traffic with load balancer.

~> **Note:** To make load balancing work one must ensure that load balancing is enabled on edge
gateway (edge gateway must be advanced).
This depends on NSX version to work properly. Please refer to [VMware Product Interoperability
Matrices](https://www.vmware.com/resources/compatibility/sim/interop_matrix.php#interop&29=&93=) 
to check supported vCloud director and NSX for vSphere configurations.

~> **Note:** The vCloud Director API for NSX supports a subset of the operations and objects defined
in the NSX vSphere API Guide. The API supports NSX 6.2, 6.3, and 6.4.

Supported in provider *v2.4+*

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::VCD::LbAppRule",
    "Properties" : {
        "<a href="#edgegateway" title="EdgeGateway">EdgeGateway</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#org" title="Org">Org</a>" : <i>String</i>,
        "<a href="#script" title="Script">Script</a>" : <i>String</i>,
        "<a href="#vdc" title="Vdc">Vdc</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::VCD::LbAppRule
Properties:
    <a href="#edgegateway" title="EdgeGateway">EdgeGateway</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#org" title="Org">Org</a>: <i>String</i>
    <a href="#script" title="Script">Script</a>: <i>String</i>
    <a href="#vdc" title="Vdc">Vdc</a>: <i>String</i>
</pre>

## Properties

#### EdgeGateway

The name of the edge gateway on which the application rule is to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Application rule name.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Org

The name of organization to use, optional if defined at provider level. Useful when connected as sysadmin working across different organisations.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Script

A multiline application rule script.
Terraform's [HEREDOC syntax](https://www.terraform.io/docs/configuration/expressions.html#string-literals)
may be useful for multiline scripts. **Note:** For information on
the application rule syntax, see more in [vCloud Director documentation]
(https://docs.vmware.com/en/vCloud-Director/9.7/com.vmware.vcloud.tenantportal.doc/GUID-AFF9F70F-85C9-4053-BA69-F2B062F34C7F.html).

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vdc

The name of VDC to use, optional if defined at provider level.

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

