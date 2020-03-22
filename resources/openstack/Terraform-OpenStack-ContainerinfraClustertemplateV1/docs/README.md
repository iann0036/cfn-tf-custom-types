# Terraform::OpenStack::ContainerinfraClustertemplateV1

Manages a V1 Magnum cluster template resource within OpenStack.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::OpenStack::ContainerinfraClustertemplateV1",
    "Properties" : {
        "<a href="#apiserverport" title="ApiserverPort">ApiserverPort</a>" : <i>Double</i>,
        "<a href="#clusterdistro" title="ClusterDistro">ClusterDistro</a>" : <i>String</i>,
        "<a href="#coe" title="Coe">Coe</a>" : <i>String</i>,
        "<a href="#dnsnameserver" title="DnsNameserver">DnsNameserver</a>" : <i>String</i>,
        "<a href="#dockerstoragedriver" title="DockerStorageDriver">DockerStorageDriver</a>" : <i>String</i>,
        "<a href="#dockervolumesize" title="DockerVolumeSize">DockerVolumeSize</a>" : <i>Double</i>,
        "<a href="#externalnetworkid" title="ExternalNetworkId">ExternalNetworkId</a>" : <i>String</i>,
        "<a href="#fixednetwork" title="FixedNetwork">FixedNetwork</a>" : <i>String</i>,
        "<a href="#fixedsubnet" title="FixedSubnet">FixedSubnet</a>" : <i>String</i>,
        "<a href="#flavor" title="Flavor">Flavor</a>" : <i>String</i>,
        "<a href="#floatingipenabled" title="FloatingIpEnabled">FloatingIpEnabled</a>" : <i>Boolean</i>,
        "<a href="#httpproxy" title="HttpProxy">HttpProxy</a>" : <i>String</i>,
        "<a href="#httpsproxy" title="HttpsProxy">HttpsProxy</a>" : <i>String</i>,
        "<a href="#image" title="Image">Image</a>" : <i>String</i>,
        "<a href="#insecureregistry" title="InsecureRegistry">InsecureRegistry</a>" : <i>String</i>,
        "<a href="#keypairid" title="KeypairId">KeypairId</a>" : <i>String</i>,
        "<a href="#labels" title="Labels">Labels</a>" : <i>[ <a href="labels.md">Labels</a>, ... ]</i>,
        "<a href="#masterflavor" title="MasterFlavor">MasterFlavor</a>" : <i>String</i>,
        "<a href="#masterlbenabled" title="MasterLbEnabled">MasterLbEnabled</a>" : <i>Boolean</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#networkdriver" title="NetworkDriver">NetworkDriver</a>" : <i>String</i>,
        "<a href="#noproxy" title="NoProxy">NoProxy</a>" : <i>String</i>,
        "<a href="#public" title="Public">Public</a>" : <i>Boolean</i>,
        "<a href="#region" title="Region">Region</a>" : <i>String</i>,
        "<a href="#registryenabled" title="RegistryEnabled">RegistryEnabled</a>" : <i>Boolean</i>,
        "<a href="#servertype" title="ServerType">ServerType</a>" : <i>String</i>,
        "<a href="#tlsdisabled" title="TlsDisabled">TlsDisabled</a>" : <i>Boolean</i>,
        "<a href="#volumedriver" title="VolumeDriver">VolumeDriver</a>" : <i>String</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeouts.md">Timeouts</a></i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::OpenStack::ContainerinfraClustertemplateV1
Properties:
    <a href="#apiserverport" title="ApiserverPort">ApiserverPort</a>: <i>Double</i>
    <a href="#clusterdistro" title="ClusterDistro">ClusterDistro</a>: <i>String</i>
    <a href="#coe" title="Coe">Coe</a>: <i>String</i>
    <a href="#dnsnameserver" title="DnsNameserver">DnsNameserver</a>: <i>String</i>
    <a href="#dockerstoragedriver" title="DockerStorageDriver">DockerStorageDriver</a>: <i>String</i>
    <a href="#dockervolumesize" title="DockerVolumeSize">DockerVolumeSize</a>: <i>Double</i>
    <a href="#externalnetworkid" title="ExternalNetworkId">ExternalNetworkId</a>: <i>String</i>
    <a href="#fixednetwork" title="FixedNetwork">FixedNetwork</a>: <i>String</i>
    <a href="#fixedsubnet" title="FixedSubnet">FixedSubnet</a>: <i>String</i>
    <a href="#flavor" title="Flavor">Flavor</a>: <i>String</i>
    <a href="#floatingipenabled" title="FloatingIpEnabled">FloatingIpEnabled</a>: <i>Boolean</i>
    <a href="#httpproxy" title="HttpProxy">HttpProxy</a>: <i>String</i>
    <a href="#httpsproxy" title="HttpsProxy">HttpsProxy</a>: <i>String</i>
    <a href="#image" title="Image">Image</a>: <i>String</i>
    <a href="#insecureregistry" title="InsecureRegistry">InsecureRegistry</a>: <i>String</i>
    <a href="#keypairid" title="KeypairId">KeypairId</a>: <i>String</i>
    <a href="#labels" title="Labels">Labels</a>: <i>
      - <a href="labels.md">Labels</a></i>
    <a href="#masterflavor" title="MasterFlavor">MasterFlavor</a>: <i>String</i>
    <a href="#masterlbenabled" title="MasterLbEnabled">MasterLbEnabled</a>: <i>Boolean</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#networkdriver" title="NetworkDriver">NetworkDriver</a>: <i>String</i>
    <a href="#noproxy" title="NoProxy">NoProxy</a>: <i>String</i>
    <a href="#public" title="Public">Public</a>: <i>Boolean</i>
    <a href="#region" title="Region">Region</a>: <i>String</i>
    <a href="#registryenabled" title="RegistryEnabled">RegistryEnabled</a>: <i>Boolean</i>
    <a href="#servertype" title="ServerType">ServerType</a>: <i>String</i>
    <a href="#tlsdisabled" title="TlsDisabled">TlsDisabled</a>: <i>Boolean</i>
    <a href="#volumedriver" title="VolumeDriver">VolumeDriver</a>: <i>String</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeouts.md">Timeouts</a></i>
</pre>

## Properties

#### ApiserverPort

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClusterDistro

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Coe

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DnsNameserver

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DockerStorageDriver

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DockerVolumeSize

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExternalNetworkId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FixedNetwork

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FixedSubnet

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Flavor

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FloatingIpEnabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HttpProxy

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HttpsProxy

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Image

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InsecureRegistry

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KeypairId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Labels

_Required_: No

_Type_: List of <a href="labels.md">Labels</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MasterFlavor

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MasterLbEnabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetworkDriver

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NoProxy

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Public

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Region

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RegistryEnabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServerType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TlsDisabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VolumeDriver

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeouts.md">Timeouts</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### CreatedAt

Returns the <code>CreatedAt</code> value.

#### Id

Returns the <code>Id</code> value.

#### ProjectId

Returns the <code>ProjectId</code> value.

#### UpdatedAt

Returns the <code>UpdatedAt</code> value.

#### UserId

Returns the <code>UserId</code> value.

