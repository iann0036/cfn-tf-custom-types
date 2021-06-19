# TF::AWS::Kinesisanalyticsv2Application VpcConfigurationDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#securitygroupids" title="SecurityGroupIds">SecurityGroupIds</a>" : <i>[ String, ... ]</i>,
    "<a href="#subnetids" title="SubnetIds">SubnetIds</a>" : <i>[ String, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#securitygroupids" title="SecurityGroupIds">SecurityGroupIds</a>: <i>
      - String</i>
<a href="#subnetids" title="SubnetIds">SubnetIds</a>: <i>
      - String</i>
</pre>

## Properties

#### SecurityGroupIds

The [Security Group](/docs/providers/aws/r/security_group.html) IDs used by the VPC configuration.

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SubnetIds

The [Subnet](/docs/providers/aws/r/subnet.html) IDs used by the VPC configuration.

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

