# TF::Spotinst::OceanAks

Manages a Spotinst Ocean AKS resource.

-> This resource contains arguments (such as `image` and `extension`) that are automatically populated from the data reported by the Ocean AKS Connector deployed into your cluster. You can override the upstream configuration by defining the corresponding arguments.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Spotinst::OceanAks",
    "Properties" : {
        "<a href="#acdidentifier" title="AcdIdentifier">AcdIdentifier</a>" : <i>String</i>,
        "<a href="#aksname" title="AksName">AksName</a>" : <i>String</i>,
        "<a href="#aksresourcegroupname" title="AksResourceGroupName">AksResourceGroupName</a>" : <i>String</i>,
        "<a href="#controllerclusterid" title="ControllerClusterId">ControllerClusterId</a>" : <i>String</i>,
        "<a href="#customdata" title="CustomData">CustomData</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>" : <i>String</i>,
        "<a href="#sshpublickey" title="SshPublicKey">SshPublicKey</a>" : <i>String</i>,
        "<a href="#username" title="UserName">UserName</a>" : <i>String</i>,
        "<a href="#autoscaler" title="Autoscaler">Autoscaler</a>" : <i>[ <a href="autoscalerdefinition.md">AutoscalerDefinition</a>, ... ]</i>,
        "<a href="#extension" title="Extension">Extension</a>" : <i>[ <a href="extensiondefinition.md">ExtensionDefinition</a>, ... ]</i>,
        "<a href="#health" title="Health">Health</a>" : <i>[ <a href="healthdefinition.md">HealthDefinition</a>, ... ]</i>,
        "<a href="#image" title="Image">Image</a>" : <i>[ <a href="imagedefinition.md">ImageDefinition</a>, ... ]</i>,
        "<a href="#loadbalancer" title="LoadBalancer">LoadBalancer</a>" : <i>[ <a href="loadbalancerdefinition.md">LoadBalancerDefinition</a>, ... ]</i>,
        "<a href="#network" title="Network">Network</a>" : <i>[ <a href="networkdefinition.md">NetworkDefinition</a>, ... ]</i>,
        "<a href="#osdisk" title="OsDisk">OsDisk</a>" : <i>[ <a href="osdiskdefinition.md">OsDiskDefinition</a>, ... ]</i>,
        "<a href="#strategy" title="Strategy">Strategy</a>" : <i>[ <a href="strategydefinition.md">StrategyDefinition</a>, ... ]</i>,
        "<a href="#tag" title="Tag">Tag</a>" : <i>[ <a href="tagdefinition.md">TagDefinition</a>, ... ]</i>,
        "<a href="#vmsizes" title="VmSizes">VmSizes</a>" : <i>[ <a href="vmsizesdefinition.md">VmSizesDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Spotinst::OceanAks
Properties:
    <a href="#acdidentifier" title="AcdIdentifier">AcdIdentifier</a>: <i>String</i>
    <a href="#aksname" title="AksName">AksName</a>: <i>String</i>
    <a href="#aksresourcegroupname" title="AksResourceGroupName">AksResourceGroupName</a>: <i>String</i>
    <a href="#controllerclusterid" title="ControllerClusterId">ControllerClusterId</a>: <i>String</i>
    <a href="#customdata" title="CustomData">CustomData</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>: <i>String</i>
    <a href="#sshpublickey" title="SshPublicKey">SshPublicKey</a>: <i>String</i>
    <a href="#username" title="UserName">UserName</a>: <i>String</i>
    <a href="#autoscaler" title="Autoscaler">Autoscaler</a>: <i>
      - <a href="autoscalerdefinition.md">AutoscalerDefinition</a></i>
    <a href="#extension" title="Extension">Extension</a>: <i>
      - <a href="extensiondefinition.md">ExtensionDefinition</a></i>
    <a href="#health" title="Health">Health</a>: <i>
      - <a href="healthdefinition.md">HealthDefinition</a></i>
    <a href="#image" title="Image">Image</a>: <i>
      - <a href="imagedefinition.md">ImageDefinition</a></i>
    <a href="#loadbalancer" title="LoadBalancer">LoadBalancer</a>: <i>
      - <a href="loadbalancerdefinition.md">LoadBalancerDefinition</a></i>
    <a href="#network" title="Network">Network</a>: <i>
      - <a href="networkdefinition.md">NetworkDefinition</a></i>
    <a href="#osdisk" title="OsDisk">OsDisk</a>: <i>
      - <a href="osdiskdefinition.md">OsDiskDefinition</a></i>
    <a href="#strategy" title="Strategy">Strategy</a>: <i>
      - <a href="strategydefinition.md">StrategyDefinition</a></i>
    <a href="#tag" title="Tag">Tag</a>: <i>
      - <a href="tagdefinition.md">TagDefinition</a></i>
    <a href="#vmsizes" title="VmSizes">VmSizes</a>: <i>
      - <a href="vmsizesdefinition.md">VmSizesDefinition</a></i>
</pre>

## Properties

#### AcdIdentifier

The AKS identifier.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AksName

The AKS cluster name.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AksResourceGroupName

Name of the Azure Resource Group where the AKS cluster is located.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ControllerClusterId

A unique identifier used for connecting the Ocean SaaS platform and the Kubernetes cluster. Typically, the cluster name is used as its identifier.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CustomData

Must contain a valid Base64 encoded string.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Name of the Load Balancer.
* `resource_group_name` - (Optional) The Resource Group name of the Load Balancer.
* `type` - (Optional) The type of load balancer. Supported value: `loadBalancer`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourceGroupName

The Resource Group name of the Load Balancer.
* `type` - (Optional) The type of load balancer. Supported value: `loadBalancer`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SshPublicKey

SSH public key for admin access to Linux VMs.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserName

Username for admin access to VMs.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Autoscaler

_Required_: No

_Type_: List of <a href="autoscalerdefinition.md">AutoscalerDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Extension

_Required_: No

_Type_: List of <a href="extensiondefinition.md">ExtensionDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Health

_Required_: No

_Type_: List of <a href="healthdefinition.md">HealthDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Image

_Required_: No

_Type_: List of <a href="imagedefinition.md">ImageDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LoadBalancer

_Required_: No

_Type_: List of <a href="loadbalancerdefinition.md">LoadBalancerDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Network

_Required_: No

_Type_: List of <a href="networkdefinition.md">NetworkDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OsDisk

_Required_: No

_Type_: List of <a href="osdiskdefinition.md">OsDiskDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Strategy

_Required_: No

_Type_: List of <a href="strategydefinition.md">StrategyDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tag

_Required_: No

_Type_: List of <a href="tagdefinition.md">TagDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VmSizes

_Required_: No

_Type_: List of <a href="vmsizesdefinition.md">VmSizesDefinition</a>

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

