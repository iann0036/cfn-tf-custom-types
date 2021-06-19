# TF::Volterra::Fleet

CloudFormation equivalent of volterra_fleet

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Volterra::Fleet",
    "Properties" : {
        "<a href="#allowallusb" title="AllowAllUsb">AllowAllUsb</a>" : <i>Boolean</i>,
        "<a href="#annotations" title="Annotations">Annotations</a>" : <i>[ <a href="annotationsdefinition.md">AnnotationsDefinition</a>, ... ]</i>,
        "<a href="#defaultconfig" title="DefaultConfig">DefaultConfig</a>" : <i>Boolean</i>,
        "<a href="#defaultstorageclass" title="DefaultStorageClass">DefaultStorageClass</a>" : <i>Boolean</i>,
        "<a href="#denyallusb" title="DenyAllUsb">DenyAllUsb</a>" : <i>Boolean</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#disable" title="Disable">Disable</a>" : <i>Boolean</i>,
        "<a href="#disablegpu" title="DisableGpu">DisableGpu</a>" : <i>Boolean</i>,
        "<a href="#enabledefaultfleetconfigdownload" title="EnableDefaultFleetConfigDownload">EnableDefaultFleetConfigDownload</a>" : <i>Boolean</i>,
        "<a href="#enablegpu" title="EnableGpu">EnableGpu</a>" : <i>Boolean</i>,
        "<a href="#fleetlabel" title="FleetLabel">FleetLabel</a>" : <i>String</i>,
        "<a href="#labels" title="Labels">Labels</a>" : <i>[ <a href="labelsdefinition.md">LabelsDefinition</a>, ... ]</i>,
        "<a href="#logsstreamingdisabled" title="LogsStreamingDisabled">LogsStreamingDisabled</a>" : <i>Boolean</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#namespace" title="Namespace">Namespace</a>" : <i>String</i>,
        "<a href="#nobonddevices" title="NoBondDevices">NoBondDevices</a>" : <i>Boolean</i>,
        "<a href="#nodcclustergroup" title="NoDcClusterGroup">NoDcClusterGroup</a>" : <i>Boolean</i>,
        "<a href="#nostoragedevice" title="NoStorageDevice">NoStorageDevice</a>" : <i>Boolean</i>,
        "<a href="#nostorageinterfaces" title="NoStorageInterfaces">NoStorageInterfaces</a>" : <i>Boolean</i>,
        "<a href="#nostoragestaticroutes" title="NoStorageStaticRoutes">NoStorageStaticRoutes</a>" : <i>Boolean</i>,
        "<a href="#operatingsystemversion" title="OperatingSystemVersion">OperatingSystemVersion</a>" : <i>String</i>,
        "<a href="#volterrasoftwareversion" title="VolterraSoftwareVersion">VolterraSoftwareVersion</a>" : <i>String</i>,
        "<a href="#bonddevicelist" title="BondDeviceList">BondDeviceList</a>" : <i>[ <a href="bonddevicelistdefinition.md">BondDeviceListDefinition</a>, ... ]</i>,
        "<a href="#dcclustergroup" title="DcClusterGroup">DcClusterGroup</a>" : <i>[ <a href="dcclustergroupdefinition.md">DcClusterGroupDefinition</a>, ... ]</i>,
        "<a href="#dcclustergroupinside" title="DcClusterGroupInside">DcClusterGroupInside</a>" : <i>[ <a href="dcclustergroupinsidedefinition.md">DcClusterGroupInsideDefinition</a>, ... ]</i>,
        "<a href="#devicelist" title="DeviceList">DeviceList</a>" : <i>[ <a href="devicelistdefinition.md">DeviceListDefinition</a>, ... ]</i>,
        "<a href="#insidevirtualnetwork" title="InsideVirtualNetwork">InsideVirtualNetwork</a>" : <i>[ <a href="insidevirtualnetworkdefinition.md">InsideVirtualNetworkDefinition</a>, ... ]</i>,
        "<a href="#interfacelist" title="InterfaceList">InterfaceList</a>" : <i>[ <a href="interfacelistdefinition.md">InterfaceListDefinition</a>, ... ]</i>,
        "<a href="#logreceiver" title="LogReceiver">LogReceiver</a>" : <i>[ <a href="logreceiverdefinition.md">LogReceiverDefinition</a>, ... ]</i>,
        "<a href="#networkconnectors" title="NetworkConnectors">NetworkConnectors</a>" : <i>[ <a href="networkconnectorsdefinition.md">NetworkConnectorsDefinition</a>, ... ]</i>,
        "<a href="#networkfirewall" title="NetworkFirewall">NetworkFirewall</a>" : <i>[ <a href="networkfirewalldefinition.md">NetworkFirewallDefinition</a>, ... ]</i>,
        "<a href="#outsidevirtualnetwork" title="OutsideVirtualNetwork">OutsideVirtualNetwork</a>" : <i>[ <a href="outsidevirtualnetworkdefinition.md">OutsideVirtualNetworkDefinition</a>, ... ]</i>,
        "<a href="#storageclasslist" title="StorageClassList">StorageClassList</a>" : <i>[ <a href="storageclasslistdefinition.md">StorageClassListDefinition</a>, ... ]</i>,
        "<a href="#storagedevicelist" title="StorageDeviceList">StorageDeviceList</a>" : <i>[ <a href="storagedevicelistdefinition.md">StorageDeviceListDefinition</a>, ... ]</i>,
        "<a href="#storageinterfacelist" title="StorageInterfaceList">StorageInterfaceList</a>" : <i>[ <a href="storageinterfacelistdefinition.md">StorageInterfaceListDefinition</a>, ... ]</i>,
        "<a href="#storagestaticroutes" title="StorageStaticRoutes">StorageStaticRoutes</a>" : <i>[ <a href="storagestaticroutesdefinition.md">StorageStaticRoutesDefinition</a>, ... ]</i>,
        "<a href="#usbpolicy" title="UsbPolicy">UsbPolicy</a>" : <i>[ <a href="usbpolicydefinition.md">UsbPolicyDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Volterra::Fleet
Properties:
    <a href="#allowallusb" title="AllowAllUsb">AllowAllUsb</a>: <i>Boolean</i>
    <a href="#annotations" title="Annotations">Annotations</a>: <i>
      - <a href="annotationsdefinition.md">AnnotationsDefinition</a></i>
    <a href="#defaultconfig" title="DefaultConfig">DefaultConfig</a>: <i>Boolean</i>
    <a href="#defaultstorageclass" title="DefaultStorageClass">DefaultStorageClass</a>: <i>Boolean</i>
    <a href="#denyallusb" title="DenyAllUsb">DenyAllUsb</a>: <i>Boolean</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#disable" title="Disable">Disable</a>: <i>Boolean</i>
    <a href="#disablegpu" title="DisableGpu">DisableGpu</a>: <i>Boolean</i>
    <a href="#enabledefaultfleetconfigdownload" title="EnableDefaultFleetConfigDownload">EnableDefaultFleetConfigDownload</a>: <i>Boolean</i>
    <a href="#enablegpu" title="EnableGpu">EnableGpu</a>: <i>Boolean</i>
    <a href="#fleetlabel" title="FleetLabel">FleetLabel</a>: <i>String</i>
    <a href="#labels" title="Labels">Labels</a>: <i>
      - <a href="labelsdefinition.md">LabelsDefinition</a></i>
    <a href="#logsstreamingdisabled" title="LogsStreamingDisabled">LogsStreamingDisabled</a>: <i>Boolean</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#namespace" title="Namespace">Namespace</a>: <i>String</i>
    <a href="#nobonddevices" title="NoBondDevices">NoBondDevices</a>: <i>Boolean</i>
    <a href="#nodcclustergroup" title="NoDcClusterGroup">NoDcClusterGroup</a>: <i>Boolean</i>
    <a href="#nostoragedevice" title="NoStorageDevice">NoStorageDevice</a>: <i>Boolean</i>
    <a href="#nostorageinterfaces" title="NoStorageInterfaces">NoStorageInterfaces</a>: <i>Boolean</i>
    <a href="#nostoragestaticroutes" title="NoStorageStaticRoutes">NoStorageStaticRoutes</a>: <i>Boolean</i>
    <a href="#operatingsystemversion" title="OperatingSystemVersion">OperatingSystemVersion</a>: <i>String</i>
    <a href="#volterrasoftwareversion" title="VolterraSoftwareVersion">VolterraSoftwareVersion</a>: <i>String</i>
    <a href="#bonddevicelist" title="BondDeviceList">BondDeviceList</a>: <i>
      - <a href="bonddevicelistdefinition.md">BondDeviceListDefinition</a></i>
    <a href="#dcclustergroup" title="DcClusterGroup">DcClusterGroup</a>: <i>
      - <a href="dcclustergroupdefinition.md">DcClusterGroupDefinition</a></i>
    <a href="#dcclustergroupinside" title="DcClusterGroupInside">DcClusterGroupInside</a>: <i>
      - <a href="dcclustergroupinsidedefinition.md">DcClusterGroupInsideDefinition</a></i>
    <a href="#devicelist" title="DeviceList">DeviceList</a>: <i>
      - <a href="devicelistdefinition.md">DeviceListDefinition</a></i>
    <a href="#insidevirtualnetwork" title="InsideVirtualNetwork">InsideVirtualNetwork</a>: <i>
      - <a href="insidevirtualnetworkdefinition.md">InsideVirtualNetworkDefinition</a></i>
    <a href="#interfacelist" title="InterfaceList">InterfaceList</a>: <i>
      - <a href="interfacelistdefinition.md">InterfaceListDefinition</a></i>
    <a href="#logreceiver" title="LogReceiver">LogReceiver</a>: <i>
      - <a href="logreceiverdefinition.md">LogReceiverDefinition</a></i>
    <a href="#networkconnectors" title="NetworkConnectors">NetworkConnectors</a>: <i>
      - <a href="networkconnectorsdefinition.md">NetworkConnectorsDefinition</a></i>
    <a href="#networkfirewall" title="NetworkFirewall">NetworkFirewall</a>: <i>
      - <a href="networkfirewalldefinition.md">NetworkFirewallDefinition</a></i>
    <a href="#outsidevirtualnetwork" title="OutsideVirtualNetwork">OutsideVirtualNetwork</a>: <i>
      - <a href="outsidevirtualnetworkdefinition.md">OutsideVirtualNetworkDefinition</a></i>
    <a href="#storageclasslist" title="StorageClassList">StorageClassList</a>: <i>
      - <a href="storageclasslistdefinition.md">StorageClassListDefinition</a></i>
    <a href="#storagedevicelist" title="StorageDeviceList">StorageDeviceList</a>: <i>
      - <a href="storagedevicelistdefinition.md">StorageDeviceListDefinition</a></i>
    <a href="#storageinterfacelist" title="StorageInterfaceList">StorageInterfaceList</a>: <i>
      - <a href="storageinterfacelistdefinition.md">StorageInterfaceListDefinition</a></i>
    <a href="#storagestaticroutes" title="StorageStaticRoutes">StorageStaticRoutes</a>: <i>
      - <a href="storagestaticroutesdefinition.md">StorageStaticRoutesDefinition</a></i>
    <a href="#usbpolicy" title="UsbPolicy">UsbPolicy</a>: <i>
      - <a href="usbpolicydefinition.md">UsbPolicyDefinition</a></i>
</pre>

## Properties

#### AllowAllUsb

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Annotations

_Required_: No

_Type_: List of <a href="annotationsdefinition.md">AnnotationsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefaultConfig

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefaultStorageClass

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DenyAllUsb

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Disable

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisableGpu

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableDefaultFleetConfigDownload

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableGpu

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FleetLabel

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Labels

_Required_: No

_Type_: List of <a href="labelsdefinition.md">LabelsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LogsStreamingDisabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Namespace

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NoBondDevices

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NoDcClusterGroup

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NoStorageDevice

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NoStorageInterfaces

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NoStorageStaticRoutes

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OperatingSystemVersion

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VolterraSoftwareVersion

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BondDeviceList

_Required_: No

_Type_: List of <a href="bonddevicelistdefinition.md">BondDeviceListDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DcClusterGroup

_Required_: No

_Type_: List of <a href="dcclustergroupdefinition.md">DcClusterGroupDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DcClusterGroupInside

_Required_: No

_Type_: List of <a href="dcclustergroupinsidedefinition.md">DcClusterGroupInsideDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeviceList

_Required_: No

_Type_: List of <a href="devicelistdefinition.md">DeviceListDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InsideVirtualNetwork

_Required_: No

_Type_: List of <a href="insidevirtualnetworkdefinition.md">InsideVirtualNetworkDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InterfaceList

_Required_: No

_Type_: List of <a href="interfacelistdefinition.md">InterfaceListDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LogReceiver

_Required_: No

_Type_: List of <a href="logreceiverdefinition.md">LogReceiverDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetworkConnectors

_Required_: No

_Type_: List of <a href="networkconnectorsdefinition.md">NetworkConnectorsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetworkFirewall

_Required_: No

_Type_: List of <a href="networkfirewalldefinition.md">NetworkFirewallDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OutsideVirtualNetwork

_Required_: No

_Type_: List of <a href="outsidevirtualnetworkdefinition.md">OutsideVirtualNetworkDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StorageClassList

_Required_: No

_Type_: List of <a href="storageclasslistdefinition.md">StorageClassListDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StorageDeviceList

_Required_: No

_Type_: List of <a href="storagedevicelistdefinition.md">StorageDeviceListDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StorageInterfaceList

_Required_: No

_Type_: List of <a href="storageinterfacelistdefinition.md">StorageInterfaceListDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StorageStaticRoutes

_Required_: No

_Type_: List of <a href="storagestaticroutesdefinition.md">StorageStaticRoutesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UsbPolicy

_Required_: No

_Type_: List of <a href="usbpolicydefinition.md">UsbPolicyDefinition</a>

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

