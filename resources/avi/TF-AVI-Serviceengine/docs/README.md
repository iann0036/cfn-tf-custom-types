# TF::AVI::Serviceengine

The ServiceEngine resource allows the creation and management of Avi ServiceEngine

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AVI::Serviceengine",
    "Properties" : {
        "<a href="#availabilityzone" title="AvailabilityZone">AvailabilityZone</a>" : <i>String</i>,
        "<a href="#cloudref" title="CloudRef">CloudRef</a>" : <i>String</i>,
        "<a href="#containermode" title="ContainerMode">ContainerMode</a>" : <i>Boolean</i>,
        "<a href="#containertype" title="ContainerType">ContainerType</a>" : <i>String</i>,
        "<a href="#controllercreated" title="ControllerCreated">ControllerCreated</a>" : <i>Boolean</i>,
        "<a href="#controllerip" title="ControllerIp">ControllerIp</a>" : <i>String</i>,
        "<a href="#enablestate" title="EnableState">EnableState</a>" : <i>String</i>,
        "<a href="#flavor" title="Flavor">Flavor</a>" : <i>String</i>,
        "<a href="#hostref" title="HostRef">HostRef</a>" : <i>String</i>,
        "<a href="#hypervisor" title="Hypervisor">Hypervisor</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#segroupref" title="SeGroupRef">SeGroupRef</a>" : <i>String</i>,
        "<a href="#tenantref" title="TenantRef">TenantRef</a>" : <i>String</i>,
        "<a href="#uuid" title="Uuid">Uuid</a>" : <i>String</i>,
        "<a href="#datavnics" title="DataVnics">DataVnics</a>" : <i>[ <a href="datavnicsdefinition.md">DataVnicsDefinition</a>, ... ]</i>,
        "<a href="#mgmtvnic" title="MgmtVnic">MgmtVnic</a>" : <i>[ <a href="mgmtvnicdefinition.md">MgmtVnicDefinition</a>, ... ]</i>,
        "<a href="#resources" title="Resources">Resources</a>" : <i>[ <a href="resourcesdefinition.md">ResourcesDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AVI::Serviceengine
Properties:
    <a href="#availabilityzone" title="AvailabilityZone">AvailabilityZone</a>: <i>String</i>
    <a href="#cloudref" title="CloudRef">CloudRef</a>: <i>String</i>
    <a href="#containermode" title="ContainerMode">ContainerMode</a>: <i>Boolean</i>
    <a href="#containertype" title="ContainerType">ContainerType</a>: <i>String</i>
    <a href="#controllercreated" title="ControllerCreated">ControllerCreated</a>: <i>Boolean</i>
    <a href="#controllerip" title="ControllerIp">ControllerIp</a>: <i>String</i>
    <a href="#enablestate" title="EnableState">EnableState</a>: <i>String</i>
    <a href="#flavor" title="Flavor">Flavor</a>: <i>String</i>
    <a href="#hostref" title="HostRef">HostRef</a>: <i>String</i>
    <a href="#hypervisor" title="Hypervisor">Hypervisor</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#segroupref" title="SeGroupRef">SeGroupRef</a>: <i>String</i>
    <a href="#tenantref" title="TenantRef">TenantRef</a>: <i>String</i>
    <a href="#uuid" title="Uuid">Uuid</a>: <i>String</i>
    <a href="#datavnics" title="DataVnics">DataVnics</a>: <i>
      - <a href="datavnicsdefinition.md">DataVnicsDefinition</a></i>
    <a href="#mgmtvnic" title="MgmtVnic">MgmtVnic</a>: <i>
      - <a href="mgmtvnicdefinition.md">MgmtVnicDefinition</a></i>
    <a href="#resources" title="Resources">Resources</a>: <i>
      - <a href="resourcesdefinition.md">ResourcesDefinition</a></i>
</pre>

## Properties

#### AvailabilityZone

Placeholder for description of property availability_zone of obj type serviceengine field type string  type str.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CloudRef

It is a reference to an object of type cloud.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ContainerMode

Boolean flag to set container_mode.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ContainerType

Enum options - container_type_bridge, container_type_host, container_type_host_dpdk.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ControllerCreated

Boolean flag to set controller_created.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ControllerIp

Placeholder for description of property controller_ip of obj type serviceengine field type string  type str.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableState

Inorder to disable se set this field appropriately. Enum options - SE_STATE_ENABLED, SE_STATE_DISABLED_FOR_PLACEMENT, SE_STATE_DISABLED, SE_STATE_DISABLED_FORCE.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Flavor

Placeholder for description of property flavor of obj type serviceengine field type string  type str.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HostRef

It is a reference to an object of type vimgrhostruntime.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Hypervisor

Enum options - default, vmware_esx, kvm, vmware_vsan, xen.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Name of the object.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SeGroupRef

It is a reference to an object of type serviceenginegroup.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TenantRef

It is a reference to an object of type tenant.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Uuid

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DataVnics

_Required_: No

_Type_: List of <a href="datavnicsdefinition.md">DataVnicsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MgmtVnic

_Required_: No

_Type_: List of <a href="mgmtvnicdefinition.md">MgmtVnicDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Resources

_Required_: No

_Type_: List of <a href="resourcesdefinition.md">ResourcesDefinition</a>

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

