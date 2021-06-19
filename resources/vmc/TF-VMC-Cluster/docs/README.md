# TF::VMC::Cluster

Provides a resource to manage clusters.
~> **Note:** Cluster resource implicitly depends on SDDC resource creation. SDDC must be provisioned before a cluster can be created. For details on how to provision a SDDC refer to [vmc_sddc](https://www.terraform.io/docs/providers/vmc/r/sddc.html).

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::VMC::Cluster",
    "Properties" : {
        "<a href="#edrspolicytype" title="EdrsPolicyType">EdrsPolicyType</a>" : <i>String</i>,
        "<a href="#enableedrs" title="EnableEdrs">EnableEdrs</a>" : <i>Boolean</i>,
        "<a href="#hostcpucorescount" title="HostCpuCoresCount">HostCpuCoresCount</a>" : <i>Double</i>,
        "<a href="#hostinstancetype" title="HostInstanceType">HostInstanceType</a>" : <i>String</i>,
        "<a href="#maxhosts" title="MaxHosts">MaxHosts</a>" : <i>Double</i>,
        "<a href="#minhosts" title="MinHosts">MinHosts</a>" : <i>Double</i>,
        "<a href="#numhosts" title="NumHosts">NumHosts</a>" : <i>Double</i>,
        "<a href="#sddcid" title="SddcId">SddcId</a>" : <i>String</i>,
        "<a href="#storagecapacity" title="StorageCapacity">StorageCapacity</a>" : <i>String</i>,
        "<a href="#microsoftlicensingconfig" title="MicrosoftLicensingConfig">MicrosoftLicensingConfig</a>" : <i>[ <a href="microsoftlicensingconfigdefinition.md">MicrosoftLicensingConfigDefinition</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::VMC::Cluster
Properties:
    <a href="#edrspolicytype" title="EdrsPolicyType">EdrsPolicyType</a>: <i>String</i>
    <a href="#enableedrs" title="EnableEdrs">EnableEdrs</a>: <i>Boolean</i>
    <a href="#hostcpucorescount" title="HostCpuCoresCount">HostCpuCoresCount</a>: <i>Double</i>
    <a href="#hostinstancetype" title="HostInstanceType">HostInstanceType</a>: <i>String</i>
    <a href="#maxhosts" title="MaxHosts">MaxHosts</a>: <i>Double</i>
    <a href="#minhosts" title="MinHosts">MinHosts</a>: <i>Double</i>
    <a href="#numhosts" title="NumHosts">NumHosts</a>: <i>Double</i>
    <a href="#sddcid" title="SddcId">SddcId</a>: <i>String</i>
    <a href="#storagecapacity" title="StorageCapacity">StorageCapacity</a>: <i>String</i>
    <a href="#microsoftlicensingconfig" title="MicrosoftLicensingConfig">MicrosoftLicensingConfig</a>: <i>
      - <a href="microsoftlicensingconfigdefinition.md">MicrosoftLicensingConfigDefinition</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### EdrsPolicyType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableEdrs

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HostCpuCoresCount

Customize CPU cores on hosts in a cluster. Specify number of cores to be enabled on hosts in a cluster.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HostInstanceType

The instance type for the esx hosts added to this cluster. Possible values are: I3_METAL, I3EN_METAL and R5_METAL. Default value: I3_METAL.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxHosts

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MinHosts

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NumHosts

Number of hosts in the cluster. The number of hosts must be between 3 - 16 hosts for a cluster.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SddcId

SDDC identifier.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StorageCapacity

For EBS-backed instances i.e: for R5_METAL only, the requested storage capacity in GiB.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MicrosoftLicensingConfig

_Required_: No

_Type_: List of <a href="microsoftlicensingconfigdefinition.md">MicrosoftLicensingConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeoutsdefinition.md">TimeoutsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### ClusterInfo

Returns the <code>ClusterInfo</code> value.

#### Id

Returns the <code>Id</code> value.

