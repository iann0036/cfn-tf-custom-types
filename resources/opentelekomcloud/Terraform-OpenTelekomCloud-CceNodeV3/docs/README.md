# Terraform::OpenTelekomCloud::CceNodeV3

Add a node to a container cluster.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::OpenTelekomCloud::CceNodeV3",
    "Properties" : {
        "<a href="#annotations" title="Annotations">Annotations</a>" : <i>[ <a href="annotations.md">Annotations</a>, ... ]</i>,
        "<a href="#availabilityzone" title="AvailabilityZone">AvailabilityZone</a>" : <i>String</i>,
        "<a href="#bandwidthchargemode" title="BandwidthChargeMode">BandwidthChargeMode</a>" : <i>String</i>,
        "<a href="#bandwidthsize" title="BandwidthSize">BandwidthSize</a>" : <i>Double</i>,
        "<a href="#billingmode" title="BillingMode">BillingMode</a>" : <i>Double</i>,
        "<a href="#clusterid" title="ClusterId">ClusterId</a>" : <i>String</i>,
        "<a href="#ecsperformancetype" title="EcsPerformanceType">EcsPerformanceType</a>" : <i>String</i>,
        "<a href="#eipcount" title="EipCount">EipCount</a>" : <i>Double</i>,
        "<a href="#eipids" title="EipIds">EipIds</a>" : <i>[ String, ... ]</i>,
        "<a href="#extendparamchargingmode" title="ExtendParamChargingMode">ExtendParamChargingMode</a>" : <i>Double</i>,
        "<a href="#flavorid" title="FlavorId">FlavorId</a>" : <i>String</i>,
        "<a href="#iptype" title="Iptype">Iptype</a>" : <i>String</i>,
        "<a href="#keypair" title="KeyPair">KeyPair</a>" : <i>String</i>,
        "<a href="#labels" title="Labels">Labels</a>" : <i>[ <a href="labels.md">Labels</a>, ... ]</i>,
        "<a href="#maxpods" title="MaxPods">MaxPods</a>" : <i>Double</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#orderid" title="OrderId">OrderId</a>" : <i>String</i>,
        "<a href="#postinstall" title="Postinstall">Postinstall</a>" : <i>String</i>,
        "<a href="#preinstall" title="Preinstall">Preinstall</a>" : <i>String</i>,
        "<a href="#productid" title="ProductId">ProductId</a>" : <i>String</i>,
        "<a href="#publickey" title="PublicKey">PublicKey</a>" : <i>String</i>,
        "<a href="#region" title="Region">Region</a>" : <i>String</i>,
        "<a href="#sharetype" title="Sharetype">Sharetype</a>" : <i>String</i>,
        "<a href="#datavolumes" title="DataVolumes">DataVolumes</a>" : <i>[ <a href="datavolumes.md">DataVolumes</a>, ... ]</i>,
        "<a href="#rootvolume" title="RootVolume">RootVolume</a>" : <i>[ <a href="rootvolume.md">RootVolume</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeouts.md">Timeouts</a></i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::OpenTelekomCloud::CceNodeV3
Properties:
    <a href="#annotations" title="Annotations">Annotations</a>: <i>
      - <a href="annotations.md">Annotations</a></i>
    <a href="#availabilityzone" title="AvailabilityZone">AvailabilityZone</a>: <i>String</i>
    <a href="#bandwidthchargemode" title="BandwidthChargeMode">BandwidthChargeMode</a>: <i>String</i>
    <a href="#bandwidthsize" title="BandwidthSize">BandwidthSize</a>: <i>Double</i>
    <a href="#billingmode" title="BillingMode">BillingMode</a>: <i>Double</i>
    <a href="#clusterid" title="ClusterId">ClusterId</a>: <i>String</i>
    <a href="#ecsperformancetype" title="EcsPerformanceType">EcsPerformanceType</a>: <i>String</i>
    <a href="#eipcount" title="EipCount">EipCount</a>: <i>Double</i>
    <a href="#eipids" title="EipIds">EipIds</a>: <i>
      - String</i>
    <a href="#extendparamchargingmode" title="ExtendParamChargingMode">ExtendParamChargingMode</a>: <i>Double</i>
    <a href="#flavorid" title="FlavorId">FlavorId</a>: <i>String</i>
    <a href="#iptype" title="Iptype">Iptype</a>: <i>String</i>
    <a href="#keypair" title="KeyPair">KeyPair</a>: <i>String</i>
    <a href="#labels" title="Labels">Labels</a>: <i>
      - <a href="labels.md">Labels</a></i>
    <a href="#maxpods" title="MaxPods">MaxPods</a>: <i>Double</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#orderid" title="OrderId">OrderId</a>: <i>String</i>
    <a href="#postinstall" title="Postinstall">Postinstall</a>: <i>String</i>
    <a href="#preinstall" title="Preinstall">Preinstall</a>: <i>String</i>
    <a href="#productid" title="ProductId">ProductId</a>: <i>String</i>
    <a href="#publickey" title="PublicKey">PublicKey</a>: <i>String</i>
    <a href="#region" title="Region">Region</a>: <i>String</i>
    <a href="#sharetype" title="Sharetype">Sharetype</a>: <i>String</i>
    <a href="#datavolumes" title="DataVolumes">DataVolumes</a>: <i>
      - <a href="datavolumes.md">DataVolumes</a></i>
    <a href="#rootvolume" title="RootVolume">RootVolume</a>: <i>
      - <a href="rootvolume.md">RootVolume</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeouts.md">Timeouts</a></i>
</pre>

## Properties

#### Annotations

Node annotation, key/value pair format. Changing this parameter will create a new resource.

_Required_: No

_Type_: List of <a href="annotations.md">Annotations</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AvailabilityZone

specify the name of the available partition (AZ). Changing this parameter will create a new resource.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BandwidthChargeMode

Bandwidth billing type. Changing this parameter will create a new resource.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BandwidthSize

Bandwidth size. Changing this parameter will create a new resource.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BillingMode

Node's billing mode: The value is 0 (on demand). Changing this parameter will create a new resource.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClusterId

ID of the cluster. Changing this parameter will create a new resource.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EcsPerformanceType

Classification of cloud server specifications. Changing this parameter will create a new cluster resource.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EipCount

Number of elastic IPs to be dynamically created. Changing this parameter will create a new resource.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EipIds

List of existing elastic IP IDs. Changing this parameter will create a new resource.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExtendParamChargingMode

Node charging mode, 0 is on-demand charging. Changing this parameter will create a new cluster resource.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FlavorId

Specifies the flavor id. Changing this parameter will create a new resource.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Iptype

Elastic IP type.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KeyPair

Key pair name when logging in to select the key pair mode. Changing this parameter will create a new resource.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Labels

Node tag, key/value pair format. Changing this parameter will create a new resource.

_Required_: No

_Type_: List of <a href="labels.md">Labels</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxPods

The maximum number of instances a node is allowed to create. Changing this parameter will create a new cluster resource.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Node Name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OrderId

Order ID, mandatory when the node payment type is the automatic payment package period type. Changing this parameter will create a new cluster resource.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Postinstall

Script required after installation. The input value can be a Base64 encoded string or not.
Changing this parameter will create a new resource.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Preinstall

Script required before installation. The input value can be a Base64 encoded string or not.
Changing this parameter will create a new resource.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProductId

The Product ID. Changing this parameter will create a new cluster resource.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PublicKey

The Public key. Changing this parameter will create a new cluster resource.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Region

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Sharetype

Bandwidth sharing type. Changing this parameter will create a new resource.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DataVolumes

_Required_: No

_Type_: List of <a href="datavolumes.md">DataVolumes</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RootVolume

_Required_: No

_Type_: List of <a href="rootvolume.md">RootVolume</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeouts.md">Timeouts</a>

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

#### PrivateIp

Returns the <code>PrivateIp</code> value.

