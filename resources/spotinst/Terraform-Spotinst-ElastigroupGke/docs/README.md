# Terraform::Spotinst::ElastigroupGke

Provides a Spotinst Elastigroup GKE resource. Please see [Importing a GKE cluster](https://api.spotinst.com/elastigroup-for-google-cloud/tutorials/import-a-gke-cluster-as-an-elastigroup/) for detailed information.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Spotinst::ElastigroupGke",
    "Properties" : {
        "<a href="#clusterid" title="ClusterId">ClusterId</a>" : <i>String</i>,
        "<a href="#clusterzonename" title="ClusterZoneName">ClusterZoneName</a>" : <i>String</i>,
        "<a href="#desiredcapacity" title="DesiredCapacity">DesiredCapacity</a>" : <i>Double</i>,
        "<a href="#drainingtimeout" title="DrainingTimeout">DrainingTimeout</a>" : <i>Double</i>,
        "<a href="#fallbacktoondemand" title="FallbackToOndemand">FallbackToOndemand</a>" : <i>Boolean</i>,
        "<a href="#instancetypesondemand" title="InstanceTypesOndemand">InstanceTypesOndemand</a>" : <i>String</i>,
        "<a href="#instancetypespreemptible" title="InstanceTypesPreemptible">InstanceTypesPreemptible</a>" : <i>[ String, ... ]</i>,
        "<a href="#ipforwarding" title="IpForwarding">IpForwarding</a>" : <i>Boolean</i>,
        "<a href="#maxsize" title="MaxSize">MaxSize</a>" : <i>Double</i>,
        "<a href="#minsize" title="MinSize">MinSize</a>" : <i>Double</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#nodeimage" title="NodeImage">NodeImage</a>" : <i>String</i>,
        "<a href="#ondemandcount" title="OndemandCount">OndemandCount</a>" : <i>Double</i>,
        "<a href="#preemptiblepercentage" title="PreemptiblePercentage">PreemptiblePercentage</a>" : <i>Double</i>,
        "<a href="#serviceaccount" title="ServiceAccount">ServiceAccount</a>" : <i>String</i>,
        "<a href="#shutdownscript" title="ShutdownScript">ShutdownScript</a>" : <i>String</i>,
        "<a href="#startupscript" title="StartupScript">StartupScript</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ String, ... ]</i>,
        "<a href="#backendservices" title="BackendServices">BackendServices</a>" : <i>[ <a href="backendservices.md">BackendServices</a>, ... ]</i>,
        "<a href="#disk" title="Disk">Disk</a>" : <i>[ <a href="disk.md">Disk</a>, ... ]</i>,
        "<a href="#gpu" title="Gpu">Gpu</a>" : <i>[ <a href="gpu.md">Gpu</a>, ... ]</i>,
        "<a href="#instancetypescustom" title="InstanceTypesCustom">InstanceTypesCustom</a>" : <i>[ <a href="instancetypescustom.md">InstanceTypesCustom</a>, ... ]</i>,
        "<a href="#integrationdockerswarm" title="IntegrationDockerSwarm">IntegrationDockerSwarm</a>" : <i>[ <a href="integrationdockerswarm.md">IntegrationDockerSwarm</a>, ... ]</i>,
        "<a href="#integrationgke" title="IntegrationGke">IntegrationGke</a>" : <i>[ <a href="integrationgke.md">IntegrationGke</a>, ... ]</i>,
        "<a href="#labels" title="Labels">Labels</a>" : <i>[ <a href="labels.md">Labels</a>, ... ]</i>,
        "<a href="#metadata" title="Metadata">Metadata</a>" : <i>[ <a href="metadata.md">Metadata</a>, ... ]</i>,
        "<a href="#networkinterface" title="NetworkInterface">NetworkInterface</a>" : <i>[ <a href="networkinterface.md">NetworkInterface</a>, ... ]</i>,
        "<a href="#scalingdownpolicy" title="ScalingDownPolicy">ScalingDownPolicy</a>" : <i>[ <a href="scalingdownpolicy.md">ScalingDownPolicy</a>, ... ]</i>,
        "<a href="#scalinguppolicy" title="ScalingUpPolicy">ScalingUpPolicy</a>" : <i>[ <a href="scalinguppolicy.md">ScalingUpPolicy</a>, ... ]</i>,
        "<a href="#namedports" title="NamedPorts">NamedPorts</a>" : <i>[ <a href="namedports.md">NamedPorts</a>, ... ]</i>,
        "<a href="#initializeparams" title="InitializeParams">InitializeParams</a>" : <i>[ <a href="initializeparams.md">InitializeParams</a>, ... ]</i>,
        "<a href="#autoscaledown" title="AutoscaleDown">AutoscaleDown</a>" : <i>[ <a href="autoscaledown.md">AutoscaleDown</a>, ... ]</i>,
        "<a href="#autoscaleheadroom" title="AutoscaleHeadroom">AutoscaleHeadroom</a>" : <i>[ <a href="autoscaleheadroom.md">AutoscaleHeadroom</a>, ... ]</i>,
        "<a href="#autoscalelabels" title="AutoscaleLabels">AutoscaleLabels</a>" : <i>[ <a href="autoscalelabels.md">AutoscaleLabels</a>, ... ]</i>,
        "<a href="#accessconfigs" title="AccessConfigs">AccessConfigs</a>" : <i>[ <a href="accessconfigs.md">AccessConfigs</a>, ... ]</i>,
        "<a href="#aliasipranges" title="AliasIpRanges">AliasIpRanges</a>" : <i>[ <a href="aliasipranges.md">AliasIpRanges</a>, ... ]</i>,
        "<a href="#dimensions" title="Dimensions">Dimensions</a>" : <i>[ <a href="dimensions.md">Dimensions</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Spotinst::ElastigroupGke
Properties:
    <a href="#clusterid" title="ClusterId">ClusterId</a>: <i>String</i>
    <a href="#clusterzonename" title="ClusterZoneName">ClusterZoneName</a>: <i>String</i>
    <a href="#desiredcapacity" title="DesiredCapacity">DesiredCapacity</a>: <i>Double</i>
    <a href="#drainingtimeout" title="DrainingTimeout">DrainingTimeout</a>: <i>Double</i>
    <a href="#fallbacktoondemand" title="FallbackToOndemand">FallbackToOndemand</a>: <i>Boolean</i>
    <a href="#instancetypesondemand" title="InstanceTypesOndemand">InstanceTypesOndemand</a>: <i>String</i>
    <a href="#instancetypespreemptible" title="InstanceTypesPreemptible">InstanceTypesPreemptible</a>: <i>
      - String</i>
    <a href="#ipforwarding" title="IpForwarding">IpForwarding</a>: <i>Boolean</i>
    <a href="#maxsize" title="MaxSize">MaxSize</a>: <i>Double</i>
    <a href="#minsize" title="MinSize">MinSize</a>: <i>Double</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#nodeimage" title="NodeImage">NodeImage</a>: <i>String</i>
    <a href="#ondemandcount" title="OndemandCount">OndemandCount</a>: <i>Double</i>
    <a href="#preemptiblepercentage" title="PreemptiblePercentage">PreemptiblePercentage</a>: <i>Double</i>
    <a href="#serviceaccount" title="ServiceAccount">ServiceAccount</a>: <i>String</i>
    <a href="#shutdownscript" title="ShutdownScript">ShutdownScript</a>: <i>String</i>
    <a href="#startupscript" title="StartupScript">StartupScript</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - String</i>
    <a href="#backendservices" title="BackendServices">BackendServices</a>: <i>
      - <a href="backendservices.md">BackendServices</a></i>
    <a href="#disk" title="Disk">Disk</a>: <i>
      - <a href="disk.md">Disk</a></i>
    <a href="#gpu" title="Gpu">Gpu</a>: <i>
      - <a href="gpu.md">Gpu</a></i>
    <a href="#instancetypescustom" title="InstanceTypesCustom">InstanceTypesCustom</a>: <i>
      - <a href="instancetypescustom.md">InstanceTypesCustom</a></i>
    <a href="#integrationdockerswarm" title="IntegrationDockerSwarm">IntegrationDockerSwarm</a>: <i>
      - <a href="integrationdockerswarm.md">IntegrationDockerSwarm</a></i>
    <a href="#integrationgke" title="IntegrationGke">IntegrationGke</a>: <i>
      - <a href="integrationgke.md">IntegrationGke</a></i>
    <a href="#labels" title="Labels">Labels</a>: <i>
      - <a href="labels.md">Labels</a></i>
    <a href="#metadata" title="Metadata">Metadata</a>: <i>
      - <a href="metadata.md">Metadata</a></i>
    <a href="#networkinterface" title="NetworkInterface">NetworkInterface</a>: <i>
      - <a href="networkinterface.md">NetworkInterface</a></i>
    <a href="#scalingdownpolicy" title="ScalingDownPolicy">ScalingDownPolicy</a>: <i>
      - <a href="scalingdownpolicy.md">ScalingDownPolicy</a></i>
    <a href="#scalinguppolicy" title="ScalingUpPolicy">ScalingUpPolicy</a>: <i>
      - <a href="scalinguppolicy.md">ScalingUpPolicy</a></i>
    <a href="#namedports" title="NamedPorts">NamedPorts</a>: <i>
      - <a href="namedports.md">NamedPorts</a></i>
    <a href="#initializeparams" title="InitializeParams">InitializeParams</a>: <i>
      - <a href="initializeparams.md">InitializeParams</a></i>
    <a href="#autoscaledown" title="AutoscaleDown">AutoscaleDown</a>: <i>
      - <a href="autoscaledown.md">AutoscaleDown</a></i>
    <a href="#autoscaleheadroom" title="AutoscaleHeadroom">AutoscaleHeadroom</a>: <i>
      - <a href="autoscaleheadroom.md">AutoscaleHeadroom</a></i>
    <a href="#autoscalelabels" title="AutoscaleLabels">AutoscaleLabels</a>: <i>
      - <a href="autoscalelabels.md">AutoscaleLabels</a></i>
    <a href="#accessconfigs" title="AccessConfigs">AccessConfigs</a>: <i>
      - <a href="accessconfigs.md">AccessConfigs</a></i>
    <a href="#aliasipranges" title="AliasIpRanges">AliasIpRanges</a>: <i>
      - <a href="aliasipranges.md">AliasIpRanges</a></i>
    <a href="#dimensions" title="Dimensions">Dimensions</a>: <i>
      - <a href="dimensions.md">Dimensions</a></i>
</pre>

## Properties

#### ClusterId

The name of the GKE cluster you wish to import.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClusterZoneName

The zone where the cluster is hosted.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DesiredCapacity

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DrainingTimeout

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FallbackToOndemand

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InstanceTypesOndemand

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InstanceTypesPreemptible

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpForwarding

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxSize

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MinSize

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NodeImage

The image that will be used for the node VMs. Possible values: COS, UBUNTU.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OndemandCount

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PreemptiblePercentage

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceAccount

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ShutdownScript

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StartupScript

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BackendServices

_Required_: No

_Type_: List of <a href="backendservices.md">BackendServices</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Disk

_Required_: No

_Type_: List of <a href="disk.md">Disk</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Gpu

_Required_: No

_Type_: List of <a href="gpu.md">Gpu</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InstanceTypesCustom

_Required_: No

_Type_: List of <a href="instancetypescustom.md">InstanceTypesCustom</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IntegrationDockerSwarm

_Required_: No

_Type_: List of <a href="integrationdockerswarm.md">IntegrationDockerSwarm</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IntegrationGke

_Required_: No

_Type_: List of <a href="integrationgke.md">IntegrationGke</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Labels

_Required_: No

_Type_: List of <a href="labels.md">Labels</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Metadata

_Required_: No

_Type_: List of <a href="metadata.md">Metadata</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetworkInterface

_Required_: No

_Type_: List of <a href="networkinterface.md">NetworkInterface</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ScalingDownPolicy

_Required_: No

_Type_: List of <a href="scalingdownpolicy.md">ScalingDownPolicy</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ScalingUpPolicy

_Required_: No

_Type_: List of <a href="scalinguppolicy.md">ScalingUpPolicy</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NamedPorts

_Required_: No

_Type_: List of <a href="namedports.md">NamedPorts</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InitializeParams

_Required_: No

_Type_: List of <a href="initializeparams.md">InitializeParams</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AutoscaleDown

_Required_: No

_Type_: List of <a href="autoscaledown.md">AutoscaleDown</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AutoscaleHeadroom

_Required_: No

_Type_: List of <a href="autoscaleheadroom.md">AutoscaleHeadroom</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AutoscaleLabels

_Required_: No

_Type_: List of <a href="autoscalelabels.md">AutoscaleLabels</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AccessConfigs

_Required_: No

_Type_: List of <a href="accessconfigs.md">AccessConfigs</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AliasIpRanges

_Required_: No

_Type_: List of <a href="aliasipranges.md">AliasIpRanges</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Dimensions

_Required_: No

_Type_: List of <a href="dimensions.md">Dimensions</a>

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

