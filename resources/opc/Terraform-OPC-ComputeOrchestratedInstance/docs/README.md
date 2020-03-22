# Terraform::OPC::ComputeOrchestratedInstance

The `opc_compute_orchestrated_instance` resource creates and manages an orchestration containing a number of
instances in an Oracle Cloud Infrastructure Compute Classic identity domain.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::OPC::ComputeOrchestratedInstance",
    "Properties" : {
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#desiredstate" title="DesiredState">DesiredState</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ String, ... ]</i>,
        "<a href="#instance" title="Instance">Instance</a>" : <i>[ <a href="instance.md">Instance</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeouts.md">Timeouts</a></i>,
        "<a href="#networkinginfo" title="NetworkingInfo">NetworkingInfo</a>" : <i>[ <a href="networkinginfo.md">NetworkingInfo</a>, ... ]</i>,
        "<a href="#storage" title="Storage">Storage</a>" : <i>[ <a href="storage.md">Storage</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::OPC::ComputeOrchestratedInstance
Properties:
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#desiredstate" title="DesiredState">DesiredState</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - String</i>
    <a href="#instance" title="Instance">Instance</a>: <i>
      - <a href="instance.md">Instance</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeouts.md">Timeouts</a></i>
    <a href="#networkinginfo" title="NetworkingInfo">NetworkingInfo</a>: <i>
      - <a href="networkinginfo.md">NetworkingInfo</a></i>
    <a href="#storage" title="Storage">Storage</a>: <i>
      - <a href="storage.md">Storage</a></i>
</pre>

## Properties

#### Description

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DesiredState

The desired state of the orchestration. Permitted values are:.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the orchestration.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Instance

_Required_: No

_Type_: List of <a href="instance.md">Instance</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeouts.md">Timeouts</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetworkingInfo

_Required_: No

_Type_: List of <a href="networkinginfo.md">NetworkingInfo</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Storage

_Required_: No

_Type_: List of <a href="storage.md">Storage</a>

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

#### Version

Returns the <code>Version</code> value.

