# TF::ECL::ProviderConnectivityTenantConnectionV2

Manages a Provider Connectivity v2 Tenant Connection resource within Enterprise Cloud.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::ECL::ProviderConnectivityTenantConnectionV2",
    "Properties" : {
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#deviceid" title="DeviceId">DeviceId</a>" : <i>String</i>,
        "<a href="#deviceinterfaceid" title="DeviceInterfaceId">DeviceInterfaceId</a>" : <i>String</i>,
        "<a href="#devicetype" title="DeviceType">DeviceType</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tagsdefinition.md">TagsDefinition</a>, ... ]</i>,
        "<a href="#tenantconnectionrequestid" title="TenantConnectionRequestId">TenantConnectionRequestId</a>" : <i>String</i>,
        "<a href="#attachmentoptsbaremetal" title="AttachmentOptsBaremetal">AttachmentOptsBaremetal</a>" : <i>[ <a href="attachmentoptsbaremetaldefinition.md">AttachmentOptsBaremetalDefinition</a>, ... ]</i>,
        "<a href="#attachmentoptscompute" title="AttachmentOptsCompute">AttachmentOptsCompute</a>" : <i>[ <a href="attachmentoptscomputedefinition.md">AttachmentOptsComputeDefinition</a>, ... ]</i>,
        "<a href="#attachmentoptsvna" title="AttachmentOptsVna">AttachmentOptsVna</a>" : <i>[ <a href="attachmentoptsvnadefinition.md">AttachmentOptsVnaDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::ECL::ProviderConnectivityTenantConnectionV2
Properties:
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#deviceid" title="DeviceId">DeviceId</a>: <i>String</i>
    <a href="#deviceinterfaceid" title="DeviceInterfaceId">DeviceInterfaceId</a>: <i>String</i>
    <a href="#devicetype" title="DeviceType">DeviceType</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tagsdefinition.md">TagsDefinition</a></i>
    <a href="#tenantconnectionrequestid" title="TenantConnectionRequestId">TenantConnectionRequestId</a>: <i>String</i>
    <a href="#attachmentoptsbaremetal" title="AttachmentOptsBaremetal">AttachmentOptsBaremetal</a>: <i>
      - <a href="attachmentoptsbaremetaldefinition.md">AttachmentOptsBaremetalDefinition</a></i>
    <a href="#attachmentoptscompute" title="AttachmentOptsCompute">AttachmentOptsCompute</a>: <i>
      - <a href="attachmentoptscomputedefinition.md">AttachmentOptsComputeDefinition</a></i>
    <a href="#attachmentoptsvna" title="AttachmentOptsVna">AttachmentOptsVna</a>: <i>
      - <a href="attachmentoptsvnadefinition.md">AttachmentOptsVnaDefinition</a></i>
</pre>

## Properties

#### Description

Description of tenant_connection.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeviceId

ID of the device of the device_type.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeviceInterfaceId

ID of the interface of the device.
Required for device_type in ECL::Baremetal::Server, ECL::VirtualNetworkAppliance::VSRX.
For device_type: ECL::Baremetal::Server, network_physical_port_id should be used.
For ECL::VirtualNetworkAppliance::VSRX, interfaces.interface_<slot_number> should be used.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeviceType

device type.
(ECL::Compute::Server/ECL::Baremetal::Server/ECL::VirtualNetworkAppliance::VSRX).

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Name of tenant_connection.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

tenant_connection tags.

_Required_: No

_Type_: List of <a href="tagsdefinition.md">TagsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TenantConnectionRequestId

ID of the tenant_connection_request.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AttachmentOptsBaremetal

_Required_: No

_Type_: List of <a href="attachmentoptsbaremetaldefinition.md">AttachmentOptsBaremetalDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AttachmentOptsCompute

_Required_: No

_Type_: List of <a href="attachmentoptscomputedefinition.md">AttachmentOptsComputeDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AttachmentOptsVna

_Required_: No

_Type_: List of <a href="attachmentoptsvnadefinition.md">AttachmentOptsVnaDefinition</a>

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

#### NetworkId

Returns the <code>NetworkId</code> value.

#### PortId

Returns the <code>PortId</code> value.

#### Status

Returns the <code>Status</code> value.

#### TenantId

Returns the <code>TenantId</code> value.

#### TenantIdOther

Returns the <code>TenantIdOther</code> value.

