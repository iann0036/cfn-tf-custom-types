# TF::AVI::Inventoryfaultconfig

The InventoryFaultConfig resource allows the creation and management of Avi InventoryFaultConfig

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AVI::Inventoryfaultconfig",
    "Properties" : {
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#tenantref" title="TenantRef">TenantRef</a>" : <i>String</i>,
        "<a href="#uuid" title="Uuid">Uuid</a>" : <i>String</i>,
        "<a href="#controllerfaults" title="ControllerFaults">ControllerFaults</a>" : <i>[ <a href="controllerfaultsdefinition.md">ControllerFaultsDefinition</a>, ... ]</i>,
        "<a href="#serviceenginefaults" title="ServiceengineFaults">ServiceengineFaults</a>" : <i>[ <a href="serviceenginefaultsdefinition.md">ServiceengineFaultsDefinition</a>, ... ]</i>,
        "<a href="#virtualservicefaults" title="VirtualserviceFaults">VirtualserviceFaults</a>" : <i>[ <a href="virtualservicefaultsdefinition.md">VirtualserviceFaultsDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AVI::Inventoryfaultconfig
Properties:
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#tenantref" title="TenantRef">TenantRef</a>: <i>String</i>
    <a href="#uuid" title="Uuid">Uuid</a>: <i>String</i>
    <a href="#controllerfaults" title="ControllerFaults">ControllerFaults</a>: <i>
      - <a href="controllerfaultsdefinition.md">ControllerFaultsDefinition</a></i>
    <a href="#serviceenginefaults" title="ServiceengineFaults">ServiceengineFaults</a>: <i>
      - <a href="serviceenginefaultsdefinition.md">ServiceengineFaultsDefinition</a></i>
    <a href="#virtualservicefaults" title="VirtualserviceFaults">VirtualserviceFaults</a>: <i>
      - <a href="virtualservicefaultsdefinition.md">VirtualserviceFaultsDefinition</a></i>
</pre>

## Properties

#### Name

Name. Field introduced in 20.1.6.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TenantRef

Tenant. It is a reference to an object of type tenant. Field introduced in 20.1.6.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Uuid

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ControllerFaults

_Required_: No

_Type_: List of <a href="controllerfaultsdefinition.md">ControllerFaultsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceengineFaults

_Required_: No

_Type_: List of <a href="serviceenginefaultsdefinition.md">ServiceengineFaultsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VirtualserviceFaults

_Required_: No

_Type_: List of <a href="virtualservicefaultsdefinition.md">VirtualserviceFaultsDefinition</a>

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

