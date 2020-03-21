# Terraform::AWS::BatchComputeEnvironment ComputeResources

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#allocationstrategy" title="AllocationStrategy">AllocationStrategy</a>" : <i>String</i>,
    "<a href="#bidpercentage" title="BidPercentage">BidPercentage</a>" : <i>Double</i>,
    "<a href="#desiredvcpus" title="DesiredVcpus">DesiredVcpus</a>" : <i>Double</i>,
    "<a href="#ec2keypair" title="Ec2KeyPair">Ec2KeyPair</a>" : <i>String</i>,
    "<a href="#imageid" title="ImageId">ImageId</a>" : <i>String</i>,
    "<a href="#instancerole" title="InstanceRole">InstanceRole</a>" : <i>String</i>,
    "<a href="#instancetype" title="InstanceType">InstanceType</a>" : <i>[ String, ... ]</i>,
    "<a href="#maxvcpus" title="MaxVcpus">MaxVcpus</a>" : <i>Double</i>,
    "<a href="#minvcpus" title="MinVcpus">MinVcpus</a>" : <i>Double</i>,
    "<a href="#securitygroupids" title="SecurityGroupIds">SecurityGroupIds</a>" : <i>[ String, ... ]</i>,
    "<a href="#spotiamfleetrole" title="SpotIamFleetRole">SpotIamFleetRole</a>" : <i>String</i>,
    "<a href="#subnets" title="Subnets">Subnets</a>" : <i>[ String, ... ]</i>,
    "<a href="#tags" title="Tags">Tags</a>" : <i>[ &lt;a href=&#34;computeresources-tags.md&#34;&gt;Tags&lt;/a&gt;, ... ]</i>,
    "<a href="#type" title="Type">Type</a>" : <i>String</i>,
    "<a href="#launchtemplate" title="LaunchTemplate">LaunchTemplate</a>" : <i>[ &lt;a href=&#34;computeresources-launchtemplate.md&#34;&gt;LaunchTemplate&lt;/a&gt;, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#allocationstrategy" title="AllocationStrategy">AllocationStrategy</a>: <i>String</i>
<a href="#bidpercentage" title="BidPercentage">BidPercentage</a>: <i>Double</i>
<a href="#desiredvcpus" title="DesiredVcpus">DesiredVcpus</a>: <i>Double</i>
<a href="#ec2keypair" title="Ec2KeyPair">Ec2KeyPair</a>: <i>String</i>
<a href="#imageid" title="ImageId">ImageId</a>: <i>String</i>
<a href="#instancerole" title="InstanceRole">InstanceRole</a>: <i>String</i>
<a href="#instancetype" title="InstanceType">InstanceType</a>: <i>
      - String</i>
<a href="#maxvcpus" title="MaxVcpus">MaxVcpus</a>: <i>Double</i>
<a href="#minvcpus" title="MinVcpus">MinVcpus</a>: <i>Double</i>
<a href="#securitygroupids" title="SecurityGroupIds">SecurityGroupIds</a>: <i>
      - String</i>
<a href="#spotiamfleetrole" title="SpotIamFleetRole">SpotIamFleetRole</a>: <i>String</i>
<a href="#subnets" title="Subnets">Subnets</a>: <i>
      - String</i>
<a href="#tags" title="Tags">Tags</a>: <i>
      - &lt;a href=&#34;computeresources-tags.md&#34;&gt;Tags&lt;/a&gt;</i>
<a href="#type" title="Type">Type</a>: <i>String</i>
<a href="#launchtemplate" title="LaunchTemplate">LaunchTemplate</a>: <i>
      - &lt;a href=&#34;computeresources-launchtemplate.md&#34;&gt;LaunchTemplate&lt;/a&gt;</i>
</pre>

## Properties

#### AllocationStrategy

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BidPercentage

_Required_: No
_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DesiredVcpus

_Required_: No
_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ec2KeyPair

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ImageId

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InstanceRole

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InstanceType

_Required_: Yes
_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxVcpus

_Required_: Yes
_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MinVcpus

_Required_: Yes
_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecurityGroupIds

_Required_: Yes
_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SpotIamFleetRole

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Subnets

_Required_: Yes
_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

_Required_: No
_Type_: List of &lt;a href=&#34;computeresources-tags.md&#34;&gt;Tags&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LaunchTemplate

_Required_: No
_Type_: List of &lt;a href=&#34;computeresources-launchtemplate.md&#34;&gt;LaunchTemplate&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

