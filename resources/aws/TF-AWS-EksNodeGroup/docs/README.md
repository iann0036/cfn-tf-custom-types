# TF::AWS::EksNodeGroup

Manages an EKS Node Group, which can provision and optionally update an Auto Scaling Group of Kubernetes worker nodes compatible with EKS. Additional documentation about this functionality can be found in the [EKS User Guide](https://docs.aws.amazon.com/eks/latest/userguide/managed-node-groups.html).

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AWS::EksNodeGroup",
    "Properties" : {
        "<a href="#amitype" title="AmiType">AmiType</a>" : <i>String</i>,
        "<a href="#capacitytype" title="CapacityType">CapacityType</a>" : <i>String</i>,
        "<a href="#clustername" title="ClusterName">ClusterName</a>" : <i>String</i>,
        "<a href="#disksize" title="DiskSize">DiskSize</a>" : <i>Double</i>,
        "<a href="#forceupdateversion" title="ForceUpdateVersion">ForceUpdateVersion</a>" : <i>Boolean</i>,
        "<a href="#instancetypes" title="InstanceTypes">InstanceTypes</a>" : <i>[ String, ... ]</i>,
        "<a href="#labels" title="Labels">Labels</a>" : <i>[ <a href="labelsdefinition.md">LabelsDefinition</a>, ... ]</i>,
        "<a href="#nodegroupname" title="NodeGroupName">NodeGroupName</a>" : <i>String</i>,
        "<a href="#nodegroupnameprefix" title="NodeGroupNamePrefix">NodeGroupNamePrefix</a>" : <i>String</i>,
        "<a href="#noderolearn" title="NodeRoleArn">NodeRoleArn</a>" : <i>String</i>,
        "<a href="#releaseversion" title="ReleaseVersion">ReleaseVersion</a>" : <i>String</i>,
        "<a href="#subnetids" title="SubnetIds">SubnetIds</a>" : <i>[ String, ... ]</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tagsdefinition.md">TagsDefinition</a>, ... ]</i>,
        "<a href="#tagsall" title="TagsAll">TagsAll</a>" : <i>[ <a href="tagsalldefinition.md">TagsAllDefinition</a>, ... ]</i>,
        "<a href="#version" title="Version">Version</a>" : <i>String</i>,
        "<a href="#launchtemplate" title="LaunchTemplate">LaunchTemplate</a>" : <i>[ <a href="launchtemplatedefinition.md">LaunchTemplateDefinition</a>, ... ]</i>,
        "<a href="#remoteaccess" title="RemoteAccess">RemoteAccess</a>" : <i>[ <a href="remoteaccessdefinition.md">RemoteAccessDefinition</a>, ... ]</i>,
        "<a href="#scalingconfig" title="ScalingConfig">ScalingConfig</a>" : <i>[ <a href="scalingconfigdefinition.md">ScalingConfigDefinition</a>, ... ]</i>,
        "<a href="#taint" title="Taint">Taint</a>" : <i>[ <a href="taintdefinition.md">TaintDefinition</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AWS::EksNodeGroup
Properties:
    <a href="#amitype" title="AmiType">AmiType</a>: <i>String</i>
    <a href="#capacitytype" title="CapacityType">CapacityType</a>: <i>String</i>
    <a href="#clustername" title="ClusterName">ClusterName</a>: <i>String</i>
    <a href="#disksize" title="DiskSize">DiskSize</a>: <i>Double</i>
    <a href="#forceupdateversion" title="ForceUpdateVersion">ForceUpdateVersion</a>: <i>Boolean</i>
    <a href="#instancetypes" title="InstanceTypes">InstanceTypes</a>: <i>
      - String</i>
    <a href="#labels" title="Labels">Labels</a>: <i>
      - <a href="labelsdefinition.md">LabelsDefinition</a></i>
    <a href="#nodegroupname" title="NodeGroupName">NodeGroupName</a>: <i>String</i>
    <a href="#nodegroupnameprefix" title="NodeGroupNamePrefix">NodeGroupNamePrefix</a>: <i>String</i>
    <a href="#noderolearn" title="NodeRoleArn">NodeRoleArn</a>: <i>String</i>
    <a href="#releaseversion" title="ReleaseVersion">ReleaseVersion</a>: <i>String</i>
    <a href="#subnetids" title="SubnetIds">SubnetIds</a>: <i>
      - String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tagsdefinition.md">TagsDefinition</a></i>
    <a href="#tagsall" title="TagsAll">TagsAll</a>: <i>
      - <a href="tagsalldefinition.md">TagsAllDefinition</a></i>
    <a href="#version" title="Version">Version</a>: <i>String</i>
    <a href="#launchtemplate" title="LaunchTemplate">LaunchTemplate</a>: <i>
      - <a href="launchtemplatedefinition.md">LaunchTemplateDefinition</a></i>
    <a href="#remoteaccess" title="RemoteAccess">RemoteAccess</a>: <i>
      - <a href="remoteaccessdefinition.md">RemoteAccessDefinition</a></i>
    <a href="#scalingconfig" title="ScalingConfig">ScalingConfig</a>: <i>
      - <a href="scalingconfigdefinition.md">ScalingConfigDefinition</a></i>
    <a href="#taint" title="Taint">Taint</a>: <i>
      - <a href="taintdefinition.md">TaintDefinition</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### AmiType

Type of Amazon Machine Image (AMI) associated with the EKS Node Group. Defaults to `AL2_x86_64`. Valid values: `AL2_x86_64`, `AL2_x86_64_GPU`, `AL2_ARM_64`, `CUSTOM`. Terraform will only perform drift detection if a configuration value is provided.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CapacityType

Type of capacity associated with the EKS Node Group. Valid values: `ON_DEMAND`, `SPOT`. Terraform will only perform drift detection if a configuration value is provided.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClusterName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DiskSize

Disk size in GiB for worker nodes. Defaults to `20`. Terraform will only perform drift detection if a configuration value is provided.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ForceUpdateVersion

Force version update if existing pods are unable to be drained due to a pod disruption budget issue.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InstanceTypes

List of instance types associated with the EKS Node Group. Defaults to `["t3.medium"]`. Terraform will only perform drift detection if a configuration value is provided.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Labels

Key-value map of Kubernetes labels. Only labels that are applied with the EKS API are managed by this argument. Other Kubernetes labels applied to the EKS Node Group will not be managed.

_Required_: No

_Type_: List of <a href="labelsdefinition.md">LabelsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NodeGroupName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NodeGroupNamePrefix

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NodeRoleArn

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReleaseVersion

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SubnetIds

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

Key-value map of resource tags. If configured with a provider [`default_tags` configuration block](https://www.terraform.io/docs/providers/aws/index.html#default_tags-configuration-block) present, tags with matching keys will overwrite those defined at the provider-level.

_Required_: No

_Type_: List of <a href="tagsdefinition.md">TagsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TagsAll

_Required_: No

_Type_: List of <a href="tagsalldefinition.md">TagsAllDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Version

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LaunchTemplate

_Required_: No

_Type_: List of <a href="launchtemplatedefinition.md">LaunchTemplateDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RemoteAccess

_Required_: No

_Type_: List of <a href="remoteaccessdefinition.md">RemoteAccessDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ScalingConfig

_Required_: No

_Type_: List of <a href="scalingconfigdefinition.md">ScalingConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Taint

_Required_: No

_Type_: List of <a href="taintdefinition.md">TaintDefinition</a>

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

#### Arn

Returns the <code>Arn</code> value.

#### Id

Returns the <code>Id</code> value.

#### Resources

Returns the <code>Resources</code> value.

#### Status

Returns the <code>Status</code> value.

