# Terraform::AWS::MskCluster BrokerNodeGroupInfo

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#azdistribution" title="AzDistribution">AzDistribution</a>" : <i>String</i>,
    "<a href="#clientsubnets" title="ClientSubnets">ClientSubnets</a>" : <i>[ String, ... ]</i>,
    "<a href="#ebsvolumesize" title="EbsVolumeSize">EbsVolumeSize</a>" : <i>Double</i>,
    "<a href="#instancetype" title="InstanceType">InstanceType</a>" : <i>String</i>,
    "<a href="#securitygroups" title="SecurityGroups">SecurityGroups</a>" : <i>[ String, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#azdistribution" title="AzDistribution">AzDistribution</a>: <i>String</i>
<a href="#clientsubnets" title="ClientSubnets">ClientSubnets</a>: <i>
      - String</i>
<a href="#ebsvolumesize" title="EbsVolumeSize">EbsVolumeSize</a>: <i>Double</i>
<a href="#instancetype" title="InstanceType">InstanceType</a>: <i>String</i>
<a href="#securitygroups" title="SecurityGroups">SecurityGroups</a>: <i>
      - String</i>
</pre>

## Properties

#### AzDistribution

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClientSubnets

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EbsVolumeSize

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InstanceType

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecurityGroups

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

