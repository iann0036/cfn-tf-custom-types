# Terraform::AzureRM::ContainerGroup

Manages as an Azure Container Group instance.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AzureRM::ContainerGroup",
    "Properties" : {
        "<a href="#dnsnamelabel" title="DnsNameLabel">DnsNameLabel</a>" : <i>String</i>,
        "<a href="#ipaddresstype" title="IpAddressType">IpAddressType</a>" : <i>String</i>,
        "<a href="#location" title="Location">Location</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#networkprofileid" title="NetworkProfileId">NetworkProfileId</a>" : <i>String</i>,
        "<a href="#ostype" title="OsType">OsType</a>" : <i>String</i>,
        "<a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>" : <i>String</i>,
        "<a href="#restartpolicy" title="RestartPolicy">RestartPolicy</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tags.md">Tags</a>, ... ]</i>,
        "<a href="#container" title="Container">Container</a>" : <i>[ <a href="container.md">Container</a>, ... ]</i>,
        "<a href="#diagnostics" title="Diagnostics">Diagnostics</a>" : <i>[ <a href="diagnostics.md">Diagnostics</a>, ... ]</i>,
        "<a href="#identity" title="Identity">Identity</a>" : <i>[ <a href="identity.md">Identity</a>, ... ]</i>,
        "<a href="#imageregistrycredential" title="ImageRegistryCredential">ImageRegistryCredential</a>" : <i>[ <a href="imageregistrycredential.md">ImageRegistryCredential</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeouts.md">Timeouts</a></i>,
        "<a href="#gpu" title="Gpu">Gpu</a>" : <i>[ <a href="gpu.md">Gpu</a>, ... ]</i>,
        "<a href="#livenessprobe" title="LivenessProbe">LivenessProbe</a>" : <i>[ <a href="livenessprobe.md">LivenessProbe</a>, ... ]</i>,
        "<a href="#ports" title="Ports">Ports</a>" : <i>[ <a href="ports.md">Ports</a>, ... ]</i>,
        "<a href="#readinessprobe" title="ReadinessProbe">ReadinessProbe</a>" : <i>[ <a href="readinessprobe.md">ReadinessProbe</a>, ... ]</i>,
        "<a href="#volume" title="Volume">Volume</a>" : <i>[ <a href="volume.md">Volume</a>, ... ]</i>,
        "<a href="#loganalytics" title="LogAnalytics">LogAnalytics</a>" : <i>[ <a href="loganalytics.md">LogAnalytics</a>, ... ]</i>,
        "<a href="#httpget" title="HttpGet">HttpGet</a>" : <i>[ <a href="httpget.md">HttpGet</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AzureRM::ContainerGroup
Properties:
    <a href="#dnsnamelabel" title="DnsNameLabel">DnsNameLabel</a>: <i>String</i>
    <a href="#ipaddresstype" title="IpAddressType">IpAddressType</a>: <i>String</i>
    <a href="#location" title="Location">Location</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#networkprofileid" title="NetworkProfileId">NetworkProfileId</a>: <i>String</i>
    <a href="#ostype" title="OsType">OsType</a>: <i>String</i>
    <a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>: <i>String</i>
    <a href="#restartpolicy" title="RestartPolicy">RestartPolicy</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tags.md">Tags</a></i>
    <a href="#container" title="Container">Container</a>: <i>
      - <a href="container.md">Container</a></i>
    <a href="#diagnostics" title="Diagnostics">Diagnostics</a>: <i>
      - <a href="diagnostics.md">Diagnostics</a></i>
    <a href="#identity" title="Identity">Identity</a>: <i>
      - <a href="identity.md">Identity</a></i>
    <a href="#imageregistrycredential" title="ImageRegistryCredential">ImageRegistryCredential</a>: <i>
      - <a href="imageregistrycredential.md">ImageRegistryCredential</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeouts.md">Timeouts</a></i>
    <a href="#gpu" title="Gpu">Gpu</a>: <i>
      - <a href="gpu.md">Gpu</a></i>
    <a href="#livenessprobe" title="LivenessProbe">LivenessProbe</a>: <i>
      - <a href="livenessprobe.md">LivenessProbe</a></i>
    <a href="#ports" title="Ports">Ports</a>: <i>
      - <a href="ports.md">Ports</a></i>
    <a href="#readinessprobe" title="ReadinessProbe">ReadinessProbe</a>: <i>
      - <a href="readinessprobe.md">ReadinessProbe</a></i>
    <a href="#volume" title="Volume">Volume</a>: <i>
      - <a href="volume.md">Volume</a></i>
    <a href="#loganalytics" title="LogAnalytics">LogAnalytics</a>: <i>
      - <a href="loganalytics.md">LogAnalytics</a></i>
    <a href="#httpget" title="HttpGet">HttpGet</a>: <i>
      - <a href="httpget.md">HttpGet</a></i>
</pre>

## Properties

#### DnsNameLabel

The DNS label/name for the container groups IP. Changing this forces a new resource to be created.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpAddressType

Specifies the ip address type of the container. `Public` or `Private`. Changing this forces a new resource to be created. If set to `Private`, `network_profile_id` also needs to be set.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Location

Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Specifies the name of the Container Group. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetworkProfileId

Network profile ID for deploying to virtual network.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OsType

The OS for the container group. Allowed values are `Linux` and `Windows`. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourceGroupName

The name of the resource group in which to create the Container Group. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RestartPolicy

Restart policy for the container group. Allowed values are `Always`, `Never`, `OnFailure`. Defaults to `Always`. Changing this forces a new resource to be created.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

A mapping of tags to assign to the resource. Changing this forces a new resource to be created.

_Required_: No

_Type_: List of <a href="tags.md">Tags</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Container

_Required_: No

_Type_: List of <a href="container.md">Container</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Diagnostics

_Required_: No

_Type_: List of <a href="diagnostics.md">Diagnostics</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Identity

_Required_: No

_Type_: List of <a href="identity.md">Identity</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ImageRegistryCredential

_Required_: No

_Type_: List of <a href="imageregistrycredential.md">ImageRegistryCredential</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeouts.md">Timeouts</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Gpu

_Required_: No

_Type_: List of <a href="gpu.md">Gpu</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LivenessProbe

_Required_: No

_Type_: List of <a href="livenessprobe.md">LivenessProbe</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ports

_Required_: No

_Type_: List of <a href="ports.md">Ports</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReadinessProbe

_Required_: No

_Type_: List of <a href="readinessprobe.md">ReadinessProbe</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Volume

_Required_: No

_Type_: List of <a href="volume.md">Volume</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LogAnalytics

_Required_: No

_Type_: List of <a href="loganalytics.md">LogAnalytics</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HttpGet

_Required_: No

_Type_: List of <a href="httpget.md">HttpGet</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Fqdn

Returns the <code>Fqdn</code> value.

#### IpAddress

Returns the <code>IpAddress</code> value.

